import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


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
    print(f"Viajes en {nombre_archivo}: {len(df)}")
    return len(df)


def convertir_hora(hora):
    try:
        hora_convertida = pd.to_datetime(hora, format='%H:%M:%S').time()
        return hora_convertida.strftime('%H:%M')
    except ValueError:
        return None


archivo_xls = '__RESUMEN DE SERVICIOS - 2022.xlsx'
df = pd.read_excel(archivo_xls, header=3)

df['FECHA'] = pd.to_datetime(df['FECHA'])
df['Mes'] = df['FECHA'].dt.month
df['HORA'] = df['HORA'].apply(convertir_hora)

columnas_a_mostrar = ['FECHA', 'HORA', 'ORIGEN', 'DESTINO']

# Filtrar solo los meses seleccionados: septiembre, enero, marzo, febrero y diciembre
meses_seleccionados = [1, 2, 3, 9, 12]
df_filtrado = df[df['Mes'].isin(meses_seleccionados)].copy()
df_filtrado.loc[:, 'FECHA'] = df_filtrado['FECHA'].dt.strftime('%d-%m-%Y')

horario_punta = df_filtrado[df_filtrado['HORA'].between(
    '06:00', '08:00') | df_filtrado['HORA'].between('19:00', '23:00')]
horario_bajo = df_filtrado[~df_filtrado['HORA'].between(
    '06:00', '08:00') & ~df_filtrado['HORA'].between('19:00', '23:00')]

total_viajes = len(df)
print(f"Viajes en el archivo Excel original: {total_viajes}")


viajes_punta = guardar_excel(
    horario_punta[columnas_a_mostrar], 'horario_punta.xlsx')
viajes_bajo = guardar_excel(
    horario_bajo[columnas_a_mostrar], 'horario_bajo.xlsx')

viajes_filtrados = total_viajes - (viajes_punta + viajes_bajo)
print(f"Viajes eliminados: {viajes_filtrados}")
