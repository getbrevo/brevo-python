from .conftest import get_client, verify_request_count


def test_process_get_processes() -> None:
    """Test getProcesses endpoint with WireMock"""
    test_id = "process.get_processes.0"
    client = get_client(test_id)
    client.process.get_processes()
    verify_request_count(test_id, "GET", "/processes", None, 1)


def test_process_get_process() -> None:
    """Test getProcess endpoint with WireMock"""
    test_id = "process.get_process.0"
    client = get_client(test_id)
    client.process.get_process(process_id=1000000)
    verify_request_count(test_id, "GET", "/processes/1000000", None, 1)
