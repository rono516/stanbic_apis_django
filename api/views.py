from django.http import JsonResponse
import requests
from django.shortcuts import render
client_id = "8721eba833943ccd29d6e74fb0bd937f"
client_secret = "7e1c5c1b1c298d71f39d49a77e28aeb4"
token_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/auth/oauth2/token"
scope = "payments"

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
        # "recipientMobileNo": "25472XXXXXXXX",
        "recipientBankAcctNo": "0100013845845",
        "recipientBankCode": "31002"
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
def index(request):
  return render(request, "api/index.html")
def sendtophone(request):
  return render(request, "api/sendtophone.html")
def sendtoaccount(request):
  return render(request, "api/sendtoaccount.html")

def auth_token(request):

    payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
    }
    response = requests.post(token_url,data=payload)
    return JsonResponse(response.json())






def make_payment(request):
    access_token = "AAIgODcyMWViYTgzMzk0M2NjZDI5ZDZlNzRmYjBiZDkzN2YwHFclprTCh09XtBA7MlLuDS4UoovZtnGlE-lFdi3IY_ASQjZLNQD9pdAFeHXNfxNoEzec3_Akwnlnn09MEmrLxdXxh_xnRPn813Yex7k6A7hTRWEui-inUl_62o3sZyI"
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

    payload = {
        "originatorAccount": "01040304011",
        # "identification": {
        #     # "mobileNumber": "254737696956" 
        #     "mobileNumber": "254721615262"
        # },        
        "requestedExecutionDate": "2024-7-17",
        "sendMoneyTo": "0100010483659",
        # "sendMoneyTo": "0710361783001",
        "dbsReferenceId": "98989271771176942",
        "txnNarrative": "TESTPESALINK",
        "callBackUrl": "https://clientdomain.com/client/Callback",
        "transferTransactionInformation": {
            "instructedAmount": "10" ,
            # {
            #     "amount": "10",
            #     "currencyCode": "KES"
            # },
            "counterpartyAccount": {
                "identification": {
                    "recipientMobileNo": "254722716838",
                    # "recipientMobileNo": "254721615262",
                    "recipientBankAcctNo": "0710361783001",
                    "recipientBankCode": "31"
                }
            },
            # "counterparty": {
            #     "name": "HEZBON",
            #     "postalAddress": {
            #         "addressLine": "KENYA",
            #         "postCode": "1100 ZZ",
            #         "town": "Nairobi",
            #         "country": "KE"
            #     }
            # },
            # "remittanceInformation": {
            #     "type": "FEES PAYMENTS",
            #     "content": "SALARY"
            # },
            "endToEndIdentification": "5e1a3da132cc"
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "accept": "application/json"
    }
    import logging
    logging.basicConfig(level=logging.DEBUG)

    response = requests.post(url, json=example_body, headers=headers)
    return JsonResponse(response.json())




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