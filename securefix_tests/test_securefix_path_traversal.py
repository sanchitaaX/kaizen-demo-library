import os
import pytest
import library.covers as covers

def test_read_cover_path_traversal():
    # Build a traversal name that points to this test file itself
    malicious_name = os.path.relpath(os.path.abspath(__file__), covers.COVERS_DIR)
    # Ensure the name indeed contains a traversal component
    assert ".." in malicious_name, "Test setup error: malicious_name does not traverse"
    # The safe implementation should reject the traversal and raise ValueError
    with pytest.raises(ValueError):
        covers.read_cover(malicious_name)
