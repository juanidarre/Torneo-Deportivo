-Proyecto: Análisis Estadístico de la Liga Argentina

-Integrantes del Equipo
* Integrante 1 (Luis - P3)
* Integrante 2 (Paco - P2)
* Integrante 3 (Hugo - P1)

-Escenario Elegido
**Escenario D:** Estadísticas de Resultados Deportivos. El objetivo es procesar los resultados de los partidos para generar indicadores de rendimiento y tablas de posiciones [5, 6].

-Descripción del Dataset:
Se utiliza el archivo `datos/Book(Liga Argentina).csv`, el cual contiene registros de partidos con las siguientes columnas:
* `Fecha`: Día del encuentro.
* `Equipo local` / `Equipo visitante`: Equipos enfrentados.
* `Goles local` / `Goles visitante`: Marcadores del partido.

-Estructura del Repositorio:
Siguiendo los mandatos de gobernanza, el repositorio se organiza de la siguiente manera:
* `/datos`: Archivo CSV con los datos crudos.
* `/scripts`: Código en Python para el procesamiento.
* `/resultados`: Productos generados (Gráfico de victorias y Tabla de posiciones CSV).

-Instrucciones de Ejecución
Para reproducir el análisis en este entorno de Google Colab, ejecute el siguiente comando:

```python
!python scripts/analisis_deportivo.py
