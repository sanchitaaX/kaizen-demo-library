"""Prints the shelf label of one book: python -m library.labels <title>"""

import sys

from library.catalog import BOOKS


def main(argv):
    title = " ".join(argv[1:]).strip()
    for _id, name, author, year in BOOKS:
        if name.lower() == title.lower():
            print(f"{name} | {author} | {year}")
            return 0
    print("not on the shelves")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
