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
- [Upgrading from v4.x](#upgrading-from-v4x)
- [Migration from v1.x](#migration-from-v1x)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
  - [Logging](#logging)

## Documentation

API reference documentation is available [here](https://developers.brevo.com).

## Installation

```sh
pip install brevo-python
```

## Reference

A full reference for this library is available [here](https://github.com/getbrevo/brevo-python/blob/v5/reference.md).

## Upgrading from v4.x

v5 is a major release. Most breaking changes come from an internal effort at Brevo to make endpoints, parameters and models more **self-descriptive** — so names, shapes and required fields convey intent without needing to cross-reference external docs (both for developers and for AI agents working against the Brevo API). Every change below applies symmetrically to both `Brevo` (sync) and `AsyncBrevo`.

v4.x remains supported. If you need to hold on v4 temporarily, pin it:

```bash
pip install "brevo-python>=4,<5"
```

<details>
<summary>View v4 → v5 migration guide</summary>

### Breaking changes

**Companies — `get_companies(filters=...)` renamed**
- The `filters` keyword is renamed to `filters_attributes_name` to match the wire format.
- The old keyword is silently dropped, the request still succeeds, and the server returns an unfiltered list. Audit every call site.

**Events — `event.create_batch_events` payload renamed**
```python
# v4
client.event.create_batch_events(request=[item1, item2])

# v5
client.event.create_batch_events(events=[item1, item2])
```
Item types renamed in lockstep: `CreateBatchEventsRequestItem` → `CreateBatchEventsRequestEventsItem` (and 5 sub-types).

**Balance — `get_contact_balances` requires `balance_definition_id`**

**Balance — `get_active_balances_api` response shape changed**
- Response type replaced with `GetLoyaltyBalanceProgramsPidActiveBalanceResponse`.

**Balance — `begin_transaction.event_time` type tightened**
- `str` → `datetime`. Type-checkers will fail on the old shape.

**CRM — `tasks.get_all_task_types` returns a list** (`List[GetCrmTasktypesResponseItem]` instead of `GetCrmTasktypesResponse`). Old `.id` / `.title` access on the response now fails.

**Webhooks — `create_webhook(events=...)` is now optional / keyword-only**. Positional callers break; switch to keyword arguments.

**Webhooks — `message_id` is now `str`** (was `int`) on history-fetch endpoints.

**Response fields removed**: `GetAccountResponse.date_time_preferences`, `GetWebhook.channel`, `GetProcessResponseInfo.export`.

**Shape collapses**:
- `SendTransacSmsTag` is now `Union[str, List[str]]` (was a pydantic model).
- `GetExtendedCampaignStats.links_stats` is now `Dict[str, int]` (was a pydantic class).
- `ConversationsMessageAttachmentsItem`: `file_name` → `name`, `inline_id` → `link`.

**Top-level imports removed (21 names)** from `from brevo import ...`. Most notably:
- `CreateBatchEventsRequestItem*` (6 names)
- `GetWebhookChannel`
- `GetAccountResponseDateTimePreferences`
- `GetExtendedCampaignStatsLinksStats`
- `SendTransacSmsTagField`
- `UpsertrecordsRequestRecordsItemAssociationsItemZero/One*` (8 names)

### Added

- New optional fields and filters across `contacts.create_contact`, `contacts.update_contact`, `email_campaigns.get_email_campaigns`, `ecommerce.get_products`, and several other endpoints.

</details>

## Migration from v1.x

> **Warning**: The legacy v1.x SDK (`brevo-python` < 4.0) will continue to receive critical security updates but no new features. We recommend migrating to v5.x.

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

**v5.x:**
```python
from brevo import Brevo

client = Brevo(api_key="YOUR_API_KEY")
account = client.account.get_your_account_information_plan_and_credits_details()
```

| Area | v1.x (`brevo_python`) | v5.x (`brevo`) |
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

### Logging

The SDK has a built-in, opt-in logger. Pass a `LogConfig` dict (or a pre-built `Logger`) via the `logging` constructor option on either `Brevo` or `AsyncBrevo`.

> **Note**: The SDK is **silent by default** (`silent=True`). Nothing is logged unless you set `silent=False`. This keeps integration changes from accidentally producing log volume in production.

```python
from brevo import Brevo
from brevo.core.logging import ConsoleLogger

client = Brevo(
    api_key="YOUR_API_KEY",
    logging={
        "level": "debug",          # "debug" | "info" | "warn" | "error"
        "logger": ConsoleLogger(), # built-in; writes to stdlib logging under the "fern" logger
        "silent": False,           # required to actually emit logs
    },
)
```

#### `LogConfig` fields

| Field | Type | Default | Description |
|---|---|---|---|
| `level` | `"debug" \| "info" \| "warn" \| "error"` | `"info"` | Minimum level forwarded to the logger |
| `logger` | `ILogger` | `ConsoleLogger()` | Logger implementation — any object conforming to the `ILogger` protocol |
| `silent` | `bool` | `True` | When `True`, all logging is suppressed regardless of `level` |

#### Custom logger

Implement the `ILogger` protocol (`debug`, `info`, `warn`, `error` methods) to forward to any logging library — stdlib `logging`, `structlog`, `loguru`, or your own sink.

```python
import logging
from brevo import Brevo
from brevo.core.logging import ILogger

logging.basicConfig(level=logging.DEBUG)

class StdlibLogger(ILogger):
    def __init__(self, name: str = "brevo") -> None:
        self._log = logging.getLogger(name)

    def debug(self, message, **kwargs): self._log.debug(message, extra=kwargs)
    def info(self,  message, **kwargs): self._log.info(message,  extra=kwargs)
    def warn(self,  message, **kwargs): self._log.warning(message, extra=kwargs)
    def error(self, message, **kwargs): self._log.error(message, extra=kwargs)

client = Brevo(
    api_key="YOUR_API_KEY",
    logging={"level": "debug", "logger": StdlibLogger(), "silent": False},
)
```

The default `ConsoleLogger` uses Python's stdlib `logging` module under the logger name `"fern"`. If you only need to filter or reformat output, configuring that logger via `logging.getLogger("fern")` may be enough — you don't always need a custom `ILogger`.

