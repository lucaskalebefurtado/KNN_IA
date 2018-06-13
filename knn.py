#coding: utf-8
# Lucas Kalebe Silva Furtado
from collections import Counter
import csv 
from math import sqrt

# abrir casos de treinamento
def training():
    dadosTreinamento = []
    with open ('treinamento.csv') as csvfile:
        reader =  csv.reader(csvfile)
        for row in reader:
            dadosTreinamento.append(row)
    return (dadosTreinamento)

#abrir casos de teste
def openTest():
    dadosTest = []
    with open ('teste.csv') as csvfile:
        reader =  csv.reader(csvfile)
        for row in reader:
            dadosTest.append(row)
    return (dadosTest)


#calcular a distancia entre dois pontos
def calculaDistancia(lista1, lista2):
    distancia = 0
    for i in range(4):   
        distancia1 = float(lista1[i])
        distancia2 = float(lista2[i])
        distancia += ((distancia1 - distancia2) ** 2)
    return sqrt(distancia)


def classificador(casoTeste, k):
    treinamento = training()    #abre o caso de treinamento
    distancias = []             #armazena as distancias
    for i in range(len(treinamento)):        
        if(i > 0): #linha da explicacao
            distancia = calculaDistancia(casoTeste, treinamento[i]) #calcula a distancia entre os pontos
            distancias.append((distancia, treinamento[i][4])) #adiciona na lista a tupla
    distancias.sort(key=lambda tup: tup[0])  #organiza de acordo com as menores distancias
    
    classificacoes = [] # lista apenas com as classificacoes
    for i in range(k):
        classificacoes.append(distancias[i][1]) #adiciona a lista apenas as k melhores classificacoes
    
    cnt = Counter(classificacoes)
    a = (cnt.most_common()) #conta o valor mais comum da lista
    return (a[0][0]) # retorna a classificacao mais comum da lista


def KNN():
    result = open('result.txt', 'w') # escreve os resultados
    teste = openTest()
    k = int(input("Tamanho do K: ")) #tamanho do K a ser utilizado
    for i in range(len(teste)): 
        if(i > 0):
            result.writelines(classificador(teste[i], k)+"\n")
    result.close()
        

def openBestResults():    
    f = open('rotulos-teste.txt', 'r')
    return (f.read().splitlines())
   
def openTrainedResults():    
    f = open('result.txt', 'r')
    return (f.read().splitlines())
   

def countMatches(results, bestResults):
    count = 0.0
    for i in range(len(results)):
        if(results[i] == bestResults[i]):
            count +=1
    return (str(count/len(results) * 100) + "% de acertos")

# Executar o KNN
KNN()

# Abre o arquivo com os resultados do treino
results = openTrainedResults()

#Abre o arquivo com os resultados corretos
bestResults = openBestResults()

#Calcula a taxa de acertos do algoritmo
acertos = countMatches(results, bestResults)

#Imprime a taxa de acertos do algoritmo
print (acertos)
