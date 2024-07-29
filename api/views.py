from django.http import JsonResponse
import requests
from django.shortcuts import render
client_id = "8721eba833943ccd29d6e74fb0bd937f"
client_secret = "7e1c5c1b1c298d71f39d49a77e28aeb4"
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

# def get_auth_token():

#     payload = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret,
#     'scope': scope
#     }
#     response = requests.post(token_url,data=payload)
#     access_token = response.json().get("access_token")
#     # print(access_token)
#     return access_token
# here we are coding in the hope that we don't produce bad code 

def get_auth_token(request):

    payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
    }
    response = requests.post(token_url,data=payload)
    return JsonResponse(response.json())





def make_payment(request):
    access_token = "AAIgODcyMWViYTgzMzk0M2NjZDI5ZDZlNzRmYjBiZDkzN2bcxjhtQTnDmZF8FRoTQ0FUvhvV0Dx0JeCt5aLaHO4pnvHAoZVVWnjIWLJ2XnWr0_Q6VpE91PS4lbaBfWrqHpa7weBuJ3QysyuvV7Jd2vye-dR5_EXdKX6k4pxu7gQ4b70"
    # print("access token" + access_token)
    # access_token = "AAIgNjdhZTVhYWVjODJlOWZjYmMzZDZjZWI4ZGNjYWViZmYnJk8w6JFPAN-VlAqxIl4jdn0f9Fc7JCj3UPWIVZvfyLwV60N4bweRhPSdydyY9er-R-N-QB3JctB3xBip7bqzc5SNMnyUGzd_IdiB1fxmf4AoalEOa1sD5iGoIVDFug8"
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

    payload = {
        "originatorAccount": {
            "identification": {
                "mobileNumber": "254721615262"
            }
        },
        "requestedExecutionDate": "2024-07-26",
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
                    # "recipientMobileNo": "254792009556",
                    "recipientBankAcctNo": "1220179020894",
                    "recipientBankCode": "68012",   
                    # "recipientBankAcctNo": "20040304211",
                    
                    # "recipientBankCode": "31000"
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

schema = {
  "type": "object",
  "description": "A Resftful(JSON) Payload request with the details required to initiate a pesalink payment. Instant payments are currently supported",
  "required": [
    "requestedExecutionDate",
    "txnNarrative",
    "dbsReferenceId",
    "transferTransactionInformation",
    "originatorAccount"
  ],
  "properties": {
    "originatorAccount": {
      "type": "object",
      "properties": {
        "identification": {
          "type": "object",
          "properties": {
            "mobileNumber": {
              "type": "string",
              "example": "254737696956"
            }
          }
        }
      }
    },
    "requestedExecutionDate": {
      "type": "string",
      "example": "2021-10-27",
      "description": "The current system date (EAT) in the format YYYY-MM-DD"
    },
    "sendMoneyTo": {
      "type": "string",
      "enum": [
        "ACCOUNT.NUMBER"
      ],
      "description": "When sending to Account Number use ACCOUNT.NUMBER",
      "example": "ACCOUNT.NUMBER"
    },
    "dbsReferenceId": {
      "type": "string",
      "example": "98989271771176942",
      "description": "This is 3rd party system unique reference. Our systems will use this reference to track your transactions."
    },
    "txnNarrative": {
      "type": "string",
      "example": "TESTPESALINK"
    },
    "callBackUrl": {
      "type": "string",
      "example": "https://clientdomain.com/client/Callback",
      "description": "Future use"
    },
    "transferTransactionInformation": {
      "type": "object",
      "properties": {
        "instructedAmount": {
          "type": "object",
          "properties": {
            "amount": {
              "type": "string",
              "example": "500"
            },
            "currencyCode": {
              "type": "string",
              "example": "KES"
            }
          }
        },
        "counterpartyAccount": {
          "type": "object",
          "properties": {
            "identification": {
              "type": "object",
              "properties": {
                "recipientMobileNo": {
                  "type": "string",
                  "example": "25472XXXXXXXX",
                  "description": "When the Mobile Number is populated, The account Number should be left blank"
                },
                "recipientBankAcctNo": {
                  "type": "string",
                  "example": "01008747142",
                  "description": "When account Number is populated"
                },
                "recipientBankCode": {
                  "type": "string",
                  "example": "07000"
                }
              }
            }
          }
        },
        "counterparty": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "example": "HEZBON"
            },
            "postalAddress": {
              "type": "object",
              "properties": {
                "addressLine": {
                  "type": "string",
                  "example": "KENYA"
                },
                "postCode": {
                  "type": "string",
                  "example": "1100 ZZ"
                },
                "town": {
                  "type": "string",
                  "example": "Nairobi"
                },
                "country": {
                  "type": "string",
                  "example": "KE"
                }
              }
            }
          }
        },
        "remittanceInformation": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "example": "FEES PAYMENTS"
            },
            "content": {
              "type": "string",
              "example": "SALARY"
            }
          }
        },
        "endToEndIdentification": {
          "type": "string",
          "example": "5e1a3da132cc"
        }
      }
    }
  }
}



# test example
# {
#   "originatorAccount": "01040304011" {
#     # "accountNumber" :"01040304011",
#     "identification": {
#       "mobileNumber": "254721615262"
#     }
#   },
#   "requestedExecutionDate": "2021-10-27",
#   "sendMoneyTo": "0710361783001",
#   "dbsReferenceId": "98989271771176942",
#   "txnNarrative": "TESTPESALINK",
#   "callBackUrl": "https://clientdomain.com/client/Callback",
#   "transferTransactionInformation": {
#     "instructedAmount": "10" {
#       # "amount": "500",
#       "currencyCode": "KES"
#     },
#     "counterpartyAccount": "01040304011" {
#       "identification": {
#         "recipientMobileNo": "254721615262",
#         "recipientBankAcctNo": "0710361783001",
#         "recipientBankCode": "63"
#       }
#     },
#     "counterparty": {
#       "name": "HEZBON",
#       "postalAddress": {
#         "addressLine": "KENYA",
#         "postCode": "1100 ZZ",
#         "town": "Nairobi",
#         "country": "KE"
#       }
#     },
#     "remittanceInformation": {
#       "type": "FEES PAYMENTS",
#       "content": "SALARY"
#     },
#     "endToEndIdentification": "5e1a3da132cc"
#   }
# }