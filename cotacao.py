#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
Programa: Calcula o binômio de Newton
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 06 de março de 2017
"""

import requests
import json
import time


def cotacao():
    try:
        req = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
        return json.loads(req.text)
    except Exception as err:
        print("Houve o seguinte erro na conexão:", err)


def chama_cotacao():
    dicionario = cotacao()
    for i in dicionario["valores"]:
        print("Moeda:", dicionario['valores'][i]['nome'], "\nValor: R$ %5.2f" % dicionario['valores'][i]['valor'],
              "\nHorário e data da Cotação:",
              time.strftime("%Hh.%Mmin. de %d/%b/%Y", time.localtime(dicionario["valores"][i]["ultima_consulta"])), "\n")


# Testa o programa
chama_cotacao()
