# Complete Bunq API Wrapper for Python
This project aims to have a complete Python wrapper for the [Bunq API](https://doc.bunq.com/). It takes inspiration from the [.NET wrapper](https://github.com/Sycade/BunqApi) written by the great [MLowijs](https://github.com/mlowijs). Some functionality, especially in `ApiClient`, is based on or taken from the thin [API wrapper](https://github.com/madeddie/python-bunq) created by [MadEddie](https://github.com/madeddie). Thanks MLowijs and MadEddie!

This project is built in **Python 3.6**

[![Build Status](https://travis-ci.org/PJUllrich/Complete-Bunq-API-Python-Wrapper.svg?branch=master)](https://travis-ci.org/PJUllrich/Complete-Bunq-API-Python-Wrapper)
[![BCH compliance](https://bettercodehub.com/edge/badge/PJUllrich/Complete-Bunq-API-Python-Wrapper?branch=master)](https://bettercodehub.com/)
[![Test Coverage](https://coveralls.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/badge.svg?branch=master)](https://coveralls.io/github/PJUllrich/Complete-Bunq-API-Python-Wrapper?branch=master) 
[![Updates](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/shield.svg)](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/)
[![Python 3](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/python-3-shield.svg)](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/)

## Getting started
1. First enter your [API Key](https://www.bunq.com/en/api) in the `apiwrapper/config/parameters.ini` file.
2. Next, [create a new Virtual Environment](https://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) based on **Python 3.6**
3. Activate your Virtual Environment and install the requirements in `requirements.txt` with `pip3.6 install -r requirements.txt`
4. Open `get_started.py`, read through the comments and follow them. After doing this you will have a ready-to-go installation and can start using the API!

## How to use this API Wrapper
Each endpoint of the [Bunq API](https://doc.bunq.com/) has its own `Endpoint` module. The existing ones are in the `apiwrapper/endpoints` package.
The **EndpointController** in `apiwrapper/endpoints/controller` has an
instance of each of these endpoints.
Any ApiClient will have an instance of this endpoint controller called
**endpoints**. After creating an ApiClient you can simply make api calls with:
```python
api_client.endpoints.ENDPOINT_OF_YOUR_CHOICE.CALL_OF_YOUR_CHOICE()
```

**Endpoint functions simply return the response from the Bunq API.**

#### [Example] Retrieve all Monetary Accounts for User
```python
import json

from apiwrapper.clients.api_client_persisting import ApiClientPersisting

user_id = 1234

api = ApiClientPersisting()
res = api.endpoints.monetary_account.get_all_accounts_for_user(user_id)

print(json.dumps(res, indent=2))
```

## Reuse Installation
If you followed the script `get_started.py` mentioned above already, you should have the following parameters saved somewhere:

- API Key
- Private Key
- Installation Token (not needed if you have the Session Token)
- Installation ID (needed to create new session tokens)
- Server Public Key
- Session Token

Note: If you saved these parameters to the config file, they will be in `apiwrapper/config/parameters.ini`

If you have the above parameters, you can go ahead and create an APIClient, which is the connector to the Bunq API.

You will have to decide which APIClient to use.
At the moment, I included one that uses the config file in `apiwrapper/config/parameters.ini`, which is the 'normal' class `APIClient`.
Also, on request from OGKevin, I included an APIClient, which does not load the parameters from a config file, called the `APIClientNonPersisting`.

So, decide on whether to use the config file or not and uncomment one of the
following lines:

If you want to use the parameters stored in `apiwrapper/config/parameters.ini`,
use the following code:
```python
from apiwrapper.clients.api_client_persisting import ApiClientPersisting

api_key = "YOUR API KEY HERE"
api = ApiClientPersisting(api_key)
```

Else, if you want to use your own parameters, use the following
lines and enter your parameters there
```python
from apiwrapper.clients.api_client import ApiClient

api_key = "YOUR API KEY HERE"
private_key = "YOUR PRIVATE KEY HERE"
session_token = "YOUR SESSION TOKEN HERE"
server_public_key = "THE SERVER PUBLIC KEY HERE"

api = ApiClient(api_key, privkey=private_key,
                                 session_token=session_token,
                                 server_pubkey=server_public_key)
```

Now, you are able to make calls to the Bunq API using the `EndpointsController`.
I have included an example of how to get the User ID from the API:
```python
from apiwrapper.clients.api_client import ApiClient
from apiwrapper.clients.api_client_persisting import ApiClientPersisting
import json

api = "MAKE SURE TO CREATE THE API CLIENT AS DESCRIBED ABOVE"

res = api.endpoints.user.get_logged_in_user()
print(json.dumps(res, indent=2))
```

## Contribute
If you want to contribute, fork this repository and start implementing one of the following points:
* Add `POST`, `PUT`, and some `DELETE` calls for all endpoints
* Add Encryption/Decryption of `/config/parameter.ini` file using Password
* Have a look at the Issues of this repository
