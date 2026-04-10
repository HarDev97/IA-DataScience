import matplotlib.pyplot as plt


def generar_grafico():

    labels = ['A', 'B', 'C', 'D', 'E']
    values = [10, 15, 7, 12, 20]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('grafico.png')
    plt.close()
