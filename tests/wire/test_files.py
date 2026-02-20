from .conftest import get_client, verify_request_count


def test_files_get_all_files() -> None:
    """Test getAllFiles endpoint with WireMock"""
    test_id = "files.get_all_files.0"
    client = get_client(test_id)
    client.files.get_all_files()
    verify_request_count(test_id, "GET", "/crm/files", None, 1)


def test_files_upload_a_file() -> None:
    """Test uploadAFile endpoint with WireMock"""
    test_id = "files.upload_a_file.0"
    client = get_client(test_id)
    client.files.upload_a_file(file="example_file")
    verify_request_count(test_id, "POST", "/crm/files", None, 1)


def test_files_download_a_file() -> None:
    """Test downloadAFile endpoint with WireMock"""
    test_id = "files.download_a_file.0"
    client = get_client(test_id)
    client.files.download_a_file(id="id")
    verify_request_count(test_id, "GET", "/crm/files/id", None, 1)


def test_files_delete_a_file() -> None:
    """Test deleteAFile endpoint with WireMock"""
    test_id = "files.delete_a_file.0"
    client = get_client(test_id)
    client.files.delete_a_file(id="id")
    verify_request_count(test_id, "DELETE", "/crm/files/id", None, 1)


def test_files_get_file_details() -> None:
    """Test getFileDetails endpoint with WireMock"""
    test_id = "files.get_file_details.0"
    client = get_client(test_id)
    client.files.get_file_details(id="id")
    verify_request_count(test_id, "GET", "/crm/files/id/data", None, 1)
