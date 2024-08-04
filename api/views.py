from django.http import JsonResponse
import requests
from django.shortcuts import render
client_id = "bde1801356912a01adc1e2b50fc4879c"
client_secret = "42a920ac85b542486ca5ca6ebbe57a60"
rtgs_client_id ="a6e7099e476feb6688935bfa38bbc183"
rtgs_client_secret="0f6eda38e4d19c51cd6a45d4976ab971"
token_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/auth/oauth2/token"
scope = "payments"

# 01040304011
# 20040304211
# 20040304411
# Member ID - 40304
# Member ID - 29999
# 0102999911
# 20029999211
# 2002999211
# 20029999411

# testkba app Credentials
# 20040304211 - account number
# 63144145b465e74f3cc7c4662516118e key
# be1985b138caceeeffe2b046857fbfc3 secret

# test stanbic app Credentials
# 0100010483659 - account number
# 8721eba833943ccd29d6e74fb0bd937f key
# 7e1c5c1b1c298d71f39d49a77e28aeb4 secret

# testkba2 Credentials
# 0100013845845 - account number
# 709816b5a594cc46494ae0d004b2aad3 key
# 3683cd5277fa0534d4db66f456ec8482 secret

# teststanbictwo Credentials
# 0100013845845 - account number
# a6e7099e476feb6688935bfa38bbc183 key
# 0f6eda38e4d19c51cd6a45d4976ab971 secret

# test kbs stanbic
# 0100013868365
# key - bde1801356912a01adc1e2b50fc4879c
# secret - 42a920ac85b542486ca5ca6ebbe57a60

# test eq
# 1220179020894
# key - 67ae5aaec82e9fcbc3d6ceb8dccaebff
# secret - e35b374256973990c21e34d09f8ca78e

# test kbs acc
# 01040304011
# key - eea0afa41279d8f8b6e4e8ecc90ba8c4
# secret - 6a8f0089f42215accfc04d3877047435

# test support acc
# 0100013644707
# key - 3c5d6214a1d2800edd8c07b2ce67bcd1
# secret - cd07e4af60866b90c233ebbb99e824a7
import json
def index(request):
  return render(request, "api/index.html")
def sendtophone(request):
  return render(request, "api/sendtophone.html")
def sendtoaccount(request):
  # api\resources\banks.json
  with open("api/resources/banks.json") as f:
     banks = json.load(f)
     return render(request, "api/sendtoaccount.html", {"banks": banks})

def return_auth_token():

    payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
    }
    response = requests.post(token_url,data=payload)
    access_token = response.json().get("access_token")
    # print(access_token)
    return access_token
def return_rtgs_auth_token():
  payload = {
    'grant_type': 'client_credentials',
    'client_id': rtgs_client_id,
    'client_secret': rtgs_client_secret,
    'scope': scope
  }
  response = requests.post(token_url,data=payload)
  acess_token = response.json().get("access_token")
  return acess_token

def get_auth_token(request):

    payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
    }
    response = requests.post(token_url,data=payload)
    return JsonResponse(response.json())


example_body = {
  "originatorAccount": {
    "identification": {
      "mobileNumber": "254737696956"
    }
  },
  "requestedExecutionDate": "2021-10-27",
  "sendMoneyTo": "ACCOUNT.NUMBER",
  "dbsReferenceId": "98989271771176942",
  "txnNarrative": "TESTPESALINK",
  "callBackUrl": "https://clientdomain.com/client/Callback",
  "transferTransactionInformation": {
    "instructedAmount": {
      "amount": "10",
      "currencyCode": "KES"
    },
    "counterpartyAccount": {
      "identification": {
        "recipientMobileNo": "25472XXXXXXXX",
        "recipientBankAcctNo": "01008747142",
        "recipientBankCode": "07000"
      }
    },
    "counterparty": {
      "name": "HEZBON",
      "postalAddress": {
        "addressLine": "KENYA",
        "postCode": "1100 ZZ",
        "town": "Nairobi",
        "country": "KE"
      }
    },
    "remittanceInformation": {
      "type": "FEES PAYMENTS",
      "content": "SALARY"
    },
    "endToEndIdentification": "5e1a3da132cc"
  }
}


def make_payment(request):
    access_token = return_auth_token()
    # print("access token" + access_token)
    # access_token = "AAIgNjdhZTVhYWVjODJlOWZjYmMzZDZjZWI4ZGNjYWViZmYnJk8w6JFPAN-VlAqxIl4jdn0f9Fc7JCj3UPWIVZvfyLwV60N4bweRhPSdydyY9er-R-N-QB3JctB3xBip7bqzc5SNMnyUGzd_IdiB1fxmf4AoalEOa1sD5iGoIVDFug8"
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

    payload = {
        "originatorAccount": {
            "identification": {
                "mobileNumber": "254721615262"
            }
        },
        "requestedExecutionDate": "2024-08-02",
        "sendMoneyTo": "ACCOUNT.NUMBER",
        "dbsReferenceId": "98989271771176944",
        "txnNarrative": "TESTPESALINK",
        "callBackUrl": "https://clientdomain.com/client/Callback",
        "transferTransactionInformation": {
            "instructedAmount": {
                "amount": "11",
                "currencyCode": "KES"
            },
             "counterpartyAccount": {
                "identification": {
                    # "recipientMobileNo": "254792009556",
                    # "recipientBankAcctNo": "1220179020894",
                    # "recipientBankCode": "68175",  # equity
                    # "recipientBankAcctNo": "0100013644707",
                    # "recipientBankCode": "31030", # stanbic
                    "recipientBankAcctNo": "01120000564000",
                    "recipientBankCode": "11170", #cooperative
                }
            },
            "counterparty": {
                "name": "HEZBONA",
                "postalAddress": {
                    "addressLine": "KENYA",
                    "postCode": "1100 ZZ",
                    "town": "Nairobi",
                    "country": "KE"
                }
            },
            "remittanceInformation": {
                "type": "FEES PAYMENTS",
                "content": "SALARY"
            },
            "endToEndIdentification": "5e1a3da132cc"
        }
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "accept": "application/json"
    }
    # import logging
    # logging.basicConfig(level=logging.DEBUG)

    response = requests.post(url, json=payload, headers=headers)
    return JsonResponse(response.json())

def send_to_mobile_money(request):
   send_money_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"
   access_token = "AAIgODcyMWViYTgzMzk0M2NjZDI5ZDZlNzRmYjBiZDkzN2Yp2bldk8UsTab7kvYNR_1aH_nW3NfRIkQb6ub85g5SL15bkXr5w_k8AZ3JwFZ-lbVl5cy0FnbMecZEt6AjLEcziDX-_yqtbIEUo6JT5IOvlBrS2cjyif94ZKdNa4-0CFA"
   payload = {
        "originatorAccount": {
          "identification": {
            "mobileNumber": "254737696956"
          }
        },
        "requestedExecutionDate": "2021-10-27",
        "dbsReferenceId": "98989271771176942",
        "txnNarrative": "TESTPESALINK",
        "callBackUrl": "https://clientdomain.com/client/Callback",
        "transferTransactionInformation": {
          "instructedAmount": {
            "amount": "500",
            "currencyCode": "KES"
          },
          "counterpartyAccount": {
            "identification": {
              "recipientMobileNo": "254792009556",
            }
          },
          "counterparty": {
            "name": "HEZBON",
            "postalAddress": {
              "addressLine": "KENYA",
              "postCode": "1100 ZZ",
              "town": "Nairobi",
              "country": "KE"
            }
          },
          "remittanceInformation": {
            "type": "FEES PAYMENTS",
            "content": "SALARY"
          },
          "endToEndIdentification": "5e1a3da132cc"
        }
      }
   headers = {
        "Authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "accept": "application/json"
    }
   response = requests.post(send_money_url, json=payload, headers=headers)
   return JsonResponse(response.json())
  #  print("Here we are")

def rtgs(request):

  access_token = return_rtgs_auth_token()
  url = "https://api.connect.stanbicbank.co.ke/api/sandbox/rtgs-payments/"
  payload = {
      "originatorAccount": {
        "identification": {
          "identification": "0100001536723",
          "debitCurrency": "KES",
          "mobileNumber": "254735084266"
        }
      },
      "requestedExecutionDate": "2021-06-03",
      "dbsReferenceId": "989892717711",
      "txnNarrative": "TESEAPS123",
      "transferTransactionInformation": {
        "instructedAmount": {
          "amount": "500",
          "creditCurrency": "UGX"
        },
        "counterpartyAccount": {
          "identification": {
            "identification": "9877665554",
            "beneficiaryBank": "SW-CERBUGKA",
            "beneficiaryChargeType": "OUR"
          }
        },
        "counterparty": {
          "name": "TAAM OIL LTD",
          "postalAddress": {
            "addressLine": "UGANDA",
            "postCode": "1100 ZZ",
            "town": "Kampala",
            "country": "UG"
          }
        },
        "remittanceInformation": {
          "type": "UNSTRUCTURED",
          "content": "SCHOOL FEES"
        },
        "endToEndIdentification": "5e1a3da132cc"
      }
    }
  headers = {
      "Authorization": f"Bearer {access_token}",
      "content-type": "application/json",
      "accept": "application/json'"
  }
  response = requests.post(url, data=payload, headers=headers)
  print(response)
  return JsonResponse(response.json())
