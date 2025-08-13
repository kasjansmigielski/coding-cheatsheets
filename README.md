# Coding Cheatsheets (Quarto)

Krótka kolekcja ściąg z Pythona i Pandas w Quarto. Każda karta to 2–3 protipy + mini-zadanie.

## Jak uruchomić lokalnie (macOS)
1. Zainstaluj Quarto:
   ```bash
   brew install quarto
   ```
2. W katalogu projektu uruchom podgląd na żywo:
   ```bash
   quarto preview
   ```
3. Wyrenderuj do statycznego HTML (do folderu `docs/`):
   ```bash
   quarto render
   ```

## Publikacja na GitHub Pages (najprościej)
1. Zrenderuj stronę: `quarto render` (pliki trafią do `docs/`).
2. W repozytorium włącz **Settings → Pages → Source: `main` / `docs`**.
3. Po chwili strona będzie dostępna pod adresem GitHub Pages.

## Struktura
```
.
├── _quarto.yml
├── docs/             # (po renderze)
├── index.qmd
├── cheatsheets/
│   ├── 01-python-basics.qmd
│   └── 02-pandas-filtering.qmd
└── styles.css
```

## Edycja / Dodawanie nowych kart
- Sklonuj plik `cheatsheets/01-python-basics.qmd` jako `03-...qmd`, zmień tytuł i treść.
- Link dodaj do nawigacji w `_quarto.yml`.
- `quarto render` i opublikuj.