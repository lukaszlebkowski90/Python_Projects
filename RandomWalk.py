from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """Klasa przeznaczona do wygenerowania błądzenia losowego"""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutów błądzenia"""
        self.num_points = num_points

        #Punkt początkowy ma współrzędne (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów dla błądzenia losowego"""

        #Wykonywania wszystkich kroków aż do chwili osiągnięcia oczekiwanej liczby punktów.
        while len(self.x_values) < self.num_points:

            #Ustalenie kierunku oraz odległości do pokonania w tym kierunku
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            #Odrzucenie ruchów, które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue

            #Ustalenie następnych wartości X i Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

#Przygotowanie danych błądzenia losowego i wyświetlenie punktów
rw = RandomWalk(50_000)
rw.fill_walk()

#Wyświetlenie punktów błądzenia losowego
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(8,5), dpi=128)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
#Podkreślenie pierwzego i ostatniego punktu błądzenia losowego
ax.scatter(0, 0, c='green', edgecolor='none', s=10)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=10)
#Ukrycie osi
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
#Wyświetlenie wykresu na ekranie
plt.show()

