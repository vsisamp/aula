'''esse programa vai abrir uma planilha, ler a primeira coluna e salvar a media, mediana e numero de linhas em um arquivo txt'''

from tkinter import filedialog, Tk
from faz_grafico import faz_grafico
def pede_arquivo():
    root = Tk()
    root.withdraw()
    nome_arquivo = filedialog.askopenfilename()
    return nome_arquivo
def abre_arquivo(nome_arquivo):
    '''retorna lista com as linhas do arquivo'''
    lista_linhas = []
    with open(nome_arquivo, 'r') as planilha:
        for linha in planilha:
            lista_linhas.append(linha.strip()) #adiciona as linhas numa lista #strip tira o espaço antes e depois
    return lista_linhas

def converte_lista_numeros(lista_linhas):
    '''recebe um alista de palavras e retornar um alista de numeros'''
    lista_numeros = []
    for linha in lista_linhas:
        a = linha.split('\t')
        if len(a) > 4:
            preço_tabela = a[4]
            preço_tabela = preço_tabela.replace(',', '.')
            preço_tabela = preço_tabela.replace('$','')
            #print(preço_tabela)
            preço_tabela = float(preço_tabela)
            lista_numeros.append(preço_tabela)
    return lista_numeros

def analise_dados(lista_numeros):
    '''recebe uma lista de numeros e retorna um tupla (media, mediana, quantidade de linhas)'''
    soma = sum(lista_numeros)
    tamanho = len(lista_numeros)
    media =soma/tamanho
    if not tamanho % 2 == 0:
        indice = int((tamanho -1)/2)
        mediana = lista_numeros[indcie]
    else:
        mediana = (lista_numeros[int(tamanho/2)] + lista_numeros[int(tamanho/2) - 1])/2
    return media, mediana, tamanho
def salva_resultado(media, mediana, tamanho):
    '''recebe os reesultados e salva num arquivo'''
    with open('texton.txt', 'w') as saindo:
        saindo.write(str(media) + ' ' + str(mediana) + ' ' + str(tamanho))
        

def main():
    '''logica principal do programa, chama todas as funções'''
    nome_arquivo = pede_arquivo()
    lista_linhas = abre_arquivo(nome_arquivo)
    lista_numeros = converte_lista_numeros(lista_linhas)
    media, mediana, tamanho = analise_dados(lista_numeros)
    salva_resultado(media, mediana, tamanho)
    faz_grafico(lista_numeros)
    
    
    
main()
