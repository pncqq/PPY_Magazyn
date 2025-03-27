# 📊 PPY_Magazyn

Prosty system zarządzania magazynem napisany w Pythonie. Umożliwia zarządzanie produktami, ich wyszukiwanie, aktualizację, usuwanie oraz generowanie raportów — wszystko z poziomu konsoli.

## 📂 Zawartość repozytorium

- `main.py` – główny plik uruchamiający aplikację (menu konsolowe)
- `product.py` – klasa reprezentująca produkt
- `warehouse_managment_system.py` – logika systemu magazynowego
- `db/` – folder z bazą danych (plik SQLite)
- `.idea/`, `__pycache__/` – pliki środowiskowe

## ⚙️ Technologie

- Python 3.x
- SQLite3 (wbudowana baza danych)

## 🧠 Funkcjonalności

1. **Dodawanie produktów**:
   - Unikalny ID, nazwa, opis, cena, ilość
2. **Wyszukiwanie produktów**:
   - Po ID lub nazwie (uwzględnia podobieństwo)
3. **Aktualizacja stanu magazynowego**:
   - Zmiana ilości, ceny, opisu itd.
4. **Generowanie raportu**:
   - Lista produktów z ID, nazwą, ilością i ceną
5. **Usuwanie produktów** *(dodatkowo)*
6. **Obsługa błędów**:
   - Sprawdzanie duplikatów, braków, niepoprawnych danych

## 🚀 Jak uruchomić

1. Sklonuj repo:
```bash
git clone https://github.com/pncqq/PPY_Magazyn.git
cd PPY_Magazyn
```

2. Uruchom aplikację:
```bash
python main.py
```

> 🔎 Program automatycznie utworzy plik bazy danych w folderze `db/`, jeśli jeszcze nie istnieje.

## 📈 Przykładowe rozszerzenia

- Filtrowanie produktów według ceny/ilości
- Sortowanie listy produktów
- Eksport do CSV
- GUI z użyciem np. Tkinter

## 👨‍💼 Autor
**Filip Michalski**  
Projekt wykonany w ramach kursu PPY (Programowanie w Pythonie).  
Ćwiczenie z zarządzania danymi, relacyjnych baz danych oraz programowania proceduralnego/obiektowego.
