from django.http import JsonResponse
import requests
from django.shortcuts import render
import random
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
def swift_account_to_account(request):
  with open("api/resources/swift.json") as f:
    banks = json.load(f)
    return render(request, "api/swift_acccount_to_account.html", {"banks": banks})



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
    """
    Handles PesaLink payment processing via Stanbic Bank's API.

    This function processes a POST request to initiate a PesaLink payment by sending a request 
    to the Stanbic Bank sandbox API. It collects payment details from the request, constructs 
    a payload, and makes an API call to the PesaLink endpoint.

    Parameters:
    - request (HttpRequest): The HTTP request object, expected to be a POST request with the 
      following form data:
        - bank: The recipient's bank code.
        - account: The recipient's bank account number.
        - amount: The amount to be transferred.
        - reason: The reason for the transfer.
        - phone: The phone number of the originator.

    Returns:
    - JsonResponse: If the request method is POST, returns the JSON response from the Stanbic 
      Bank API.
    - HttpResponse: If the request method is not POST, renders the "sendtoaccount.html" template.

    API Details:
    - Endpoint: https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/
    - Authorization: Bearer token obtained from return_auth_token() function
    - Payload:
      - originatorAccount: Contains the mobile number of the originator.
        - requestedExecutionDate: Static date set to "2024-08-09".
        - sendMoneyTo: Static value "ACCOUNT.NUMBER".
        - dbsReferenceId: Randomly generated 6-digit reference ID.
        - txnNarrative: Static value "TESTPESALINK".
        - callBackUrl: Static callback URL "https://clientdomain.com/client/Callback".
        - transferTransactionInformation: Contains details about the amount, counterparty 
          account, counterparty identity, and remittance information.
    Example Usage:
    - Sending a POST request with the necessary form data to initiate a PesaLink payment.
    """
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
          "requestedExecutionDate": "2024-08-09",
          "sendMoneyTo": "ACCOUNT.NUMBER",
          "dbsReferenceId": str(random.randrange(100000, 1000000)),
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
  """
    Handles Real-Time Gross Settlement (RTGS) payment processing via Stanbic Bank's API.

    This function processes a POST request to initiate an RTGS payment by sending a request 
    to the Stanbic Bank sandbox API. It collects payment details from the request, constructs 
    a payload, and makes an API call to the RTGS endpoint.

    Parameters:
    - request (HttpRequest): The HTTP request object, expected to be a POST request with the 
      following form data:
        - from_account: The originator's bank account number.
        - phone: The phone number of the originator.
        - to_account: The recipient's bank account number.
        - bank: The recipient's bank code.
        - amount: The amount to be transferred.
        - reason: The reason for the transfer.

    Returns:
    - JsonResponse: If the request method is POST, returns the JSON response from the Stanbic 
      Bank API.
    - HttpResponse: If the request method is not POST, renders the "rtgs_acccount_to_account.html" template.

    API Details:
    - Endpoint: https://api.connect.stanbicbank.co.ke/api/sandbox/rtgs-payments/
    - Authorization: Bearer token obtained from return_auth_token()
    - Payload:
        - originatorAccount: Contains the account and mobile number of the originator.
        - requestedExecutionDate: Static date set to "2024-08-09".
        - dbsReferenceId: Randomly generated 6-digit reference ID.
        - txnNarrative: Static value "TESEAPS123".
        - transferTransactionInformation: Contains details about the amount, counterparty 
          account, counterparty identity, and remittance information.

    Example Usage:
    - Sending a POST request with the necessary form data to initiate an RTGS payment.
  """
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
        "dbsReferenceId": str(random.randrange(100000, 1000000)),
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
  """
    Handles SWIFT payment processing via Stanbic Bank's API.

    This function processes a POST request to initiate a SWIFT payment by sending a request 
    to the Stanbic Bank sandbox API. It collects payment details from the request, constructs 
    a payload, and makes an API call to the SWIFT endpoint.

    Parameters:
    - request (HttpRequest): The HTTP request object, expected to be a POST request with the 
      following form data:
        - from_account: The originator's bank account number.
        - to_account: The recipient's bank account number.
        - phone: The phone number of the originator.
        - from_bank: The originator's bank code.
        - to_bank: The recipient's bank code.
        - amount: The amount to be transferred.
        - reason: The reason for the transfer.

    Returns:
    - JsonResponse: If the request method is POST, returns the JSON response from the Stanbic 
      Bank API.
    - HttpResponse: If the request method is not POST, renders the "swift_acccount_to_account.html" template.

    API Details:
    - Endpoint: https://api.connect.stanbicbank.co.ke/api/sandbox/swift-payments/
    - Authorization: Bearer token obtained from return_auth_token()
    - Payload:
        - originatorAccount: Contains the account and mobile number of the originator.
        - requestedExecutionDate: Static date set to "2024-08-09".
        - dbsReferenceId: Randomly generated 6-digit reference ID.
        - txnNarrative: Static value "TESEAPS123".
        - callBackUrl: Static callback URL "https://clientdomain.com/client/Callback".
        - schedule: Contains scheduling information such as transfer frequency and date range.
        - transferTransactionInformation: Contains details about the amount, counterparty 
          account, counterparty identity, and remittance information.

    Example Usage:
    - Sending a POST request with the necessary form data to initiate a SWIFT payment.
    """
  if request.method == "POST":
    access_token = return_auth_token()
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/swift-payments/"
    headers = {
      "Authorization": f"Bearer {access_token}",
      "content-type": "application/json",
      "accept": "application/json"
    }
    
    from_account = request.POST.get("from_account")
    to_account = request.POST.get("to_account")
    phone = request.POST.get("phone")
    from_bank = request.POST.get("from_bank")
    to_bank = request.POST.get("to_bank")
    amount = request.POST.get("amount")
    reason = request.POST.get("reason")
    payload = {
    "originatorAccount": {
      "identification": {
        "identification": from_account,
        "debitCurrency": "KES",
        "mobileNumber": phone
      }
    },
    "requestedExecutionDate": "2024-08-09",
    "dbsReferenceId": str(random.randrange(100000, 1000000)),
    "txnNarrative": "TESEAPS123",
    "callBackUrl": "https://clientdomain.com/client/Callback",
    "schedule": {
      "transferFrequency": "DAILY",
      "on": "12",
      "startDate": "2021-02-13",
      "endDate": "2022-01-03",
      "repeat": "3",
      "every": "1"
    },
    # 1220179020894 0100013845845
    "transferTransactionInformation": {
      "instructedAmount": {
        "amount": amount,
        "creditCurrency": "UGX"
      },
      "counterpartyAccount": {
        "identification": {
          "identification": to_account,
          "correspondentBank": from_bank,
          "beneficiaryBank": to_bank
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
          "type": reason,
          "content": reason
        },
        "endToEndIdentification": "5e1a3da132cc"
      }
    }

    response = requests.post(url=url,headers=headers,json=payload)
    # print("response "+response)
    # print(payload)
    return JsonResponse(response.json())
  else:
    return render( request,"api/swift_acccount_to_account.html")

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

