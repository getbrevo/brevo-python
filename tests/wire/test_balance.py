from .conftest import get_client, verify_request_count


def test_balance_get_active_balances_api() -> None:
    """Test getActiveBalancesApi endpoint with WireMock"""
    test_id = "balance.get_active_balances_api.0"
    client = get_client(test_id)
    client.balance.get_active_balances_api(pid="pid", contact_id=1, balance_definition_id="balance_definition_id")
    verify_request_count(
        test_id,
        "GET",
        "/loyalty/balance/programs/pid/active-balance",
        {"contact_id": "1", "balance_definition_id": "balance_definition_id"},
        1,
    )


def test_balance_get_balance_definition_list() -> None:
    """Test getBalanceDefinitionList endpoint with WireMock"""
    test_id = "balance.get_balance_definition_list.0"
    client = get_client(test_id)
    client.balance.get_balance_definition_list(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/balance/programs/pid/balance-definitions", None, 1)


def test_balance_create_balance_definition() -> None:
    """Test createBalanceDefinition endpoint with WireMock"""
    test_id = "balance.create_balance_definition.0"
    client = get_client(test_id)
    client.balance.create_balance_definition(pid="pid", name="name", unit="POINTS")
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/balance-definitions", None, 1)


def test_balance_get_balance_definition() -> None:
    """Test getBalanceDefinition endpoint with WireMock"""
    test_id = "balance.get_balance_definition.0"
    client = get_client(test_id)
    client.balance.get_balance_definition(pid="pid", bdid="bdid")
    verify_request_count(test_id, "GET", "/loyalty/balance/programs/pid/balance-definitions/bdid", None, 1)


def test_balance_update_balance_definition() -> None:
    """Test updateBalanceDefinition endpoint with WireMock"""
    test_id = "balance.update_balance_definition.0"
    client = get_client(test_id)
    client.balance.update_balance_definition(pid="pid", bdid="bdid", name="name", unit="POINTS")
    verify_request_count(test_id, "PUT", "/loyalty/balance/programs/pid/balance-definitions/bdid", None, 1)


def test_balance_delete_balance_definition() -> None:
    """Test deleteBalanceDefinition endpoint with WireMock"""
    test_id = "balance.delete_balance_definition.0"
    client = get_client(test_id)
    client.balance.delete_balance_definition(pid="pid", bdid="bdid")
    verify_request_count(test_id, "DELETE", "/loyalty/balance/programs/pid/balance-definitions/bdid", None, 1)


def test_balance_create_balance_limit() -> None:
    """Test createBalanceLimit endpoint with WireMock"""
    test_id = "balance.create_balance_limit.0"
    client = get_client(test_id)
    client.balance.create_balance_limit(
        pid="pid",
        bdid="bdid",
        constraint_type="transaction",
        duration_unit="day",
        duration_value=1,
        transaction_type="credit",
        value=1,
    )
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/balance-definitions/bdid/limits", None, 1)


def test_balance_get_balance_limit() -> None:
    """Test getBalanceLimit endpoint with WireMock"""
    test_id = "balance.get_balance_limit.0"
    client = get_client(test_id)
    client.balance.get_balance_limit(pid="pid", bdid="bdid", blid="blid")
    verify_request_count(test_id, "GET", "/loyalty/balance/programs/pid/balance-definitions/bdid/limits/blid", None, 1)


def test_balance_update_balance_limit() -> None:
    """Test updateBalanceLimit endpoint with WireMock"""
    test_id = "balance.update_balance_limit.0"
    client = get_client(test_id)
    client.balance.update_balance_limit(
        pid="pid",
        bdid="bdid",
        blid="blid",
        constraint_type="transaction",
        duration_unit="day",
        duration_value=1,
        transaction_type="credit",
        value=1,
    )
    verify_request_count(test_id, "PUT", "/loyalty/balance/programs/pid/balance-definitions/bdid/limits/blid", None, 1)


def test_balance_delete_balance_limit() -> None:
    """Test deleteBalanceLimit endpoint with WireMock"""
    test_id = "balance.delete_balance_limit.0"
    client = get_client(test_id)
    client.balance.delete_balance_limit(pid="pid", bdid="bdid", blid="blid")
    verify_request_count(
        test_id, "DELETE", "/loyalty/balance/programs/pid/balance-definitions/bdid/limits/blid", None, 1
    )


def test_balance_get_contact_balances() -> None:
    """Test getContactBalances endpoint with WireMock"""
    test_id = "balance.get_contact_balances.0"
    client = get_client(test_id)
    client.balance.get_contact_balances(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/balance/programs/pid/contact-balances", None, 1)


def test_balance_create_balance_order() -> None:
    """Test createBalanceOrder endpoint with WireMock"""
    test_id = "balance.create_balance_order.0"
    client = get_client(test_id)
    client.balance.create_balance_order(
        pid="pid",
        amount=1.1,
        balance_definition_id="balanceDefinitionId",
        contact_id=1,
        due_at="dueAt",
        source="source",
    )
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/create-order", None, 1)


def test_balance_get_subscription_balances() -> None:
    """Test getSubscriptionBalances endpoint with WireMock"""
    test_id = "balance.get_subscription_balances.0"
    client = get_client(test_id)
    client.balance.get_subscription_balances(pid="pid", cid="cid")
    verify_request_count(test_id, "GET", "/loyalty/balance/programs/pid/subscriptions/cid/balances", None, 1)


def test_balance_create_subscription_balances() -> None:
    """Test createSubscriptionBalances endpoint with WireMock"""
    test_id = "balance.create_subscription_balances.0"
    client = get_client(test_id)
    client.balance.create_subscription_balances(pid="pid", cid="cid", balance_definition_id="balanceDefinitionId")
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/subscriptions/cid/balances", None, 1)


def test_balance_get_transaction_history_api() -> None:
    """Test getTransactionHistoryApi endpoint with WireMock"""
    test_id = "balance.get_transaction_history_api.0"
    client = get_client(test_id)
    client.balance.get_transaction_history_api(pid="pid", contact_id=1, balance_definition_id="balance_definition_id")
    verify_request_count(
        test_id,
        "GET",
        "/loyalty/balance/programs/pid/transaction-history",
        {"contact_id": "1", "balance_definition_id": "balance_definition_id"},
        1,
    )


def test_balance_begin_transaction() -> None:
    """Test beginTransaction endpoint with WireMock"""
    test_id = "balance.begin_transaction.0"
    client = get_client(test_id)
    client.balance.begin_transaction(pid="pid", amount=1.1, balance_definition_id="balanceDefinitionId")
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/transactions", None, 1)


def test_balance_cancel_transaction() -> None:
    """Test cancelTransaction endpoint with WireMock"""
    test_id = "balance.cancel_transaction.0"
    client = get_client(test_id)
    client.balance.cancel_transaction(pid="pid", tid="tid")
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/transactions/tid/cancel", None, 1)


def test_balance_complete_transaction() -> None:
    """Test completeTransaction endpoint with WireMock"""
    test_id = "balance.complete_transaction.0"
    client = get_client(test_id)
    client.balance.complete_transaction(pid="pid", tid="tid")
    verify_request_count(test_id, "POST", "/loyalty/balance/programs/pid/transactions/tid/complete", None, 1)
