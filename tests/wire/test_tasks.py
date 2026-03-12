from datetime import datetime

from .conftest import get_client, verify_request_count


def test_tasks_get_all_tasks() -> None:
    """Test getAllTasks endpoint with WireMock"""
    test_id = "tasks.get_all_tasks.0"
    client = get_client(test_id)
    client.tasks.get_all_tasks(sort_by="name")
    verify_request_count(test_id, "GET", "/crm/tasks", {"sortBy": "name"}, 1)


def test_tasks_create_a_task() -> None:
    """Test createATask endpoint with WireMock"""
    test_id = "tasks.create_a_task.0"
    client = get_client(test_id)
    client.tasks.create_a_task(
        date=datetime.fromisoformat("2021-11-01T17:44:54+00:00"),
        name="Task: Connect with client_dev",
        task_type_id="61a5cd07ca1347c82306ad09",
    )
    verify_request_count(test_id, "POST", "/crm/tasks", None, 1)


def test_tasks_get_a_task() -> None:
    """Test getATask endpoint with WireMock"""
    test_id = "tasks.get_a_task.0"
    client = get_client(test_id)
    client.tasks.get_a_task(id="id")
    verify_request_count(test_id, "GET", "/crm/tasks/id", None, 1)


def test_tasks_delete_a_task() -> None:
    """Test deleteATask endpoint with WireMock"""
    test_id = "tasks.delete_a_task.0"
    client = get_client(test_id)
    client.tasks.delete_a_task(id="id")
    verify_request_count(test_id, "DELETE", "/crm/tasks/id", None, 1)


def test_tasks_update_a_task() -> None:
    """Test updateATask endpoint with WireMock"""
    test_id = "tasks.update_a_task.0"
    client = get_client(test_id)
    client.tasks.update_a_task(id="id")
    verify_request_count(test_id, "PATCH", "/crm/tasks/id", None, 1)


def test_tasks_get_all_task_types() -> None:
    """Test getAllTaskTypes endpoint with WireMock"""
    test_id = "tasks.get_all_task_types.0"
    client = get_client(test_id)
    client.tasks.get_all_task_types()
    verify_request_count(test_id, "GET", "/crm/tasktypes", None, 1)
