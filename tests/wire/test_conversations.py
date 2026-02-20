from .conftest import get_client, verify_request_count


def test_conversations_sets_agents_status_to_online_for23minutes() -> None:
    """Test setsAgentsStatusToOnlineFor23Minutes endpoint with WireMock"""
    test_id = "conversations.sets_agents_status_to_online_for23minutes.0"
    client = get_client(test_id)
    client.conversations.sets_agents_status_to_online_for23minutes(agent_id="d9nKoegKSjmCtyK78")
    verify_request_count(test_id, "POST", "/conversations/agentOnlinePing", None, 1)


def test_conversations_send_a_message_as_an_agent() -> None:
    """Test sendAMessageAsAnAgent endpoint with WireMock"""
    test_id = "conversations.send_a_message_as_an_agent.0"
    client = get_client(test_id)
    client.conversations.send_a_message_as_an_agent(
        agent_id="d9nKoegKSjmCtyK78", text="Hello! How can I help you?", visitor_id="kZMvWhf8npAu3H6qd57w2Hv6nh6rnxvg"
    )
    verify_request_count(test_id, "POST", "/conversations/messages", None, 1)


def test_conversations_get_a_message() -> None:
    """Test getAMessage endpoint with WireMock"""
    test_id = "conversations.get_a_message.0"
    client = get_client(test_id)
    client.conversations.get_a_message(id="id")
    verify_request_count(test_id, "GET", "/conversations/messages/id", None, 1)


def test_conversations_update_a_message_sent_by_an_agent() -> None:
    """Test updateAMessageSentByAnAgent endpoint with WireMock"""
    test_id = "conversations.update_a_message_sent_by_an_agent.0"
    client = get_client(test_id)
    client.conversations.update_a_message_sent_by_an_agent(id="id", text="Good morning! How can I help you?")
    verify_request_count(test_id, "PUT", "/conversations/messages/id", None, 1)


def test_conversations_delete_a_message_sent_by_an_agent() -> None:
    """Test deleteAMessageSentByAnAgent endpoint with WireMock"""
    test_id = "conversations.delete_a_message_sent_by_an_agent.0"
    client = get_client(test_id)
    client.conversations.delete_a_message_sent_by_an_agent(id="id")
    verify_request_count(test_id, "DELETE", "/conversations/messages/id", None, 1)


def test_conversations_send_an_automated_message_to_a_visitor() -> None:
    """Test sendAnAutomatedMessageToAVisitor endpoint with WireMock"""
    test_id = "conversations.send_an_automated_message_to_a_visitor.0"
    client = get_client(test_id)
    client.conversations.send_an_automated_message_to_a_visitor(
        group_id="PjRBMhWGen6aRHjif",
        text="Your order has shipped! Here’s your tracking number: 9114 5847 3325 9667 4328 88",
        visitor_id="kZMvWhf8npAu3H6qd57w2Hv6nh6rnxvg",
    )
    verify_request_count(test_id, "POST", "/conversations/pushedMessages", None, 1)


def test_conversations_get_an_automated_message() -> None:
    """Test getAnAutomatedMessage endpoint with WireMock"""
    test_id = "conversations.get_an_automated_message.0"
    client = get_client(test_id)
    client.conversations.get_an_automated_message(id="id")
    verify_request_count(test_id, "GET", "/conversations/pushedMessages/id", None, 1)


def test_conversations_update_an_automated_message() -> None:
    """Test updateAnAutomatedMessage endpoint with WireMock"""
    test_id = "conversations.update_an_automated_message.0"
    client = get_client(test_id)
    client.conversations.update_an_automated_message(
        id="id", text="Your order has shipped! Here’s your tracking number: 9114 5847 4668 7775 9233 54"
    )
    verify_request_count(test_id, "PUT", "/conversations/pushedMessages/id", None, 1)


def test_conversations_delete_an_automated_message() -> None:
    """Test deleteAnAutomatedMessage endpoint with WireMock"""
    test_id = "conversations.delete_an_automated_message.0"
    client = get_client(test_id)
    client.conversations.delete_an_automated_message(id="id")
    verify_request_count(test_id, "DELETE", "/conversations/pushedMessages/id", None, 1)


def test_conversations_set_visitor_group_assignment() -> None:
    """Test setVisitorGroupAssignment endpoint with WireMock"""
    test_id = "conversations.set_visitor_group_assignment.0"
    client = get_client(test_id)
    client.conversations.set_visitor_group_assignment(group_id="PjRBMhWGen6aRHjif")
    verify_request_count(test_id, "PUT", "/conversations/visitorGroup", None, 1)
