from .conftest import get_client, verify_request_count


def test_coupons_get_coupon_collections() -> None:
    """Test getCouponCollections endpoint with WireMock"""
    test_id = "coupons.get_coupon_collections.0"
    client = get_client(test_id)
    client.coupons.get_coupon_collections()
    verify_request_count(test_id, "GET", "/couponCollections", None, 1)


def test_coupons_create_coupon_collection() -> None:
    """Test createCouponCollection endpoint with WireMock"""
    test_id = "coupons.create_coupon_collection.0"
    client = get_client(test_id)
    client.coupons.create_coupon_collection(default_coupon="Winter", name="10%OFF")
    verify_request_count(test_id, "POST", "/couponCollections", None, 1)


def test_coupons_get_coupon_collection() -> None:
    """Test getCouponCollection endpoint with WireMock"""
    test_id = "coupons.get_coupon_collection.0"
    client = get_client(test_id)
    client.coupons.get_coupon_collection(id="id")
    verify_request_count(test_id, "GET", "/couponCollections/id", None, 1)


def test_coupons_update_coupon_collection() -> None:
    """Test updateCouponCollection endpoint with WireMock"""
    test_id = "coupons.update_coupon_collection.0"
    client = get_client(test_id)
    client.coupons.update_coupon_collection(id="id")
    verify_request_count(test_id, "PATCH", "/couponCollections/id", None, 1)


def test_coupons_create_coupons() -> None:
    """Test createCoupons endpoint with WireMock"""
    test_id = "coupons.create_coupons.0"
    client = get_client(test_id)
    client.coupons.create_coupons(collection_id="23befbae-1505-47a8-bd27-e30ef739f32c", coupons=["Uf12AF"])
    verify_request_count(test_id, "POST", "/coupons", None, 1)
