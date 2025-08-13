# 🚀 Live Code Editor - Instrukcja uruchomienia

## Szybki start

### 1. Uruchom stronę Quarto
```bash
conda activate quarto-py
quarto preview
```

### 2. Otwórz stronę w przeglądarce
- Przejdź na http://localhost:4467
- Kliknij "✏️ Tryb Edycji"
- Poczekaj aż Python się załaduje (10-15 sekund)
- Kliknij "▶️ Run" aby uruchomić kod!

## 🌐 Dla wersji GitHub Pages
- Otwórz stronę w przeglądarce (bez lokalnego serwera!)
- Wszystko działa bezpośrednio w przeglądarce
- Pierwszy start może potrwać chwilę (ładowanie Python)

## Co robi każdy komponent?

### 🐍 **Pyodide** - Python w przeglądarce!
- **Pełny Python** - działa bezpośrednio w przeglądarce
- **Pandas & Numpy** - automatycznie dostępne
- **Zero konfiguracji** - nic nie trzeba instalować
- **Bezpieczny** - izolowane środowisko
- **GitHub Pages ready** - działa na każdym hostingu

### Frontend (w _quarto.yml)
- ✏️ **CodeMirror editor** - profesjonalny edytor kodu
- 🐍 **Integracja z Pyodide** - Python uruchamia się lokalnie
- 📺 **Wyświetlanie wyników** - kolorowe output z błędami
- 💾 **Lokalne zapisywanie** - zmiany w sesji przeglądarki

## Rozwiązywanie problemów

### ❌ "Python jeszcze się ładuje"
- **Przyczyna:** Pyodide dopiero się inicjalizuje
- **Rozwiązanie:** Poczekaj 10-15 sekund i spróbuj ponownie

### ❌ "Błąd ładowania Python"
- **Przyczyna:** Brak połączenia z internetem
- **Rozwiązanie:** Sprawdź połączenie i odśwież stronę

### ❌ "Kod nie działa jak powinien"
- **Pandas/Numpy:** Powinny działać od razu
- **Matplotlib:** Może wymagać dodatkowej konfiguracji
- **Inne biblioteki:** Nie wszystkie są dostępne w Pyodide

## ✅ Bezpieczeństwo

🎉 **Pyodide jest całkowicie bezpieczny!**

- Kod wykonuje się **w przeglądarce użytkownika**
- **Brak dostępu do systemu plików**
- **Izolowane środowisko** - nie ma dostępu do innych stron
- **Idealne na GitHub Pages** - zero ryzyka bezpieczeństwa

## Architektura

```
┌─────────────────────────────────────┐
│           Przeglądarka              │
│  ┌─────────────┐  ┌───────────────┐ │
│  │   Frontend  │  │   Pyodide     │ │
│  │  (Quarto +  │  │  (Python +    │ │
│  │ CodeMirror) │──│ Pandas/Numpy) │ │
│  └─────────────┘  └───────────────┘ │
└─────────────────────────────────────┘
       ↕️ Internet (tylko do pobrania Pyodide)
┌─────────────────────────────────────┐
│          CDN jsdelivr              │
│     (Python libraries)             │
└─────────────────────────────────────┘
```

## Rozszerzenia

### Dodaj nową bibliotekę Pyodide:
1. Sprawdź czy biblioteka jest dostępna: https://pyodide.org/en/stable/usage/packages-in-pyodide.html
2. Dodaj do `initPyodide()` w `_quarto.yml`:
   ```javascript
   await pyodide.loadPackage(["numpy", "pandas", "matplotlib"]);
   ```
3. Rebuild strony: `quarto render`

### Dostępne biblioteki w Pyodide:
- **Data Science:** pandas, numpy, scipy, matplotlib, seaborn
- **ML:** scikit-learn, statsmodels
- **Web:** requests, beautifulsoup4
- **Inne:** pillow, lxml, i wiele więcej!

---

🎉 **Gotowe!** Masz teraz prawdziwy Python w przeglądarce, który działa na GitHub Pages!
