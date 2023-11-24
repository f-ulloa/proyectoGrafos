import requests

def obtener_distancia_entre_coordenadas(coordenadas_origen, coordenadas_destino):
    # Reemplaza "TU_API_KEY" con tu clave API de Google Maps
    api_key = "TU_API_KEY"

    # Construir la URL de la solicitud
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={coordenadas_origen}&destination={coordenadas_destino}&key={api_key}"

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción en caso de error HTTP

        # Analizar la respuesta JSON
        data = response.json()

        # Verificar si la solicitud fue exitosa
        if data['status'] == 'OK':
            # Obtener la distancia del camino más corto
            distancia_texto = data['routes'][0]['legs'][0]['distance']['text']
            return distancia_texto
        else:
            print(f"No se pudo obtener la distancia. Estado: {data['status']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None

# Ejemplo de uso
coordenadas_origen = "37.7749,-122.4194"  # Por ejemplo, San Francisco, CA
coordenadas_destino = "34.0522,-118.2437"  # Por ejemplo, Los Angeles, CA

distancia = obtener_distancia_entre_coordenadas(coordenadas_origen, coordenadas_destino)

if distancia is not None:
    print(f"Distancia: {distancia}")
