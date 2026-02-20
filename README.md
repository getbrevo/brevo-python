# Brevo Python SDK
![](banner.png)

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fgetbrevo%2Fbrevo-python)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![PyPI version](https://img.shields.io/pypi/v/brevo-python)](https://pypi.org/project/brevo-python/)
[![PyPI downloads](https://img.shields.io/pypi/dm/brevo-python)](https://pypi.org/project/brevo-python/)
[![Python versions](https://img.shields.io/pypi/pyversions/brevo-python)](https://pypi.org/project/brevo-python/)

[Website](https://brevo.com) · [API Reference](https://developers.brevo.com) · [Support](mailto:support@brevo.com)

---

## Installation

```bash
pip install brevo-python
```

## Quick start

```python
from brevo import Brevo

client = Brevo(api_key="your-api-key")

result = client.transactional_emails.send_a_transactional_email(
    subject="Hello",
    text_content="Hello world!",
    sender={"name": "Sender", "email": "sender@example.com"},
    to=[{"email": "recipient@example.com"}],
)

print("Email sent:", result)
```

---

## Configuration

```python
from brevo import Brevo

client = Brevo(
    api_key="your-api-key",
    timeout=30.0,        # 30 seconds
)
```

---

## Error handling

The SDK raises `ApiError` (or a subclass) for non-success HTTP status codes.

```python
from brevo.core.api_error import ApiError

try:
    client.transactional_emails.send_a_transactional_email(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

**Error properties:**
- `status_code`: HTTP status code
- `body`: Parsed error response body

---

## Async client

The SDK exports an `AsyncBrevo` client for non-blocking calls. If you pass a custom httpx client, use `httpx.AsyncClient()` instead of `httpx.Client()`.

```python
import asyncio
from brevo import AsyncBrevo

client = AsyncBrevo(api_key="your-api-key")

async def main() -> None:
    result = await client.transactional_emails.send_a_transactional_email(
        subject="Hello",
        text_content="Hello world!",
        sender={"name": "Sender", "email": "sender@example.com"},
        to=[{"email": "recipient@example.com"}],
    )
    print("Email sent:", result)

asyncio.run(main())
```

---

## Retries

Automatic retries with exponential backoff are enabled by default (2 retries).

```python
# Client-level
client = Brevo(
    api_key="your-api-key",
)

# Request-level
client.transactional_emails.send_a_transactional_email(..., request_options={
    "max_retries": 5
})
```

**Retryable status codes:** `408`, `429`, `5xx`

<details>
<summary>How retries work</summary>

- Exponential backoff with jitter
- Can be disabled per request with `max_retries: 0`

</details>

---

## Timeouts

Default timeout is 60 seconds. Configure at client or request level.

```python
from brevo import Brevo

# Client-level
client = Brevo(
    api_key="your-api-key",
    timeout=30.0,
)

# Request-level
client.transactional_emails.send_a_transactional_email(..., request_options={
    "timeout_in_seconds": 10
})
```

**Recommended values:**
- Standard API calls: `30-60s` (default)
- Quick operations: `10-15s`
- Bulk operations: `120-300s`

---

## Request options

### Additional headers

```python
client.transactional_emails.send_a_transactional_email(..., request_options={
    "additional_headers": {
        "X-Custom-Header": "custom-value"
    }
})
```

### Additional query parameters

```python
client.transactional_emails.send_a_transactional_email(..., request_options={
    "additional_query_parameters": {
        "custom_param": "value"
    }
})
```

---

## Raw response access

The SDK provides access to raw response data, including headers, through `.with_raw_response`.

```python
from brevo import Brevo

client = Brevo(api_key="your-api-key")

response = client.transactional_emails.with_raw_response.send_a_transactional_email(...)

print(response.headers)
print(response.status_code)
print(response.data)
```

---

## Type hints

The SDK ships with full type annotations. All request and response types are importable from the `brevo` package for use in your own type hints.

```python
from brevo import Brevo

client = Brevo(api_key="your-api-key")

client.transactional_emails.send_a_transactional_email(
    subject="First email",
    text_content="Hello world!",
    sender={"name": "Bob Wilson", "email": "bob.wilson@example.com"},
    to=[{"email": "sarah.davis@example.com", "name": "Sarah Davis"}],
)
```

---

## Custom HTTP client

Override the `httpx` client for proxies, custom transports, or mTLS.

```python
import httpx
from brevo import Brevo

client = Brevo(
    api_key="your-api-key",
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

<details>
<summary>Async custom client</summary>

```python
import httpx
from brevo import AsyncBrevo

client = AsyncBrevo(
    api_key="your-api-key",
    httpx_client=httpx.AsyncClient(
        proxy="http://my.test.proxy.example.com",
    ),
)
```

</details>

---

## Requirements

- Python 3.8+
- `httpx` >= 0.21.2
- `pydantic` >= 1.9.2
- `typing_extensions` >= 4.0.0

---

## Migration from v1.x

<details>
<summary>View migration guide</summary>

This version includes breaking changes.

**Key changes:**
- New client initialization via single `Brevo(api_key="...")` entry point
- Native async support with `AsyncBrevo`
- Pydantic-based typed models
- Automatic retries with exponential backoff
- `httpx` replaces `urllib3`

**Import path:**

| v1.x | v4.x |
|---|---|
| `import brevo_python` | `from brevo import Brevo` |

**Client initialization:**

```python
# v1.x
import brevo_python
from brevo_python.rest import ApiException

configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
api_instance = brevo_python.AccountApi(brevo_python.ApiClient(configuration))
api_response = api_instance.get_account()
```

```python
# v4.x
from brevo import Brevo

client = Brevo(api_key="YOUR_API_KEY")
account = client.account.get_your_account_information_plan_and_credits_details()
```

**Error handling:**

```python
# v1.x
from brevo_python.rest import ApiException
try:
    api_response = api_instance.get_account()
except ApiException as e:
    print("Exception: %s\n" % e)
```

```python
# v4.x
from brevo.core.api_error import ApiError
try:
    account = client.account.get_your_account_information_plan_and_credits_details()
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

**Summary:**

| Area | v1.x (`brevo_python`) | v4.x (`brevo`) |
|---|---|---|
| Module | `import brevo_python` | `from brevo import Brevo` |
| Client | `AccountApi(ApiClient(config))` | `Brevo(api_key="...")` |
| Config | `Configuration()` + `api_key['api-key']` | Constructor parameter `api_key` |
| Errors | `ApiException` | `ApiError` with `.status_code`, `.body` |
| HTTP | `urllib3` | `httpx` |
| Async | Not available | `AsyncBrevo` |
| Retries | Not built-in | Automatic with exponential backoff |
| Timeouts | Manual | 60s default, configurable |
| Python | 2.7, 3.4+ | 3.8+ |
| Build | `setup.py` | `pyproject.toml` (Poetry) |

</details>

> [!WARNING]
> The legacy v1.x SDK (`brevo-python` < 4.0) will continue to receive critical security updates but no new features. We recommend migrating to v4.x.

---

## Contributing

This library is generated programmatically. Changes made directly to the library would be overwritten. Please open an issue first to discuss changes.

Contributions to this README are always welcome!

---

## Support

- [API Reference](https://developers.brevo.com)
- [GitHub Issues](https://github.com/getbrevo/brevo-python/issues)
- [Email Support](mailto:support@brevo.com)
