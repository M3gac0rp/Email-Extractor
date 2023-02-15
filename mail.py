import re
import requests
from bs4 import BeautifulSoup
import json

def extract_all_emails_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = []
    for tag in soup.find_all(text=email_regex):
        emails += re.findall(email_regex, tag)
    return emails


#uncomment and put a url
#url = "url"
emails = extract_all_emails_from_webpage(url)
if emails:
    print("Adresses email trouvées :")
    for email in emails:
        print(" -", email)
else:
    print("Aucune adresse email trouvée")

with open('emails.txt', 'a') as email_file:
    for email in emails:
        if 'wixpress.com' not in email:
            email_file.write(email + '\n')

