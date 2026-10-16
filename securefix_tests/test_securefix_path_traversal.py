import os, pytest
import library.covers as covers

def test_read_cover_path_traversal():
    # Resolve a path to this test file that is outside the covers directory
    outside_path = os.path.abspath(__file__)
    malicious_name = os.path.relpath(outside_path, covers.COVERS_DIR)
    # The vulnerable implementation would read the test file and return its contents.
    # The fixed implementation should raise a ValueError (or any exception) for invalid traversal.
    with pytest.raises(ValueError, match="Invalid cover name"):
        covers.read_cover(malicious_name)
