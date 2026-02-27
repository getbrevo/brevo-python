from datetime import datetime

from .conftest import get_client, verify_request_count


def test_ecommerce_get_categories() -> None:
    """Test getCategories endpoint with WireMock"""
    test_id = "ecommerce.get_categories.0"
    client = get_client(test_id)
    client.ecommerce.get_categories()
    verify_request_count(test_id, "GET", "/categories", None, 1)


def test_ecommerce_create_update_category() -> None:
    """Test createUpdateCategory endpoint with WireMock"""
    test_id = "ecommerce.create_update_category.0"
    client = get_client(test_id)
    client.ecommerce.create_update_category(id="CAT123")
    verify_request_count(test_id, "POST", "/categories", None, 1)


def test_ecommerce_create_update_batch_category() -> None:
    """Test createUpdateBatchCategory endpoint with WireMock"""
    test_id = "ecommerce.create_update_batch_category.0"
    client = get_client(test_id)
    client.ecommerce.create_update_batch_category(categories=[{"id": "CAT123"}])
    verify_request_count(test_id, "POST", "/categories/batch", None, 1)


def test_ecommerce_get_category_info() -> None:
    """Test getCategoryInfo endpoint with WireMock"""
    test_id = "ecommerce.get_category_info.0"
    client = get_client(test_id)
    client.ecommerce.get_category_info(id="id")
    verify_request_count(test_id, "GET", "/categories/id", None, 1)


def test_ecommerce_activate_the_e_commerce_app() -> None:
    """Test activateTheECommerceApp endpoint with WireMock"""
    test_id = "ecommerce.activate_the_e_commerce_app.0"
    client = get_client(test_id)
    client.ecommerce.activate_the_e_commerce_app()
    verify_request_count(test_id, "POST", "/ecommerce/activate", None, 1)


def test_ecommerce_get_attribution_metrics_for_one_or_more_brevo_campaigns_or_workflows() -> None:
    """Test getAttributionMetricsForOneOrMoreBrevoCampaignsOrWorkflows endpoint with WireMock"""
    test_id = "ecommerce.get_attribution_metrics_for_one_or_more_brevo_campaigns_or_workflows.0"
    client = get_client(test_id)
    client.ecommerce.get_attribution_metrics_for_one_or_more_brevo_campaigns_or_workflows(
        period_from=datetime.fromisoformat("2022-01-02T00:00:00+00:00"),
        period_to=datetime.fromisoformat("2022-01-03T00:00:00+00:00"),
    )
    verify_request_count(
        test_id,
        "GET",
        "/ecommerce/attribution/metrics",
        {"periodFrom": "2022-01-02T00:00:00Z", "periodTo": "2022-01-03T00:00:00Z"},
        1,
    )


def test_ecommerce_get_detailed_attribution_metrics_for_a_single_brevo_campaign_or_workflow() -> None:
    """Test getDetailedAttributionMetricsForASingleBrevoCampaignOrWorkflow endpoint with WireMock"""
    test_id = "ecommerce.get_detailed_attribution_metrics_for_a_single_brevo_campaign_or_workflow.0"
    client = get_client(test_id)
    client.ecommerce.get_detailed_attribution_metrics_for_a_single_brevo_campaign_or_workflow(
        conversion_source="email_campaign", conversion_source_id="sale"
    )
    verify_request_count(test_id, "GET", "/ecommerce/attribution/metrics/email_campaign/sale", None, 1)


def test_ecommerce_get_attributed_product_sales_for_a_single_brevo_campaign_or_workflow() -> None:
    """Test getAttributedProductSalesForASingleBrevoCampaignOrWorkflow endpoint with WireMock"""
    test_id = "ecommerce.get_attributed_product_sales_for_a_single_brevo_campaign_or_workflow.0"
    client = get_client(test_id)
    client.ecommerce.get_attributed_product_sales_for_a_single_brevo_campaign_or_workflow(
        conversion_source="email_campaign", conversion_source_id="sale"
    )
    verify_request_count(test_id, "GET", "/ecommerce/attribution/products/email_campaign/sale", None, 1)


def test_ecommerce_get_the_iso4217compliant_display_currency_code_for_your_brevo_account() -> None:
    """Test getTheIso4217CompliantDisplayCurrencyCodeForYourBrevoAccount endpoint with WireMock"""
    test_id = "ecommerce.get_the_iso4217compliant_display_currency_code_for_your_brevo_account.0"
    client = get_client(test_id)
    client.ecommerce.get_the_iso4217compliant_display_currency_code_for_your_brevo_account()
    verify_request_count(test_id, "GET", "/ecommerce/config/displayCurrency", None, 1)


def test_ecommerce_set_config_display_currency() -> None:
    """Test setConfigDisplayCurrency endpoint with WireMock"""
    test_id = "ecommerce.set_config_display_currency.0"
    client = get_client(test_id)
    client.ecommerce.set_config_display_currency(code="EUR")
    verify_request_count(test_id, "POST", "/ecommerce/config/displayCurrency", None, 1)


def test_ecommerce_get_orders() -> None:
    """Test getOrders endpoint with WireMock"""
    test_id = "ecommerce.get_orders.0"
    client = get_client(test_id)
    client.ecommerce.get_orders()
    verify_request_count(test_id, "GET", "/orders", None, 1)


def test_ecommerce_create_order() -> None:
    """Test createOrder endpoint with WireMock"""
    test_id = "ecommerce.create_order.0"
    client = get_client(test_id)
    client.ecommerce.create_order(
        amount=308.42,
        created_at="2021-07-29T20:59:23.383Z",
        id="14",
        products=[{"quantity": 10}],
        status="completed",
        updated_at="2021-07-30T10:59:23.383Z",
    )
    verify_request_count(test_id, "POST", "/orders/status", None, 1)


def test_ecommerce_create_batch_order() -> None:
    """Test createBatchOrder endpoint with WireMock"""
    test_id = "ecommerce.create_batch_order.0"
    client = get_client(test_id)
    client.ecommerce.create_batch_order(
        orders=[
            {
                "amount": 308.42,
                "created_at": "2021-07-29T20:59:23.383Z",
                "id": "14",
                "products": [{"quantity": 10}],
                "status": "completed",
                "updated_at": "2021-07-30T10:59:23.383Z",
            }
        ]
    )
    verify_request_count(test_id, "POST", "/orders/status/batch", None, 1)


def test_ecommerce_get_products() -> None:
    """Test getProducts endpoint with WireMock"""
    test_id = "ecommerce.get_products.0"
    client = get_client(test_id)
    client.ecommerce.get_products()
    verify_request_count(test_id, "GET", "/products", None, 1)


def test_ecommerce_create_update_product() -> None:
    """Test createUpdateProduct endpoint with WireMock"""
    test_id = "ecommerce.create_update_product.0"
    client = get_client(test_id)
    client.ecommerce.create_update_product(id="P11", name="Iphone 11")
    verify_request_count(test_id, "POST", "/products", None, 1)


def test_ecommerce_create_update_batch_products() -> None:
    """Test createUpdateBatchProducts endpoint with WireMock"""
    test_id = "ecommerce.create_update_batch_products.0"
    client = get_client(test_id)
    client.ecommerce.create_update_batch_products(products=[{"id": "P11", "name": "Iphone 11"}])
    verify_request_count(test_id, "POST", "/products/batch", None, 1)


def test_ecommerce_get_product_info() -> None:
    """Test getProductInfo endpoint with WireMock"""
    test_id = "ecommerce.get_product_info.0"
    client = get_client(test_id)
    client.ecommerce.get_product_info(id="id")
    verify_request_count(test_id, "GET", "/products/id", None, 1)


def test_ecommerce_create_product_alert() -> None:
    """Test createProductAlert endpoint with WireMock"""
    test_id = "ecommerce.create_product_alert.0"
    client = get_client(test_id)
    client.ecommerce.create_product_alert(id="id")
    verify_request_count(test_id, "POST", "/products/id/alerts/back_in_stock", None, 1)
