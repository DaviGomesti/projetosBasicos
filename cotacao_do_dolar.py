import json
import requests
import time
import datetime


while True:
    requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

    cotacao = json.loads(requisicao.text)



    print('#### Cotação ####', datetime.datetime.now())
    print('Dólar: ', cotacao['valores']['USD']['valor'])
    print('Euro: ', cotacao['valores']['EUR']['valor'])
    print('Btc: ',cotacao['valores']['BTC']['valor'])
    time.sleep(2)