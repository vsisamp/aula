from tkinter import filedialog, Tk
def pede_arquivo():
    root = Tk()
    root.withdraw()
    txtludopedia = filedialog.askopenfilename()
    return txtludopedia

def abretexto(txtludopedia):
    lista_ludo = []
    with open(txtludopedia, 'r') as jogos:
        for linha in jogos:
          #  lista_ludo.append(linha.strip()) #adiciona as linhas numa lista #strip tira o espaço antes e depois
            if 'nome-produto' in linha:
                linha = linha.split('<')[1] #\t\t\t\<h4 class="nome-produto">Barcos para Puerto Rico (5 unidades) - Bucaneiros</h4><span>A partir de</span><br>
                linha = linha.split('>')[1]
                lista_ludo.append(linha)
                print(linha) 
        #print(lista_ludo)
    return lista_ludo

def salva_txt(lista_ludo):
    with open('jogosludo.txt', 'w', encoding='utf-8') as saindo:
        texto = '\n'.join(lista_ludo)
        saindo.write(texto)
        
a = pede_arquivo()
lista_dados = abretexto(a)
salva_txt(lista_dados)