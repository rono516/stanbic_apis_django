from django.http import JsonResponse
import requests
from django.shortcuts import render
client_id = "bde1801356912a01adc1e2b50fc4879c"
client_secret = "42a920ac85b542486ca5ca6ebbe57a60"
token_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/auth/oauth2/token"
scope = "payments"


import json
def index(request):
  return render(request, "api/index.html")
def sendtophone(request):
  return render(request, "api/sendtophone.html")
def sendtoaccount(request):
  with open("api/resources/banks.json") as f:
     banks = json.load(f)
     return render(request, "api/sendtoaccount.html", {"banks": banks})
def rtgs_account_to_account(request):
   with open("api/resources/swift.json") as f:
     banks = json.load(f)
     return render(request, "api/rtgs_acccount_to_account.html", {"banks": banks})

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


def get_auth_token(request):

    payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
    }
    response = requests.post(token_url,data=payload)
    return JsonResponse(response.json())


def pesalink(request):
    if request.method == "POST":
      access_token = return_auth_token()
      url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

      # Data from request
      bank_code = request.POST.get("bank")
      account_no = request.POST.get("account")
      amount = request.POST.get("amount")
      reason = request.POST.get("reason")
      phone = request.POST.get("phone")

      payload = {
          "originatorAccount": {
              "identification": {
                  "mobileNumber": phone
              }
          },
          "requestedExecutionDate": "2024-08-02",
          "sendMoneyTo": "ACCOUNT.NUMBER",
          "dbsReferenceId": "9898927177117694688",
          "txnNarrative": "TESTPESALINK",
          "callBackUrl": "https://clientdomain.com/client/Callback",
          "transferTransactionInformation": {
              "instructedAmount": {
                  "amount": amount,
                  "currencyCode": "KES"
              },
              "counterpartyAccount": {
                  "identification": {
                      "recipientBankAcctNo": account_no,
                      "recipientBankCode": bank_code, #cooperative bank
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
                  "type": reason,
                  "content": reason
              },
              "endToEndIdentification": "5e1a3da132cc"
          }
      }
      headers = {
          "Authorization": f"Bearer {access_token}",
          "content-type": "application/json",
          "accept": "application/json"
      }

      print(bank_code)

      response = requests.post(url, json=payload, headers=headers)
      return JsonResponse(response.json())
    else:
       return render(request,"api/sendtoaccount.html")
  
def rtgs(request):
  if request.method == "POST":
    access_token = return_auth_token()
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/rtgs-payments/"
    # Data from request
    from_account = request.POST.get("from_account")
    phone = request.POST.get("phone")
    to_account = request.POST.get("to_account")
    bank = request.POST.get("bank")
    amount = request.POST.get("amount")
    reason = request.POST.get("reason")

    payload ={
        "originatorAccount": {
          "identification": {
            "identification": from_account,
            "debitCurrency": "KES",
            "mobileNumber": phone
          }
        },
        "requestedExecutionDate": "2024-08-09",
        "dbsReferenceId": "9898927177110",
        "txnNarrative": "TESEAPS123",
        "transferTransactionInformation": {
          "instructedAmount": {
            "amount": amount,
            "creditCurrency": "KES"
          },
          "counterpartyAccount": {
            "identification": {
              "identification": to_account,
              "beneficiaryBank": bank,
              "beneficiaryChargeType": "OUR"
            }
          },
          "counterparty": {
            "name": "Collins K Rono",
            "postalAddress": {
              "addressLine": "KENYA",
              "postCode": "1100 ZZ",
              "town": "Nairobi",
              "country": "KE"
            }
            },
          "remittanceInformation": {
            "type": reason,
            "content": reason
          },
          "endToEndIdentification": "5e1a3da132cc"
        }
      }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "accept": "application/json'"
    }
    response = requests.post(url, json=payload, headers=headers)
    # print(response)
    return JsonResponse(response.json())
  else:
     return render( request,"api/rtgs_acccount_to_account.html")
    
  

def swift_payment(request):
  #  print("Here we are")
  access_token = return_auth_token()
  url = "https://api.connect.stanbicbank.co.ke/api/sandbox/swift-payments/"
  headers = {
     "Authorization": f"Bearer {access_token}",
     "content-type": "application/json",
     "accept": "application/json"
  }
  payload = {
      "originatorAccount": {
        "identification": {
          "identification": "1220179020894",
          "debitCurrency": "KES",
          "mobileNumber": "254792009556"
        }
      },
      "requestedExecutionDate": "2021-05-27",
      "dbsReferenceId": "989892717711908",
      "txnNarrative": "TESEAPS123",
      "callBackUrl": "https://clientdomain.com/client/Callback",
      "schedule": {
        "transferFrequency": "MONTHLY",
        "on": "12",
        "startDate": "2021-02-13",
        "endDate": "2022-01-03",
        "repeat": "3",
        "every": "1"
      },
      "transferTransactionInformation": {
        "instructedAmount": {
          "amount": "50",
          "creditCurrency": "KES"
        },
        "counterpartyAccount": {
          "identification": {
            "identification": "00105011763050",
            "correspondentBank": "UGBAUGKAXXX",
            "beneficiaryBank": "IMBLKENA"
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
          "type": "FEES PAYMENTS",
          "content": "SALARY"
        },
        "endToEndIdentification": "5e1a3da132cc"
      }
    }
  response = requests.post(url=url,headers=headers,json=payload)
  print("response "+response)
  return JsonResponse(response.json())

def send_to_mobile_money(request):
   
   send_money_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"
   access_token = return_auth_token()
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
          # "endToEndIdentification": "5e1a3da132cc"
        }
      }
   headers = {
        "Authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "accept": "application/json"
    }
    
   response = requests.post(send_money_url, json=payload, headers=headers)
   return JsonResponse(response.json())
 
