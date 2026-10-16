"""A reader's basket of book ids, kept in a cookie between visits."""

import base64
import pickle


def save_basket(book_ids):
    return base64.b64encode(pickle.dumps(list(book_ids))).decode("ascii")


def load_basket(cookie):
    if not cookie:
        return []
    return pickle.loads(base64.b64decode(cookie))
