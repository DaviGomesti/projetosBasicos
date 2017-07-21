import requests
import json


cidadade = input("Digite o nome da sua cidade : ")
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidadade+'&appid=399f83925a8d5153592e4260d559794b')

tempo = json.loads(requisicao.text)

print('Condições do Tempo',tempo['weather'][0]['main'])
print('Temperatura de ',float(tempo['main']['temp']) - 273.15)