import os
import pytest
import library.covers as covers

def test_read_cover_path_traversal():
    base = covers.COVERS_DIR
    # Build a path that points to this test file but is expressed relative to the covers directory
    malicious = os.path.relpath(os.path.abspath(__file__), base)
    # The safe implementation must reject the traversal
    with pytest.raises(ValueError):
        covers.read_cover(malicious)
