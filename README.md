# Complete Bunq API Wrapper for Python
This project aims to have a complete Python wrapper for the [Bunq API](https://doc.bunq.com/). It takes inspiration from the [.NET wrapper](https://github.com/Sycade/BunqApi) written by the great [MLowijs](https://github.com/mlowijs). Some functionality, especially in `ApiClient`, is based on or taken from the thin [API wrapper](https://github.com/madeddie/python-bunq) created by [MadEddie](https://github.com/madeddie). Thanks MLowijs and MadEddie!

This project is built in **Python 3.6**

[![BCH compliance](https://bettercodehub.com/edge/badge/PJUllrich/Complete-Bunq-API-Python-Wrapper?branch=master)](https://bettercodehub.com/)
[![Test Coverage](https://coveralls.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/badge.svg?branch=master)](https://coveralls.io/github/PJUllrich/Complete-Bunq-API-Python-Wrapper?branch=master) 
[![Updates](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/shield.svg)](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/)
[![Python 3](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/python-3-shield.svg)](https://pyup.io/repos/github/PJUllrich/Complete-Bunq-API-Python-Wrapper/)

## Getting started
1. First enter your [API Key](https://www.bunq.com/en/api) in the `/config/parameters.ini` file.
2. Next, [create a new Virtual Enviroment](https://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) based on **Python 3.6**
3. Activate your Virtual Environment and install the requirements in `requirements.txt` with `pip3.6 install -r requirements.txt` 
4. Run `python3.6 setup.py`-> It will create a new public/private key pair and register it
5. Loop over the following until no function calls are left
   1. Comment out (i.e. put a # before) the function calls without # in `setup.py`
   2. Remove the # before the next function call.
   3. Run `python3.6 setup.py` again
6. Once you have called all functions in `setup.py`, you have successfully configured your API Wrapper and can start using it!

## How to use this API Wrapper
Each endpoint of the [Bunq API](https://doc.bunq.com/) has (or will have) its own `Endpoint` module. The existing ones are in the `/endpoints` package.
The `/endpoints/controller` has an instance of each of these endpointsn. You can call the functions of the `Endpoint` modules through the `/endpoints/controller`. 

**Endpoint functions simply return the JSON response from the Bunq API**

#### [Example] Retrieve the currently logged-in user
```python
import json
from endpoints.controller import Controller as Endpoints

res = Endpoints.user.get_logged_in_user()
print(json.dumps(res, indent=2))
```

#### [Example] Retrieve all Monetary Accounts for User
```python
import json
from endpoints.controller import Controller as Endpoints

user_id = 1234
res = Endpoints.monetary_account.get_all_monetary_accounts_for_user(user_id)
print(json.dumps(res, indent=2))
```

## Contribute
If you want to contribute, fork this repository and start implementing one of the following points:
* Add missing Endpoints which are listed in `/endpoints/endpoint`below the `TODO` comment.
* Add `POST`, `PUT`, and some `DELETE` calls for all endpoints
* Find a way for Python to wait for the function calls in `setup.py` to finish before calling the next function.
