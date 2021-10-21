### PYTHON NATIVE DEPENDENCIES
import json

### DEPENDENCIES TO IMPORT ON THE GH WORKFLOW
import requests

### SCRIPT SAMPLE EXECUTED THROUGH GH WORKFLOW
print(f"💡 \033[36mScript example: Getting Mexico Covid-19 datas\033[0m")

try:
  response1 = requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=Mexico")

  country_datas = response1.json()

  cases = country_datas["All"]

  print("🤒🇷 Confirmed cases:", cases["confirmed"])
  print("🥳   Recovered cases:", cases["recovered"])
  print("😢🇷 Deaths:", cases["deaths"])

except:
   print("Couldn't extract Mexico cases datas") 

try:    
  response2 = requests.get("https://covid-api.mmediagroup.fr/v1/vaccines?country=Mexico")

  vaccines_datas = response2.json()

  vaccines = vaccines_datas["All"]

  print("📦  Vaccines quantity:", vaccines["administered"])
  print("💉  Vaccinated people:", vaccines["people_vaccinated"])

except:
  print("Couldn't extract Mexico vaccines datas") 
  
