"""A reader's library card, as an HTML snippet for the desk screen."""


def reader_card(name, books_out):
    return f"<div class=card><h2>{__import__('html').escape(name)}</h2><p>{books_out} books out</p></div>"
