import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define a range para as variáveis de entrada
bedrooms = ctrl.Antecedent(np.arange(0, 11, 1), 'bedrooms')
area = ctrl.Antecedent(np.arange(0, 801, 1), 'area') # m²
location = ctrl.Antecedent(np.arange(0, 11, 1), 'location')
population = ctrl.Antecedent(np.arange(0, 10001, 1), 'population') # 1k

# Define a range para a variável de saída
price = ctrl.Consequent(np.arange(25_000, 4_000_000, 1), 'price')

# Cria os conjuntos fuzzy utilizando curvas gaussianas
# Conjuntos Fuzzy para a variável "bedrooms"
bedrooms['low'] = fuzz.gaussmf(bedrooms.universe, 1, 1) # 0.5
bedrooms['medium'] = fuzz.gaussmf(bedrooms.universe, 3, 1) # 1.5
bedrooms['high'] = fuzz.gaussmf(bedrooms.universe, 8, 1.5) # 2

# Conjuntos Fuzzy para a variável "area"
area['low'] = fuzz.gaussmf(area.universe, 0, 35) # 1
area['medium'] = fuzz.gaussmf(area.universe, 175, 45) # 2
area['high'] = fuzz.gaussmf(area.universe, 800, 200) # 3

# Conjuntos Fuzzy para a variável "location"
location['faraway'] = fuzz.gaussmf(location.universe, 2, 1) # 0
location['medium']  = fuzz.gaussmf(location.universe, 5, 1) # 1
location['nearby']  = fuzz.gaussmf(location.universe, 8, 1) # 2

# Conjuntos Fuzzy para a variável "population"
population['low'] = fuzz.gaussmf(population.universe, 0, 50) # 0.5
population['medium'] = fuzz.gaussmf(population.universe, 240, 75) # 1
population['high'] = fuzz.gaussmf(population.universe, 900, 230) # 2
population['very high'] = fuzz.gaussmf(population.universe, 10_000, 2_750) # 3

# Conjuntos Fuzzy para a variável de saída "price"
sigma_price = 50000
price['cheap'] = fuzz.gaussmf(price.universe, 0, sigma_price)
price['low'] = fuzz.gaussmf(price.universe, 120_000, sigma_price)
price['medium'] = fuzz.gaussmf(price.universe, 250_000, sigma_price)
price['high'] = fuzz.gaussmf(price.universe, 500_000, sigma_price * 3)
price['expensive'] = fuzz.gaussmf(price.universe, 4_000_000, sigma_price * 20)


rules = [
   ctrl.Rule(bedrooms["low"] & area["low"] & location["faraway"] & population["low"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["faraway"] & population["medium"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["faraway"] & population["high"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["faraway"] & population["very high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["medium"] & population["low"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["medium"] & population["medium"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["medium"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["medium"] & population["very high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["nearby"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["nearby"] & population["medium"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["nearby"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["low"] & location["nearby"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["faraway"] & population["low"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["faraway"] & population["medium"], price["cheap"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["faraway"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["faraway"] & population["very high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["medium"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["medium"] & population["medium"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["medium"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["medium"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["nearby"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["nearby"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["nearby"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["medium"] & location["nearby"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["faraway"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["faraway"] & population["medium"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["faraway"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["faraway"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["medium"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["medium"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["medium"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["medium"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["nearby"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["nearby"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["nearby"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["low"] & area["high"] & location["nearby"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["faraway"] & population["low"], price["cheap"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["faraway"] & population["medium"], price["cheap"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["faraway"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["faraway"] & population["very high"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["medium"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["medium"] & population["medium"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["medium"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["medium"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["nearby"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["nearby"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["nearby"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["low"] & location["nearby"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["faraway"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["faraway"] & population["medium"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["faraway"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["faraway"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["medium"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["medium"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["medium"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["medium"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["nearby"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["nearby"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["nearby"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["medium"] & location["nearby"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["faraway"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["faraway"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["faraway"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["faraway"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["medium"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["medium"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["medium"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["medium"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["nearby"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["nearby"] & population["medium"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["nearby"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["medium"] & area["high"] & location["nearby"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["faraway"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["faraway"] & population["medium"], price["low"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["faraway"] & population["high"], price["low"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["faraway"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["medium"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["medium"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["medium"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["medium"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["nearby"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["nearby"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["nearby"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["low"] & location["nearby"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["faraway"] & population["low"], price["low"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["faraway"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["faraway"] & population["high"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["faraway"] & population["very high"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["medium"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["medium"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["medium"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["medium"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["nearby"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["nearby"] & population["medium"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["nearby"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["medium"] & location["nearby"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["faraway"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["faraway"] & population["medium"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["faraway"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["faraway"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["medium"] & population["low"], price["medium"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["medium"] & population["medium"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["medium"] & population["high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["medium"] & population["very high"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["nearby"] & population["low"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["nearby"] & population["medium"], price["high"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["nearby"] & population["high"], price["expensive"]),
   ctrl.Rule(bedrooms["high"] & area["high"] & location["nearby"] & population["very high"], price["expensive"])
]


# Prepara o código para simular as entradas
pricing_ctrl = ctrl.ControlSystem(rules)
pricing = ctrl.ControlSystemSimulation(pricing_ctrl)

# Recebe as entradas pelo terminal e insere no sistema Fuzzy
pricing.inputs({
   'bedrooms' : int(input("bedrooms [0-10]: ")),
   'area': int(input("area [0-1000]: ")),
   'location': int(input("location [0-10]: ")),
   'population': int(input("population [0-10000]k: "))
})

# Computa a saída, mostra o preço e o gráfico do centroide
pricing.compute()
print(pricing.output['price'])
price.view(sim=pricing)
plt.show()
