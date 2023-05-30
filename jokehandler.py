import requests

#import datetime

#https://foolishdeveloper.com/random-joke-generator-using-javascript-api/
#https://v2.jokeapi.dev/#url-parameters

#Hämtar giltiga personnummer frå skatteverket 
#Anväder Thunder client för att testa request
#pip install requests
#python.exe -m pip install --upgrade pip

class Jokehandler:

    def __init__(self, adress):
        self.adress = adress
        #nu = datetime.datetime.now()
        #print("Konstruktor körs tid:" + nu)

    def get_joke(self):
        
        #req = requests.get(self.adress)
        req = requests.get("https://v2.jokeapi.dev/joke/Any?type=singl")
        json_data = req.json()
        joke = json_data['joke']
        
        return joke


    