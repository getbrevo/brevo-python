# Reference
## Account
<details><summary><code>client.account.<a href="src/brevo/account/client.py">get_account</a>() -> GetAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of your Brevo account.

**Use this to:**
- Get account information (email, name, company, address)
- Check plan details (type, credits, expiration)
- Get relay information (for transactional emails)
- Check Marketing Automation status
- View date/time preferences and account settings
- Access organization and user identifiers

**Key information returned:**
- Complete account details (organization ID, user ID, company information)
- Address and contact information
- Plan configurations and credit allocations across different verticals
- Marketing Automation settings and tracker key
- SMTP relay configuration for transactional emails
- Date/time preferences and account settings
- Enterprise features availability status

**Important considerations:**
- Provides comprehensive account overview for billing and configuration management
- Essential for understanding current plan limitations and feature availability
- Marketing Automation key required for advanced automation features
- Plan verticals show detailed breakdown across Marketing, Chat, and CRM categories
- Relay configuration crucial for transactional email setup and deliverability
- Date/time preferences affect campaign scheduling and reporting displays
- Enterprise status determines access to advanced features and sub-account management
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.account.get_account()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/brevo/account/client.py">get_account_activity</a>(...) -> GetAccountActivityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves user activity logs from your organization for security monitoring and audit compliance.

Use this to:
- Monitor user login activities and access patterns
- Track account modifications and configuration changes
- Generate security audit reports and compliance documentation
- Investigate suspicious activities and unauthorized access
- Monitor team member actions and account usage

Key information returned:
- Complete user activity details and timestamps
- User identification (email, IP address, browser)
- Action types and activity descriptions
- Security-relevant events and access logs
- Historical activity data for audit trails

Note: Requires Enterprise plan for access to organization activity logs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.account.get_account_activity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` 

Mandatory if endDate is used. Enter start date in UTC date (YYYY-MM-DD)
format to filter the activity in your account. Maximum time period that
can be selected is one month. Additionally, you can retrieve activity
logs from the past 12 months from the date of your search.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 

Mandatory if startDate is used. Enter end date in UTC date (YYYY-MM-DD)
format to filter the activity in your account. Maximum time period that
can be selected is one month.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Enter the user's email address to filter their activity in the account.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MasterAccount
<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">create_a_new_group_of_sub_accounts</a>(...) -> PostCorporateGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows to create a group of sub-accounts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.create_a_new_group_of_sub_accounts(
    group_name="My group",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_name:** `str` — The name of the group of sub-accounts
    
</dd>
</dl>

<dl>
<dd>

**sub_account_ids:** `typing.Optional[typing.List[int]]` — Pass the list of sub-account Ids to be included in the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">delete_sub_account_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to remove a sub-organization from a group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.delete_sub_account_from_group(
    group_id="groupId",
    sub_account_ids=[
        423432,
        234323,
        87678
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — Group id
    
</dd>
</dl>

<dl>
<dd>

**sub_account_ids:** `typing.List[int]` — List of sub-account ids
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_a_group_details</a>(...) -> GetCorporateGroupIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to retrieve a specific group’s information such as
the list of sub-organizations and the user associated with the group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_a_group_details(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the group of sub-organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">update_a_group_of_sub_accounts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows to update a group of sub-accounts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.update_a_group_of_sub_accounts(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the group
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The name of the group of sub-accounts
    
</dd>
</dl>

<dl>
<dd>

**sub_account_ids:** `typing.Optional[typing.List[int]]` — Pass the list of sub-account Ids to be included in the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">delete_a_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to delete a group of sub-organizations. When a
group is deleted, the sub-organizations are no longer part of this group.
The users associated with the group are no longer associated with the group
once deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.delete_a_group(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_sub_account_groups</a>() -> typing.List[GetSubAccountGroupsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to list all groups created on your Admin account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_sub_account_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_corporate_invited_users_list</a>(...) -> GetCorporateInvitedUsersListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to list all Admin users of your Admin account. You
can filter users by type (active or pending) and paginate results using
offset and limit.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_corporate_invited_users_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[str]` 

User type (active | pending). This is required if offset is provided for
limited result.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 

Page number for the result set. This is optional, default value will be
the 1st page.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Number of users to be displayed on each page. This is optional, the
default limit is 20, but max allowed limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">list_of_all_i_ps</a>() -> typing.List[GetCorporateIpResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to retrieve the list of active IPs on your Admin
account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.list_of_all_i_ps()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_the_details_of_requested_master_account</a>() -> GetCorporateMasterAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will provide the details of the master account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_the_details_of_requested_master_account()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">generate_sso_token_to_access_admin_account</a>(...) -> GetSsoToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint generates an SSO token to authenticate and access the admin
account using the endpoint
https://account-app.brevo.com/account/login/corporate/sso/[token], where
[token] will be replaced by the actual token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.generate_sso_token_to_access_admin_account(
    email="vipin+ent-user@brevo.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — User email of admin account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_the_list_of_all_the_sub_accounts_of_the_master_account</a>(...) -> GetCorporateSubAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will provide the list all the sub-accounts of the master
account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_the_list_of_all_the_sub_accounts_of_the_master_account(
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `int` — Index of the first sub-account in the page
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Number of sub-accounts to be displayed on each page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">create_a_new_sub_account_under_a_master_account</a>(...) -> PostCorporateSubAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will create a new sub-account under a master account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.create_a_new_sub_account_under_a_master_account(
    company_name="Test Sub-account",
    email="test-sub@example.com",
    group_ids=[
        "5f8f8c3b5f56a02d4433b3a7",
        "5f8f8c3b5f56a02d4433b3a8"
    ],
    language="fr",
    timezone="Europe/Paris",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_name:** `str` — Set the name of the sub-account company
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address for the organization
    
</dd>
</dl>

<dl>
<dd>

**group_ids:** `typing.Optional[typing.List[str]]` — Set the group(s) for the sub-account
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[PostCorporateSubAccountRequestLanguage]` — Set the language of the sub-account
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Set the timezone of the sub-account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">associate_an_ip_to_sub_accounts</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows to associate an IP to sub-accounts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.associate_an_ip_to_sub_accounts(
    ids=[
        234322,
        325553,
        893432
    ],
    ip="103.11.32.88",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.List[int]` 

Pass the list of sub-account Ids to be associated with the IP
address
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — IP address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">dissociate_an_ip_to_sub_accounts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows to dissociate an IP from sub-accounts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.dissociate_an_ip_to_sub_accounts(
    ids=[
        234322,
        325553,
        893432
    ],
    ip="103.11.32.88",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.List[int]` 

Pass the list of sub-account Ids to be dissociated from the IP
address
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — IP address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">create_an_api_key_for_a_sub_account</a>(...) -> PostCorporateSubAccountKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will generate an API v3 key for a sub-account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.create_an_api_key_for_a_sub_account(
    id=3232323,
    name="My Api Key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the sub-account organization
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the API key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">generate_sso_token_to_access_sub_account</a>(...) -> GetSsoToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint generates an sso token to authenticate and access a
sub-account of the master using the account endpoint
https://account-app.brevo.com/account/login/sub-account/sso/[token], where
[token] will be replaced by the actual token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.generate_sso_token_to_access_sub_account(
    id=3232323,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the sub-account organization
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — User email of sub-account organization
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[PostCorporateSubAccountSsoTokenRequestTarget]` 

**Set target after login success** * **automation** - Redirect
to Automation after login * **email_campaign** - Redirect to
Email Campaign after login * **contacts** - Redirect to Contacts
after login * **landing_pages** - Redirect to Landing Pages
after login * **email_transactional** - Redirect to Email
Transactional after login * **senders** - Redirect to Senders
after login * **sms_campaign** - Redirect to Sms Campaign after
login * **sms_transactional** - Redirect to Sms Transactional
after login
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 

Set the full target URL after login success. The user will land
directly on this target URL after login
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_sub_account_details</a>(...) -> GetCorporateSubAccountIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will provide the details for the specified sub-account company
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_sub_account_details(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the sub-account organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">delete_a_sub_account</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.delete_a_sub_account(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the sub-account organization to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">enable_disable_sub_account_application_s</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API endpoint for the Corporate owner to enable/disable applications on the
sub-account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.enable_disable_sub_account_application_s(
    id=1000000,
    landing_pages=True,
    meetings=True,
    sms_campaigns=False,
    web_push=False,
    whatsapp=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the sub-account organization (mandatory)
    
</dd>
</dl>

<dl>
<dd>

**automation:** `typing.Optional[bool]` 

Set this field to enable or disable Automation on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**conversations:** `typing.Optional[bool]` 

Set this field to enable or disable Conversations on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**crm:** `typing.Optional[bool]` — Set this field to enable or disable Sales CRM on the sub-account
    
</dd>
</dl>

<dl>
<dd>

**email_campaigns:** `typing.Optional[bool]` 

Set this field to enable or disable Email Campaigns on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**facebook_ads:** `typing.Optional[bool]` 

Set this field to enable or disable Facebook ads on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**inbox:** `typing.Optional[bool]` 

Set this field to enable or disable Inbox on the sub-account /
Not applicable on ENTv2
    
</dd>
</dl>

<dl>
<dd>

**landing_pages:** `typing.Optional[bool]` 

Set this field to enable or disable Landing pages on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**meetings:** `typing.Optional[bool]` — Set this field to enable or disable Meetings on the sub-account
    
</dd>
</dl>

<dl>
<dd>

**sms_campaigns:** `typing.Optional[bool]` 

Set this field to enable or disable SMS Marketing on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**transactional_emails:** `typing.Optional[bool]` 

Set this field to enable or disable Transactional Email on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**transactional_sms:** `typing.Optional[bool]` 

Set this field to enable or disable Transactional SMS on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**web_push:** `typing.Optional[bool]` — Set this field to enable or disable Web Push on the sub-account
    
</dd>
</dl>

<dl>
<dd>

**whatsapp:** `typing.Optional[bool]` 

Set this field to enable or disable Whatsapp campaigns on the
sub-account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">update_sub_account_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will update the sub-account plan. On the Corporate solution
new version v2, you can set an unlimited number of credits in your
sub-organization. Please pass the value “-1" to set the consumable in
unlimited mode.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.master_account import PutCorporateSubAccountIdPlanRequestCredits, PutCorporateSubAccountIdPlanRequestFeatures

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.update_sub_account_plan(
    id=1000000,
    credits=PutCorporateSubAccountIdPlanRequestCredits(
        email=5000,
        external_feeds=1,
        sms=2000,
        whatsapp=100,
        wp_subscribers=-1,
    ),
    features=PutCorporateSubAccountIdPlanRequestFeatures(
        inbox=10,
        landing_page=20,
        sales_users=6,
        users=15,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the sub-account organization
    
</dd>
</dl>

<dl>
<dd>

**credits:** `typing.Optional[PutCorporateSubAccountIdPlanRequestCredits]` — Credit details to update
    
</dd>
</dl>

<dl>
<dd>

**features:** `typing.Optional[PutCorporateSubAccountIdPlanRequestFeatures]` — Features details to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">update_sub_accounts_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will update multiple sub-accounts plan. On the Corporate
solution new version v2, you can set an unlimited number of credits in your
sub-organization. Please pass the value “-1" to set the consumable in
unlimited mode.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.master_account import PutCorporateSubAccountsPlanRequestCredits, PutCorporateSubAccountsPlanRequestFeatures

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.update_sub_accounts_plan(
    credits=PutCorporateSubAccountsPlanRequestCredits(
        email=5000,
        external_feeds=1,
        sms=2000,
        whatsapp=100,
        wp_subscribers=-1,
    ),
    features=PutCorporateSubAccountsPlanRequestFeatures(
        landing_page=20,
        sales_users=6,
        users=15,
    ),
    sub_account_ids=[
        4534345,
        987893,
        876785
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credits:** `typing.Optional[PutCorporateSubAccountsPlanRequestCredits]` — Credit details to update
    
</dd>
</dl>

<dl>
<dd>

**features:** `typing.Optional[PutCorporateSubAccountsPlanRequestFeatures]` — Features details to update
    
</dd>
</dl>

<dl>
<dd>

**sub_account_ids:** `typing.Optional[typing.List[int]]` — List of sub-account ids
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">invite_admin_user</a>(...) -> InviteAdminUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`This endpoint allows you to invite a member to manage the Admin account
Features and their respective permissions are as below: - `my_plan`:
  - "all"
- `api`:
  - "none"
- `user_management`:
  - "all"
- `app_management` | Not available in ENTv2:
  - "all"
- `sub_organization_groups`
  - "create"
  - "edit_delete"
- `create_sub_organizations`
  - "all"
- `manage_sub_organizations`
  - "all"
- `analytics`
  - "download_data"
  - "create_alerts"
  - "my_looks"
  - "explore_create"
- `security`
  - "all"
**Note**: - If `all_features_access: false` then only privileges are
required otherwise if `true` then it's assumed that all permissions will be
there for the invited admin user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.master_account import InviteAdminUserRequestPrivilegesItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.invite_admin_user(
    all_features_access=True,
    email="inviteuser@example.com",
    privileges=[
        InviteAdminUserRequestPrivilegesItem()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_features_access:** `bool` — All access to the features
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address for the organization
    
</dd>
</dl>

<dl>
<dd>

**privileges:** `typing.List[InviteAdminUserRequestPrivilegesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**group_ids:** `typing.Optional[typing.List[str]]` — Ids of Group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">resend_cancel_admin_user_invitation</a>(...) -> PutCorporateUserInvitationActionEmailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will allow the user to:
- Resend an admin user invitation
- Cancel an admin user invitation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.resend_cancel_admin_user_invitation(
    action="resend",
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PutCorporateUserInvitationActionEmailRequestAction` — Action to be performed (cancel / resend)
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address of the recipient
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">revoke_an_admin_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows to revoke/remove an invited member of your Admin
account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.revoke_an_admin_user(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the invited user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">get_corporate_user_permission</a>(...) -> GetCorporateUserPermissionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will provide the list of admin user permissions
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.get_corporate_user_permission(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the invited user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.master_account.<a href="src/brevo/master_account/client.py">change_admin_user_permissions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will allow you to change the permissions of Admin users of
your Admin account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.master_account import PutCorporateUserEmailPermissionsRequestPrivilegesItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.master_account.change_admin_user_permissions(
    email="email",
    all_features_access=False,
    privileges=[
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="user_management",
            permissions=[
                "all"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="api",
            permissions=[
                "all"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="my_plan",
            permissions=[
                "none"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="apps_management",
            permissions=[
                "all"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="create_sub_organizations",
            permissions=[
                "all"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="sub_organization_groups",
            permissions=[
                "create",
                "edit_delete"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="manage_sub_organizations",
            permissions=[
                "all"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="security",
            permissions=[
                "none"
            ],
        ),
        PutCorporateUserEmailPermissionsRequestPrivilegesItem(
            feature="analytics",
            permissions=[
                "create_alerts",
                "download_data",
                "my_looks",
                "explore_create"
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email address of Admin user
    
</dd>
</dl>

<dl>
<dd>

**all_features_access:** `bool` — All access to the features
    
</dd>
</dl>

<dl>
<dd>

**privileges:** `typing.List[PutCorporateUserEmailPermissionsRequestPrivilegesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User
<details><summary><code>client.user.<a href="src/brevo/user/client.py">get_invited_users_list</a>() -> GetInvitedUsersListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.user.get_invited_users_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/brevo/user/client.py">put_revoke_user_permission</a>(...) -> PutRevokeUserPermissionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.user.put_revoke_user_permission(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the invited user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/brevo/user/client.py">inviteuser</a>(...) -> InviteuserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`Feature` - A Feature represents a specific functionality like Email
campaign, Deals, Calls, Automations, etc. on Brevo. While inviting a user,
determine which feature you want to manage access to. You must specify the
feature accurately to avoid errors. `Permission` - A Permission defines the
level of access or control a user has over a specific feature. While
inviting user, decide on the permission level required for the selected
feature. Make sure the chosen permission is related to the selected feature.
Features and their respective permissions are as below: - `email_campaigns`:
  - "create_edit_delete"
  - "send_schedule_suspend"
- `sms_campaigns`:
  - "create_edit_delete"
  - "send_schedule_suspend"
- `contacts`:
  - "view"
  - "create_edit_delete"
  - "import"
  - "export"
  - "list_and_attributes"
  - "forms"
- `templates`:
  - "create_edit_delete"
  - "activate_deactivate"
- `workflows`:
  - "create_edit_delete"
  - "activate_deactivate_pause"
  - "settings"
- `landing_pages`:
  - "all"
- `transactional_emails`:
  - "settings"
  - "logs"
- `smtp_api`:
  - "smtp"
  - "api_keys"
  - "authorized_ips"
- `user_management`:
  - "all"
- `sales_platform`:
  - "create_edit_deals"
  - "delete_deals"
  - "manage_others_deals_tasks"
  - "reports"
  - "settings"
- `phone`:
  - "all"
- `conversations`:
  - "access"
  - "assign"
  - "configure"
- `senders_domains_dedicated_ips`:
  - "senders_management"
  - "domains_management"
  - "dedicated_ips_management"
- `push_notifications`:
  - "view"
  - "create_edit_delete"
  - "send"
  - "settings"
- `companies`:
  - "manage_owned_companies"
  - "manage_other_companies"
  - "settings"
**Note**: - If `all_features_access: false` then only privileges are
required otherwise if `true` then it's assumed that all permissions will be
there for the invited user. - The availability of feature and its permission
depends on your current plan. Please select the features and permissions
accordingly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, InviteuserPrivilegesItem
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.user.inviteuser(
    all_features_access=True,
    email="inviteuser@example.com",
    privileges=[
        InviteuserPrivilegesItem()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Inviteuser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/brevo/user/client.py">putresendcancelinvitation</a>(...) -> PutresendcancelinvitationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.user.putresendcancelinvitation(
    action="resend",
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PutresendcancelinvitationRequestAction` — action
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email of the invited user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/brevo/user/client.py">edit_user_permission</a>(...) -> EditUserPermissionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`Feature` - A Feature represents a specific functionality like Email
campaign, Deals, Calls, Automations, etc. on Brevo. While inviting a user,
determine which feature you want to manage access to. You must specify the
feature accurately to avoid errors. `Permission` - A Permission defines the
level of access or control a user has over a specific feature. While
inviting user, decide on the permission level required for the selected
feature. Make sure the chosen permission is related to the selected feature.
Features and their respective permissions are as below: - `email_campaigns`:
  - "create_edit_delete"
  - "send_schedule_suspend"
- `sms_campaigns`:
  - "create_edit_delete"
  - "send_schedule_suspend"
- `contacts`:
  - "view"
  - "create_edit_delete"
  - "import"
  - "export"
  - "list_and_attributes"
  - "forms"
- `templates`:
  - "create_edit_delete"
  - "activate_deactivate"
- `workflows`:
  - "create_edit_delete"
  - "activate_deactivate_pause"
  - "settings"
- `landing_pages`:
  - "all"
- `transactional_emails`:
  - "settings"
  - "logs"
- `smtp_api`:
  - "smtp"
  - "api_keys"
  - "authorized_ips"
- `user_management`:
  - "all"
- `sales_platform`:
  - "create_edit_deals"
  - "delete_deals"
  - "manage_others_deals_tasks"
  - "reports"
  - "settings"
- `phone`:
  - "all"
- `conversations`:
  - "access"
  - "assign"
  - "configure"
- `senders_domains_dedicated_ips`:
  - "senders_management"
  - "domains_management"
  - "dedicated_ips_management"
- `push_notifications`:
  - "view"
  - "create_edit_delete"
  - "send"
  - "settings"
- `companies`:
  - "manage_owned_companies"
  - "manage_other_companies"
  - "settings"
**Note**: - The privileges array remains the same as in the send invitation;
the user simply needs to provide the permissions that need to be updated. -
The availability of feature and its permission depends on your current plan.
Please select the features and permissions accordingly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, InviteuserPrivilegesItem
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.user.edit_user_permission(
    all_features_access=True,
    email="inviteuser@example.com",
    privileges=[
        InviteuserPrivilegesItem()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Inviteuser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/brevo/user/client.py">get_user_permission</a>(...) -> GetUserPermissionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.user.get_user_permission(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the invited user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Process
<details><summary><code>client.process.<a href="src/brevo/process/client.py">get_processes</a>(...) -> GetProcessesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of background processes from your Brevo account with filtering and pagination.

**Use this to:**
- Monitor background process activity and status
- Track long-running operations and tasks
- Find process IDs for detailed status checking
- Review process history and performance
- Identify failed or stuck processes for troubleshooting

**Key information returned:**
- Process details (ID, name, type, status)
- Process creation and completion timestamps
- Process progress and completion status
- Error information for failed processes
- Process result data and download links

**Important considerations:**
- Background processes handle long-running operations like imports and exports
- Process status indicates current state (queued, processing, completed, failed, cancelled)
- Export processes provide download URLs when completed
- Failed processes include error messages for troubleshooting
- Use pagination for accounts with many historical processes
- Sort options available for creation order (ascending or descending)
- Different process types handle specific operations (imports, exports, calculations)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.process.get_processes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number limitation for the result returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Beginning point in the list to retrieve from.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetProcessesRequestSort]` 

Sort the results in the ascending/descending order of record creation.
Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.process.<a href="src/brevo/process/client.py">get_process</a>(...) -> GetProcessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific background process.

**Use this to:**
- Get detailed status of a specific process
- Monitor process progress and completion
- Download results from completed export processes
- Check error details for failed processes
- Track process execution times

**Key information returned:**
- Complete process details and status
- Import/export statistics and results
- Error information for troubleshooting
- Download URLs for export processes
- Process timing and performance data

**Important considerations:**
- Process ID must exist in your account
- Completed processes provide detailed statistics and results
- Export processes include download URLs when successful
- Failed processes contain error messages for debugging
- Timing information helps with performance analysis
- Different process types return different result structures
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.process.get_process(
    process_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**process_id:** `int` — Id of the process
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders
<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">get_senders</a>(...) -> GetSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all email senders from your Brevo account with optional filtering.

**Use this to:**
- Get all available senders for email campaign setup
- Find sender details including ID, name, and email address
- Filter senders by IP address for dedicated IP users
- Filter senders by domain for domain-specific configurations
- Monitor sender configuration and status

**Key information returned:**
- Sender details (ID, name, email address)
- Sender status and verification information
- Associated IP addresses and domains (for dedicated IP accounts)
- Sender configuration settings

**Important considerations:**
- Standard accounts show empty IP arrays, dedicated IP accounts show IP assignments
- Filtering by IP only available for accounts with dedicated IPs
- Domain filtering helps organize senders by business units or brands
- Sender status indicates if sender is active and ready for campaign use
- Email verification required before sender can be used in campaigns
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.get_senders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ip:** `typing.Optional[str]` — Filter your senders for a specific ip. **Available for dedicated IP usage only**
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Filter your senders for a specific domain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">create_sender</a>(...) -> CreateSenderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new email sender in your Brevo account.

**Use this to:**
- Add new senders for email campaigns
- Configure sender identity (name and email)
- Associate dedicated IPs with the sender (for dedicated IP accounts)
- Set up domain-based sender configurations

**Key information returned:**
- Created sender ID
- DKIM and SPF configuration status
- Success confirmation

**Important considerations:**
- Verification email sent to specified sender address
- DKIM and SPF configuration affects deliverability
- Dedicated IP accounts require IP association during creation
- IP weights must sum to 100 when specified
- Sender must be verified before use in campaigns
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.create_sender(
    email="support@example.com",
    name="Support Team",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 

From email to use for the sender. A verification email will be
sent to this address.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — From Name to use for the sender
    
</dd>
</dl>

<dl>
<dd>

**ips:** `typing.Optional[typing.List[CreateSenderRequestIpsItem]]` 

**Mandatory in case of dedicated IP**. IPs to associate to the
sender. Not required for standard accounts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">get_ips</a>() -> GetIpsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all dedicated IPs associated with your Brevo account.

Use this to:
- List all your dedicated IPs
- Check the status of your dedicated IPs (active/inactive)
- Find IP addresses and associated domains for configuration purposes
- Monitor your IP reputation and deliverability
- Verify available IPs for sender configuration

Key information returned:
- IP ID and address
- Associated domain
- Active status
- IP configuration details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.get_ips()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">update_sender</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing email sender's configuration.

Use this to:
- Modify sender display name or email address
- Update dedicated IP associations
- Change sender configuration settings
- Correct sender information

Key information returned:
- Success confirmation
- Updated sender details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.update_sender(
    sender_id=1000000,
    name="New Support Team",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `int` — Id of the sender
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — From Email to update the sender
    
</dd>
</dl>

<dl>
<dd>

**ips:** `typing.Optional[typing.List[UpdateSenderRequestIpsItem]]` 

**Only in case of dedicated IP**. IPs to associate to the
sender. If passed, will replace all the existing IPs. Not required for standard accounts.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — From Name to update the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">delete_sender</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an email sender from your Brevo account.

Use this to:
- Remove senders that are no longer needed
- Clean up sender configurations
- Remove duplicate or test senders

Key information returned:
- Success confirmation message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.delete_sender(
    sender_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `int` — Id of the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">get_ips_from_sender</a>(...) -> GetIpsFromSenderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the dedicated IPs associated with a specific sender.

Use this to:
- Check IP configuration for a sender
- Verify dedicated IP associations
- Get IP details for troubleshooting
- Monitor sender IP configuration

Key information returned:
- List of associated dedicated IPs
- IP addresses and domain configurations
- IP status and settings
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.get_ips_from_sender(
    sender_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `int` — Id of the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/brevo/senders/client.py">validate_sender_by_otp</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a sender using the OTP (One-Time Password) received via email.

Use this to:
- Complete sender verification process
- Activate a newly created sender
- Verify ownership of the sender email address
- Enable the sender for use in email campaigns

Key information returned:
- Success confirmation of sender verification
- Sender activation status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.senders.validate_sender_by_otp(
    sender_id=1000000,
    otp=123456,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `int` — Id of the sender
    
</dd>
</dl>

<dl>
<dd>

**otp:** `int` — 6 digit OTP received on email
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Domains
<details><summary><code>client.domains.<a href="src/brevo/domains/client.py">get_domains</a>() -> GetDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all domains associated with the account.

Use this to:
- List all domains
- Verify domain existence
- Check domain authentication and verification status
- Monitor domain configuration and provider information
- Review domain creation history and ownership

Key information returned:
- Domain details (ID, name, authentication status)
- Verification and authentication states
- Associated IP addresses and DNS providers
- Creator information and creation timestamps
- Pagination information for large domain lists
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.domains.get_domains()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/brevo/domains/client.py">create_domain</a>(...) -> CreateDomainResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new domain in Brevo.

Use this to:
- Add new domains for sending emails
- Set up domain authentication for better deliverability
- Configure DNS records for email authentication
- Establish domain-based sender identities

Key information returned:
- Created domain ID and configuration
- Required DNS records for authentication
- Domain provider detection results
- Setup instructions and next steps
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.domains.create_domain(
    name="mycompany.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Domain name to be added
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/brevo/domains/client.py">get_domain_configuration</a>(...) -> GetDomainConfigurationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves configuration of a specific domain, to know if the domain is valid or not.

Use this to:
- Check domain configuration
- Validate a domain configuration
- Monitor DNS record status
- Troubleshoot authentication issues

Key information returned:
- Domain verification and authentication status
- DNS records configuration and validation status
- Detailed authentication requirements
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.domains.get_domain_configuration(
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — Domain name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/brevo/domains/client.py">delete_domain</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a domain from Brevo.

Use this to:
- Remove existing domains
- Clean up unused domain configurations
- Remove test domains

Key information returned:
- Success confirmation message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.domains.delete_domain(
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — Domain name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/brevo/domains/client.py">authenticate_domain</a>(...) -> AuthenticateDomainResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authenticates a specific domain.

Use this to:
- Authenticate a domain
- Verify DNS record configuration
- Complete domain setup for sending
- Enable domain for email authentication

Key information returned:
- Authentication success confirmation
- Domain readiness status for email sending
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.domains.authenticate_domain(
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — Domain name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/brevo/webhooks/client.py">get_webhooks</a>(...) -> GetWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all webhooks from your Brevo account with filtering and sorting options.

Use this to:
- Monitor webhook configurations and event handling
- List webhooks by type (transactional, marketing, inbound)
- Review webhook endpoints and authentication
- Track webhook creation and modification history
- Audit webhook event subscriptions

Key information returned:
- Complete webhook details and configuration
- Event types and channel subscriptions
- Authentication and security settings
- Webhook URLs and custom headers
- Creation and modification timestamps
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.webhooks.get_webhooks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[GetWebhooksRequestType]` — Filter on webhook type
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetWebhooksRequestSort]` — Sort the results in the ascending/descending order of webhook creation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/brevo/webhooks/client.py">create_webhook</a>(...) -> CreateWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new webhook to receive real-time notifications for specified events.

Use this to:
- Set up event notifications for transactional or marketing emails
- Configure webhook endpoints for campaign tracking
- Enable real-time monitoring of email delivery status
- Subscribe to contact list changes and updates
- Implement custom event handling and automation

Key information returned:
- Created webhook ID and configuration
- Success confirmation and setup details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.webhooks.create_webhook(
    events=[
        "sent"
    ],
    url="http://requestb.in/173lyyx1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**events:** `typing.List[CreateWebhookRequestEventsItem]` 

- Events triggering the webhook. Possible values for
**Transactional** type webhook: #### `sent` OR `request`,
`delivered`, `hardBounce`, `softBounce`, `blocked`, `spam`,
`invalid`, `deferred`, `click`, `opened`, `uniqueOpened` and
`unsubscribed` - Possible values for **Marketing** type webhook:
#### `spam`, `opened`, `click`, `hardBounce`, `softBounce`,
`unsubscribed`, `listAddition` & `delivered` - Possible values
for **Inbound** type webhook: #### `inboundEmailProcessed` -
Possible values for type **Transactional** and channel **SMS**
####
`accepted`,`delivered`,`softBounce`,`hardBounce`,`unsubscribe`,`reply`,
`subscribe`,`sent`,`blacklisted`,`skip` - Possible values for
type **Marketing**  channel **SMS** ####
`sent`,`delivered`,`softBounce`,`hardBounce`,`unsubscribe`,`reply`,
`subscribe`,`skip`
#### `reply`
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL of the webhook
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[CreateWebhookRequestAuth]` — Add authentication on webhook url
    
</dd>
</dl>

<dl>
<dd>

**batched:** `typing.Optional[bool]` — To send batched webhooks
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[CreateWebhookRequestChannel]` — channel of webhook
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the webhook
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` 

Inbound domain of webhook, required in case of event type
`inbound`
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.List[CreateWebhookRequestHeadersItem]]` — Custom headers to be send with webhooks
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreateWebhookRequestType]` — Type of the webhook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/brevo/webhooks/client.py">export_webhooks_history</a>(...) -> ExportWebhooksHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>
This is an enterprise feature. Contact us to activate it for your account.
</Note>

Submits a request to export webhook event history as a CSV file. The download link is sent to the `notifyURL` you provide in the request body.

Use this endpoint to:
- Export webhook event history filtered by date range, event type, or email address
- Generate reports for compliance, auditing, or performance analysis
- Track delivery patterns and webhook reliability over time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.webhooks.export_webhooks_history(
    event="invalid_parameter",
    notify_url="https://brevo.com",
    type="transactional",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event:** `ExportWebhooksHistoryRequestEvent` — Filter the history for a specific event type
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `str` — Webhook URL to receive CSV file link
    
</dd>
</dl>

<dl>
<dd>

**type:** `ExportWebhooksHistoryRequestType` — Filter the history based on webhook type
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` 

Number of days in the past including today (positive
integer). _Not compatible with 'startDate' and 'endDate'_
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter the history for a specific email
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 

Mandatory if startDate is used. Ending date of the report
(YYYY-MM-DD). Must be greater than equal to startDate
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[int]` 

Filter the history for a specific message id. Applicable
only for transactional webhooks.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sorting order of records (asc or desc)
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` 

Mandatory if endDate is used. Starting date of the history
(YYYY-MM-DD). Must be lower than equal to endDate
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `typing.Optional[int]` — Filter the history for a specific webhook id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/brevo/webhooks/client.py">get_webhook</a>(...) -> GetWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific webhook configuration.

Use this to:
- Get complete webhook configuration and settings
- Check webhook event subscriptions and triggers
- Review authentication and security settings
- Verify webhook URL and custom headers
- Access webhook creation and modification history

Key information returned:
- Complete webhook details and configuration
- Event types and channel subscriptions
- Authentication credentials and methods
- Custom headers and request settings
- Webhook status and activity information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.webhooks.get_webhook(
    webhook_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `int` — Id of the webhook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/brevo/webhooks/client.py">update_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing webhook configuration and event subscriptions.

Use this to:
- Modify webhook event subscriptions and triggers
- Update webhook URL and endpoint configuration
- Change authentication settings and credentials
- Adjust custom headers and request parameters
- Enable or disable specific webhook events

Key information returned:
- Success confirmation of webhook updates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.webhooks.update_webhook(
    webhook_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `int` — Id of the webhook
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[UpdateWebhookRequestAuth]` — Add authentication on webhook url
    
</dd>
</dl>

<dl>
<dd>

**batched:** `typing.Optional[bool]` — To send batched webhooks
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the webhook
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Inbound domain of webhook, used in case of event type `inbound`
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[UpdateWebhookRequestEventsItem]]` 

- Events triggering the webhook. Possible values for
**Transactional** type webhook: #### `sent` OR `request`,
`delivered`, `hardBounce`, `softBounce`, `blocked`, `spam`,
`invalid`, `deferred`, `click`, `opened`, `uniqueOpened` and
`unsubscribed` - Possible values for **Marketing** type webhook:
#### `spam`, `opened`, `click`, `hardBounce`, `softBounce`,
`unsubscribed`, `listAddition` & `delivered` - Possible values
for **Inbound** type webhook: #### `inboundEmailProcessed`
#### `reply`
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.List[UpdateWebhookRequestHeadersItem]]` — Custom headers to be send with webhooks
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the webhook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/brevo/webhooks/client.py">delete_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a webhook and stops all event notifications.

Use this to:
- Remove unused or obsolete webhook configurations
- Clean up webhook endpoints and subscriptions
- Stop event notifications to specific URLs
- Maintain organized webhook management

Key information returned:
- Success confirmation of webhook deletion
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.webhooks.delete_webhook(
    webhook_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `int` — Id of the webhook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExternalFeeds
<details><summary><code>client.external_feeds.<a href="src/brevo/external_feeds/client.py">get_all_external_feeds</a>(...) -> GetAllExternalFeedsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all external feeds from your Brevo account with filtering and pagination.

**Use this to:**
- Get an overview of all external data feeds
- Find feeds by name using search functionality
- Filter feeds by creation date range
- Browse feeds by authentication type
- Monitor feed library organization and usage

**Key information returned:**
- Feed details (UUID, name, URL, authentication type)
- Feed configuration and settings
- Creation and modification timestamps
- Feed status and error information
- Authentication and header configurations

**Important considerations:**
- External feeds enable dynamic content in email campaigns
- Feeds must be accessible from Brevo servers
- Authentication credentials are securely stored
- Feed performance affects campaign delivery
- Use pagination for accounts with many feeds
- Date range filtering limited to 30 days maximum
- Search functionality works on feed name matching
- Internal feeds are system-managed and cannot be modified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
import datetime

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.external_feeds.get_all_external_feeds(
    search="product",
    start_date=datetime.date.fromisoformat("2024-01-01"),
    end_date=datetime.date.fromisoformat("2024-01-31"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Can be used to filter records by search keyword on feed name
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 

Mandatory if `endDate` is used. Starting date (YYYY-MM-DD) from which
you want to fetch the list. Can be maximum 30 days older than current
date.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 

Mandatory if `startDate` is used. Ending date (YYYY-MM-DD) till which
you want to fetch the list. Maximum time period that can be selected is
one month.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetAllExternalFeedsRequestSort]` 

Sort the results in the ascending/descending order of record creation.
Default order is **descending** if `sort` is not passed.
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[GetAllExternalFeedsRequestAuthType]` — Filter the records by `authType` of the feed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document on the page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external_feeds.<a href="src/brevo/external_feeds/client.py">create_external_feed</a>(...) -> CreateExternalFeedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new external feed for dynamic content in email campaigns.

**Use this to:**
- Set up external data sources for dynamic content
- Configure authentication for protected feeds
- Enable real-time content updates in campaigns
- Establish connections to product catalogs, blogs, or APIs

**Key information returned:**
- Created feed UUID for reference in campaigns
- Success confirmation

**Important considerations:**
- Feed URL must be accessible from Brevo infrastructure
- Authentication credentials are securely encrypted
- Test feed accessibility before campaign use
- Consider feed response time for campaign performance
- Monitor feed reliability and uptime
- Use caching for frequently accessed feeds
- Maximum 5 retry attempts allowed for failed requests
- Custom headers support for API integration requirements
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.external_feeds.create_external_feed(
    name="Public API Feed",
    url="https://jsonplaceholder.typicode.com/posts",
    auth_type="noAuth",
    max_retries=3,
    cache=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the feed
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL of the external data source
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[CreateExternalFeedRequestAuthType]` — Authentication type for accessing the feed
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Username for basic authentication (required if authType is 'basic')
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password for basic authentication (required if authType is 'basic')
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — Token for token-based authentication (required if authType is 'token')
    
</dd>
</dl>

<dl>
<dd>

**max_retries:** `typing.Optional[int]` — Maximum number of retry attempts for failed requests
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — Whether to cache the feed response
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.List[CreateExternalFeedRequestHeadersItem]]` — Custom HTTP headers for the feed request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external_feeds.<a href="src/brevo/external_feeds/client.py">get_external_feed_by_uuid</a>(...) -> GetExternalFeedByUuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of a specific external feed by its UUID.

**Use this to:**
- Get complete configuration of an external feed
- Check feed authentication settings
- Review feed personalization options
- Verify feed URL and parameters
- Monitor feed modification history

**Key information returned:**
- Complete feed configuration and settings
- Authentication credentials and headers
- Personalization and fallback settings
- Creation and modification timestamps
- Cache and retry configurations

**Important considerations:**
- UUID must exist in your account
- Provides complete feed information for troubleshooting
- Essential before making modifications
- Shows current feed health status
- Useful for debugging feed issues
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.external_feeds.get_external_feed_by_uuid(
    uuid_="b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid:** `str` — UUID of the feed to fetch
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external_feeds.<a href="src/brevo/external_feeds/client.py">update_external_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates configuration of an existing external feed.

**Use this to:**
- Update feed URLs when data sources change
- Modify authentication credentials
- Change cache and retry settings
- Update custom headers
- Rename feeds for better organization

**Key information returned:**
- Success confirmation message

**Important considerations:**
- Only provided fields will be updated
- Feed UUID must exist in your account
- Authentication changes require verification
- URL changes should be tested before campaign use
- Monitor campaigns using this feed after updates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.external_feeds.update_external_feed(
    uuid_="b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6",
    name="Updated Product Catalog",
    url="https://api.newstore.com/products/v2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid:** `str` — UUID of the feed to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the feed
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the external data source
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[UpdateExternalFeedRequestAuthType]` — Authentication type for accessing the feed
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Username for basic authentication
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password for basic authentication
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — Token for token-based authentication
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.List[UpdateExternalFeedRequestHeadersItem]]` — Custom HTTP headers for the feed request
    
</dd>
</dl>

<dl>
<dd>

**max_retries:** `typing.Optional[int]` — Maximum number of retry attempts for failed requests
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — Whether to cache the feed response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.external_feeds.<a href="src/brevo/external_feeds/client.py">delete_external_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an external feed from your Brevo account.

**Use this to:**
- Remove external feeds that are no longer needed
- Clean up unused data sources
- Remove test or outdated feeds
- Maintain organized feed library

**Key information returned:**
- Success confirmation message

**Important considerations:**
- This action is PERMANENT and cannot be undone
- Feed configuration and history will be lost
- Check if feed is used in active campaigns before deletion
- Remove feed references from email templates
- Consider deactivating instead of deleting if unsure
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.external_feeds.delete_external_feed(
    uuid_="b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid:** `str` — UUID of the feed to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomObjects
<details><summary><code>client.custom_objects.<a href="src/brevo/custom_objects/client.py">upsertrecords</a>(...) -> UpsertrecordsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note title="Enterprise access only">Custom objects are only available to Enterprise plans.
This feature is in beta. These are subject to change.</Note>
This API allows bulk upsert of object records in a single request. Each object record may include
  - Attributes
  - Identifiers
  - Associations
**Response:**
  The API processes the request asynchronously and returns a processId that you can use to track the background process status.
**API and Schema Limitation:**
  - Size:
      - Max 1000 objects records per request
      - Max request body size: 1 MB
  - Max 500 attributes defined per object record upsert request
    - This is coherent with schema limitation: an object cannot have more than 500 attributes.
    - Worth noting: Nothing happens If an attribute is mentioned in the request, but was not previously defined for the object schema (no error, no attribute creation)
  - Max 10 associations defined per associated object type, in each record of the request
    - This is not a schema limitation. You can associate an object record to an unlimited number of other object records by running multiple requests.
**Errors:**
    - Make sure both object records exist before associating them, else the API will return an error.
    - This route does not create objects. The object where the object records are upserted by this API must be created already else the API will return an error "invalid object type".
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.custom_objects import UpsertrecordsRequestRecordsItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.custom_objects.upsertrecords(
    object_type="vehicle",
    records=[
        UpsertrecordsRequestRecordsItem()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `str` — object type for the attribute
    
</dd>
</dl>

<dl>
<dd>

**records:** `typing.List[UpsertrecordsRequestRecordsItem]` — List of object records to be upsert. Each record can have attributes, identifiers, and associations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/brevo/custom_objects/client.py">getrecords</a>(...) -> GetrecordsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note title="Enterprise access only">Custom objects are only available to Enterprise plans.
This feature is in beta. These are subject to change.</Note>
This API retrieves a list of object records along with their associated records and provides the total count of records for the specified object. **Note**: Contact as object type is not supported in this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.custom_objects.getrecords(
    object_type="vehicle",
    limit=1000000,
    page_num=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `str` — object type for the attribute
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Number of records returned per page
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `int` — Page number for pagination. It's used to fetch the object records on a provided page number. Must be a valid positive integer.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetrecordsRequestSort]` — Sort order, must be 'asc' or 'desc'. Default to 'desc' if not provided.
    
</dd>
</dl>

<dl>
<dd>

**association:** `typing.Optional[GetrecordsRequestAssociation]` — Whether to include associations, must be 'true' or 'false'. Default to 'false' if not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/brevo/custom_objects/client.py">batch_delete_object_records</a>(...) -> BatchDeleteObjectRecordsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to delete multiple object records of the same object-type in one request.
The request is accepted and processed asynchronously.   You can track the status of the deletion process using the returned **processId**.
**API and Schema Limitations:** - Each request can contain up to **1000** object record identifiers   - If more records must be deleted → send multiple batch requests
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.custom_objects import BatchDeleteObjectRecordsRequestIdentifiersIds

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.custom_objects.batch_delete_object_records(
    object_type="vehicle",
    identifiers=BatchDeleteObjectRecordsRequestIdentifiersIds(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `str` — Object type for the records to delete
    
</dd>
</dl>

<dl>
<dd>

**identifiers:** `typing.Optional[BatchDeleteObjectRecordsRequestIdentifiers]` — One of the below must be provided
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contacts
<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_contacts</a>(...) -> GetContacts</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_contacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetContactsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `typing.Optional[int]` — Id of the segment. **Either listIds or segmentId can be passed.**
    
</dd>
</dl>

<dl>
<dd>

**list_ids:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Ids of the list. **Either listIds or segmentId can be passed.**
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Filter the contacts on the basis of attributes. **Allowed operator: equals. For multiple-choice options, the filter will apply an AND condition between the options. For category attributes, the filter will work with both id and value. (e.g. filter=equals(FIRSTNAME,"Antoine"), filter=equals(B1, true), filter=equals(DOB, "1989-11-23"), filter=equals(GENDER, "1"), filter=equals(GENDER, "MALE"), filter=equals(COUNTRY,"USA, INDIA")**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">create_contact</a>(...) -> CreateContactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Follow this format when passing a "SMS" phone number as an attribute.
Accepted Number Formats 91xxxxxxxxxx +91xxxxxxxxxx 0091xxxxxxxxxx</Note>
Creates new contacts on Brevo. Contacts can be created by passing either - <br><br> 1. email address of the contact (email_id),  <br> 2. phone number of the contact (to be passed as "SMS" field in "attributes" along with proper country code), For example- {"SMS":"+91xxxxxxxxxx"} or {"SMS":"0091xxxxxxxxxx"} <br> 3. ext_id <br>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.create_contact()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, CreateContactRequestAttributesValue]]` — Pass the set of attributes and their values. The attribute's parameter should be passed in capital letter while creating a contact. Values that don't match the attribute type (e.g. text or string in a date attribute) will be ignored. **These attributes must be present in your Brevo account**. For eg: **{"FNAME":"Elly", "LNAME":"Roger", "COUNTRIES": ["India","China"]}**
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the user. **Mandatory if "ext_id"  & "SMS" field is not passed.**
    
</dd>
</dl>

<dl>
<dd>

**email_blacklisted:** `typing.Optional[bool]` — Set this field to blacklist the contact for emails (emailBlacklisted = true)
    
</dd>
</dl>

<dl>
<dd>

**ext_id:** `typing.Optional[str]` — Pass your own Id to create a contact.
    
</dd>
</dl>

<dl>
<dd>

**list_ids:** `typing.Optional[typing.List[int]]` — Ids of the lists to add the contact to
    
</dd>
</dl>

<dl>
<dd>

**sms_blacklisted:** `typing.Optional[bool]` — Set this field to blacklist the contact for SMS (smsBlacklisted = true)
    
</dd>
</dl>

<dl>
<dd>

**smtp_blacklist_sender:** `typing.Optional[typing.List[str]]` — transactional email forbidden sender for contact. Use only for email Contact ( only available if updateEnabled = true )
    
</dd>
</dl>

<dl>
<dd>

**update_enabled:** `typing.Optional[bool]` — Facilitate to update the existing contact in the same request (updateEnabled = true)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_attributes</a>() -> GetAttributesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_attributes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">create_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.create_attribute(
    attribute_category="normal",
    attribute_name="attributeName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_category:** `CreateAttributeRequestAttributeCategory` — Category of the attribute
    
</dd>
</dl>

<dl>
<dd>

**attribute_name:** `str` — Name of the attribute
    
</dd>
</dl>

<dl>
<dd>

**enumeration:** `typing.Optional[typing.List[CreateAttributeRequestEnumerationItem]]` — List of values and labels that the attribute can take. **Use only if the attribute's category is "category"**. None of the category options can exceed max 200 characters. For example: **[{"value":1, "label":"male"}, {"value":2, "label":"female"}]**
    
</dd>
</dl>

<dl>
<dd>

**is_recurring:** `typing.Optional[bool]` — Type of the attribute. **Use only if the attribute's category is 'calculated' or 'global'**
    
</dd>
</dl>

<dl>
<dd>

**multi_category_options:** `typing.Optional[typing.List[str]]` — List of options you want to add for multiple-choice attribute. **Use only if the attribute's category is "normal" and attribute's type is "multiple-choice". None of the multicategory options can exceed max 200 characters.** For example: **["USA","INDIA"]**
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreateAttributeRequestType]` — Type of the attribute. **Use only if the attribute's category is 'normal', 'category' or 'transactional'** Type **user and multiple-choice** is only available if the category is **normal** attribute Type **id** is only available if the category is **transactional** attribute Type **category** is only available if the category is **category** attribute
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Value of the attribute. **Use only if the attribute's category is 'calculated' or 'global'**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">update_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.update_attribute(
    attribute_category="category",
    attribute_name="attributeName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_category:** `UpdateAttributeRequestAttributeCategory` — Category of the attribute
    
</dd>
</dl>

<dl>
<dd>

**attribute_name:** `str` — Name of the existing attribute
    
</dd>
</dl>

<dl>
<dd>

**enumeration:** `typing.Optional[typing.List[UpdateAttributeRequestEnumerationItem]]` — List of the values and labels that the attribute can take. **Use only if the attribute's category is "category"** None of the category options can exceed max 200 characters. For example, **[{"value":1, "label":"male"}, {"value":2, "label":"female"}]**
    
</dd>
</dl>

<dl>
<dd>

**multi_category_options:** `typing.Optional[typing.List[str]]` — Use this option to add multiple-choice attributes options only if the attribute's category is "normal". **This option is specifically designed for updating multiple-choice attributes. None of the multicategory options can exceed max 200 characters.**. For example: **["USA","INDIA"]**
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Value of the attribute to update. **Use only if the attribute's category is 'calculated' or 'global'**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">delete_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.delete_attribute(
    attribute_category="normal",
    attribute_name="attributeName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_category:** `DeleteAttributeRequestAttributeCategory` — Category of the attribute
    
</dd>
</dl>

<dl>
<dd>

**attribute_name:** `str` — Name of the existing attribute
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">delete_multi_attribute_options</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.delete_multi_attribute_options(
    multiple_choice_attribute="multipleChoiceAttribute",
    multiple_choice_attribute_option="multipleChoiceAttributeOption",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_type:** `typing.Literal` — Type of the attribute
    
</dd>
</dl>

<dl>
<dd>

**multiple_choice_attribute:** `str` — Name of the existing multiple-choice attribute
    
</dd>
</dl>

<dl>
<dd>

**multiple_choice_attribute_option:** `str` — Name of the existing multiple-choice attribute option that you want to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">update_batch_contacts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.update_batch_contacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contacts:** `typing.Optional[typing.List[UpdateBatchContactsRequestContactsItem]]` — List of contacts to be updated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">create_doi_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note title="How to use attributes param?">attributes param in this endpoint is an object containing key-value pairs where values can be either a string, integer, array, or boolean. You can create key-value pairs with these four datatypes. When a value is an array, it should be an array of strings.</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.create_doi_contact(
    email="elly@example.com",
    include_list_ids=[
        36
    ],
    redirection_url="http://requestb.in/173lyyx1",
    template_id=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email address where the confirmation email will be sent. This email address will be the identifier for all other contact attributes.
    
</dd>
</dl>

<dl>
<dd>

**include_list_ids:** `typing.List[int]` — Lists under user account where contact should be added
    
</dd>
</dl>

<dl>
<dd>

**redirection_url:** `str` — URL of the web page that user will be redirected to after clicking on the double opt in URL. When editing your DOI template you can reference this URL by using the tag **{{ params.DOIurl }}**.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `int` — Id of the Double opt-in (DOI) template
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, CreateDoiContactRequestAttributesValue]]` — Pass the set of attributes and their values. **These attributes must be present in your Brevo account**. For eg. **{'FNAME':'Elly', 'LNAME':'Roger', 'COUNTRIES': ['India','China']}**
    
</dd>
</dl>

<dl>
<dd>

**exclude_list_ids:** `typing.Optional[typing.List[int]]` — Lists under user account where contact should not be added
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">request_contact_export</a>(...) -> RequestContactExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

It returns the background process ID which on completion calls the notify URL that you have set in the input. File will be available in csv.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.contacts import RequestContactExportRequestCustomContactFilter

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.request_contact_export(
    custom_contact_filter=RequestContactExportRequestCustomContactFilter(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_contact_filter:** `RequestContactExportRequestCustomContactFilter` — Set the filter for the contacts to be exported.
    
</dd>
</dl>

<dl>
<dd>

**disable_notification:** `typing.Optional[bool]` — To avoid generating the email notification upon contact export, pass **true**
    
</dd>
</dl>

<dl>
<dd>

**export_attributes:** `typing.Optional[typing.List[str]]` — List of all the attributes that you want to export. **These attributes must be present in your contact database. It is required if exportMandatoryAttributes is set false. ** For example: **['fname', 'lname', 'email']**
    
</dd>
</dl>

<dl>
<dd>

**export_mandatory_attributes:** `typing.Optional[bool]` — To export mandatory attributes like EMAIL, ADDED_TIME, MODIFIED_TIME
    
</dd>
</dl>

<dl>
<dd>

**export_metadata:** `typing.Optional[typing.List[str]]` — Export metadata of contacts such as _listIds, ADDED_TIME, MODIFIED_TIME.
    
</dd>
</dl>

<dl>
<dd>

**export_date_in_utc:** `typing.Optional[bool]` — Specifies whether the date fields createdAt, modifiedAt in the exported data should be returned in UTC format.
    
</dd>
</dl>

<dl>
<dd>

**export_subscription_status:** `typing.Optional[typing.List[str]]` — Export subscription status of contacts for email & sms marketting. Pass email_marketing to obtain the marketing email subscription status & sms_marketing to retrieve the marketing SMS status of the contact.
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — Webhook that will be called once the export process is finished. For reference, https://help.brevo.com/hc/en-us/articles/360007666479
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_folders</a>(...) -> GetFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Ongoing changes for this endpoint
We're dropping support for the response attributes totalSubscribers and totalBlacklisted.
These are non breaking changes.
The default value for the attributes will be 0.
The uniqueSubscribers field is deprecated</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetFoldersRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">create_folder</a>(...) -> CreateFolderResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.create_folder()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateUpdateFolder` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_folder</a>(...) -> GetFolder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Ongoing changes for this endpoint.
We're dropping support for the response attributes totalSubscribers and totalBlacklisted.
These are non breaking changes. The default value for the attributes will be 0.</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_folder(
    folder_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` — id of the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">update_folder</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.update_folder(
    folder_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` — Id of the folder
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateUpdateFolder` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">delete_folder</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.delete_folder(
    folder_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` — Id of the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_folder_lists</a>(...) -> GetFolderListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Ongoing changes for this endpoint.
We're dropping support for the response attributes totalSubscribers and totalBlacklisted.
These are non breaking changes. The default value for the attributes will be 0.</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_folder_lists(
    folder_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` — Id of the folder
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetFolderListsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">import_contacts</a>(...) -> ImportContactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

It returns the background process ID which on completion calls the notify URL that you have set in the input. **Note**: - Any contact attribute that doesn't exist in your account will be ignored at import end.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.import_contacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**disable_notification:** `typing.Optional[bool]` — To disable email notification
    
</dd>
</dl>

<dl>
<dd>

**email_blacklist:** `typing.Optional[bool]` — To blacklist all the contacts for email
    
</dd>
</dl>

<dl>
<dd>

**empty_contacts_attributes:** `typing.Optional[bool]` — To facilitate the choice to erase any attribute of the existing contacts with empty value. emptyContactsAttributes = true means the empty fields in your import will erase any attribute that currently contain data in Brevo, & emptyContactsAttributes = false means the empty fields will not affect your existing data ( **only available if `updateExistingContacts` set to true **)
    
</dd>
</dl>

<dl>
<dd>

**file_body:** `typing.Optional[str]` — **Mandatory if fileUrl and jsonBody is not defined.** CSV content to be imported. Use semicolon to separate multiple attributes. **Maximum allowed file body size is 10MB** . However we recommend a safe limit of around 8 MB to avoid the issues caused due to increase of file body size while parsing. Please use fileUrl instead to import bigger files.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — **Mandatory if fileBody and jsonBody is not defined.** URL of the file to be imported (**no local file**). Possible file formats: #### .txt, .csv, .json
    
</dd>
</dl>

<dl>
<dd>

**json_body:** `typing.Optional[typing.List[ImportContactsRequestJsonBodyItem]]` — **Mandatory if fileUrl and fileBody is not defined.** JSON content to be imported. **Maximum allowed json body size is 10MB** . However we recommend a safe limit of around 8 MB to avoid the issues caused due to increase of json body size while parsing. Please use fileUrl instead to import bigger files.
    
</dd>
</dl>

<dl>
<dd>

**list_ids:** `typing.Optional[typing.List[int]]` — **Mandatory if newList is not defined.** Ids of the lists in which the contacts shall be imported. For example, **[2, 4, 7]**.
    
</dd>
</dl>

<dl>
<dd>

**new_list:** `typing.Optional[ImportContactsRequestNewList]` — To create a new list and import the contacts into it, pass the listName and an optional folderId.
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — URL that will be called once the import process is finished. For reference, https://help.brevo.com/hc/en-us/articles/360007666479
    
</dd>
</dl>

<dl>
<dd>

**sms_blacklist:** `typing.Optional[bool]` — To blacklist all the contacts for sms
    
</dd>
</dl>

<dl>
<dd>

**update_existing_contacts:** `typing.Optional[bool]` — To facilitate the choice to update the existing contacts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_lists</a>(...) -> GetListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Ongoing changes for this endpoint.
We're dropping support for the response attributes totalSubscribers and totalBlacklisted.
These are non breaking changes. The default value for the attributes will be 0.</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_lists()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetListsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">create_list</a>(...) -> CreateListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.create_list(
    folder_id=2,
    name="Magento Customer - ES",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` — Id of the parent folder in which this list is to be created
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the list
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_list</a>(...) -> GetListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_list(
    list_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `int` — Id of the list
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to aggregate the sent email campaigns for a specific list id. **Prefer to pass your timezone in date-time format for accurate result**
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to aggregate the sent email campaigns for a specific list id. **Prefer to pass your timezone in date-time format for accurate result**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">update_list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.update_list(
    list_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `int` — Id of the list
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` — Id of the folder in which the list is to be moved. Either of the two parameters (name, folderId) can be updated at a time.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the list. Either of the two parameters (name, folderId) can be updated at a time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">delete_list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.delete_list(
    list_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `int` — Id of the list
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_contacts_from_list</a>(...) -> GetContacts</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_contacts_from_list(
    list_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `int` — Id of the list
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetContactsFromListRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">add_contact_to_list</a>(...) -> PostContactInfo</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.contacts import AddContactToListRequestBodyEmails

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.add_contact_to_list(
    list_id=1000000,
    request=AddContactToListRequestBodyEmails(
        emails=[
            "jeff32@example.com",
            "jim56@example.com"
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `int` — Id of the list
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddContactToListRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">remove_contact_from_list</a>(...) -> PostContactInfo</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.contacts import RemoveContactFromListRequestBodyEmails

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.remove_contact_from_list(
    list_id=1000000,
    request=RemoveContactFromListRequestBodyEmails(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `int` — Id of the list
    
</dd>
</dl>

<dl>
<dd>

**request:** `RemoveContactFromListRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_segments</a>(...) -> GetSegmentsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_segments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetSegmentsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_contact_info</a>(...) -> GetContactInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Follow this format when passing a "SMS" phone number as an attribute.
Accepted Number Formats 91xxxxxxxxxx +91xxxxxxxxxx 0091xxxxxxxxxx</Note>
There are 2 ways to get a contact <br><br> Option 1- https://api.brevo.com/v3/contacts/{identifier} <br><br> Option 2- https://api.brevo.com/v3/contacts/{identifier}?identifierType={} <br> <br> Option 1 only works if identifierType is email_id (for EMAIL), phone_id (for SMS) or contact_id (for ID of the contact),where you can directly pass the value of EMAIL, SMS and ID of the contact.   <br><br> Option 2 works for all identifierType, use email_id for EMAIL attribute, phone_id for SMS attribute, contact_id for ID of the contact, ext_id for EXT_ID attribute, whatsapp_id for WHATSAPP attribute, landline_number_id for LANDLINE_NUMBER attribute <br><br>Along with the contact details, this endpoint will show the statistics of contact for the recent 90 days by default. To fetch the earlier statistics, please use Get contact campaign stats ``https://developers.brevo.com/reference/contacts-7#getcontactstats`` endpoint with the appropriate date ranges.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_contact_info(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `GetContactInfoRequestIdentifier` — Email (urlencoded) OR ID of the contact OR its SMS attribute value OR EXT_ID attribute (urlencoded)
    
</dd>
</dl>

<dl>
<dd>

**identifier_type:** `typing.Optional[GetContactInfoRequestIdentifierType]` — email_id for Email, phone_id for SMS attribute, contact_id for ID of the contact, ext_id for EXT_ID attribute, whatsapp_id for WHATSAPP attribute, landline_number_id for LANDLINE_NUMBER attribute
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) of the statistic events specific to campaigns. Must be lower than equal to endDate
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) of the statistic events specific to campaigns. Must be greater than equal to startDate.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">update_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>Follow this format when passing a "SMS" phone number as an attribute.
Accepted Number Formats 91xxxxxxxxxx +91xxxxxxxxxx 0091xxxxxxxxxx</Note>
There are 2 ways to update a contact <br><br> Option 1- https://api.brevo.com/v3/contacts/{identifier} <br><br> Option 2- https://api.brevo.com/v3/contacts/{identifier}?identifierType={} <br> <br> Option 1 only works if identifierType is email_id (for EMAIL) or contact_id (for ID of the contact),where you can directly pass the value of EMAIL and ID of the contact.   <br><br> Option 2 works for all identifierType, use email_id for EMAIL attribute, contact_id for ID of the contact, ext_id for EXT_ID attribute, phone_id for SMS attribute, whatsapp_id for WHATSAPP attribute, landline_number_id for LANDLINE attribute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.update_contact(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `UpdateContactRequestIdentifier` — Email (urlencoded) OR ID of the contact OR EXT_ID attribute (urlencoded) OR its SMS attribute value OR its WHATSAPP attribute value OR its LANDLINE attribute value
    
</dd>
</dl>

<dl>
<dd>

**identifier_type:** `typing.Optional[UpdateContactRequestIdentifierType]` — email_id for Email, contact_id for ID of the contact, ext_id for EXT_ID attribute, phone_id for SMS attribute, whatsapp_id for WHATSAPP attribute, landline_number_id for LANDLINE attribute
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, UpdateContactRequestAttributesValue]]` — Pass the set of attributes to be updated. **These attributes must be present in your account**. To update existing email address of a contact with the new one please pass EMAIL in attributes. For example, **{ "EMAIL":"newemail@domain.com", "FNAME":"Ellie", "LNAME":"Roger", "COUNTRIES":["India","China"]}**. The attribute's parameter should be passed in capital letter while updating a contact. Values that don't match the attribute type (e.g. text or string in a date attribute) will be ignored .Keep in mind transactional attributes can be updated the same way as normal attributes. Mobile Number in **SMS** field should be passed with proper country code. For example: **{"SMS":"+91xxxxxxxxxx"} or {"SMS":"0091xxxxxxxxxx"}**
    
</dd>
</dl>

<dl>
<dd>

**email_blacklisted:** `typing.Optional[bool]` — Set/unset this field to blacklist/allow the contact for emails (emailBlacklisted = true)
    
</dd>
</dl>

<dl>
<dd>

**ext_id:** `typing.Optional[str]` — Pass your own Id to update ext_id of a contact.
    
</dd>
</dl>

<dl>
<dd>

**list_ids:** `typing.Optional[typing.List[int]]` — Ids of the lists to add the contact to
    
</dd>
</dl>

<dl>
<dd>

**sms_blacklisted:** `typing.Optional[bool]` — Set/unset this field to blacklist/allow the contact for SMS (smsBlacklisted = true)
    
</dd>
</dl>

<dl>
<dd>

**smtp_blacklist_sender:** `typing.Optional[typing.List[str]]` — transactional email forbidden sender for contact. Use only for email Contact
    
</dd>
</dl>

<dl>
<dd>

**unlink_list_ids:** `typing.Optional[typing.List[int]]` — Ids of the lists to remove the contact from
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">delete_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

There are 2 ways to delete a contact <br><br> Option 1- https://api.brevo.com/v3/contacts/{identifier} <br><br> Option 2- https://api.brevo.com/v3/contacts/{identifier}?identifierType={} <br> <br> Option 1 only works if identifierType is email_id (for EMAIL) or contact_id (for ID of the contact),where you can directly pass the value of EMAIL and ID of the contact.   <br><br> Option 2 works for all identifierType, use email_id for EMAIL attribute, contact_id for ID of the contact, ext_id for EXT_ID attribute, phone_id for SMS attribute, whatsapp_id for WHATSAPP attribute, landline_number_id for LANDLINE_NUMBER attribute.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.delete_contact(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `DeleteContactRequestIdentifier` — Email (urlencoded) OR ID of the contact OR EXT_ID attribute (urlencoded)
    
</dd>
</dl>

<dl>
<dd>

**identifier_type:** `typing.Optional[DeleteContactRequestIdentifierType]` — email_id for Email, contact_id for ID of the contact, ext_id for EXT_ID attribute, phone_id for SMS attribute, whatsapp_id for WHATSAPP attribute, landline_number_id for LANDLINE_NUMBER attribute
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/brevo/contacts/client.py">get_contact_stats</a>(...) -> GetContactStatsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.contacts.get_contact_stats(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `GetContactStatsRequestIdentifier` — Email (urlencoded) OR ID of the contact
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) of the statistic events specific to campaigns. Must be lower than equal to endDate
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) of the statistic events specific to campaigns. Must be greater than equal to startDate. Maximum difference between startDate and endDate should not be greater than 90 days
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conversations
<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">sets_agents_status_to_online_for23minutes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

We recommend pinging this endpoint every minute for as long as the agent has to be considered online.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.sets_agents_status_to_online_for23minutes(
    agent_id="d9nKoegKSjmCtyK78",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_email:** `typing.Optional[typing.Any]` — agent email. When sending online pings from a standalone system, it’s hard to maintain a 1-to-1 relationship between the users of both systems. In this case, an agent can be specified by their email address. If there’s no agent with the specified email address in your Brevo organization, a dummy agent will be created automatically.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[typing.Any]` — agent ID. It can be found on agent’s page or received <a href="https://developers.brevo.com/docs/conversations-webhooks">from a webhook</a>. Alternatively, you can use `agentEmail` + `agentName` + `receivedFrom` instead (all 3 fields required).
    
</dd>
</dl>

<dl>
<dd>

**agent_name:** `typing.Optional[typing.Any]` — agent name
    
</dd>
</dl>

<dl>
<dd>

**received_from:** `typing.Optional[typing.Any]` — mark your messages to distinguish messages created by you from the others.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">send_a_message_as_an_agent</a>(...) -> ConversationsMessage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.send_a_message_as_an_agent(
    agent_id="d9nKoegKSjmCtyK78",
    text="Hello! How can I help you?",
    visitor_id="kZMvWhf8npAu3H6qd57w2Hv6nh6rnxvg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**visitor_id:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**agent_email:** `typing.Optional[typing.Any]` — agent email. When sending messages from a standalone system, it’s hard to maintain a 1-to-1 relationship between the users of both systems. In this case, an agent can be specified by their email address.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[typing.Any]` — agent ID. It can be found on agent’s page or received <a href="https://developers.brevo.com/docs/conversations-webhooks">from a webhook</a>. Alternatively, you can use `agentEmail` + `agentName` + `receivedFrom` instead (all 3 fields required).
    
</dd>
</dl>

<dl>
<dd>

**agent_name:** `typing.Optional[typing.Any]` — agent name
    
</dd>
</dl>

<dl>
<dd>

**received_from:** `typing.Optional[typing.Any]` — mark your messages to distinguish messages created by you from the others.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">get_a_message</a>(...) -> ConversationsMessage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.get_a_message(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the message
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">update_a_message_sent_by_an_agent</a>(...) -> ConversationsMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only agents’ messages can be edited.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.update_a_message_sent_by_an_agent(
    id="id",
    text="Good morning! How can I help you?",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the message
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — edited message text
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">delete_a_message_sent_by_an_agent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only agents’ messages can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.delete_a_message_sent_by_an_agent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the message
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">send_an_automated_message_to_a_visitor</a>(...) -> ConversationsMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Example of automated messages: order status, announce new features in your web app, etc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.send_an_automated_message_to_a_visitor(
    group_id="PjRBMhWGen6aRHjif",
    text="Your order has shipped! Here’s your tracking number: 9114 5847 3325 9667 4328 88",
    visitor_id="kZMvWhf8npAu3H6qd57w2Hv6nh6rnxvg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**visitor_id:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[typing.Any]` — agent ID. It can be found on agent’s page or received <a href="https://developers.brevo.com/docs/conversations-webhooks">from a webhook</a>.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[typing.Any]` — group ID. It can be found on group’s page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">get_an_automated_message</a>(...) -> ConversationsMessage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.get_an_automated_message(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the message sent previously
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">update_an_automated_message</a>(...) -> ConversationsMessage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.update_an_automated_message(
    id="id",
    text="Your order has shipped! Here’s your tracking number: 9114 5847 4668 7775 9233 54",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the message
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — edited message text
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">delete_an_automated_message</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.delete_an_automated_message(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the message
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/brevo/conversations/client.py">set_visitor_group_assignment</a>(...) -> PutConversationsVisitorGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns a visitor to a specific agent group or removes them from their current group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.conversations.set_visitor_group_assignment(
    group_id="PjRBMhWGen6aRHjif",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ecommerce
<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_categories</a>(...) -> GetCategoriesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCategoriesRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by category ids
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by category name
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the categories modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[str]` — Filter (urlencoded) the categories created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**is_deleted:** `typing.Optional[str]` — Filter categories by their deletion status. If `false` is passed, only categories that are not deleted will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_update_category</a>(...) -> CreateUpdateCategoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_update_category(
    id="CAT123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique Category ID as saved in the shop
    
</dd>
</dl>

<dl>
<dd>

**deleted_at:** `typing.Optional[str]` — UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) of the category deleted from the shop's database
    
</dd>
</dl>

<dl>
<dd>

**is_deleted:** `typing.Optional[bool]` — category deleted from the shop's database
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — **Mandatory in case of creation**. Name of the Category, as displayed in the shop
    
</dd>
</dl>

<dl>
<dd>

**update_enabled:** `typing.Optional[bool]` — Facilitate to update the existing category in the same request (updateEnabled = true)
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL to the category
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_update_batch_category</a>(...) -> CreateUpdateBatchCategoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.ecommerce import CreateUpdateBatchCategoryRequestCategoriesItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_update_batch_category(
    categories=[
        CreateUpdateBatchCategoryRequestCategoriesItem(
            id="CAT123",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**categories:** `typing.List[CreateUpdateBatchCategoryRequestCategoriesItem]` — array of categories objects
    
</dd>
</dl>

<dl>
<dd>

**update_enabled:** `typing.Optional[bool]` — Facilitate to update the existing categories in the same request (updateEnabled = true)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_category_info</a>(...) -> GetCategoryDetails</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_category_info(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Category ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">activate_the_e_commerce_app</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Getting access to Brevo eCommerce.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.activate_the_e_commerce_app()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_attribution_metrics_for_one_or_more_brevo_campaigns_or_workflows</a>(...) -> GetEcommerceAttributionMetricsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
import datetime

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_attribution_metrics_for_one_or_more_brevo_campaigns_or_workflows(
    period_from=datetime.datetime.fromisoformat("2022-01-02T00:00:00+00:00"),
    period_to=datetime.datetime.fromisoformat("2022-01-03T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**period_from:** `typing.Optional[datetime.datetime]` — When getting metrics for a specific period, define the starting datetime in RFC3339 format
    
</dd>
</dl>

<dl>
<dd>

**period_to:** `typing.Optional[datetime.datetime]` — When getting metrics for a specific period, define the end datetime in RFC3339 format
    
</dd>
</dl>

<dl>
<dd>

**email_campaign_id_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The email campaign ID(s) to get metrics for
    
</dd>
</dl>

<dl>
<dd>

**sms_campaign_id_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The SMS campaign ID(s) to get metrics for
    
</dd>
</dl>

<dl>
<dd>

**automation_workflow_email_id_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The automation workflow ID(s) to get email attribution metrics for
    
</dd>
</dl>

<dl>
<dd>

**automation_workflow_sms_id_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The automation workflow ID(s) to get SMS attribution metrics for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_detailed_attribution_metrics_for_a_single_brevo_campaign_or_workflow</a>(...) -> GetEcommerceAttributionMetricsConversionSourceConversionSourceIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_detailed_attribution_metrics_for_a_single_brevo_campaign_or_workflow(
    conversion_source="email_campaign",
    conversion_source_id="sale",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversion_source:** `GetEcommerceAttributionMetricsConversionSourceConversionSourceIdRequestConversionSource` — The Brevo campaign type or workflow type for which data will be retrieved
    
</dd>
</dl>

<dl>
<dd>

**conversion_source_id:** `str` — The Brevo campaign or automation workflow id for which data will be retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_attributed_product_sales_for_a_single_brevo_campaign_or_workflow</a>(...) -> GetEcommerceAttributionProductsConversionSourceConversionSourceIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_attributed_product_sales_for_a_single_brevo_campaign_or_workflow(
    conversion_source="email_campaign",
    conversion_source_id="sale",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversion_source:** `GetEcommerceAttributionProductsConversionSourceConversionSourceIdRequestConversionSource` — The Brevo campaign or automation workflow type for which data will be retrieved
    
</dd>
</dl>

<dl>
<dd>

**conversion_source_id:** `str` — The Brevo campaign or automation workflow id for which data will be retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_the_iso4217compliant_display_currency_code_for_your_brevo_account</a>() -> GetEcommerceConfigDisplayCurrencyResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_the_iso4217compliant_display_currency_code_for_your_brevo_account()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">set_config_display_currency</a>(...) -> SetConfigDisplayCurrencyResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.set_config_display_currency(
    code="EUR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` — ISO 4217 compliant display currency code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_orders</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the orders
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_orders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetOrdersRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the orders modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[str]` — Filter (urlencoded) the orders created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manages the transactional status of the order
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, OrderProductsItem
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_order(
    amount=308.42,
    created_at="2021-07-29T20:59:23.383Z",
    id="14",
    products=[
        OrderProductsItem(
            price=99.99,
            product_id="P1",
        )
    ],
    status="completed",
    updated_at="2021-07-30T10:59:23.383Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Order` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_batch_order</a>(...) -> CreateBatchOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple orders at one time instead of one order at a time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, Order, OrderProductsItem
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_batch_order(
    orders=[
        Order(
            amount=308.42,
            created_at="2021-07-29T20:59:23.383Z",
            id="14",
            products=[
                OrderProductsItem(
                    price=99.99,
                    product_id="P1",
                )
            ],
            status="completed",
            updated_at="2021-07-30T10:59:23.383Z",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**orders:** `typing.List[Order]` — array of order objects
    
</dd>
</dl>

<dl>
<dd>

**historical:** `typing.Optional[bool]` — Defines wether you want your orders to be considered as live data or as historical data (import of past data, synchronising data). True: orders will not trigger any automation workflows. False: orders will trigger workflows as usual.
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — Notify Url provided by client_dev to get the status of batch request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_products</a>(...) -> GetProductsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_products()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetProductsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by product ids
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by product name, minimum 3 characters should be present for search.
    
</dd>
</dl>

<dl>
<dd>

**price_lte:** `typing.Optional[float]` — Price filter for products less than and equals to particular amount
    
</dd>
</dl>

<dl>
<dd>

**price_gte:** `typing.Optional[float]` — Price filter for products greater than and equals to particular amount
    
</dd>
</dl>

<dl>
<dd>

**price_lt:** `typing.Optional[float]` — Price filter for products less than particular amount
    
</dd>
</dl>

<dl>
<dd>

**price_gt:** `typing.Optional[float]` — Price filter for products greater than particular amount
    
</dd>
</dl>

<dl>
<dd>

**price_eq:** `typing.Optional[float]` — Price filter for products equals to particular amount
    
</dd>
</dl>

<dl>
<dd>

**price_ne:** `typing.Optional[float]` — Price filter for products not equals to particular amount
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by categories ids
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the orders modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[str]` — Filter (urlencoded) the orders created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**is_deleted:** `typing.Optional[str]` — Filter products by their deletion status. If `false` is passed, only products that are not deleted will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_update_product</a>(...) -> CreateUpdateProductResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_update_product(
    id="P11",
    name="Iphone 11",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Product ID for which you requested the details
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Mandatory in case of creation**. Name of the product for which you requested the details
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.List[str]]` — Category ID-s of the product
    
</dd>
</dl>

<dl>
<dd>

**deleted_at:** `typing.Optional[str]` — UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) of the product deleted from the shop's database
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — Absolute URL to the cover image of the product
    
</dd>
</dl>

<dl>
<dd>

**is_deleted:** `typing.Optional[bool]` — product deleted from the shop's database
    
</dd>
</dl>

<dl>
<dd>

**meta_info:** `typing.Optional[typing.Dict[str, CreateUpdateProductRequestMetaInfoValue]]` — Meta data of product such as description, vendor, producer, stock level. The size of cumulative metaInfo shall not exceed **1000 KB**. Maximum length of metaInfo object can be 20.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent product id of the product
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[float]` — Price of the product
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — Product identifier from the shop
    
</dd>
</dl>

<dl>
<dd>

**stock:** `typing.Optional[float]` — Current stock value of the product from the shop's database
    
</dd>
</dl>

<dl>
<dd>

**update_enabled:** `typing.Optional[bool]` — Facilitate to update the existing category in the same request (updateEnabled = true)
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL to the product
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_update_batch_products</a>(...) -> CreateUpdateBatchProductsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.ecommerce import CreateUpdateBatchProductsRequestProductsItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_update_batch_products(
    products=[
        CreateUpdateBatchProductsRequestProductsItem(
            id="P11",
            name="Iphone 11",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**products:** `typing.List[CreateUpdateBatchProductsRequestProductsItem]` — array of products objects
    
</dd>
</dl>

<dl>
<dd>

**update_enabled:** `typing.Optional[bool]` — Facilitate to update the existing categories in the same request (updateEnabled = true)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">get_product_info</a>(...) -> GetProductDetails</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.get_product_info(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Product ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/brevo/ecommerce/client.py">create_product_alert</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.ecommerce.create_product_alert(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Product ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Literal` — Alert type
    
</dd>
</dl>

<dl>
<dd>

**contact_identifiers:** `typing.Optional[CreateProductAlertRequestContactIdentifiers]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Coupons
<details><summary><code>client.coupons.<a href="src/brevo/coupons/client.py">get_coupon_collections</a>(...) -> GetCouponCollection</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.coupons.get_coupon_collections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document on the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCouponCollectionsRequestSort]` — Sort the results by creation time in ascending/descending order
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetCouponCollectionsRequestSortBy]` — The field used to sort coupon collections
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.coupons.<a href="src/brevo/coupons/client.py">create_coupon_collection</a>(...) -> CreateCouponCollectionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.coupons.create_coupon_collection(
    default_coupon="Winter",
    name="10%OFF",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**default_coupon:** `str` — Default coupons collection name
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the coupons collection
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[datetime.datetime]` — Specify an expiration date for the coupon collection in RFC3339 format. Use null to remove the expiration date.
    
</dd>
</dl>

<dl>
<dd>

**remaining_coupons_alert:** `typing.Optional[int]` — Send a notification alert (email) when the remaining coupons count is equal or fall bellow this number. Use null to disable alerts.
    
</dd>
</dl>

<dl>
<dd>

**remaining_days_alert:** `typing.Optional[int]` — Send a notification alert (email) when the remaining days until the expiration date are equal or fall bellow this number. Use null to disable alerts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.coupons.<a href="src/brevo/coupons/client.py">get_coupon_collection</a>(...) -> GetCouponCollection</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.coupons.get_coupon_collection(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the collection to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.coupons.<a href="src/brevo/coupons/client.py">update_coupon_collection</a>(...) -> UpdateCouponCollectionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.coupons.update_coupon_collection(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the collection to update
    
</dd>
</dl>

<dl>
<dd>

**default_coupon:** `typing.Optional[str]` — A default coupon to be used in case there are no coupons left
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[datetime.datetime]` — Specify an expiration date for the coupon collection in RFC3339 format. Use null to remove the expiration date.
    
</dd>
</dl>

<dl>
<dd>

**remaining_coupons_alert:** `typing.Optional[int]` — Send a notification alert (email) when the remaining coupons count is equal or fall bellow this number. Use null to disable alerts.
    
</dd>
</dl>

<dl>
<dd>

**remaining_days_alert:** `typing.Optional[int]` — Send a notification alert (email) when the remaining days until the expiration date are equal or fall bellow this number. Use null to disable alerts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.coupons.<a href="src/brevo/coupons/client.py">create_coupons</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.coupons.create_coupons(
    collection_id="23befbae-1505-47a8-bd27-e30ef739f32c",
    coupons=[
        "Uf12AF"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — The id of the coupon collection for which the coupons will be created
    
</dd>
</dl>

<dl>
<dd>

**coupons:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payments
<details><summary><code>client.payments.<a href="src/brevo/payments/client.py">create_payment_request</a>(...) -> CreatePaymentRequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, Cart
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.payments.create_payment_request(
    cart=Cart(
        currency="EUR",
        specific_amount=1200,
    ),
    contact_id=43,
    reference="Invoice #INV0001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cart:** `Cart` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `int` — Brevo ID of the contact requested to pay.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `str` — Reference of the payment request, it will appear on the payment page.
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[Configuration]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of payment request.
    
</dd>
</dl>

<dl>
<dd>

**notification:** `typing.Optional[Notification]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/brevo/payments/client.py">get_payment_request</a>(...) -> GetPaymentRequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.payments.get_payment_request(
    id="050db7b0-9bb7-4c1e-9c68-5a8dace8c1dc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the payment Request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/brevo/payments/client.py">delete_payment_request</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.payments.delete_payment_request(
    id="9ae7d68a-565c-4695-9381-d8fb3e3a14cc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the payment request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Event
<details><summary><code>client.event.<a href="src/brevo/event/client.py">create_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an event to track a contact's interaction.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.event import CreateEventRequestIdentifiers

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.event.create_event(
    event_name="video_played",
    identifiers=CreateEventRequestIdentifiers(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_name:** `str` — The name of the event that occurred. This is how you will find your event in Brevo. Limited to 255 characters, alphanumerical characters and - _ only.
    
</dd>
</dl>

<dl>
<dd>

**identifiers:** `CreateEventRequestIdentifiers` — Identifies the contact associated with the event. At least one identifier is required.
    
</dd>
</dl>

<dl>
<dd>

**contact_properties:** `typing.Optional[typing.Dict[str, CreateEventRequestContactPropertiesValue]]` — Properties defining the state of the contact associated to this event. Useful to update contact attributes defined in your contacts database while passing the event. For example: **"FIRSTNAME": "Jane" , "AGE": 37**
    
</dd>
</dl>

<dl>
<dd>

**event_date:** `typing.Optional[str]` — Timestamp of when the event occurred (e.g. "2024-01-24T17:39:57+01:00"). If no value is passed, the timestamp of the event creation is used.
    
</dd>
</dl>

<dl>
<dd>

**event_properties:** `typing.Optional[typing.Dict[str, CreateEventRequestEventPropertiesValue]]` — Properties of the event. Top level properties and nested properties can be used to better segment contacts and personalise workflow conditions. The following field type are supported: string, number, boolean (true/false), date (Timestamp e.g. "2024-01-24T17:39:57+01:00"). Keys are limited to 255 characters, alphanumerical characters and - _ only. Size is limited to 50Kb.
    
</dd>
</dl>

<dl>
<dd>

**object:** `typing.Optional[CreateEventRequestObject]` — Identifiers of the object record associated with this event. Ignored if the object type or identifier for this record does not exist on the account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event.<a href="src/brevo/event/client.py">create_batch_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple events to track contacts' interactions in a single request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.event import CreateBatchEventsRequestItem, CreateBatchEventsRequestItemIdentifiers

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.event.create_batch_events(
    request=[
        CreateBatchEventsRequestItem(
            event_name="order_created",
            identifiers=CreateBatchEventsRequestItemIdentifiers(),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.List[CreateBatchEventsRequestItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InboundParsing
<details><summary><code>client.inbound_parsing.<a href="src/brevo/inbound_parsing/client.py">get_inbound_email_events</a>(...) -> GetInboundEmailEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will show the list of all the events for the received emails.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.inbound_parsing.get_inbound_email_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender:** `typing.Optional[str]` — Email address of the sender.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Mandatory if endDate is used. Starting date (YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss.SSSZ) from which you want to fetch the list. Maximum time period that can be selected is one month.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Mandatory if startDate is used. Ending date (YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss.SSSZ) till which you want to fetch the list. Maximum time period that can be selected is one month.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document on the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetInboundEmailEventsRequestSort]` — Sort the results in the ascending/descending order of record creation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inbound_parsing.<a href="src/brevo/inbound_parsing/client.py">get_inbound_email_events_by_uuid</a>(...) -> GetInboundEmailEventsByUuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will show the list of all events history for one particular received email.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.inbound_parsing.get_inbound_email_events_by_uuid(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid:** `str` — UUID to fetch events specific to received email
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inbound_parsing.<a href="src/brevo/inbound_parsing/client.py">get_inbound_email_attachment</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will retrieve inbound attachment with download token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.inbound_parsing.get_inbound_email_attachment(
    download_token="downloadToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**download_token:** `str` — Token to fetch a particular attachment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Balance
<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_active_balances_api</a>(...) -> BalanceLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Active Balances
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_active_balances_api(
    pid="pid",
    contact_id=1,
    balance_definition_id="balance_definition_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `int` — Contact ID
    
</dd>
</dl>

<dl>
<dd>

**balance_definition_id:** `str` — Balance Definition ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[str]` — Sort Field
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort Order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_balance_definition_list</a>(...) -> GetBalanceDefinitionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns balance definition page
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_balance_definition_list(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset to paginate records
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetBalanceDefinitionListRequestSortField]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetBalanceDefinitionListRequestSort]` — Sort direction
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetBalanceDefinitionListRequestVersion]` — Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">create_balance_definition</a>(...) -> BalanceDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates balance definition and returns information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.create_balance_definition(
    pid="pid",
    name="name",
    unit="POINTS",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the balance definition.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `PostLoyaltyBalanceProgramsPidBalanceDefinitionsRequestUnit` — Unit of balance measurement.
    
</dd>
</dl>

<dl>
<dd>

**balance_availability_duration_modifier:** `typing.Optional[PostLoyaltyBalanceProgramsPidBalanceDefinitionsRequestBalanceAvailabilityDurationModifier]` — Defines when the balance expires within the selected duration.
    
</dd>
</dl>

<dl>
<dd>

**balance_availability_duration_unit:** `typing.Optional[PostLoyaltyBalanceProgramsPidBalanceDefinitionsRequestBalanceAvailabilityDurationUnit]` — Unit of time for balance validity.
    
</dd>
</dl>

<dl>
<dd>

**balance_availability_duration_value:** `typing.Optional[int]` — Number of time units before the balance expires.
    
</dd>
</dl>

<dl>
<dd>

**balance_expiration_date:** `typing.Optional[datetime.date]` — Fixed expiration date (`dd/mm` format) as an alternative to duration-based expiry.
    
</dd>
</dl>

<dl>
<dd>

**balance_option_amount_overtaking_strategy:** `typing.Optional[PostLoyaltyBalanceProgramsPidBalanceDefinitionsRequestBalanceOptionAmountOvertakingStrategy]` — Defines whether partial credit is allowed when reaching max balance.
    
</dd>
</dl>

<dl>
<dd>

**balance_option_credit_rounding:** `typing.Optional[PostLoyaltyBalanceProgramsPidBalanceDefinitionsRequestBalanceOptionCreditRounding]` — Defines rounding strategy for credit transactions.
    
</dd>
</dl>

<dl>
<dd>

**balance_option_debit_rounding:** `typing.Optional[PostLoyaltyBalanceProgramsPidBalanceDefinitionsRequestBalanceOptionDebitRounding]` — Defines rounding strategy for debit transactions.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Short description of the balance definition.
    
</dd>
</dl>

<dl>
<dd>

**image_ref:** `typing.Optional[str]` — URL of an optional image reference.
    
</dd>
</dl>

<dl>
<dd>

**max_amount:** `typing.Optional[float]` — Maximum allowable balance amount.
    
</dd>
</dl>

<dl>
<dd>

**max_credit_amount_limit:** `typing.Optional[float]` — Maximum credit allowed per operation.
    
</dd>
</dl>

<dl>
<dd>

**max_debit_amount_limit:** `typing.Optional[float]` — Maximum debit allowed per operation.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional metadata for the balance definition.
    
</dd>
</dl>

<dl>
<dd>

**min_amount:** `typing.Optional[float]` — Minimum allowable balance amount.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_balance_definition</a>(...) -> BalanceDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns balance definition
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_balance_definition(
    pid="pid",
    bdid="bdid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetBalanceDefinitionRequestVersion]` — Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">update_balance_definition</a>(...) -> BalanceDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates Balance definition
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.update_balance_definition(
    pid="pid",
    bdid="bdid",
    name="name",
    unit="POINTS",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the balance definition.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `UpdateBalanceDefinitionRequestUnit` — Unit of balance measurement.
    
</dd>
</dl>

<dl>
<dd>

**balance_availability_duration_modifier:** `typing.Optional[UpdateBalanceDefinitionRequestBalanceAvailabilityDurationModifier]` — Defines when the balance expires within the selected duration.
    
</dd>
</dl>

<dl>
<dd>

**balance_availability_duration_unit:** `typing.Optional[UpdateBalanceDefinitionRequestBalanceAvailabilityDurationUnit]` — Unit of time for balance validity.
    
</dd>
</dl>

<dl>
<dd>

**balance_availability_duration_value:** `typing.Optional[int]` — Number of time units before the balance expires.
    
</dd>
</dl>

<dl>
<dd>

**balance_expiration_date:** `typing.Optional[str]` — Expiration date (`dd/mm` format) or empty if not applicable.
    
</dd>
</dl>

<dl>
<dd>

**balance_option_amount_overtaking_strategy:** `typing.Optional[UpdateBalanceDefinitionRequestBalanceOptionAmountOvertakingStrategy]` — Defines whether partial credit is allowed when reaching max balance.
    
</dd>
</dl>

<dl>
<dd>

**balance_option_credit_rounding:** `typing.Optional[UpdateBalanceDefinitionRequestBalanceOptionCreditRounding]` — Rounding strategy for credit transactions.
    
</dd>
</dl>

<dl>
<dd>

**balance_option_debit_rounding:** `typing.Optional[UpdateBalanceDefinitionRequestBalanceOptionDebitRounding]` — Rounding strategy for debit transactions.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Short description of the balance definition.
    
</dd>
</dl>

<dl>
<dd>

**image_ref:** `typing.Optional[str]` — URL of an optional image reference.
    
</dd>
</dl>

<dl>
<dd>

**max_amount:** `typing.Optional[float]` — Maximum allowable balance amount.
    
</dd>
</dl>

<dl>
<dd>

**max_credit_amount_limit:** `typing.Optional[float]` — Maximum credit allowed per operation.
    
</dd>
</dl>

<dl>
<dd>

**max_debit_amount_limit:** `typing.Optional[float]` — Maximum debit allowed per operation.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata for the balance definition.
    
</dd>
</dl>

<dl>
<dd>

**min_amount:** `typing.Optional[float]` — Minimum allowable balance amount.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">delete_balance_definition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Balance definition
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.delete_balance_definition(
    pid="pid",
    bdid="bdid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">create_balance_limit</a>(...) -> BalanceLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates balance limit and sends the created UUID along with the data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.create_balance_limit(
    pid="pid",
    bdid="bdid",
    constraint_type="transaction",
    duration_unit="day",
    duration_value=1,
    transaction_type="credit",
    value=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**constraint_type:** `CreateBalanceLimitRequestConstraintType` — Defines whether the limit applies to transaction count or amount.
    
</dd>
</dl>

<dl>
<dd>

**duration_unit:** `CreateBalanceLimitRequestDurationUnit` — Unit of time for which the limit is applicable.
    
</dd>
</dl>

<dl>
<dd>

**duration_value:** `int` — Number of time units for the balance limit.
    
</dd>
</dl>

<dl>
<dd>

**transaction_type:** `CreateBalanceLimitRequestTransactionType` — Specifies whether the limit applies to credit or debit transactions.
    
</dd>
</dl>

<dl>
<dd>

**value:** `int` — Maximum allowed value for the specified constraint type.
    
</dd>
</dl>

<dl>
<dd>

**sliding_schedule:** `typing.Optional[bool]` — Determines if the limit resets on a rolling schedule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_balance_limit</a>(...) -> BalanceLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches balance limits and send the created UUID along with the data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_balance_limit(
    pid="pid",
    bdid="bdid",
    blid="blid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**blid:** `str` — Balance Limit Id
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetBalanceLimitRequestVersion]` — Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">update_balance_limit</a>(...) -> BalanceLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates balance limit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**blid:** `str` — Balance Limit Id
    
</dd>
</dl>

<dl>
<dd>

**constraint_type:** `UpdateBalanceLimitRequestConstraintType` — Defines whether the limit applies to transaction count or amount.
    
</dd>
</dl>

<dl>
<dd>

**duration_unit:** `UpdateBalanceLimitRequestDurationUnit` — Unit of time for which the limit is applicable.
    
</dd>
</dl>

<dl>
<dd>

**duration_value:** `int` — Number of time units for the balance limit.
    
</dd>
</dl>

<dl>
<dd>

**transaction_type:** `UpdateBalanceLimitRequestTransactionType` — Specifies whether the limit applies to credit or debit transactions.
    
</dd>
</dl>

<dl>
<dd>

**value:** `int` — Maximum allowed value for the specified constraint type.
    
</dd>
</dl>

<dl>
<dd>

**sliding_schedule:** `typing.Optional[bool]` — Determines if the limit resets on a rolling schedule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">delete_balance_limit</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete balance limit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.delete_balance_limit(
    pid="pid",
    bdid="bdid",
    blid="blid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**bdid:** `str` — Balance Definition Id
    
</dd>
</dl>

<dl>
<dd>

**blid:** `str` — Balance Limit Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_contact_balances</a>(...) -> GetContactBalancesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns balance list
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_contact_balances(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">create_balance_order</a>(...) -> CreateBalanceOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns created order
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.create_balance_order(
    pid="pid",
    amount=1.1,
    balance_definition_id="balanceDefinitionId",
    contact_id=1,
    due_at="dueAt",
    source="source",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — Order amount (must be non-zero).
    
</dd>
</dl>

<dl>
<dd>

**balance_definition_id:** `str` — Unique identifier (UUID) of the associated balance definition.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `int` — Unique identifier of the contact placing the order (must be ≥ 1).
    
</dd>
</dl>

<dl>
<dd>

**due_at:** `str` — RFC3339 timestamp specifying when the order is due.
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` — Specifies the origin of the order (`engine` or `user`).
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` — Optional RFC3339 timestamp defining order expiration.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_subscription_balances</a>(...) -> GetSubscriptionBalancesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns subscription balances
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_subscription_balances(
    pid="pid",
    cid="cid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**cid:** `str` — Contact Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">create_subscription_balances</a>(...) -> PostLoyaltyBalanceProgramsPidSubscriptionsCidBalancesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a balance for a contact
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.create_subscription_balances(
    pid="pid",
    cid="cid",
    balance_definition_id="balanceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**cid:** `str` — Contact Id
    
</dd>
</dl>

<dl>
<dd>

**balance_definition_id:** `str` — Unique identifier (UUID) of the balance definition associated with the new balance.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">get_transaction_history_api</a>(...) -> GetLoyaltyBalanceProgramsPidTransactionHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns transaction history
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.get_transaction_history_api(
    pid="pid",
    contact_id=1,
    balance_definition_id="balanceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `int` — Contact ID
    
</dd>
</dl>

<dl>
<dd>

**balance_definition_id:** `str` — Balance Definition ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Skip a number of records
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[typing.Literal]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetLoyaltyBalanceProgramsPidTransactionHistoryRequestSort]` — Sort order, either asc or desc
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filters to apply
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">begin_transaction</a>(...) -> Transaction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates new transaction and returns information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.begin_transaction(
    pid="pid",
    amount=1.1,
    balance_definition_id="balanceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — Transaction amount (must be provided).
    
</dd>
</dl>

<dl>
<dd>

**balance_definition_id:** `str` — Unique identifier (UUID) of the associated balance definition.
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — Unique identifier for the loyalty subscription (required unless `contactId` is provided).
    
</dd>
</dl>

<dl>
<dd>

**auto_complete:** `typing.Optional[bool]` — Whether the transaction should be automatically completed.
    
</dd>
</dl>

<dl>
<dd>

**balance_expiry_in_minutes:** `typing.Optional[int]` — Optional expiry time for the balance in minutes (must be greater than 0 if provided).
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[int]` — Unique identifier of the contact involved in the transaction (required unless `LoyaltySubscriptionId` is provided).
    
</dd>
</dl>

<dl>
<dd>

**event_time:** `typing.Optional[str]` — Optional timestamp specifying when the transaction occurred.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata associated with the transaction.
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[int]` — Optional time-to-live for the transaction (must be greater than 0 if provided).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">cancel_transaction</a>(...) -> Transaction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.cancel_transaction(
    pid="pid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/brevo/balance/client.py">complete_transaction</a>(...) -> Transaction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.balance.complete_transaction(
    pid="pid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program Id
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Program
<details><summary><code>client.program.<a href="src/brevo/program/client.py">get_lp_list</a>(...) -> GetLpListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of loyalty programs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.get_lp_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetLpListRequestSortField]` — Sort documents by field
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort documents by field
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">create_new_lp</a>(...) -> LoyaltyProgram</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates loyalty program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.create_new_lp(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Required name of the loyalty program (max 128 chars).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the loyalty program (max 256 chars).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Optional unique document ID.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata related to the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">get_loyalty_program_info</a>(...) -> LoyaltyProgram</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns loyalty program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.get_loyalty_program_info(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">update_loyalty_program</a>(...) -> LoyaltyProgram</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates loyalty program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.update_loyalty_program(
    pid="pid",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Loyalty Program name
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Loyalty Program description
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Loyalty Program meta data
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">delete_loyalty_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes Loyalty Program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.delete_loyalty_program(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">partially_update_loyalty_program</a>(...) -> LoyaltyProgram</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially updates loyalty program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.partially_update_loyalty_program(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Loyalty Program description
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Loyalty Program meta data
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Loyalty Program name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">get_parameter_subscription_info</a>(...) -> GetParameterSubscriptionInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Information of balances, tiers, rewards and subscription members for a subscription
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.get_parameter_subscription_info(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — The contact ID to filter by.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[str]` — A list of filter parameters for querying the subscription info.
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — The loyalty subscription ID to filter by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">delete_contact_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete subscription for a contact
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.delete_contact_subscription(
    pid="pid",
    cid=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**cid:** `int` — Contact ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">publish_loyalty_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes loyalty program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.publish_loyalty_program(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">subscribe_member_to_a_subscription</a>(...) -> SubscribeMemberToASubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add member to a subscription
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.subscribe_member_to_a_subscription(
    pid="pid",
    member_contact_ids=[
        1
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**member_contact_ids:** `typing.List[int]` — Required, each item must be greater than or equal to 1
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[int]` — Required if LoyaltySubscriptionId is not provided, must be greater than 0
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — Required if ContactId is not provided, max length 64
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">delete_contact_members</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes member from a subscription
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.delete_contact_members(
    pid="pid",
    member_contact_ids="memberContactIds",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**member_contact_ids:** `str` — Comma-separated list of member contact IDs to delete from the subscription.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.program.<a href="src/brevo/program/client.py">subscribe_to_loyalty_program</a>(...) -> SubscribeToLoyaltyProgramResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribes to a loyalty program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.program.subscribe_to_loyalty_program(
    pid="pid",
    contact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID. A unique identifier for the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `int` — Required contact ID; must be greater than 0.
    
</dd>
</dl>

<dl>
<dd>

**creation_date:** `typing.Optional[str]` — Optional custom date-time format.
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — Optional subscription ID (max length 64).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reward
<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">get_code_count</a>(...) -> GetCodeCountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get code count
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.get_code_count(
    pid="pid",
    cpid="cpid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**cpid:** `str` — Code Pool ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">get_reward_page_api</a>(...) -> GetLoyaltyOfferProgramsPidOffersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a reward page
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.get_reward_page_api(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Pagination offset
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — State of the reward
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetLoyaltyOfferProgramsPidOffersRequestVersion]` — Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">create_reward</a>(...) -> CreateRewardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new reward in the loyalty program.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.create_reward(
    pid="pid",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Internal name of the reward
    
</dd>
</dl>

<dl>
<dd>

**public_description:** `typing.Optional[str]` — Public facing description of the reward
    
</dd>
</dl>

<dl>
<dd>

**public_image:** `typing.Optional[str]` — URL of the public image for the reward
    
</dd>
</dl>

<dl>
<dd>

**public_name:** `typing.Optional[str]` — Public facing name of the reward
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">create_voucher</a>(...) -> CreateVoucherResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a voucher and attribute it to a specific membership.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.create_voucher(
    pid="pid",
    reward_id="rewardId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**reward_id:** `str` — Reward id
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Code generated to attribute reward to a contact
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[int]` — Contact to attribute the reward
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[str]` — Reward expiration date
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — One of contactId or loyaltySubscriptionId is required
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Offer meta information (key/value object)
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[float]` — Value of the selected reward config
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">redeem_voucher</a>(...) -> Redeem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a request to redeem a voucher.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.redeem_voucher(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**attributed_reward_id:** `typing.Optional[str]` — Unique identifier for the attributed reward
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Redemption code for the reward
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[int]` — Unique identifier for the contact
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — Identifier for the loyalty subscription
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional metadata associated with the redeem request
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[RedeemVoucherRequestOrder]` — Order details for the redemption
    
</dd>
</dl>

<dl>
<dd>

**reward_id:** `typing.Optional[str]` — Unique identifier for the reward
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[int]` — Time to live in seconds for the redemption request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">complete_redeem_transaction</a>(...) -> Redeem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes voucher redeem request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.complete_redeem_transaction(
    pid="pid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — Redeem transaction ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">revoke_vouchers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke attributed vouchers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.revoke_vouchers(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**attributed_reward_ids:** `typing.Optional[str]` — Reward Attribution IDs (comma seperated)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">validate_reward</a>(...) -> ValidateRewardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a reward.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.validate_reward(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**attributed_reward_id:** `typing.Optional[str]` — Unique identifier for the attributed reward
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Validation code for the reward
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[int]` — Unique identifier for the contact
    
</dd>
</dl>

<dl>
<dd>

**loyalty_subscription_id:** `typing.Optional[str]` — Identifier for the loyalty subscription
    
</dd>
</dl>

<dl>
<dd>

**point_of_sell_id:** `typing.Optional[str]` — Identifier for the point of sale
    
</dd>
</dl>

<dl>
<dd>

**reward_id:** `typing.Optional[str]` — Unique identifier for the reward
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">get_reward_information</a>(...) -> GetLoyaltyOfferProgramsPidRewardsRidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns reward information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.get_reward_information(
    pid="pid",
    rid="rid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**rid:** `str` — Reward ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetLoyaltyOfferProgramsPidRewardsRidRequestVersion]` — Version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/brevo/reward/client.py">get_voucher_for_a_contact</a>(...) -> GetLoyaltyOfferProgramsPidVouchersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get voucher for a contact
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.reward.get_voucher_for_a_contact(
    pid="pid",
    contact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `int` — Contact ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Pagination offset
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetLoyaltyOfferProgramsPidVouchersRequestSort]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetLoyaltyOfferProgramsPidVouchersRequestSortField]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**metadata_key_value:** `typing.Optional[str]` — Metadata value for a Key filter
    
</dd>
</dl>

<dl>
<dd>

**reward_id:** `typing.Optional[str]` — Reward ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tier
<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">add_subscription_to_tier</a>(...) -> AddSubscriptionToTierResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually assigns a tier to a specific membership.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.add_subscription_to_tier(
    pid="pid",
    cid="cid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**cid:** `str` — Contact ID
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — Tier ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">get_list_of_tier_groups</a>(...) -> GetListOfTierGroupsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of tier groups defined within the loyalty program.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.get_list_of_tier_groups(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetListOfTierGroupsRequestVersion]` — Select 'active' to retrieve list of all tier groups which are live for clients. Select draft to retrieve list of all non deleted tier groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">create_tier_group</a>(...) -> TierGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new tier group in a loyalty program. *(The changes will take effect with the next publication of the loyalty program)*
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.create_tier_group(
    pid="pid",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the tier group
    
</dd>
</dl>

<dl>
<dd>

**downgrade_strategy:** `typing.Optional[CreateTierGroupRequestDowngradeStrategy]` — Select real_time to downgrade tier on real time balance updates. Select membership_anniversary to downgrade tier on subscription anniversary. Select tier_anniversary to downgrade tier on tier anniversary.
    
</dd>
</dl>

<dl>
<dd>

**tier_order:** `typing.Optional[typing.List[str]]` — Order of the tiers in the group in ascending order
    
</dd>
</dl>

<dl>
<dd>

**upgrade_strategy:** `typing.Optional[CreateTierGroupRequestUpgradeStrategy]` — Select real_time to upgrade tier on real time balance updates. Select membership_anniversary to upgrade tier on subscription anniversary. Select tier_anniversary to upgrade tier on tier anniversary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">get_tier_group</a>(...) -> TierGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns tier group information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.get_tier_group(
    pid="pid",
    gid="gid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — Tier group ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetTierGroupRequestVersion]` — Select active to retrieve active version of tier group. Select draft to retrieve latest changes in tier group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">update_tier_group</a>(...) -> TierGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a tier group from a loyalty program. *(The changes will take effect with the next publication of the loyalty program)*
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.update_tier_group(
    pid="pid",
    gid="gid",
    downgrade_strategy="real_time",
    name="name",
    tier_order=[
        "tierOrder"
    ],
    upgrade_strategy="real_time",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — Tier group ID
    
</dd>
</dl>

<dl>
<dd>

**downgrade_strategy:** `UpdateTierGroupRequestDowngradeStrategy` — Select real_time to downgrade tier on real time balance updates. Select membership_anniversary to downgrade tier on subscription anniversary. Select tier_anniversary to downgrade tier on tier anniversary.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the tier group
    
</dd>
</dl>

<dl>
<dd>

**tier_order:** `typing.List[str]` — Order of the tiers in the group in ascending order
    
</dd>
</dl>

<dl>
<dd>

**upgrade_strategy:** `UpdateTierGroupRequestUpgradeStrategy` — Select real_time to upgrade tier on real time balance updates. Select membership_anniversary to upgrade tier on subscription anniversary. Select tier_anniversary to upgrade tier on tier anniversary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">delete_tier_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a tier group from a loyalty program. *(The changes will take effect with the next publication of the loyalty program)*
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.delete_tier_group(
    pid="pid",
    gid="gid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — Tier group ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">create_tier_for_tier_group</a>(...) -> Tier</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new tier in a loyalty program tier group. *(The changes will take effect with the next publication of the loyalty program)*
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.tier import CreateTierForTierGroupRequestAccessConditionsItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.create_tier_for_tier_group(
    pid="pid",
    gid="gid",
    access_conditions=[
        CreateTierForTierGroupRequestAccessConditionsItem()
    ],
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — Tier group ID
    
</dd>
</dl>

<dl>
<dd>

**access_conditions:** `typing.List[CreateTierForTierGroupRequestAccessConditionsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the tier to be created
    
</dd>
</dl>

<dl>
<dd>

**image_ref:** `typing.Optional[str]` — Image of the tier
    
</dd>
</dl>

<dl>
<dd>

**tier_rewards:** `typing.Optional[typing.List[CreateTierForTierGroupRequestTierRewardsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">get_loyalty_program_tier</a>(...) -> GetLoyaltyProgramTierResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of tiers defined within the loyalty program.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.get_loyalty_program_tier(
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[GetLoyaltyProgramTierRequestVersion]` — Select 'active' to retrieve list of all tiers which are live for clients. Select draft to retrieve list of all non deleted tiers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">update_tier</a>(...) -> Tier</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modifies an existing tier for the specified tier group *(The changes will take effect with the next publication of the loyalty program)*
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.tier import UpdateTierRequestAccessConditionsItem, UpdateTierRequestTierRewardsItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.update_tier(
    pid="pid",
    tid="tid",
    access_conditions=[
        UpdateTierRequestAccessConditionsItem()
    ],
    name="name",
    tier_rewards=[
        UpdateTierRequestTierRewardsItem()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — Tier ID
    
</dd>
</dl>

<dl>
<dd>

**access_conditions:** `typing.List[UpdateTierRequestAccessConditionsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the tier to be created
    
</dd>
</dl>

<dl>
<dd>

**tier_rewards:** `typing.List[UpdateTierRequestTierRewardsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**image_ref:** `typing.Optional[str]` — Image of the tier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tier.<a href="src/brevo/tier/client.py">delete_tier</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a tier from a loyalty program tier group. *(The changes will take effect with the next publication of the loyalty program)*
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tier.delete_tier(
    pid="pid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid:** `str` — Loyalty Program ID
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — Tier ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EmailCampaigns
<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">get_email_campaigns</a>(...) -> GetEmailCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>The response payload for this endpoint has changed
You now need to specify which type of statistics you would like to retrieve. For more information visit [this page](https://developers.brevo.com/changelog/get-all-marketing-campaigns).</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.get_email_campaigns()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[GetEmailCampaignsRequestType]` — Filter on the type of the campaigns
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetEmailCampaignsRequestStatus]` — Filter on the status of the campaign
    
</dd>
</dl>

<dl>
<dd>

**statistics:** `typing.Optional[GetEmailCampaignsRequestStatistics]` — Filter on type of the statistics required. Example **globalStats** value will only fetch globalStats info of the campaign in returned response.This option only returns data for events occurred in the last 6 months.For older campaigns, it’s advisable to use the **Get Campaign Report** endpoint.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent email campaigns. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' )
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent email campaigns. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' )
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetEmailCampaignsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**exclude_html_content:** `typing.Optional[bool]` — Use this flag to exclude htmlContent from the response body. If set to **true**, htmlContent field will be returned as empty string in the response body
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">create_email_campaign</a>(...) -> CreateEmailCampaignResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.email_campaigns import CreateEmailCampaignRequestSender

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.create_email_campaign(
    name="Newsletter - May 2017",
    sender=CreateEmailCampaignRequestSender(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the campaign
    
</dd>
</dl>

<dl>
<dd>

**sender:** `CreateEmailCampaignRequestSender` — Sender details including id or email and name (_optional_). Only one of either Sender's email or Sender's ID shall be passed in one request at a time. For example: **{"name":"xyz", "email":"example@abc.com"}** **{"name":"xyz", "id":123}**
    
</dd>
</dl>

<dl>
<dd>

**ab_testing:** `typing.Optional[bool]` — Status of A/B Test. abTesting = false means it is disabled & abTesting = true means it is enabled. **subjectA, subjectB, splitRule, winnerCriteria & winnerDelay** will be considered when abTesting is set to true. subjectA & subjectB are mandatory together & subject if passed is ignored. **Can be set to true only if sendAtBestTime is false**. You will be able to set up two subject lines for your campaign and send them to a random sample of your total recipients. Half of the test group will receive version A, and the other half will receive version B
    
</dd>
</dl>

<dl>
<dd>

**attachment_url:** `typing.Optional[str]` — Absolute url of the attachment (no local file). Extension allowed: #### xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps
    
</dd>
</dl>

<dl>
<dd>

**email_expiration_date:** `typing.Optional[CreateEmailCampaignRequestEmailExpirationDate]` — To reduce your carbon footprint, set an expiration date for your email. If supported, it will be automatically deleted from the recipient’s inbox, saving storage space and energy. Learn more about setting an email expiration date. For reference , ``https://help.brevo.com/hc/en-us/articles/4413566705298-Create-an-email-campaign``
    
</dd>
</dl>

<dl>
<dd>

**footer:** `typing.Optional[str]` — Footer of the email campaign
    
</dd>
</dl>

<dl>
<dd>

**header:** `typing.Optional[str]` — Header of the email campaign
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — Mandatory if htmlUrl and templateId are empty. Body of the message (HTML).
    
</dd>
</dl>

<dl>
<dd>

**html_url:** `typing.Optional[str]` — **Mandatory if htmlContent and templateId are empty**. Url to the message (HTML). For example: **https://html.domain.com**
    
</dd>
</dl>

<dl>
<dd>

**increase_rate:** `typing.Optional[int]` — **Mandatory if ipWarmupEnable is set to true**. Set a percentage increase rate for warming up your ip. We recommend you set the increase rate to 30% per day. If you want to send the same number of emails every day, set the daily increase value to 0%.
    
</dd>
</dl>

<dl>
<dd>

**initial_quota:** `typing.Optional[int]` — **Mandatory if ipWarmupEnable is set to true**. Set an initial quota greater than 1 for warming up your ip. We recommend you set a value of 3000.
    
</dd>
</dl>

<dl>
<dd>

**inline_image_activation:** `typing.Optional[bool]` — Use true to embedded the images in your email. Final size of the email should be less than **4MB**. Campaigns with embedded images can _not be sent to more than 5000 contacts_
    
</dd>
</dl>

<dl>
<dd>

**ip_warmup_enable:** `typing.Optional[bool]` — **Available for dedicated ip clients**. Set this to true if you wish to warm up your ip.
    
</dd>
</dl>

<dl>
<dd>

**mirror_active:** `typing.Optional[bool]` — Use true to enable the mirror link
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Pass the set of attributes to customize the type classic campaign. For example: **{"FNAME":"Joe", "LNAME":"Doe"}**. Only available if **type** is **classic**. It's considered only if campaign is in _New Template Language format_. The New Template Language is dependent on the values of **subject, htmlContent/htmlUrl, sender.name & toField**
    
</dd>
</dl>

<dl>
<dd>

**preview_text:** `typing.Optional[str]` — Preview text or preheader of the email campaign
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[CreateEmailCampaignRequestRecipients]` — Segment ids and List ids to include/exclude from campaign
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Email on which the campaign recipients will be able to reply to
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[str]` — Sending UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result**. If sendAtBestTime is set to true, your campaign will be sent according to the date passed (ignoring the time part). For example: **2017-06-01T12:30:00+02:00**
    
</dd>
</dl>

<dl>
<dd>

**send_at_best_time:** `typing.Optional[bool]` — Set this to true if you want to send your campaign at best time.
    
</dd>
</dl>

<dl>
<dd>

**split_rule:** `typing.Optional[int]` — Add the size of your test groups. **Mandatory if abTesting = true & 'recipients' is passed**. We'll send version A and B to a random sample of recipients, and then the winning version to everyone else
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject of the campaign. **Mandatory if abTesting is false**. Ignored if abTesting is true.
    
</dd>
</dl>

<dl>
<dd>

**subject_a:** `typing.Optional[str]` — Subject A of the campaign. **Mandatory if abTesting = true**. subjectA & subjectB should have unique value
    
</dd>
</dl>

<dl>
<dd>

**subject_b:** `typing.Optional[str]` — Subject B of the campaign. **Mandatory if abTesting = true**. subjectA & subjectB should have unique value
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag of the campaign
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[int]` — **Mandatory if htmlContent and htmlUrl are empty**. Id of the transactional email template with status _active_. Used to copy only its content fetched from htmlContent/htmlUrl to an email campaign for RSS feature.
    
</dd>
</dl>

<dl>
<dd>

**to_field:** `typing.Optional[str]` — To personalize the **To** Field. If you want to include the first name and last name of your recipient, add **{FNAME} {LNAME}**. These contact attributes must already exist in your Brevo account. If input parameter **params** used please use **{{contact.FNAME}} {{contact.LNAME}}** for personalization
    
</dd>
</dl>

<dl>
<dd>

**unsubscription_page_id:** `typing.Optional[str]` — Enter an unsubscription page id. The page id is a 24 digit alphanumeric id that can be found in the URL when editing the page. If not entered, then the default unsubscription page will be used.
    
</dd>
</dl>

<dl>
<dd>

**update_form_id:** `typing.Optional[str]` — **Mandatory if templateId is used containing the {{ update_profile }} tag**. Enter an update profile form id. The form id is a 24 digit alphanumeric id that can be found in the URL when editing the form. If not entered, then the default update profile form will be used.
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` — Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed
    
</dd>
</dl>

<dl>
<dd>

**winner_criteria:** `typing.Optional[CreateEmailCampaignRequestWinnerCriteria]` — Choose the metrics that will determinate the winning version. **Mandatory if _splitRule_ >= 1 and < 50**. If splitRule = 50, `winnerCriteria` is ignored if passed
    
</dd>
</dl>

<dl>
<dd>

**winner_delay:** `typing.Optional[int]` — Choose the duration of the test in hours. Maximum is 7 days, pass 24*7 = 168 hours. The winning version will be sent at the end of the test. **Mandatory if _splitRule_ >= 1 and < 50**. If splitRule = 50, `winnerDelay` is ignored if passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">upload_image_to_gallery</a>(...) -> UploadImageToGalleryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.upload_image_to_gallery(
    image_url="https://somedomain.com/image1.jpg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_url:** `str` — The absolute url of the image (**no local file**). Maximum allowed size for image is **2MB**. Allowed extensions for images are: #### jpeg, jpg, png, bmp, gif.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the image.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">get_email_campaign</a>(...) -> GetEmailCampaignResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.get_email_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**statistics:** `typing.Optional[GetEmailCampaignRequestStatistics]` — Filter on type of the statistics required. Example **globalStats** value will only fetch globalStats info of the campaign in returned response.
    
</dd>
</dl>

<dl>
<dd>

**exclude_html_content:** `typing.Optional[bool]` — Use this flag to exclude htmlContent from the response body. If set to **true**, htmlContent field will be returned as empty string in the response body
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">update_email_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.update_email_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**ab_testing:** `typing.Optional[bool]` — Status of A/B Test. abTesting = false means it is disabled & abTesting = true means it is enabled. **subjectA, subjectB, splitRule, winnerCriteria & winnerDelay** will be considered when abTesting is set to true. subjectA & subjectB are mandatory together & subject if passed is ignored. **Can be set to true only if sendAtBestTime is false**. You will be able to set up two subject lines for your campaign and send them to a random sample of your total recipients. Half of the test group will receive version A, and the other half will receive version B
    
</dd>
</dl>

<dl>
<dd>

**attachment_url:** `typing.Optional[str]` — Absolute url of the attachment (no local file). Extension allowed: #### xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps'
    
</dd>
</dl>

<dl>
<dd>

**email_expiration_date:** `typing.Optional[UpdateEmailCampaignRequestEmailExpirationDate]` — To reduce your carbon footprint, set an expiration date for your email. If supported, it will be automatically deleted from the recipient’s inbox, saving storage space and energy.
    
</dd>
</dl>

<dl>
<dd>

**footer:** `typing.Optional[str]` — Footer of the email campaign
    
</dd>
</dl>

<dl>
<dd>

**header:** `typing.Optional[str]` — Header of the email campaign
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — Body of the message (HTML version). If the campaign is designed using Drag & Drop editor via HTML content, then the design page will not have Drag & Drop editor access for that campaign. **REQUIRED if htmlUrl is empty**
    
</dd>
</dl>

<dl>
<dd>

**html_url:** `typing.Optional[str]` — Url which contents the body of the email message. **REQUIRED if htmlContent is empty**
    
</dd>
</dl>

<dl>
<dd>

**increase_rate:** `typing.Optional[int]` — Set a percentage increase rate for warming up your ip. We recommend you set the increase rate to 30% per day. If you want to send the same number of emails every day, set the daily increase value to 0%.
    
</dd>
</dl>

<dl>
<dd>

**initial_quota:** `typing.Optional[int]` — Set an initial quota greater than 1 for warming up your ip. We recommend you set a value of 3000.
    
</dd>
</dl>

<dl>
<dd>

**inline_image_activation:** `typing.Optional[bool]` — Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email. You cannot send a campaign of more than **4MB** with images embedded in the email. Campaigns with the images embedded in the email _must be sent to less than 5000 contacts_.
    
</dd>
</dl>

<dl>
<dd>

**ip_warmup_enable:** `typing.Optional[bool]` — **Available for dedicated ip clients**. Set this to true if you wish to warm up your ip.
    
</dd>
</dl>

<dl>
<dd>

**mirror_active:** `typing.Optional[bool]` — Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the campaign
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Pass the set of attributes to customize the type classic campaign. For example: **{"FNAME":"Joe", "LNAME":"Doe"}**. Only available if **type** is **classic**. It's considered only if campaign is in _New Template Language format_. The New Template Language is dependent on the values of **subject, htmlContent/htmlUrl, sender.name & toField**
    
</dd>
</dl>

<dl>
<dd>

**preview_text:** `typing.Optional[str]` — Preview text or preheader of the email campaign
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[UpdateEmailCampaignRequestRecipients]` — Segment ids and List ids to include/exclude from campaign
    
</dd>
</dl>

<dl>
<dd>

**recurring:** `typing.Optional[bool]` — **FOR TRIGGER ONLY !** Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Email on which campaign recipients will be able to reply to
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[str]` — UTC date-time on which the campaign has to run (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.** If sendAtBestTime is set to true, your campaign will be sent according to the date passed (ignoring the time part).
    
</dd>
</dl>

<dl>
<dd>

**send_at_best_time:** `typing.Optional[bool]` — Set this to true if you want to send your campaign at best time. Note:- **if true, warmup ip will be disabled.**
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[UpdateEmailCampaignRequestSender]` — Sender details including id or email and name (optional). Only one of either Sender's email or Sender's ID shall be passed in one request at a time. For example: **{"name":"xyz", "email":"example@abc.com"}** **{"name":"xyz", "id":123}**
    
</dd>
</dl>

<dl>
<dd>

**split_rule:** `typing.Optional[int]` — Add the size of your test groups. **Mandatory if abTesting = true & 'recipients' is passed**. We'll send version A and B to a random sample of recipients, and then the winning version to everyone else
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject of the campaign
    
</dd>
</dl>

<dl>
<dd>

**subject_a:** `typing.Optional[str]` — Subject A of the campaign. **Mandatory if abTesting = true**. subjectA & subjectB should have unique value
    
</dd>
</dl>

<dl>
<dd>

**subject_b:** `typing.Optional[str]` — Subject B of the campaign. **Mandatory if abTesting = true**. subjectA & subjectB should have unique value
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag of the campaign
    
</dd>
</dl>

<dl>
<dd>

**to_field:** `typing.Optional[str]` — To personalize the **To** Field. If you want to include the first name and last name of your recipient, add **{FNAME} {LNAME}**. These contact attributes must already exist in your Brevo account. If input parameter **params** used please use **{{contact.FNAME}} {{contact.LNAME}}** for personalization
    
</dd>
</dl>

<dl>
<dd>

**unsubscription_page_id:** `typing.Optional[str]` — Enter an unsubscription page id. The page id is a 24 digit alphanumeric id that can be found in the URL when editing the page.
    
</dd>
</dl>

<dl>
<dd>

**update_form_id:** `typing.Optional[str]` — **Mandatory if templateId is used containing the {{ update_profile }} tag**. Enter an update profile form id. The form id is a 24 digit alphanumeric id that can be found in the URL when editing the form.
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` — Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed
    
</dd>
</dl>

<dl>
<dd>

**winner_criteria:** `typing.Optional[UpdateEmailCampaignRequestWinnerCriteria]` — Choose the metrics that will determinate the winning version. **Mandatory if _splitRule_ >= 1 and < 50**. If splitRule = 50, `winnerCriteria` is ignored if passed
    
</dd>
</dl>

<dl>
<dd>

**winner_delay:** `typing.Optional[int]` — Choose the duration of the test in hours. Maximum is 7 days, pass 24*7 = 168 hours. The winning version will be sent at the end of the test. **Mandatory if _splitRule_ >= 1 and < 50**. If splitRule = 50, `winnerDelay` is ignored if passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">delete_email_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.delete_email_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">get_ab_test_campaign_result</a>(...) -> GetAbTestCampaignResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain winning version of an A/B test email campaign
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.get_ab_test_campaign_result(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the A/B test campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">email_export_recipients</a>(...) -> EmailExportRecipientsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.email_export_recipients(
    campaign_id=1000000,
    recipients_type="all",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**recipients_type:** `EmailExportRecipientsRequestRecipientsType` — Type of recipients to export for a campaign
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — Webhook called once the export process is finished. For reference, https://help.brevo.com/hc/en-us/articles/360007666479
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">send_email_campaign_now</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.send_email_campaign_now(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">send_report</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A PDF will be sent to the specified email addresses
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, SendReportEmail
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.send_report(
    campaign_id=1000000,
    email=SendReportEmail(
        body="Please find attached the report of our last email campaign.",
        to=[
            "jim.suehan@example.com"
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request:** `SendReport` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">send_test_email</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.send_test_email(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request:** `SendTestEmail` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">get_shared_template_url</a>(...) -> GetSharedTemplateUrlResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a unique URL to share & import an email template from one Brevo account to another.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.get_shared_template_url(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign or template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_campaigns.<a href="src/brevo/email_campaigns/client.py">update_campaign_status</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.email_campaigns.update_campaign_status(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateCampaignStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SmsCampaigns
<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">get_sms_campaigns</a>(...) -> GetSmsCampaignsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.get_sms_campaigns()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status:** `typing.Optional[GetSmsCampaignsRequestStatus]` — Status of campaign.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent sms campaigns. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' )
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent sms campaigns. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' )
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number limitation for the result returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Beginning point in the list to retrieve from.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetSmsCampaignsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">create_sms_campaign</a>(...) -> CreateSmsCampaignResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.create_sms_campaign(
    content="Get a discount by visiting our NY store and saying : Happy Spring!",
    name="Spring Promo Code",
    sender="MyShop",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content:** `str` — Content of the message. The **maximum characters used per SMS is 160**, if used more than that, it will be counted as more than one SMS.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the campaign
    
</dd>
</dl>

<dl>
<dd>

**sender:** `str` — Name of the sender. **The number of characters is limited to 11 for alphanumeric characters and 15 for numeric characters**
    
</dd>
</dl>

<dl>
<dd>

**organisation_prefix:** `typing.Optional[str]` — A recognizable prefix will ensure your audience knows who you are. Recommended by U.S. carriers. This will be added as your Brand Name before the message content. **Prefer verifying maximum length of 160 characters including this prefix in message content to avoid multiple sending of same sms.**
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[CreateSmsCampaignRequestRecipients]` 
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[str]` — UTC date-time on which the campaign has to run (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**unicode_enabled:** `typing.Optional[bool]` — Format of the message. It indicates whether the content should be treated as unicode or not.
    
</dd>
</dl>

<dl>
<dd>

**unsubscribe_instruction:** `typing.Optional[str]` — Instructions to unsubscribe from future communications. Recommended by U.S. carriers. Must include **STOP** keyword. This will be added as instructions after the end of message content. **Prefer verifying maximum length of 160 characters including this instructions in message content to avoid multiple sending of same sms.**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">get_sms_campaign</a>(...) -> GetSmsCampaignResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.get_sms_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the SMS campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">update_sms_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.update_sms_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the SMS campaign
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — Content of the message. The **maximum characters used per SMS is 160**, if used more than that, it will be counted as more than one SMS
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the campaign
    
</dd>
</dl>

<dl>
<dd>

**organisation_prefix:** `typing.Optional[str]` — A recognizable prefix will ensure your audience knows who you are. Recommended by U.S. carriers. This will be added as your Brand Name before the message content. **Prefer verifying maximum length of 160 characters including this prefix in message content to avoid multiple sending of same sms.**
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[UpdateSmsCampaignRequestRecipients]` 
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[str]` — UTC date-time on which the campaign has to run (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — Name of the sender. **The number of characters is limited to 11 for alphanumeric characters and 15 for numeric characters**
    
</dd>
</dl>

<dl>
<dd>

**unicode_enabled:** `typing.Optional[bool]` — Format of the message. It indicates whether the content should be treated as unicode or not.
    
</dd>
</dl>

<dl>
<dd>

**unsubscribe_instruction:** `typing.Optional[str]` — Instructions to unsubscribe from future communications. Recommended by U.S. carriers. Must include **STOP** keyword. This will be added as instructions after the end of message content. **Prefer verifying maximum length of 160 characters including this instructions in message content to avoid multiple sending of same sms.**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">delete_sms_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.delete_sms_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the SMS campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">request_sms_recipient_export</a>(...) -> RequestSmsRecipientExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

It returns the background process ID which on completion calls the notify URL that you have set in the input.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.request_sms_recipient_export(
    campaign_id=1000000,
    recipients_type="all",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**recipients_type:** `RequestSmsRecipientExportRequestRecipientsType` — Filter the recipients based on how they interacted with the campaign
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — URL that will be called once the export process is finished. For reference, https://help.brevo.com/hc/en-us/articles/360007666479
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">send_sms_campaign_now</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.send_sms_campaign_now(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">send_sms_report</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send report of Sent and Archived campaign, to the specified email addresses, with respective data and a pdf attachment in detail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo, SendReportEmail
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.send_sms_report(
    campaign_id=1000000,
    email=SendReportEmail(
        body="Please find attached the report of our last email campaign.",
        to=[
            "jim.suehan@example.com"
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request:** `SendReport` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">send_test_sms</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.send_test_sms(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the SMS campaign
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Mobile number of the recipient with the country code. This number **must belong to one of your contacts in Brevo account and must not be blacklisted**
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/brevo/sms_campaigns/client.py">update_sms_campaign_status</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_campaigns.update_sms_campaign_status(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateCampaignStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WhatsAppCampaigns
<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">get_whats_app_campaigns</a>(...) -> GetWhatsAppCampaignsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.get_whats_app_campaigns()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the WhatsApp campaigns created. **Prefer to pass your timezone in date-time format for accurate result**
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the WhatsApp campaigns created. **Prefer to pass your timezone in date-time format for accurate result**
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetWhatsAppCampaignsRequestSort]` — Sort the results in the ascending/descending order of record modification. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">create_whats_app_campaign</a>(...) -> CreateWhatsAppCampaignResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating Whatsapp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
<Note>This API requires the List and Segment ids as recipients in Body params.You can use the below Contact endpoints to get the required information.
[Get all the Lists](https://developers.brevo.com/reference/getlists-1)
[Get all the Segments](https://developers.brevo.com/reference/getsegments)</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.whats_app_campaigns import CreateWhatsAppCampaignRequestRecipients

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.create_whats_app_campaign(
    name="Test Campaign",
    recipients=CreateWhatsAppCampaignRequestRecipients(),
    scheduled_at="2017-06-01T12:30:00+02:00",
    template_id=19,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the WhatsApp campaign creation
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `CreateWhatsAppCampaignRequestRecipients` — Segment ids and List ids to include/exclude from campaign
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `str` — Sending UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.For example: **2017-06-01T12:30:00+02:00**
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `int` — Id of the WhatsApp template in **approved** state
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">get_whats_app_config</a>() -> GetWhatsAppConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating WhatsApp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.get_whats_app_config()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">create_whats_app_template</a>(...) -> CreateWhatsAppTemplateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating WhatsApp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.create_whats_app_template(
    body_text="making it look like readable English",
    category="MARKETING",
    language="en",
    name="Test template",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body_text:** `str` — Body of the template. **Maximum allowed characters are 1024**
    
</dd>
</dl>

<dl>
<dd>

**category:** `CreateWhatsAppTemplateRequestCategory` — Category of the template
    
</dd>
</dl>

<dl>
<dd>

**language:** `str` 

Language of the template. For Example :
**en** for English
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the template
    
</dd>
</dl>

<dl>
<dd>

**header_text:** `typing.Optional[str]` — Text content of the header in the template.  **Maximum allowed characters are 45** **Use this field to add text content in template header and if mediaUrl is empty**
    
</dd>
</dl>

<dl>
<dd>

**media_url:** `typing.Optional[str]` — Absolute url of the media file **(no local file)** for the header. **Use this field in you want to add media in Template header and headerText is empty** Allowed extensions for media files are: #### jpeg | png | mp4 | pdf
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[CreateWhatsAppTemplateRequestSource]` — source of the template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">get_whats_app_templates</a>(...) -> GetWhatsAppTemplatesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.get_whats_app_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result**
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result**
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetWhatsAppTemplatesRequestSort]` — Sort the results in the ascending/descending order of record modification. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[GetWhatsAppTemplatesRequestSource]` — source of the template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">send_whats_app_template_approval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating WhatsApp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.send_whats_app_template_approval(
    template_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `int` — id of the template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">get_whats_app_campaign</a>(...) -> GetWhatsAppCampaignResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating Whatsapp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
<Note>This API requires the List and Segment ids as recipients in Body params.You can use the below Contact endpoints to get the required information.
[Get all the Lists](https://developers.brevo.com/reference/getlists-1)
[Get all the Segments](https://developers.brevo.com/reference/getsegments)</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.get_whats_app_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — Id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">update_whats_app_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating Whatsapp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
<Note>This API requires the List and Segment ids as recipients in Body params.You can use the below Contact endpoints to get the required information.
[Get all the Lists](https://developers.brevo.com/reference/getlists-1)
[Get all the Segments](https://developers.brevo.com/reference/getsegments)</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.update_whats_app_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**campaign_name:** `typing.Optional[str]` — Name of the campaign
    
</dd>
</dl>

<dl>
<dd>

**campaign_status:** `typing.Optional[UpdateWhatsAppCampaignRequestCampaignStatus]` — Status of the campaign
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[UpdateWhatsAppCampaignRequestRecipients]` — Segment ids and List ids to include/exclude from campaign
    
</dd>
</dl>

<dl>
<dd>

**reschedule_for:** `typing.Optional[str]` — Reschedule the sending UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) of campaign. **Prefer to pass your timezone in date-time format for accurate result.For example: **2017-06-01T12:30:00+02:00** Use this field to update the scheduledAt of any existing draft or scheduled WhatsApp campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whats_app_campaigns.<a href="src/brevo/whats_app_campaigns/client.py">delete_whats_app_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.whats_app_campaigns.delete_whats_app_campaign(
    campaign_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `int` — id of the campaign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Companies
<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">get_all_companies</a>(...) -> GetCompaniesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.get_all_companies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filters:** `typing.Optional[str]` — Filter by attrbutes. If you have filter for owner on your side please send it as {"attributes.owner":"6299dcf3874a14eacbc65c46"}
    
</dd>
</dl>

<dl>
<dd>

**linked_contacts_ids:** `typing.Optional[int]` — Filter by linked contacts ids
    
</dd>
</dl>

<dl>
<dd>

**linked_deals_ids:** `typing.Optional[str]` — Filter by linked Deals ids
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCompaniesRequestSort]` — Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field used to sort field names.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">create_a_company</a>(...) -> PostCompaniesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.create_a_company(
    name="company",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of company
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` — Attributes for company creation
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[int]` — Country code if phone_number is passed in attributes.
    
</dd>
</dl>

<dl>
<dd>

**linked_contacts_ids:** `typing.Optional[typing.List[int]]` — Contact ids to be linked with company
    
</dd>
</dl>

<dl>
<dd>

**linked_deals_ids:** `typing.Optional[typing.List[str]]` — Deal ids to be linked with company
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">import_companies_creation_and_updation</a>(...) -> PostCompaniesImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import companies from a CSV file with mapping options.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.import_companies_creation_and_updation(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The CSV file to upload.The file should have the first row as the mapping attribute. Some default attribute names are (a) company_id [brevo mongoID to update deals] (b) associated_contact (c) associated_deal (f) any other attribute with internal name
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[typing.Dict[str, typing.Any]]` 

The mapping options in JSON format. Here is an example of the JSON structure: ```json {
  "link_entities": true, // Determines whether to link related entities during the import process
  "unlink_entities": false, // Determines whether to unlink related entities during the import process
  "update_existing_records": true, // Determines whether to update based on company ID or treat every row as create
  "unset_empty_attributes": false // Determines whether to unset a specific attribute during update if the values input is blank
} ```
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">link_and_unlink_company_with_contact_and_deal</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.link_and_unlink_company_with_contact_and_deal(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**link_contact_ids:** `typing.Optional[typing.List[int]]` — Contact ids for contacts to be linked with company
    
</dd>
</dl>

<dl>
<dd>

**link_deals_ids:** `typing.Optional[typing.List[str]]` — Deal ids for deals to be linked with company
    
</dd>
</dl>

<dl>
<dd>

**unlink_contact_ids:** `typing.Optional[typing.List[int]]` — Contact ids for contacts to be unlinked from company
    
</dd>
</dl>

<dl>
<dd>

**unlink_deals_ids:** `typing.Optional[typing.List[str]]` — Deal ids for deals to be unlinked from company
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">get_a_company</a>(...) -> Company</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.get_a_company(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Get Company Details
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">delete_a_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.delete_a_company(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Company ID to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">update_a_company</a>(...) -> Company</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.update_a_company(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` — Attributes for company update
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[int]` — Country code if phone_number is passed in attributes.
    
</dd>
</dl>

<dl>
<dd>

**linked_contacts_ids:** `typing.Optional[typing.List[int]]` — Warning - Using PATCH on linkedContactIds replaces the list of linked contacts. Omitted IDs will be removed.
    
</dd>
</dl>

<dl>
<dd>

**linked_deals_ids:** `typing.Optional[typing.List[str]]` — Warning - Using PATCH on linkedDealsIds replaces the list of linked contacts. Omitted IDs will be removed.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of company
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">create_a_company_deal_attribute</a>(...) -> PostCrmAttributesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.create_a_company_deal_attribute(
    attribute_type="text",
    label="Attribute Label",
    object_type="companies",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_type:** `PostCrmAttributesRequestAttributeType` — The type of attribute (must be one of the defined enums)
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The label for the attribute (max 50 characters, cannot be empty)
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `PostCrmAttributesRequestObjectType` — The type of object the attribute belongs to (prefilled with `companies`, mandatory)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the attribute
    
</dd>
</dl>

<dl>
<dd>

**options_labels:** `typing.Optional[typing.List[str]]` — Options for multi-choice or single-select attributes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">delete_an_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.delete_an_attribute(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Attribute ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">update_an_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.update_an_attribute(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Attribute ID
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Attribute display label
    
</dd>
</dl>

<dl>
<dd>

**options_labels:** `typing.Optional[typing.List[PatchCrmAttributesIdRequestOptionsLabelsItem]]` — Updated labels for selectable options
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[PatchCrmAttributesIdRequestObjectType]` — The type of object the attribute belongs to, it cannot be updated after creation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/brevo/companies/client.py">get_company_attributes</a>() -> typing.List[GetCrmAttributesCompaniesResponseItem]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.companies.get_company_attributes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Deals
<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">get_deal_attributes</a>() -> typing.List[GetCrmAttributesDealsResponseItem]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.get_deal_attributes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">get_all_deals</a>(...) -> GetCrmDealsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.get_all_deals()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filters_attributes_deal_name:** `typing.Optional[str]` — Filter by attributes. If you have a filter for the owner on your end, please send it as filters[attributes.deal_owner] and utilize the account email for the filtering.
    
</dd>
</dl>

<dl>
<dd>

**filters_linked_companies_ids:** `typing.Optional[str]` — Filter by linked companies ids
    
</dd>
</dl>

<dl>
<dd>

**filters_linked_contacts_ids:** `typing.Optional[str]` — Filter by linked companies ids
    
</dd>
</dl>

<dl>
<dd>

**modified_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[str]` — Filter (urlencoded) the contacts created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCrmDealsRequestSort]` — Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">create_a_deal</a>(...) -> PostCrmDealsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.create_a_deal(
    name="Deal: Connect with company",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of deal
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` — Attributes for deal creation To assign owner of a Deal you can send attributes.deal_owner and utilize the account email or ID. If you want to create a deal on a specific pipeline and stage you can use the following attributes `pipeline` and `deal_stage`. Pipeline and deal_stage are ids you can fetch using this endpoint `/crm/pipeline/details/{pipelineID}`
    
</dd>
</dl>

<dl>
<dd>

**linked_companies_ids:** `typing.Optional[typing.List[str]]` — Company ids to be linked with deal
    
</dd>
</dl>

<dl>
<dd>

**linked_contacts_ids:** `typing.Optional[typing.List[int]]` — Contact ids to be linked with deal
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">import_deals_creation_and_updation</a>(...) -> PostCrmDealsImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import deals from a CSV file with mapping options.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.import_deals_creation_and_updation(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The CSV file to upload.The file should have the first row as the mapping attribute. Some default attribute names are (a) deal_id [brevo mongoID to update deals] (b) associated_contact (c) associated_company (f) any other attribute with internal name
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[typing.Dict[str, typing.Any]]` 

The mapping options in JSON format. Here is an example of the JSON structure: ```json {
  "link_entities": true, // Determines whether to link related entities during the import process
  "unlink_entities": false, // Determines whether to unlink related entities during the import process
  "update_existing_records": true, // Determines whether to update based on company ID or treat every row as create
  "unset_empty_attributes": false // Determines whether to unset a specific attribute during update if the values input is blank
} ```
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">link_and_unlink_a_deal_with_contacts_and_companies</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.link_and_unlink_a_deal_with_contacts_and_companies(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**link_company_ids:** `typing.Optional[typing.List[str]]` — Company ids to be linked with deal
    
</dd>
</dl>

<dl>
<dd>

**link_contact_ids:** `typing.Optional[typing.List[int]]` — Contact ids for contacts to be linked with deal
    
</dd>
</dl>

<dl>
<dd>

**unlink_company_ids:** `typing.Optional[typing.List[str]]` — Company ids to be unlinked from deal
    
</dd>
</dl>

<dl>
<dd>

**unlink_contact_ids:** `typing.Optional[typing.List[int]]` — Contact ids for contacts to be unlinked from deal
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">get_a_deal</a>(...) -> Deal</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.get_a_deal(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">delete_a_deal</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.delete_a_deal(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">update_a_deal</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.update_a_deal(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` — Attributes for deal update To assign owner of a Deal you can send attributes.deal_owner and utilize the account email or ID. If you wish to update the pipeline of a deal you need to provide the `pipeline` and the `deal_stage` Pipeline and deal_stage are ids you can fetch using this endpoint `/crm/pipeline/details/{pipelineID}`
    
</dd>
</dl>

<dl>
<dd>

**linked_companies_ids:** `typing.Optional[typing.List[str]]` — Warning - Using PATCH on linkedCompaniesIds replaces the list of linked contacts. Omitted IDs will be removed.
    
</dd>
</dl>

<dl>
<dd>

**linked_contacts_ids:** `typing.Optional[typing.List[int]]` — Warning - Using PATCH on linkedContactIds replaces the list of linked contacts. Omitted IDs will be removed.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of deal
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">get_pipeline_stages</a>() -> Pipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is deprecated. Prefer /crm/pipeline/details/{pipelineID} instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.get_pipeline_stages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">get_all_pipelines</a>() -> Pipelines</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.get_all_pipelines()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/brevo/deals/client.py">get_a_pipeline</a>(...) -> Pipelines</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.deals.get_a_pipeline(
    pipeline_id="pipelineID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pipeline_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/brevo/files/client.py">get_all_files</a>(...) -> typing.List[FileData]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.files.get_all_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity:** `typing.Optional[GetCrmFilesRequestEntity]` — Filter by file entity type
    
</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[str]` — Filter by file entity IDs
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[int]` — dateFrom to date range filter type (timestamp in milliseconds)
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[int]` — dateTo to date range filter type (timestamp in milliseconds)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCrmFilesRequestSort]` — Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/brevo/files/client.py">upload_a_file</a>(...) -> FileData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.files.upload_a_file(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` — File data to create a file.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**deal_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/brevo/files/client.py">download_a_file</a>(...) -> GetCrmFilesIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.files.download_a_file(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — File id to download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/brevo/files/client.py">delete_a_file</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.files.delete_a_file(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — File id to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/brevo/files/client.py">get_file_details</a>(...) -> FileData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.files.get_file_details(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — File id to get file data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notes
<details><summary><code>client.notes.<a href="src/brevo/notes/client.py">get_all_notes</a>(...) -> typing.List[Note]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.notes.get_all_notes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity:** `typing.Optional[GetCrmNotesRequestEntity]` — Filter by note entity type
    
</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[str]` — Filter by note entity IDs
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[int]` — dateFrom to date range filter type (timestamp in milliseconds)
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[int]` — dateTo to date range filter type (timestamp in milliseconds)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCrmNotesRequestSort]` — Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notes.<a href="src/brevo/notes/client.py">create_a_note</a>(...) -> PostCrmNotesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.notes.create_a_note(
    text="In communication with client_dev for resolution of queries.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `NoteData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notes.<a href="src/brevo/notes/client.py">get_a_note</a>(...) -> Note</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.notes.get_a_note(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Note ID to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notes.<a href="src/brevo/notes/client.py">delete_a_note</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.notes.delete_a_note(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Note ID to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notes.<a href="src/brevo/notes/client.py">update_a_note</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.notes.update_a_note(
    id="id",
    text="In communication with client_dev for resolution of queries.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Note ID to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `NoteData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks
<details><summary><code>client.tasks.<a href="src/brevo/tasks/client.py">get_all_tasks</a>(...) -> GetCrmTasksResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tasks.get_all_tasks(
    sort_by="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_type:** `typing.Optional[str]` — Filter by task type (ID)
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[GetCrmTasksRequestFilterStatus]` — Filter by task status
    
</dd>
</dl>

<dl>
<dd>

**filter_date:** `typing.Optional[GetCrmTasksRequestFilterDate]` — Filter by date
    
</dd>
</dl>

<dl>
<dd>

**filter_assign_to:** `typing.Optional[str]` — Filter by the "assignTo" ID. You can utilize account emails for the "assignTo" attribute.
    
</dd>
</dl>

<dl>
<dd>

**filter_contacts:** `typing.Optional[str]` — Filter by contact ids
    
</dd>
</dl>

<dl>
<dd>

**filter_deals:** `typing.Optional[str]` — Filter by deals ids
    
</dd>
</dl>

<dl>
<dd>

**filter_companies:** `typing.Optional[str]` — Filter by companies ids
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[int]` — dateFrom to date range filter type (timestamp in milliseconds)
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[int]` — dateTo to date range filter type (timestamp in milliseconds)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCrmTasksRequestSort]` — Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field used to sort field names.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/brevo/tasks/client.py">create_a_task</a>(...) -> PostCrmTasksResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
import datetime

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tasks.create_a_task(
    date=datetime.datetime.fromisoformat("2021-11-01T17:44:54+00:00"),
    name="Task: Connect with client_dev",
    task_type_id="61a5cd07ca1347c82306ad09",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date:** `datetime.datetime` — Task due date and time
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of task
    
</dd>
</dl>

<dl>
<dd>

**task_type_id:** `str` — Id for type of task e.g Call / Email / Meeting etc.
    
</dd>
</dl>

<dl>
<dd>

**assign_to_id:** `typing.Optional[str]` — To assign a task to a user you can use either the account email or ID.
    
</dd>
</dl>

<dl>
<dd>

**companies_ids:** `typing.Optional[typing.List[str]]` — Companies ids for companies a task is linked to
    
</dd>
</dl>

<dl>
<dd>

**contacts_ids:** `typing.Optional[typing.List[int]]` — Contact ids for contacts linked to this task
    
</dd>
</dl>

<dl>
<dd>

**deals_ids:** `typing.Optional[typing.List[str]]` — Deal ids for deals a task is linked to
    
</dd>
</dl>

<dl>
<dd>

**done:** `typing.Optional[bool]` — Task marked as done
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` — Duration of task in milliseconds [1 minute = 60000 ms]
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes added to a task
    
</dd>
</dl>

<dl>
<dd>

**reminder:** `typing.Optional[TaskReminder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/brevo/tasks/client.py">get_a_task</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tasks.get_a_task(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/brevo/tasks/client.py">delete_a_task</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tasks.delete_a_task(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/brevo/tasks/client.py">update_a_task</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tasks.update_a_task(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**assign_to_id:** `typing.Optional[str]` — To assign a task to a user you can use either the account email or ID.
    
</dd>
</dl>

<dl>
<dd>

**companies_ids:** `typing.Optional[typing.List[str]]` — Companies ids for companies a task is linked to
    
</dd>
</dl>

<dl>
<dd>

**contacts_ids:** `typing.Optional[typing.List[int]]` — Contact ids for contacts linked to this task
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[datetime.datetime]` — Task date/time
    
</dd>
</dl>

<dl>
<dd>

**deals_ids:** `typing.Optional[typing.List[str]]` — Deal ids for deals a task is linked to
    
</dd>
</dl>

<dl>
<dd>

**done:** `typing.Optional[bool]` — Task marked as done
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` — Duration of task in milliseconds [1 minute = 60000 ms]
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of task
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes added to a task
    
</dd>
</dl>

<dl>
<dd>

**reminder:** `typing.Optional[TaskReminder]` 
    
</dd>
</dl>

<dl>
<dd>

**task_type_id:** `typing.Optional[str]` — Id for type of task e.g Call / Email / Meeting etc.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/brevo/tasks/client.py">get_all_task_types</a>() -> GetCrmTasktypesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.tasks.get_all_task_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TransactionalWhatsApp
<details><summary><code>client.transactional_whats_app.<a href="src/brevo/transactional_whats_app/client.py">send_whatsapp_message</a>(...) -> SendWhatsappMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>You can use this API for WhatsApp only if you have setup your WhatsApp account on Brevo platform. To setup your WhatsApp account, follow the steps in the guide below.
[Activating Whatsapp](https://developers.brevo.com/docs/whatsapp-campaigns-1) in your account</Note>
This endpoint is used to send a WhatsApp message. <br/>(**The first message you send using the API must contain a Template ID. You must create a template on WhatsApp on the Brevo platform to fetch the Template ID.**)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.transactional_whats_app import SendWhatsappMessageRequestParams

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_whats_app.send_whatsapp_message(
    request=SendWhatsappMessageRequestParams(
        contact_numbers=[
            "contactNumbers"
        ],
        sender_number="senderNumber",
        template_id=123,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SendWhatsappMessageRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_whats_app.<a href="src/brevo/transactional_whats_app/client.py">get_whatsapp_event_report</a>(...) -> GetWhatsappEventReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will show the unaggregated statistics for WhatsApp activity (30 days by default if `startDate` and `endDate` or `days` is not passed. The date range can not exceed 90 days)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_whats_app.get_whatsapp_event_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number limitation for the result returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Beginning point in the list to retrieve from
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). _Not compatible with 'startDate' and 'endDate'_
    
</dd>
</dl>

<dl>
<dd>

**contact_number:** `typing.Optional[str]` — Filter results for specific contact (WhatsApp Number with country code. Example, 85264318721)
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[GetWhatsappEventReportRequestEvent]` — Filter the report for a specific event type
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetWhatsappEventReportRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TransactionalEmails
<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_transac_blocked_contacts</a>(...) -> GetTransacBlockedContactsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_transac_blocked_contacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) from which you want to fetch the blocked or unsubscribed contacts
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) till which you want to fetch the blocked or unsubscribed contacts
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document on the page
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of emails of the senders from which contacts are blocked or unsubscribed
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetTransacBlockedContactsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">unblock_or_resubscribe_a_transactional_contact</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.unblock_or_resubscribe_a_transactional_contact(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — contact email (urlencoded) to unblock.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_blocked_domains</a>() -> GetBlockedDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of blocked domains
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_blocked_domains()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">block_new_domain</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Blocks a new domain in order to avoid messages being sent to the same
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.block_new_domain(
    domain="example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — name of the domain to be blocked
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">delete_blocked_domain</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unblocks an existing domain from the list of blocked domains
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.delete_blocked_domain(
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — The name of the domain to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">delete_hardbounces</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete hardbounces. To use carefully (e.g. in case of temporary ISP failures)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.delete_hardbounces()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_email:** `typing.Optional[str]` — Target a specific email address
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Ending date (YYYY-MM-DD) of the time period for deletion. The hardbounces until this date will be deleted. Must be greater than or equal to the startDate
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Starting date (YYYY-MM-DD) of the time period for deletion. The hardbounces occurred after this date will be deleted. Must be less than or equal to the endDate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">send_transac_email</a>(...) -> SendTransacEmailResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.transactional_emails import SendTransacEmailRequestSender, SendTransacEmailRequestToItem

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.send_transac_email(
    html_content="<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Brevo.</p></body></html>",
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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attachment:** `typing.Optional[typing.List[SendTransacEmailRequestAttachmentItem]]` — Array of attachment objects. Each attachment must include either an absolute URL (no local file paths) or base64-encoded content, along with the attachment filename. The `name` field is required when `content` is provided. Supported file extensions: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub, eps, odt, mp3, m4a, m4v, wma, ogg, flac, wav, aif, aifc, aiff, mp4, mov, avi, mkv, mpeg, mpg, wmv, pkpass, xlsm. When `templateId` is specified: if the template uses the New Template Language format, both `url` and `content` attachment types are supported; if the template uses the Old Template Language format, the `attachment` parameter is ignored.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` — UUIDv4 identifier for the scheduled batch of transactional emails. If omitted, a valid UUIDv4 batch identifier is automatically generated.
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `typing.Optional[typing.List[SendTransacEmailRequestBccItem]]` — Array of BCC recipient objects. Each object contains an email address and an optional name.
    
</dd>
</dl>

<dl>
<dd>

**cc:** `typing.Optional[typing.List[SendTransacEmailRequestCcItem]]` — Array of CC recipient objects. Each object contains an email address and an optional name.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Any]]` — Custom email headers (non-standard headers) to include in the email. The `sender.ip` header can be set to specify the IP address used for sending transactional emails (dedicated IP users only). Header names must use Title-Case-Format (words separated by hyphens with the first letter of each word capitalized). Headers not in this format are automatically converted. Standard email headers are not supported. Example: `{"sender.ip":"1.2.3.4", "X-Mailin-custom":"some_custom_value", "Idempotency-Key":"abc-123"}`
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — HTML body content of the email. Required when `templateId` is not provided. Ignored when `templateId` is provided.
    
</dd>
</dl>

<dl>
<dd>

**message_versions:** `typing.Optional[typing.List[SendTransacEmailRequestMessageVersionsItem]]` — Array of message version objects for sending customized email variants. The `templateId` can be customized per version only if a global `templateId` is provided. The `htmlContent` and `textContent` can be customized per version only if at least one of these is present in the global parameters. Global parameters such as `to` (required), `bcc`, `cc`, `replyTo`, and `subject` can be customized per version. Maximum total recipients per API request is 2000. Maximum recipients per message version is 99. Individual `params` objects must not exceed 100 KB. Cumulative `params` across all versions must not exceed 1000 KB. See https://developers.brevo.com/docs/batch-send-transactional-emails for detailed usage instructions.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Key-value pairs for template variable substitution. Only applicable when the template uses the New Template Language format.
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[SendTransacEmailRequestReplyTo]` — Reply-to email address (required) and optional display name. Recipients will use this address when replying to the email.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[datetime.datetime]` — UTC date-time when the email should be sent (format: YYYY-MM-DDTHH:mm:ss.SSSZ). Include timezone information in the date-time value. Scheduled emails may be delayed by up to 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[SendTransacEmailRequestSender]` — Sender information. Required when `templateId` is not provided. Specify either an email address (with optional name) or a sender ID. The `name` field is ignored when `id` is provided.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Email subject line. Required when `templateId` is not provided.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Array of tags for categorizing and filtering emails
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[int]` — Template identifier
    
</dd>
</dl>

<dl>
<dd>

**text_content:** `typing.Optional[str]` — Plain text body content of the email. Ignored when `templateId` is provided.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[typing.List[SendTransacEmailRequestToItem]]` — Array of recipient objects. Each object contains an email address and an optional display name. Required when `messageVersions` is not provided. Ignored when `messageVersions` is provided. Example: `[{"name":"Jimmy", "email":"jimmy@example.com"}, {"name":"Joe", "email":"joe@example.com"}]`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">delete_scheduled_email_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete scheduled batch of emails by batchId or single scheduled email by messageId
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.delete_scheduled_email_by_id(
    identifier="4320f270-a4e3-4a2e-b591-edfe30a5e627",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — The `batchId` of scheduled emails batch (Should be a valid UUIDv4) or the `messageId` of scheduled email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_scheduled_email_by_id</a>(...) -> GetScheduledEmailByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch scheduled batch of emails by batchId or single scheduled email by messageId (Can retrieve data upto 30 days old)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
import datetime

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_scheduled_email_by_id(
    identifier="4320f270-a4e3-4a2e-b591-edfe30a5e627",
    start_date=datetime.date.fromisoformat("2022-02-02"),
    end_date=datetime.date.fromisoformat("2022-03-02"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — The `batchId` of scheduled emails batch (Should be a valid UUIDv4) or the `messageId` of scheduled email.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Mandatory if `endDate` is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older tha current date.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Mandatory if `startDate` is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetScheduledEmailByIdRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed. Not valid when identifier is `messageId`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetScheduledEmailByIdRequestStatus]` — Filter the records by `status` of the scheduled email batch or message. Not valid when identifier is `messageId`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page. Not valid when identifier is `messageId`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document on the page.  Not valid when identifier is `messageId`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_transac_emails_list</a>(...) -> GetTransacEmailsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will show the list of emails for past 30 days by default. To retrieve emails before that time, please pass startDate and endDate in query filters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_transac_emails_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` — **Mandatory if templateId and messageId are not passed in query filters.** Email address to which transactional email has been sent.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[int]` — **Mandatory if email and messageId are not passed in query filters.** Id of the template that was used to compose transactional email.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[str]` — **Mandatory if templateId and email are not passed in query filters.** Message ID of the transactional email sent.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) from which you want to fetch the list. **Maximum time period that can be selected is one month**.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) till which you want to fetch the list. **Maximum time period that can be selected is one month.**
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetTransacEmailsListRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_transac_email_content</a>(...) -> GetTransacEmailContentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note title="How to get uuid">You can get the uuid using either of the following methods:
Send a GET request to https://api.brevo.com/v3/smtp/emails and pass the message_id in the url. Use your api-key to authenticate the request and you will get your uuid as a response.
The uuid can also be fetched from the transactional logs page in your Brevo account, from the address URL.</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_transac_email_content(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid:** `str` — Unique id of the transactional email that has been sent to a particular contact
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">delete_an_smtp_transactional_log</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.delete_an_smtp_transactional_log(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — MessageId of the transactional log(s) to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_aggregated_smtp_report</a>(...) -> GetAggregatedSmtpReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will show the aggregated stats for past 90 days by default if `startDate` and `endDate` OR `days` is not passed. The date range can not exceed 90 days
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_aggregated_smtp_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). _Not compatible with 'startDate' and 'endDate'_
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag of the emails
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_email_event_report</a>(...) -> GetEmailEventReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will show the aggregated stats for past 30 days by default if `startDate` and `endDate` OR `days` is not passed. The date range can not exceed 90 days
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_email_event_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number limitation for the result returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Beginning point in the list to retrieve from.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). _Not compatible with 'startDate' and 'endDate'_
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter the report for a specific email addresses
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[GetEmailEventReportRequestEvent]` — Filter the report for a specific event type
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter the report for tags (serialized and urlencoded array)
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[str]` — Filter on a specific message id
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[int]` — Filter on a specific template id
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetEmailEventReportRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_smtp_report</a>(...) -> GetSmtpReportResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_smtp_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document on the page
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date of the report (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date of the report (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). _Not compatible with 'startDate' and 'endDate'_
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag of the emails
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetSmtpReportRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">post_preview_smtp_email_templates</a>(...) -> PostPreviewSmtpEmailTemplatesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.post_preview_smtp_email_templates(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_smtp_templates</a>(...) -> GetSmtpTemplatesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_smtp_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_status:** `typing.Optional[bool]` — Filter on the status of the template. Active = true, inactive = false
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetSmtpTemplatesRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">create_smtp_template</a>(...) -> CreateSmtpTemplateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment
from brevo.transactional_emails import CreateSmtpTemplateRequestSender

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.create_smtp_template(
    sender=CreateSmtpTemplateRequestSender(),
    subject="Thanks for your purchase !",
    template_name="Order Confirmation - EN",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender:** `CreateSmtpTemplateRequestSender` — Sender details including id or email and name (_optional_). Only one of either Sender's email or Sender's ID shall be passed in one request at a time. For example: **{"name":"xyz", "email":"example@abc.com"}** **{"name":"xyz", "id":123}**
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the template
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — Name of the template
    
</dd>
</dl>

<dl>
<dd>

**attachment_url:** `typing.Optional[str]` — Absolute url of the attachment (**no local file**). Extension allowed: #### xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps'
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — Body of the message (HTML version). The field must have more than 10 characters. **REQUIRED if htmlUrl is empty**
    
</dd>
</dl>

<dl>
<dd>

**html_url:** `typing.Optional[str]` — Url which contents the body of the email message. REQUIRED if htmlContent is empty
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` — Status of template. isActive = true means template is active and isActive = false means template is inactive
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Email on which campaign recipients will be able to reply to
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag of the template
    
</dd>
</dl>

<dl>
<dd>

**to_field:** `typing.Optional[str]` — To personalize the **To** Field. If you want to include the first name and last name of your recipient, add **{FNAME} {LNAME}**. These contact attributes must already exist in your Brevo account. If input parameter **params** used please use **{{contact.FNAME}} {{contact.LNAME}}** for personalization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">get_smtp_template</a>(...) -> GetSmtpTemplateOverview</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.get_smtp_template(
    template_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `int` — id of the template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">update_smtp_template</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.update_smtp_template(
    template_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `int` — id of the template
    
</dd>
</dl>

<dl>
<dd>

**attachment_url:** `typing.Optional[str]` — Absolute url of the attachment (**no local file**). Extensions allowed: #### xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — **Required if htmlUrl is empty**. If the template is designed using Drag & Drop editor via HTML content, then the design page will not have Drag & Drop editor access for that template. Body of the message (HTML must have more than 10 characters)
    
</dd>
</dl>

<dl>
<dd>

**html_url:** `typing.Optional[str]` — **Required if htmlContent is empty**. URL to the body of the email (HTML)
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` — Status of the template. isActive = false means template is inactive, isActive = true means template is active
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Email on which campaign recipients will be able to reply to
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[UpdateSmtpTemplateRequestSender]` — Sender details including id or email and name (_optional_). Only one of either Sender's email or Sender's ID shall be passed in one request at a time. For example: **{"name":"xyz", "email":"example@abc.com"}** **{"name":"xyz", "id":123}**
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject of the email
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag of the template
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `typing.Optional[str]` — Name of the template
    
</dd>
</dl>

<dl>
<dd>

**to_field:** `typing.Optional[str]` — To personalize the **To** Field. If you want to include the first name and last name of your recipient, add **{FNAME} {LNAME}**. These contact attributes must already exist in your Brevo account. If input parameter **params** used please use **{{contact.FNAME}} {{contact.LNAME}}** for personalization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">delete_smtp_template</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.delete_smtp_template(
    template_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `int` — id of the template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_emails.<a href="src/brevo/transactional_emails/client.py">send_test_template</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_emails.send_test_template(
    template_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `int` — Id of the template
    
</dd>
</dl>

<dl>
<dd>

**request:** `SendTestEmail` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TransactionalSms
<details><summary><code>client.transactional_sms.<a href="src/brevo/transactional_sms/client.py">send_async_transactional_sms</a>(...) -> SendAsyncTransactionalSmsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>If the user includes stop code in the Transactional SMS, then it will be switched to Marketing SMS automatically and it will be interpreted as a Marketing SMS. To send Transactional SMS as Transactional, it is important not to use stop code.
Note: For adding a stop code, client has to add reply STOP to [STOP_CODE] and the [STOP_CODE] will be replaced with the number.</Note>
<Note title="For end users in France">Transactional SMS can be sent at any time without time restrictions. However, if a message is categorized as Marketing, it must adhere to specific time restrictions. Messages sent outside of these restricted hours will experience delays and will be processed during allowable times. Specifically, Marketing SMS cannot be processed between 10pm and 8am, on Sundays, and on French public holidays.</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_sms.send_async_transactional_sms(
    recipient="33689965433",
    sender="MyShop",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SendTransacSms` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_sms.<a href="src/brevo/transactional_sms/client.py">send_transac_sms</a>(...) -> SendTransacSmsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_sms.send_transac_sms(
    recipient="33689965433",
    sender="MyShop",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SendTransacSms` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_sms.<a href="src/brevo/transactional_sms/client.py">get_transac_aggregated_sms_report</a>(...) -> GetTransacAggregatedSmsReportResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_sms.get_transac_aggregated_sms_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) of the report
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) of the report
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). **Not compatible with startDate and endDate**
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Filter on a tag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_sms.<a href="src/brevo/transactional_sms/client.py">get_sms_events</a>(...) -> GetSmsEventsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_sms.get_sms_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents per page
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) of the report
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) of the report
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document of the page
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). **Not compatible with 'startDate' and 'endDate'**
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Filter the report for a specific phone number
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[GetSmsEventsRequestEvent]` — Filter the report for specific events
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter the report for specific tags passed as a serialized urlencoded array
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetSmsEventsRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactional_sms.<a href="src/brevo/transactional_sms/client.py">get_transac_sms_report</a>(...) -> GetTransacSmsReportResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.transactional_sms.get_transac_sms_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — **Mandatory if endDate is used.** Starting date (YYYY-MM-DD) of the report
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — **Mandatory if startDate is used.** Ending date (YYYY-MM-DD) of the report
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Number of days in the past including today (positive integer). **Not compatible with 'startDate' and 'endDate'**
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Filter on a tag
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetTransacSmsReportRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SmsTemplates
<details><summary><code>client.sms_templates.<a href="src/brevo/sms_templates/client.py">get_sms_templates</a>(...) -> GetSmsTemplatesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from brevo import Brevo
from brevo.environment import BrevoEnvironment

client = Brevo(
    api_key="<value>",
    environment=BrevoEnvironment.DEFAULT,
)

client.sms_templates.get_sms_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents returned per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Index of the first document in the page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetSmsTemplatesRequestSort]` — Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

