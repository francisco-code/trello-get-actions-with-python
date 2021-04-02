#######################################################################################################################







#Rascunho 2


"""
Script do Dashboard

-Os dados são extraídos do 'Trello', monitorados/carregados no 'Prometheus' e
exibidos no 'Grafana'.

"""


#---------------------BIBLIOTECAS--------------------

import requests
import json
from trello.trelloclient import TrelloClient
import trello
#from trello import TrelloApi
from trello import TrelloClient
from trello import Card
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import random
from prometheus_client import start_http_server, Summary
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import datetime
from tkinter import*



#----------------------------------------------------







#print("Passou por aqui 1!")
print()
print()





#------------------CHAVE DE AUTORIZAÇÃO DA api DO TRELLO--------------------

client = TrelloClient(
    api_key='insira a sua chave',
    api_secret='insira o seu'
)

#---------------------------------------------------------------------------






#print("Passou por aqui 2!")
print()
print()







#----------------------------OBTENDO AS BOARDS, LISTAS, CARDS E AÇÕES--------------------------------------

#Todas as boards que existem na minha chave
print()
all_boards = client.list_boards()     #Lista com todas as minhas boards


print("****************************************************************")
my_board = all_boards[0]       #Posições do vetor boards (essa posição corresponde à board 'Demanda Time AE')
print("NOME DA NOSSA BOARD DE TRABALHO: ", my_board)
#Todas as listas (vendedores) que existem na minha board 
all_lists = my_board.list_lists()
print()
print("QUANTIDADE DE LISTAS (COLUNAS) DA BOARD INTEIRA: ", len(all_lists))
print("****************************************************************")
print()
print()
print()

#-----------------------------------------------------------------------------------------------------------




#print("Passou por aqui 3!")
print()
print()













#----------------------------MAIN PROG--------------------------------------

for i in range(16):
    print()
    print()
    print()
    print()
    print("#################################################################################################")
    colunas = all_lists[i]        #Posições do vetor listas
    print("COLUNA DO: ", colunas)
    print()
    all_cards = all_lists[i].list_cards()       #Todos os cartões do vendedor da posição 2 do vetor listas
    #my_lists = all_cards[5]       #Posições do vetor cards  
    #print("Quantidade de cartões em ", my_lists, ": ", len(all_cards))
    print("QUANTIDADE DE CARTÕES: ", len(all_cards))
    print()
    print()
    print()
    print("********** CARTÕES: **********")
    print()  
    
    for j in range(len(all_cards)):
        #Ações de todos os cards
        all_action = all_cards[j].fetch_actions() 
        #my_action = all_action
    
        print()
        print("AÇÕES DO CARTÃO ", all_cards[j], ": \n", json.dumps(all_action))
        print()
        print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

#---------------------------------------------------------------------------



"""
sns.set(style="ticks", color_codes=True)
g = sns.countplot(x="idList", data=df)
g.set_title(“Cartoes por coluna”)
g.set_xlabel(‘Colunas’)
g.set_ylabel(‘Número de cartoes’)
"""







print("OK. O PROGRAMA RODOU ATÉ O FIM!!!")
print()
print()
print()
print()




"""
url = "https://api.trello.com/1/boards/id_board/actions"

querystring = {"fields":"all","key":"","token":""}

response = requests.request("GET", url, params=querystring)

print(response.text)
"""


