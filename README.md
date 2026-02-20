# Brevo Python SDK
![](banner.png)

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fgetbrevo%2Fbrevo-python)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![pypi version](https://img.shields.io/pypi/v/brevo-python)](https://pypi.python.org/pypi/brevo-python)
[![pypi downloads](https://img.shields.io/pypi/dm/brevo-python)](https://pypi.python.org/pypi/brevo-python)

[Website](https://brevo.com) • [API Reference](https://developers.brevo.com) • [Support](mailto:support@brevo.com)

---

## Installation

```bash
pip install brevo-python
```

## Quick start

```python
from brevo import Brevo

client = Brevo(api_key="your-api-key")

result = client.transactional_emails.send_transac_email(
    subject="Hello",
    text_content="Hello world!",
    sender={"name": "Sender", "email": "sender@example.com"},
    to=[{"email": "recipient@example.com"}],
)

print("Email sent:", result)
```

---

## Async support

The SDK provides a fully asynchronous client for use with `asyncio`.

```python
import asyncio
from brevo import AsyncBrevo

client = AsyncBrevo(api_key="your-api-key")

async def main():
    result = await client.transactional_emails.send_transac_email(
        subject="Hello",
        text_content="Hello world!",
        sender={"name": "Sender", "email": "sender@example.com"},
        to=[{"email": "recipient@example.com"}],
    )
    print("Email sent:", result)

asyncio.run(main())
```

> **Note:** If passing a custom `httpx` client, use `httpx.AsyncClient()` instead of `httpx.Client()` for the async variant.

---

## Configuration

```python
from brevo import Brevo, BrevoEnvironment

client = Brevo(
    api_key="your-api-key",
    environment=BrevoEnvironment.DEFAULT,  # https://api.brevo.com/v3
    timeout=30.0,           # seconds (default: 60)
    follow_redirects=True,  # default: True
)
```

To point at a custom base URL (e.g. a proxy or staging environment):

```python
client = Brevo(
    api_key="your-api-key",
    base_url="https://custom-api.example.com/v3",
)
```

---

## Error handling

The SDK raises typed exceptions for non-success HTTP responses. All errors extend `ApiError`.

```python
from brevo import Brevo
from brevo.core.api_error import ApiError
from brevo.errors import UnauthorizedError, TooManyRequestsError

client = Brevo(api_key="your-api-key")

try:
    client.transactional_emails.send_transac_email(...)
except UnauthorizedError as e:
    print("Invalid API key")
except TooManyRequestsError as e:
    print(f"Rate limited (status {e.status_code})")
except ApiError as e:
    print(f"API error {e.status_code}: {e.body}")
```

**Error types:**

| Status code | Exception                  |
|-------------|----------------------------|
| `400`       | `BadRequestError`          |
| `401`       | `UnauthorizedError`        |
| `402`       | `PaymentRequiredError`     |
| `403`       | `ForbiddenError`           |
| `404`       | `NotFoundError`            |
| `405`       | `MethodNotAllowedError`    |
| `408`       | Retried automatically      |
| `409`       | `ConflictError`            |
| `412`       | `PreconditionFailedError`  |
| `415`       | `UnsupportedMediaTypeError`|
| `417`       | `ExpectationFailedError`   |
| `422`       | `UnprocessableEntityError` |
| `424`       | `FailedDependencyError`    |
| `425`       | `TooEarlyError`            |
| `429`       | `TooManyRequestsError`     |
| `500+`      | `InternalServerError`      |

<details>
<summary>Error properties</summary>

All `ApiError` instances provide:
- `status_code`: HTTP status code
- `body`: Parsed error response body
- `headers`: Response headers (dict)

</details>

---

## Retries

Automatic retries with exponential backoff are enabled by default (2 retries).

```python
# Client-level
client = Brevo(api_key="your-api-key")

# Request-level override
client.transactional_emails.send_transac_email(
    ...,
    request_options={"max_retries": 5}
)
```

**Retryable status codes:** `408`, `409`, `429`, `5xx`

<details>
<summary>How retries work</summary>

- Exponential backoff starting at ~1s, doubling each attempt (capped at 60s)
- ±10% symmetric jitter to avoid thundering herd
- Respects `Retry-After` and `X-RateLimit-Reset` headers
- Can be disabled per request with `"max_retries": 0`

</details>

---

## Timeouts

Default timeout is 60 seconds. Configure at client or request level.

```python
# Client-level
client = Brevo(
    api_key="your-api-key",
    timeout=30.0,
)

# Request-level override
client.transactional_emails.send_transac_email(
    ...,
    request_options={"timeout_in_seconds": 10}
)
```

**Recommended values:**
- Standard API calls: `30-60s` (default)
- Quick operations: `10-15s`
- Bulk operations: `120-300s`
- Real-time: `5-10s`

---

## Request options

Every method accepts an optional `request_options` dict as a keyword argument.

```python
from brevo.core.request_options import RequestOptions
```

### Additional headers

```python
client.transactional_emails.send_transac_email(
    ...,
    request_options={
        "additional_headers": {"X-Custom-Header": "custom-value"}
    }
)
```

### Additional query parameters

```python
client.contacts.get_contacts(
    ...,
    request_options={
        "additional_query_parameters": {"customParam": "value"}
    }
)
```

### Additional body parameters

```python
client.transactional_emails.send_transac_email(
    ...,
    request_options={
        "additional_body_parameters": {"customField": "value"}
    }
)
```

### Raw response

Access headers and status code alongside the parsed response.

```python
response = client.transactional_emails.with_raw_response.send_transac_email(...)

print(response.status_code)
print(response.headers)
print(response.data)
```

---

## Type hints

All request and response models are fully typed with Pydantic and support IDE autocompletion.

```python
from brevo.transactional_emails.types import SendSmtpEmail

email: SendSmtpEmail = SendSmtpEmail(
    subject="First email",
    text_content="Hello world!",
    sender={"name": "Bob Wilson", "email": "bob.wilson@example.com"},
    to=[{"email": "sarah.davis@example.com", "name": "Sarah Davis"}],
)
```

---

## Logging

```python
from brevo import Brevo
from brevo.core.logging import ConsoleLogger

client = Brevo(
    api_key="your-api-key",
    logging={
        "level": "debug",
        "logger": ConsoleLogger(),
        "silent": False,
    }
)
```

<details>
<summary>Custom logger example</summary>

Implement the `ILogger` protocol to use any logging framework.

```python
import logging

class CustomLogger:
    def __init__(self):
        self._logger = logging.getLogger("brevo")
        self._logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        self._logger.addHandler(handler)

    def debug(self, message: str, **kwargs) -> None:
        self._logger.debug(message, **kwargs)

    def info(self, message: str, **kwargs) -> None:
        self._logger.info(message, **kwargs)

    def warn(self, message: str, **kwargs) -> None:
        self._logger.warning(message, **kwargs)

    def error(self, message: str, **kwargs) -> None:
        self._logger.error(message, **kwargs)

client = Brevo(
    api_key="your-api-key",
    logging={
        "level": "debug",
        "logger": CustomLogger(),
        "silent": False,
    }
)
```

</details>

---

## Custom HTTP client

Override the default `httpx` client for proxies, custom transports, or other advanced use cases.

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
<summary>Common use cases</summary>

**With a proxy:**
```python
import httpx
from brevo import Brevo

client = Brevo(
    api_key="your-api-key",
    httpx_client=httpx.Client(proxy="http://proxy.example.com:8080"),
)
```

**With custom certificates:**
```python
import httpx
from brevo import Brevo

client = Brevo(
    api_key="your-api-key",
    httpx_client=httpx.Client(verify="/path/to/custom-ca-bundle.crt"),
)
```

**Async with proxy:**
```python
import httpx
from brevo import AsyncBrevo

client = AsyncBrevo(
    api_key="your-api-key",
    httpx_client=httpx.AsyncClient(proxy="http://proxy.example.com:8080"),
)
```

</details>

---

## Runtime compatibility

- Python 3.8+
- Works with `asyncio`, `uvloop`, and `trio` (via `anyio`)
- Compatible with virtual environments, Docker, AWS Lambda, and GCP Cloud Functions

### Dependencies

| Package            | Version        |
|--------------------|----------------|
| `httpx`            | >= 0.21.2      |
| `pydantic`         | >= 1.9.2       |
| `pydantic-core`    | >= 2.18.2      |
| `typing_extensions`| >= 4.0.0       |

---

## Migration from v1.x

<details>
<summary>View migration guide</summary>

This version includes breaking changes from the legacy `brevo-python` / `sib-api-v3-sdk` packages.

**Key changes:**
- New client initialization (no more `Configuration` object)
- Direct method calls instead of separate API class instantiation
- Built-in async support
- Typed Pydantic models for all requests and responses
- Standardized error handling via `ApiError`

**v1.x:**
```python
import brevo_python
from brevo_python.rest import ApiException

configuration = brevo_python.Configuration()
configuration.api_key["api-key"] = "xkeysib-xxx"

api_instance = brevo_python.TransactionalEmailsApi(
    brevo_python.ApiClient(configuration)
)

send_smtp_email = brevo_python.SendSmtpEmail(
    subject="First email",
    text_content="Hello world!",
    sender={"name": "Bob Wilson", "email": "bob.wilson@example.com"},
    to=[{"email": "sarah.davis@example.com", "name": "Sarah Davis"}],
)

try:
    api_instance.send_transac_email(send_smtp_email)
except ApiException as e:
    print("Error: %s" % e)
```

**v4.x:**
```python
from brevo import Brevo

client = Brevo(api_key="xkeysib-xxx")

client.transactional_emails.send_transac_email(
    subject="First email",
    text_content="Hello world!",
    sender={"name": "Bob Wilson", "email": "bob.wilson@example.com"},
    to=[{"email": "sarah.davis@example.com", "name": "Sarah Davis"}],
)
```

</details>

> [!WARNING]
> The legacy v1.x SDK (`brevo-python`) will continue to receive critical security updates but no new features. We recommend migrating to v4.x.

---

## Contributing

This library is generated programmatically. Changes made directly to the library would be overwritten. Please open an issue first to discuss changes.

Contributions to this README are always welcome!

---

## Support

- [API Reference](https://developers.brevo.com)
- [GitHub Issues](https://github.com/getbrevo/brevo-python/issues)
- [Email Support](mailto:support@brevo.com)
