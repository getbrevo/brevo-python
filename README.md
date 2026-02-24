# Brevo Python SDK
![](banner.png)

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fgetbrevo%2Fbrevo-python)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![PyPI version](https://img.shields.io/pypi/v/brevo-python)](https://pypi.org/project/brevo-python/)
[![PyPI downloads](https://img.shields.io/pypi/dm/brevo-python)](https://pypi.org/project/brevo-python/)
[![Python versions](https://img.shields.io/pypi/pyversions/brevo-python)](https://pypi.org/project/brevo-python/)

[Website](https://brevo.com) · [API Reference](https://developers.brevo.com) · [Support](mailto:support@brevo.com)

---
Official SDK for the Brevo API.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Migration From V1X](#migration-from-v1x)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)

## Documentation

API reference documentation is available [here](https://developers.brevo.com).

## Installation

```sh
pip install brevo
```

## Reference

A full reference for this library is available [here](https://github.com/mourraille/fern-sdk/blob/HEAD/./reference.md).

## Migration from v1.x

> **Warning**: The legacy v1.x SDK (`brevo-python` < 4.0) will continue to receive critical security updates but no new features. We recommend migrating to v4.x.

<details>
<summary>View migration guide</summary>

**Key changes:**
- New client initialization via `Brevo(api_key="...")`
- Native async support with `AsyncBrevo`
- Pydantic-based typed models
- Automatic retries with exponential backoff
- `httpx` replaces `urllib3`

**v1.x:**
```python
import brevo_python
from brevo_python.rest import ApiException

configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
api_instance = brevo_python.AccountApi(brevo_python.ApiClient(configuration))
api_response = api_instance.get_account()
```

**v4.x:**
```python
from brevo import Brevo

client = Brevo(api_key="YOUR_API_KEY")
account = client.account.get_your_account_information_plan_and_credits_details()
```

| Area | v1.x (`brevo_python`) | v4.x (`brevo`) |
|---|---|---|
| Module | `import brevo_python` | `from brevo import Brevo` |
| Client | `AccountApi(ApiClient(config))` | `Brevo(api_key="...")` |
| Errors | `ApiException` | `ApiError` with `.status_code`, `.body` |
| HTTP | `urllib3` | `httpx` |
| Async | Not available | `AsyncBrevo` |
| Retries | Not built-in | Automatic with exponential backoff |
| Python | 2.7, 3.4+ | 3.8+ |

</details>


## Usage

Instantiate and use the client with the following:

```python
from brevo import Brevo
from brevo.transactional_emails import (
    SendTransacEmailRequestSender,
    SendTransacEmailRequestToItem,
)

client = Brevo(
    api_key="YOUR_API_KEY",
)
client.transactional_emails.send_transac_email(
    html_content="<html><head></head><body>Your delivery is expected {{params.estimatedArrival}}.Your tracking code: {{params.trackingCode}}</p></body></html>",
    params={
        "trackingCode": "JD01460000300002350000",
        "estimatedArrival": "Tomorrow",
    },
    sender=SendTransacEmailRequestSender(
        email="hello@brevo.com",
        name="Alex from Brevo",
    ),
    subject="Hello from Brevo!",
    to=[
        SendTransacEmailRequestToItem(
            email="johndoe@example.com",
            name="John Doe",
        )
    ],
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from brevo import AsyncBrevo
from brevo.transactional_emails import (
    SendTransacEmailRequestSender,
    SendTransacEmailRequestToItem,
)

client = AsyncBrevo(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.transactional_emails.send_transac_email(
        html_content="<html><head></head><body>Your delivery is expected {{params.estimatedArrival}}.Your tracking code: {{params.trackingCode}}</p></body></html>",
        params={
            "trackingCode": "JD01460000300002350000",
            "estimatedArrival": "Tomorrow",
        },
        sender=SendTransacEmailRequestSender(
            email="hello@brevo.com",
            name="Alex from Brevo",
        ),
        subject="Hello from Brevo!",
        to=[
            SendTransacEmailRequestToItem(
                email="johndoe@example.com",
                name="John Doe",
            )
        ],
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from brevo.core.api_error import ApiError

try:
    client.transactional_emails.send_transac_email(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from brevo import Brevo

client = Brevo(
    ...,
)
response = client.transactional_emails.with_raw_response.send_transac_email(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.transactional_emails.send_transac_email(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from brevo import Brevo

client = Brevo(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.transactional_emails.send_transac_email(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from brevo import Brevo

client = Brevo(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

