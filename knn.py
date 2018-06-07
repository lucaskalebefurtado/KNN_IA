#coding: utf-8
# Lucas Kalebe Silva Furtado


import csv 
from math import sqrt

def training():
    dadosTreinamento = []
    with open ('treinamento.csv') as csvfile:
        reader =  csv.reader(csvfile)
        for row in reader:
            dadosTreinamento.append(row)
    return (dadosTreinamento)


def openTest():
    dadosTest = []
    with open ('teste.csv') as csvfile:
        reader =  csv.reader(csvfile)
        for row in reader:
            dadosTest.append(row)
    return (dadosTest)



def calculaDistancia(lista1, lista2):
    distancia = 0
    for i in range(4):
        distancia1 = float(lista1[i])
        distancia2 = float(lista2[i])

    distancia += ((distancia1 - distancia2) ** 2)
    return sqrt(distancia)
    

def classificador(casoTeste):
    treinamento = training()    
    menorDistancia = 100000000000    
    classificacao = "a"

    for i in range(len(treinamento)):
        if(i>0):
            distancia = calculaDistancia(casoTeste, treinamento[i])
            if(distancia < menorDistancia):
                menorDistancia = distancia
                classificacao = treinamento[i][4]
    return (classificacao)
        



def KNN():
    result = open('result.txt', 'w')
    teste = openTest()
    for i in range(len(teste)):
        if(i > 0):
            result.writelines(classificador(teste[i])+"\n")
    result.close()
        

def openBestResults():    
    f = open('rotulos-teste.txt', 'r')
    return (f.read().splitlines())
   
def openTrainedResults():    
    f = open('result.txt', 'r')
    return (f.read().splitlines())
   

def countMatches(results, bestResults):
    count = 0
    for i in range(len(results)):
        if(results[i] == bestResults[i]):
            count +=1

    return (str(int(count/len(results) * 100)) + "% de acertos")

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
