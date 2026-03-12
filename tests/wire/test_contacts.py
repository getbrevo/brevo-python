from .conftest import get_client, verify_request_count


def test_contacts_get_contacts() -> None:
    """Test getContacts endpoint with WireMock"""
    test_id = "contacts.get_contacts.0"
    client = get_client(test_id)
    client.contacts.get_contacts()
    verify_request_count(test_id, "GET", "/contacts", None, 1)


def test_contacts_create_contact() -> None:
    """Test createContact endpoint with WireMock"""
    test_id = "contacts.create_contact.0"
    client = get_client(test_id)
    client.contacts.create_contact()
    verify_request_count(test_id, "POST", "/contacts", None, 1)


def test_contacts_get_attributes() -> None:
    """Test getAttributes endpoint with WireMock"""
    test_id = "contacts.get_attributes.0"
    client = get_client(test_id)
    client.contacts.get_attributes()
    verify_request_count(test_id, "GET", "/contacts/attributes", None, 1)


def test_contacts_create_attribute() -> None:
    """Test createAttribute endpoint with WireMock"""
    test_id = "contacts.create_attribute.0"
    client = get_client(test_id)
    client.contacts.create_attribute(attribute_category="normal", attribute_name="attributeName")
    verify_request_count(test_id, "POST", "/contacts/attributes/normal/attributeName", None, 1)


def test_contacts_update_attribute() -> None:
    """Test updateAttribute endpoint with WireMock"""
    test_id = "contacts.update_attribute.0"
    client = get_client(test_id)
    client.contacts.update_attribute(attribute_category="category", attribute_name="attributeName")
    verify_request_count(test_id, "PUT", "/contacts/attributes/category/attributeName", None, 1)


def test_contacts_delete_attribute() -> None:
    """Test deleteAttribute endpoint with WireMock"""
    test_id = "contacts.delete_attribute.0"
    client = get_client(test_id)
    client.contacts.delete_attribute(attribute_category="normal", attribute_name="attributeName")
    verify_request_count(test_id, "DELETE", "/contacts/attributes/normal/attributeName", None, 1)


def test_contacts_delete_multi_attribute_options() -> None:
    """Test deleteMultiAttributeOptions endpoint with WireMock"""
    test_id = "contacts.delete_multi_attribute_options.0"
    client = get_client(test_id)
    client.contacts.delete_multi_attribute_options(
        multiple_choice_attribute="multipleChoiceAttribute",
        multiple_choice_attribute_option="multipleChoiceAttributeOption",
    )
    verify_request_count(
        test_id,
        "DELETE",
        "/contacts/attributes/multiple-choice/multipleChoiceAttribute/multipleChoiceAttributeOption",
        None,
        1,
    )


def test_contacts_update_batch_contacts() -> None:
    """Test updateBatchContacts endpoint with WireMock"""
    test_id = "contacts.update_batch_contacts.0"
    client = get_client(test_id)
    client.contacts.update_batch_contacts()
    verify_request_count(test_id, "POST", "/contacts/batch", None, 1)


def test_contacts_create_doi_contact() -> None:
    """Test createDoiContact endpoint with WireMock"""
    test_id = "contacts.create_doi_contact.0"
    client = get_client(test_id)
    client.contacts.create_doi_contact(
        email="elly@example.com", include_list_ids=[36], redirection_url="http://requestb.in/173lyyx1", template_id=2
    )
    verify_request_count(test_id, "POST", "/contacts/doubleOptinConfirmation", None, 1)


def test_contacts_request_contact_export() -> None:
    """Test requestContactExport endpoint with WireMock"""
    test_id = "contacts.request_contact_export.0"
    client = get_client(test_id)
    client.contacts.request_contact_export(custom_contact_filter={})
    verify_request_count(test_id, "POST", "/contacts/export", None, 1)


def test_contacts_get_folders() -> None:
    """Test getFolders endpoint with WireMock"""
    test_id = "contacts.get_folders.0"
    client = get_client(test_id)
    client.contacts.get_folders()
    verify_request_count(test_id, "GET", "/contacts/folders", None, 1)


def test_contacts_create_folder() -> None:
    """Test createFolder endpoint with WireMock"""
    test_id = "contacts.create_folder.0"
    client = get_client(test_id)
    client.contacts.create_folder()
    verify_request_count(test_id, "POST", "/contacts/folders", None, 1)


def test_contacts_get_folder() -> None:
    """Test getFolder endpoint with WireMock"""
    test_id = "contacts.get_folder.0"
    client = get_client(test_id)
    client.contacts.get_folder(folder_id=1000000)
    verify_request_count(test_id, "GET", "/contacts/folders/1000000", None, 1)


def test_contacts_update_folder() -> None:
    """Test updateFolder endpoint with WireMock"""
    test_id = "contacts.update_folder.0"
    client = get_client(test_id)
    client.contacts.update_folder(folder_id=1000000)
    verify_request_count(test_id, "PUT", "/contacts/folders/1000000", None, 1)


def test_contacts_delete_folder() -> None:
    """Test deleteFolder endpoint with WireMock"""
    test_id = "contacts.delete_folder.0"
    client = get_client(test_id)
    client.contacts.delete_folder(folder_id=1000000)
    verify_request_count(test_id, "DELETE", "/contacts/folders/1000000", None, 1)


def test_contacts_get_folder_lists() -> None:
    """Test getFolderLists endpoint with WireMock"""
    test_id = "contacts.get_folder_lists.0"
    client = get_client(test_id)
    client.contacts.get_folder_lists(folder_id=1000000)
    verify_request_count(test_id, "GET", "/contacts/folders/1000000/lists", None, 1)


def test_contacts_import_contacts() -> None:
    """Test importContacts endpoint with WireMock"""
    test_id = "contacts.import_contacts.0"
    client = get_client(test_id)
    client.contacts.import_contacts()
    verify_request_count(test_id, "POST", "/contacts/import", None, 1)


def test_contacts_get_lists() -> None:
    """Test getLists endpoint with WireMock"""
    test_id = "contacts.get_lists.0"
    client = get_client(test_id)
    client.contacts.get_lists()
    verify_request_count(test_id, "GET", "/contacts/lists", None, 1)


def test_contacts_create_list() -> None:
    """Test createList endpoint with WireMock"""
    test_id = "contacts.create_list.0"
    client = get_client(test_id)
    client.contacts.create_list(folder_id=2, name="Magento Customer - ES")
    verify_request_count(test_id, "POST", "/contacts/lists", None, 1)


def test_contacts_get_list() -> None:
    """Test getList endpoint with WireMock"""
    test_id = "contacts.get_list.0"
    client = get_client(test_id)
    client.contacts.get_list(list_id=1000000)
    verify_request_count(test_id, "GET", "/contacts/lists/1000000", None, 1)


def test_contacts_update_list() -> None:
    """Test updateList endpoint with WireMock"""
    test_id = "contacts.update_list.0"
    client = get_client(test_id)
    client.contacts.update_list(list_id=1000000)
    verify_request_count(test_id, "PUT", "/contacts/lists/1000000", None, 1)


def test_contacts_delete_list() -> None:
    """Test deleteList endpoint with WireMock"""
    test_id = "contacts.delete_list.0"
    client = get_client(test_id)
    client.contacts.delete_list(list_id=1000000)
    verify_request_count(test_id, "DELETE", "/contacts/lists/1000000", None, 1)


def test_contacts_get_contacts_from_list() -> None:
    """Test getContactsFromList endpoint with WireMock"""
    test_id = "contacts.get_contacts_from_list.0"
    client = get_client(test_id)
    client.contacts.get_contacts_from_list(list_id=1000000)
    verify_request_count(test_id, "GET", "/contacts/lists/1000000/contacts", None, 1)


def test_contacts_add_contact_to_list() -> None:
    """Test addContactToList endpoint with WireMock"""
    test_id = "contacts.add_contact_to_list.0"
    client = get_client(test_id)
    client.contacts.add_contact_to_list(
        list_id=1000000, request={"emails": ["jeff32@example.com", "jim56@example.com"]}
    )
    verify_request_count(test_id, "POST", "/contacts/lists/1000000/contacts/add", None, 1)


def test_contacts_remove_contact_from_list() -> None:
    """Test removeContactFromList endpoint with WireMock"""
    test_id = "contacts.remove_contact_from_list.0"
    client = get_client(test_id)
    client.contacts.remove_contact_from_list(list_id=1000000, request={})
    verify_request_count(test_id, "POST", "/contacts/lists/1000000/contacts/remove", None, 1)


def test_contacts_get_segments() -> None:
    """Test getSegments endpoint with WireMock"""
    test_id = "contacts.get_segments.0"
    client = get_client(test_id)
    client.contacts.get_segments()
    verify_request_count(test_id, "GET", "/contacts/segments", None, 1)


def test_contacts_get_contact_info() -> None:
    """Test getContactInfo endpoint with WireMock"""
    test_id = "contacts.get_contact_info.0"
    client = get_client(test_id)
    client.contacts.get_contact_info(identifier="identifier")
    verify_request_count(test_id, "GET", "/contacts/identifier", None, 1)


def test_contacts_update_contact() -> None:
    """Test updateContact endpoint with WireMock"""
    test_id = "contacts.update_contact.0"
    client = get_client(test_id)
    client.contacts.update_contact(identifier="identifier")
    verify_request_count(test_id, "PUT", "/contacts/identifier", None, 1)


def test_contacts_delete_contact() -> None:
    """Test deleteContact endpoint with WireMock"""
    test_id = "contacts.delete_contact.0"
    client = get_client(test_id)
    client.contacts.delete_contact(identifier="identifier")
    verify_request_count(test_id, "DELETE", "/contacts/identifier", None, 1)


def test_contacts_get_contact_stats() -> None:
    """Test getContactStats endpoint with WireMock"""
    test_id = "contacts.get_contact_stats.0"
    client = get_client(test_id)
    client.contacts.get_contact_stats(identifier="identifier")
    verify_request_count(test_id, "GET", "/contacts/identifier/campaignStats", None, 1)
