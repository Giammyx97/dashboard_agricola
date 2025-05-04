import numpy as np
import pandas as pd
import random

# Imposta il numero di giorni da simulare
days = 30

# Generazione dei dati ambientali
temperature = np.random.normal(loc=25, scale=5, size=days)  # Temperatura media con variazione
humidity = np.random.uniform(low=40, high=90, size=days)    # Umidità tra 40% e 90%
precipitations = np.random.choice(
    [0, 5, 10, 15, 20, 25],
    size=days,
    p=[0.5, 0.2, 0.15, 0.1, 0.04, 0.01]
)  # Probabilità di pioggia

# Generazione dei dati di produzione agricola
crop_yield = np.maximum(0, np.random.normal(loc=500, scale=100, size=days))  # Produzione in kg
growth_time = np.random.randint(low=60, high=120, size=days)  # Giorni di crescita

# Dati finanziari
prezzo_kg = np.random.uniform(0.8, 1.2, size=days)  # Prezzo al kg in €
costo_totale = np.random.uniform(300, 400, size=days)  # Costo giornaliero in €
valore_produzione = crop_yield * prezzo_kg
profitto = valore_produzione - costo_totale

# Calcolo efficienza (%)
efficiency = np.clip(
    100 - np.abs(temperature - 25) * 2 - humidity * 0.1 - precipitations,
    30,
    100
)

# Creazione del DataFrame
data = pd.DataFrame({
    'Giorno': range(1, days + 1),
    'Temperatura (°C)': np.round(temperature, 2),
    'Umidità (%)': np.round(humidity, 2),
    'Precipitazioni (mm)': precipitations,
    'Raccolto (kg)': np.round(crop_yield, 2),
    'Tempo di crescita (giorni)': growth_time,
    'Efficienza (%)': np.round(efficiency, 2),
    'Valore produzione (€)': np.round(valore_produzione, 2),
    'Costi totali (€)': np.round(costo_totale, 2),
    'Profitto (€)': np.round(profitto, 2)
})

# Salvataggio su file CSV
data.to_csv("dati_simulati.csv", index=False)

# Stampa dei primi cinque dati per la verifica
print(data.head())
