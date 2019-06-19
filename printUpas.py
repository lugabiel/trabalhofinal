import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    dadoGrafico = open('upas2.txt','r').read()
    linhas = dadoGrafico.split('\n')
    xs = []
    ys = []
    for linha in linhas:
        if len(linha) > 1:
            x, y = linha.split(' ')
            xs.append(int(x))
            ys.append(int(y))
    ax1.clear()
    ax1.scatter(xs,ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
