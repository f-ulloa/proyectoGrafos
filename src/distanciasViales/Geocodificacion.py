import requests

def obtener_latitud_longitud(direccion):
    # Reemplaza "TU_API_KEY" con tu clave API de Google Maps
    api_key = "TU_API_KEY"

    # Construir la URL de la solicitud
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={direccion}&key={api_key}"

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción en caso de error HTTP

        # Analizar la respuesta JSON
        data = response.json()

        # Obtener la ubicación (latitud y longitud) desde la respuesta JSON
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            latitud = location['lat']
            longitud = location['lng']

            return latitud, longitud
        else:
            print(f"No se pudo obtener la ubicación. Estado: {data['status']}")
            return None, None

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None, None

# Ejemplo de uso
direccion_ejemplo = "1600 Amphitheatre Parkway, Mountain View, CA"
latitud, longitud = obtener_latitud_longitud(direccion_ejemplo)

if latitud is not None and longitud is not None:
    print(f"Latitud: {latitud}")
    print(f"Longitud: {longitud}")
