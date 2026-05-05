import pandas as pd
import matplotlib.pyplot as plt

file_path = 'datos/Book(Liga Argentina).csv'

try:
    df = pd.read_csv(file_path, encoding='latin-1', sep=None, engine='python')
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Equipo local', 'Equipo visitante'], how='any')
    print(f"Archivo '{file_path}' cargado y limpiado exitosamente.")
except Exception as e:
    print(f"Error fatal: {e}")
    exit()

c_local, c_visitante = 'Equipo local', 'Equipo visitante'
g_local, g_visitante = 'Goles local', 'Goles visitante'

ganadores = []
for _, row in df.iterrows():
    if row[g_local] > row[g_visitante]:
        ganadores.append(row[c_local])
    elif row[g_visitante] > row[g_local]:
        ganadores.append(row[c_visitante])

victorias = pd.Series(ganadores).value_counts()

posiciones = {equipo: 0 for equipo in pd.concat([df[c_local], df[c_visitante]]).unique()}
for _, row in df.iterrows():
    if row[g_local] > row[g_visitante]:
        posiciones[row[c_local]] += 3
    elif row[g_visitante] > row[g_local]:
        posiciones[row[c_visitante]] += 3
    else:
        posiciones[row[c_local]] += 1
        posiciones[row[c_visitante]] += 1

tabla_posiciones = pd.Series(posiciones).sort_values(ascending=False)

print("\nTabla de Posiciones Real:\n", tabla_posiciones)

plt.figure(figsize=(10,6))
victorias.plot(kind='bar', color='skyblue', edgecolor='navy')
plt.title('Victorias por Equipo - Liga Argentina')
plt.savefig('resultados/grafico_rendimiento.png')
tabla_posiciones.to_csv('resultados/tabla_posiciones.csv')

print("\nAnálisis finalizado. Los productos se guardaron en la carpeta /resultados.")
