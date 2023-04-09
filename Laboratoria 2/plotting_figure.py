"""Zadanie z kreślenia wykresów."""
import math
import matplotlib.pyplot as plt
import numpy as np

# chcemy zapisać dwa wykresy ułożone w jednym wierszu i dwóh kolumnach
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))


# wykers pierwszy
# x to dziedzina: 50 próbek z zakresu [-3, 3] wygenerowanych liniowo
# y to exp(-x^2)
# y_err to szum pochodzący z rozkładu normalnego o zadanych parametrach
## TODO
x = np.linspace(-3,3,50)
#y = math.e**(-x**2)
y = np.exp(-x**2)
y_err = np.random.normal(loc=np.mean(y), scale=0.1, size=len(y))


# plotujemy x, y oraz obszar szumu wokół funkcji
## TODO
ax[0].plot(x,y, label="exp(-x^2)", marker="o")
ax[0].fill_between(x, y - y_err, y + y_err, alpha=0.2, label="+/- szum")

# dodajemy oznaczenia osi i legendę na górze po lewej stronie
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[0].legend(loc="upper left")


# wykres drugi
# definiujemy dziedzinę (x) oraz funkcje do wykreślenia (y_1, y_2)
x = np.arange(start=-50.0, stop=50.0, step=0.1)
y_1 = np.cos(x / 3.0)
y_2 = np.sin(x)

# kreślimy obie funkcje
## TODO
ax[1].plot(x, y_1, label="cos(x/3)")
ax[1].plot(x, y_2, label="sin(x)")

# ustawiamy skalę osi x na symetryczną-logarytmiczną oraz dodajemy siatkę w
# tle kreślonych krzywych
## TODO
ax[1].set_xscale("symlog")
ax[1].set_axisbelow(True)
ax[1].yaxis.grid(color='gray', linestyle='solid')
ax[1].xaxis.grid(color='gray', linestyle='solid')


# dodajemy oznaczenia osi i legendę na dole po prawej stronie
ax[1].set_xlabel("x")
ax[1].set_ylabel("Y")
## TODO 
ax[1].legend(loc="lower right")

# dodajemy tytuł "Funkcje wygenerowane w 'numpy' i wykreślone w 'matplotlib'" i zapisujemy jako 'moj_wykres.png'
## TODO

fig.suptitle("Funkcje wygenerowane w numpy i wykreślone w matplotlib")
plt.savefig("moj_wykres.png")

#plt.show()
