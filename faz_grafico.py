from matplotlib import pyplot

def faz_grafico(lista_numeros):
    fig1, ax1 = pyplot.subplots()
    ax1.boxplot(lista_numeros)
    pyplot.show()