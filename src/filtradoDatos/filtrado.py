import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import datetime


def guardar_excel(df, nombre_archivo):
    wb = Workbook()
    ws = wb.active
    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 20

    wb.save(nombre_archivo)


def convertir_hora(hora):
    try:
        return pd.to_datetime(hora, format='%H:%M:%S').time()
    except ValueError:
        return None


archivo_xls = '__RESUMEN DE SERVICIOS - 2022.xlsx'
df = pd.read_excel(archivo_xls, header=3)

df['FECHA'] = pd.to_datetime(df['FECHA']).dt.date
df['HORA'] = df['HORA'].apply(convertir_hora)

columnas_a_mostrar = ['FECHA', 'HORA', 'ORIGEN', 'DESTINO']

df_filtrado = df.dropna(subset=columnas_a_mostrar)

horario_punta = df_filtrado[df_filtrado['HORA'].between(datetime.time(6, 0), datetime.time(8, 0)) |
                            df_filtrado['HORA'].between(datetime.time(19, 0), datetime.time(23, 0))]

horario_bajo = df_filtrado[~df_filtrado['HORA'].between(datetime.time(6, 0), datetime.time(8, 0)) &
                           ~df_filtrado['HORA'].between(datetime.time(19, 0), datetime.time(23, 0))]

guardar_excel(horario_punta[columnas_a_mostrar], 'viajes_horario_punta.xlsx')
guardar_excel(horario_bajo[columnas_a_mostrar], 'viajes_horario_bajo.xlsx')

print(f"Filas en el archivo Excel original: {len(df)}")
print(f"Filas en el archivo Excel de horario punta: {len(horario_punta)}")
print(f"Filas en el archivo Excel de horario bajo: {len(horario_bajo)}")
print(
    f"Filas filtradas (no incluidas en horario punta o bajo): {len(df) - len(horario_punta) - len(horario_bajo)}")
