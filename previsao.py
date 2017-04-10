"""
Programa: Traz a previso do tempo para a cidade informada
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 06 de março de 2017
"""

import requests
import json
import time
import urllib.parse


def previsao(cidade):
    cidade_parse = urllib.parse.quote(cidade, safe="")
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + cidade_parse + "&APPID=80e3d2fe9f1f309908cf02df5a61d65a&lang=pt&units=metric"
        tempo = requests.get(url)
        return json.loads(tempo.text)
    except Exception as err:
        print("Houve o seguinte erro na conexão:", err)
        exit()


def chama_previsao():
    print("Previsão do Tempo\n")
    cidade = input("Entre com a cidade: ")
    dicionario = previsao(cidade)
    print("Cidade:", dicionario["name"])
    print("Dia da previsão:", time.strftime("%d/%b/%Y", time.localtime(dicionario["dt"])))
    print("Alvorecer:", time.strftime("%Hh.%Mmin.",time.localtime(dicionario["sys"]["sunrise"])))
    print("Entardecer:", time.strftime("%Hh.%Mmin.",time.localtime(dicionario["sys"]["sunset"])))
    print("Temperatura Atual é de %2.1fºC" % dicionario["main"]["temp"])
    try:
        chuva = dicionario["rain"]["3h"] * 25.4
        print("Intensidade da Chuva no momento: %3.2fmm" % chuva)
    except:
        print("Intensidade da Chuva no momento: 0.0mm")
    print("Clima Atual:", str.capitalize(dicionario["weather"][0]["description"]))
    print("Humidade Relativa:", str(dicionario["main"]["humidity"]) + "%")
    print("Pressão Atmosférica:", str(dicionario["main"]["pressure"]), "hpa")

# Testa o programa
chama_previsao()
