import pytest

from library.covers import list_covers, read_cover


def test_lists_covers():
    assert list_covers() == ["dune.svg", "emma.svg"]


def test_reads_a_cover():
    assert read_cover("dune.svg").startswith(b"<svg")


def test_missing_cover_raises():
    with pytest.raises(OSError):
        read_cover("nope.svg")
