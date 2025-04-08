import time 
import random
import requests
import sys

user_agents = list()
emails = list()
password = list()

# base_url is the target phish page
base_url = "http://***login.php"

with open("useragents.txt", "rb") as useragents_file:
  for useragent in useragents_file:
    user_agents.append(useragent.strip())

with open("emails.txt", "rb") as emails_file:
  for email in emails_file:
    emails.append(email.strip())

with open("pwd.txt", "rb") as pwds_file:
  for pwd in pwds_file:
    password.append(pwd.strip())


while True:
  wait = random.uniform(0, 29)
  print "\nSleep:", wait
  
  time.sleep(wait)

  headers = {"User-Agent":random.choice(user_agents),
             'X-Forwarded-For':'54.39.215.1',
             "Content-Type": "application/x-www-form-urlencoded"
            }
  
  data = "UserName="+random.choice(emails)+"&Password="+random.choice(password)+"&AuthMethod=FormsAuthentication"
  response = requests.post(base_url,headers=headers, data=data)
  print response.text
  
  time.sleep(random.uniform(0, 11))

  token = ""
  for i in range(0,6): token += str(random.randint(0,9))

  data = "UserName="+token+"&AuthMethod=FormsAuthentication"
  response = requests.post(base_url,headers=headers, data=data)

  print response.text

  # sys.exit()
