from .conftest import get_client, verify_request_count


def test_customObjects_upsertrecords() -> None:
    """Test upsertrecords endpoint with WireMock"""
    test_id = "custom_objects.upsertrecords.0"
    client = get_client(test_id)
    client.custom_objects.upsertrecords(object_type="vehicle", records=[{}])
    verify_request_count(test_id, "POST", "/objects/vehicle/batch/upsert", None, 1)


def test_customObjects_getrecords() -> None:
    """Test getrecords endpoint with WireMock"""
    test_id = "custom_objects.getrecords.0"
    client = get_client(test_id)
    client.custom_objects.getrecords(object_type="vehicle", limit=1000000, page_num=1000000)
    verify_request_count(test_id, "GET", "/objects/vehicle/records", {"limit": "1000000", "page_num": "1000000"}, 1)


def test_customObjects_batch_delete_object_records() -> None:
    """Test batchDeleteObjectRecords endpoint with WireMock"""
    test_id = "custom_objects.batch_delete_object_records.0"
    client = get_client(test_id)
    client.custom_objects.batch_delete_object_records(object_type="vehicle", identifiers={})
    verify_request_count(test_id, "POST", "/objects/vehicle/batch/delete", None, 1)
