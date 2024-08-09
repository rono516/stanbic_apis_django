
# Stanbic APIS with django

These APIs cover Pesalink, RTGS and SWIFT payments with Django

Pesalink API
http://127.0.0.1:8000/api/pesalink

RTGS API
http://127.0.0.1:8000/api/rtgs

SWIFT API
http://127.0.0.1:8000/api/swift_payment

# Pesalink API
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

# RTGS API
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
    


