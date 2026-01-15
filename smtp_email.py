import requests
from os import environ

url = "https://smtpapi.mxroute.com/"

def send_smtp_email(to_email, name, code):

    smtp_pass = environ.get("SMTP_PASSWORD")

    body = f"""<p>Thanks for verifying {name}!</p>
    <p>Go back to where you entered the verification command and enter the command /code.</p>
    <p>Then paste the following code: {code}</p>"""
    
    payload = {
        "server": "wednesday.mxrouting.net",
        "username": "verify@ucrcyber.org",
        "password": smtp_pass,
        "from": "verify@ucrcyber.org",
        "to": to_email,
        "subject": "UCR Clubs Email Verification",
        "body": body,
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()  # raises if non-2xx
    print(response.text)
