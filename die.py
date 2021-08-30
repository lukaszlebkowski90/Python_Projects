from random import randint
from plotly.graph_objs import Layout, Bar
from plotly import offline

class Die():
    """Klasa przedstawiająca pojedynczą kość do gry"""

    def __init__(self, num_sides=6):
        """Przyjęcie założenia, że kość do gry ma postać sześcianu"""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartości z zakresu od 1 do liczby ścianek, którą ma kośc do gry"""
        return randint(1, self.num_sides)

#Utworzenie kości typu D6
die = Die()

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analiza wyników
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Wizualizacja wyników
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania pojedynczą kością D6 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
