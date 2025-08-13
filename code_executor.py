#!/usr/bin/env python3
"""
Prosty serwer do uruchamiania kodu Python dla edytora cheatsheets
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import io
import contextlib
import traceback
import json

app = Flask(__name__)
CORS(app)  # Pozwól na żądania z różnych domen

@app.route('/execute', methods=['POST'])
def execute_code():
    """Uruchom kod Python i zwróć wyniki"""
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code.strip():
            return jsonify({
                'success': False,
                'output': '',
                'error': 'Brak kodu do uruchomienia'
            })
        
        # Przechwytuj stdout i stderr
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            # Przekieruj output
            sys.stdout = stdout_capture
            sys.stderr = stderr_capture
            
            # Stwórz bezpieczne środowisko wykonywania
            namespace = {
                '__builtins__': {
                    'print': print,
                    'len': len,
                    'str': str,
                    'int': int,
                    'float': float,
                    'list': list,
                    'dict': dict,
                    'tuple': tuple,
                    'set': set,
                    'range': range,
                    'enumerate': enumerate,
                    'zip': zip,
                    'sorted': sorted,
                    'sum': sum,
                    'max': max,
                    'min': min,
                    'abs': abs,
                    'round': round,
                    'type': type,
                    'isinstance': isinstance,
                    'hasattr': hasattr,
                    'getattr': getattr,
                    'setattr': setattr,
                    '__import__': __import__,
                }
            }
            
            # Dodaj popularne moduły
            try:
                import pandas as pd
                namespace['pd'] = pd
                namespace['pandas'] = pd
            except ImportError:
                pass
                
            try:
                import numpy as np
                namespace['np'] = np
                namespace['numpy'] = np
            except ImportError:
                pass
                
            try:
                import matplotlib.pyplot as plt
                namespace['plt'] = plt
            except ImportError:
                pass
            
            # Wykonaj kod
            exec(code, namespace)
            
            # Pobierz wyniki
            stdout_value = stdout_capture.getvalue()
            stderr_value = stderr_capture.getvalue()
            
            # Przywróć standardowe strumienie
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            
            if stderr_value:
                return jsonify({
                    'success': False,
                    'output': stdout_value,
                    'error': stderr_value
                })
            else:
                return jsonify({
                    'success': True,
                    'output': stdout_value or 'Kod wykonany pomyślnie (brak outputu)',
                    'error': ''
                })
                
        except Exception as e:
            # Przywróć standardowe strumienie
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            
            error_msg = f"{type(e).__name__}: {str(e)}"
            stdout_value = stdout_capture.getvalue()
            
            return jsonify({
                'success': False,
                'output': stdout_value,
                'error': error_msg
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'output': '',
            'error': f'Błąd serwera: {str(e)}'
        })

@app.route('/health', methods=['GET'])
def health_check():
    """Sprawdź czy serwer działa"""
    return jsonify({'status': 'ok', 'message': 'Code executor is running'})

if __name__ == '__main__':
    print("🚀 Uruchamianie serwera do wykonywania kodu Python...")
    print("🌐 Serwer będzie dostępny na: http://localhost:8080")
    print("🔧 Endpoint do wykonywania kodu: POST /execute")
    print("💡 Aby zatrzymać serwer: Ctrl+C")
    print()
    
    app.run(
        host='localhost',
        port=8080,
        debug=True,
        use_reloader=False  # Wyłącz auto-reload żeby nie było problemów
    )
