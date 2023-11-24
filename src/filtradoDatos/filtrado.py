import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

archivo_xls = '__RESUMEN DE SERVICIOS - 2022.xlsx'

df = pd.read_excel(archivo_xls, header=3)
df_filtrado = df[df['FECHA'].notna() & df['HORA'].notna(
) & df['ORIGEN'].notna() & df['DESTINO'].notna()].copy()
df_filtrado.loc[:, 'FECHA'] = pd.to_datetime(df_filtrado['FECHA']).dt.date

columnas_a_mostrar = ['FECHA', 'HORA', 'ORIGEN', 'DESTINO']
df_filtrado = df_filtrado[columnas_a_mostrar]

wb = Workbook()
ws = wb.active

for r in dataframe_to_rows(df_filtrado, index=False, header=True):
    ws.append(r)

ws.column_dimensions['A'].width = 15
ws.column_dimensions['C'].width = 30
ws.column_dimensions['D'].width = 30

wb.save('viajes_filtrados.xlsx')
