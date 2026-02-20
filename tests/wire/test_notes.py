from .conftest import get_client, verify_request_count


def test_notes_get_all_notes() -> None:
    """Test getAllNotes endpoint with WireMock"""
    test_id = "notes.get_all_notes.0"
    client = get_client(test_id)
    client.notes.get_all_notes()
    verify_request_count(test_id, "GET", "/crm/notes", None, 1)


def test_notes_create_a_note() -> None:
    """Test createANote endpoint with WireMock"""
    test_id = "notes.create_a_note.0"
    client = get_client(test_id)
    client.notes.create_a_note(text="In communication with client_dev for resolution of queries.")
    verify_request_count(test_id, "POST", "/crm/notes", None, 1)


def test_notes_get_a_note() -> None:
    """Test getANote endpoint with WireMock"""
    test_id = "notes.get_a_note.0"
    client = get_client(test_id)
    client.notes.get_a_note(id="id")
    verify_request_count(test_id, "GET", "/crm/notes/id", None, 1)


def test_notes_delete_a_note() -> None:
    """Test deleteANote endpoint with WireMock"""
    test_id = "notes.delete_a_note.0"
    client = get_client(test_id)
    client.notes.delete_a_note(id="id")
    verify_request_count(test_id, "DELETE", "/crm/notes/id", None, 1)


def test_notes_update_a_note() -> None:
    """Test updateANote endpoint with WireMock"""
    test_id = "notes.update_a_note.0"
    client = get_client(test_id)
    client.notes.update_a_note(id="id", text="In communication with client_dev for resolution of queries.")
    verify_request_count(test_id, "PATCH", "/crm/notes/id", None, 1)
