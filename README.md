# 🐍 Coding Cheatsheets - Interaktywne protipsy Python & Pandas

Kolekcja praktycznych ściąg z programowania, gdzie możesz **uruchamiać kod bezpośrednio w przeglądarce**! Każda karta zawiera 2–3 konkretne protipsy + mini-zadanie do rozwiązania.

## 🚀 Jak używać (dla kursantów)

### Na GitHub Pages (ZALECANE)
1. **Otwórz stronę:** [link do GitHub Pages]
2. **Wybierz ściągę** z menu Cheatsheets
3. **Kliknij "✏️ Tryb Edycji"** (gdzie dostępny)
4. **Poczekaj 10-15 sekund** aż Python się załaduje
5. **Eksperymentuj z kodem** i klikaj "▶️ Run"!

**✨ Magia:** Python + Pandas działają bezpośrednio w przeglądarce dzięki Pyodide!

## 🛠️ Development (dla autorów)

### Lokalne uruchomienie
```bash
# Zainstaluj Quarto
brew install quarto

# Podgląd na żywo
quarto preview

# Renderowanie do docs/
quarto render
```

### Publikacja z aliasem
```bash
# Alias dla szybkiego render + push
alias qpush="quarto render && git add . && git commit -m 'Update cheatsheets' && git push"

# Użycie
qpush
```

### GitHub Pages setup
1. **Settings → Pages → Source:** `main` branch, `/docs` folder
2. Po pierwszym push strona będzie dostępna pod `https://username.github.io/repo-name`
3. Automatyczne aktualizacje przy każdym push!

## 📁 Struktura projektu
```
.
├── _quarto.yml           # Konfiguracja + Pyodide integration
├── docs/                 # Wyrenderowane pliki (GitHub Pages)
├── index.qmd             # Strona główna
├── cheatsheets/
│   ├── 01-python-basics.qmd      # Python basics (z trybem edycji)
│   └── 02-pandas-filtering.qmd   # Pandas filtering (tylko odczyt)
├── styles.css
└── requirements.txt      # Python dependencies dla Pyodide
```

## ✏️ Dodawanie nowych ściąg

### 1. Utwórz nowy plik
```bash
cp cheatsheets/01-python-basics.qmd cheatsheets/03-new-topic.qmd
```

### 2. Edytuj zawartość
- Zmień tytuł w YAML header
- Dodaj swoje protipsy (2-3 na ściągę)
- Dodaj mini-zadanie na końcu

### 3. Dodaj do nawigacji
W `_quarto.yml` dodaj nowy link:
```yaml
navbar:
  left:
    - text: "Cheatsheets"
      menu:
        - text: "New Topic"
          href: cheatsheets/03-new-topic.qmd
```

### 4. Opublikuj
```bash
qpush  # alias render + commit + push
```

## 🎛️ Konfiguracja trybu edycji

**Tryb edycji (Pyodide) włączony domyślnie na:**
- Python Basics ✅
- Inne nowe ściągi ✅

**Tryb edycji wyłączony na:**
- Stronie głównej (index)
- Pandas Filtering (przykład read-only)

**Aby wyłączyć tryb edycji** na konkretnej stronie, dodaj nazwę do `shouldHideButton` w `_quarto.yml`.

## 🐍 Dostępne biblioteki w Pyodide

- **Data Science:** pandas, numpy, scipy, matplotlib, seaborn
- **ML:** scikit-learn, statsmodels  
- **Web:** requests, beautifulsoup4
- **Inne:** pillow, lxml, sympy

**Pełna lista:** https://pyodide.org/en/stable/usage/packages-in-pyodide.html

## 🚨 Rozwiązywanie problemów

**"Python jeszcze się ładuje"**
- Poczekaj 10-15 sekund i spróbuj ponownie
- Przy pierwszym uruchomieniu Pyodide pobiera biblioteki z CDN

**"Błąd ładowania Python"**  
- Sprawdź połączenie internetowe
- Odśwież stronę (F5)

**"Kod nie działa"**
- Sprawdź czy używasz obsługiwanych bibliotek
- Matplotlib może wymagać dodatkowej konfiguracji