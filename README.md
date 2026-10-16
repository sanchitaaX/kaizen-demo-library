# Little Library

A small front-desk toolkit for a neighbourhood library, written with the Python standard library only.

- `library/catalog.py` keeps the book catalogue in SQLite and lists the books by one author.
- `library/printer.py` prints shelf labels through the label script (`python -m library.labels <title>`).
- `library/cards.py` shows a reader's library card on the desk screen.
- `library/covers.py` serves cover images from `library/covers/` by file name.

## Run the tests

No packages to install beyond pytest:

```
python -m pytest -q
```
