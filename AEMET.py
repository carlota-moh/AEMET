import requests

def extract_data(url, api_key):
    """
    Function used for extracting data from API

    Params
    - url: string
        Desired url from which to extract data
    
    - api_key: string
        Secret API key, used as a query parameter

    Returns
    - data: array with dictionaries
        Contains information for the desired weather stations

    """
    params = {"api_key": api_key}
    response = requests.get(url, params=params).json()
    if isinstance(response, dict):
        data = response['datos']
        return extract_data(url=data, api_key=api_key)
    else:
        return response

# url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones"
# station_data = extract_data(url, api_key=secret_key)

def get_indicative(station_data, station_name):
    """
    Function used for filtering data in order to extract a desired indicative value

    Params:
    -data: array with dictionaries
        Data obtained from API call. Each dictionary contains information for one 
        particular weather station. 
    
    -station_name: string
        Name of the desired staion from which to obtain the indicative value

    Returns:
    -idema: string
        indicative value for desired station    
    
    """
    try:
        for station in station_data:
            if station['nombre'] == station_name:
                idema = station['indicativo']
                return idema
    except:
        raise Exception('Could not find desired station')

# station_name = 'MADRID, CIUDAD UNIVERSITARIA'
# idema = get_indicative(station_data=station_data, station_name=station_name)

def call_endpoint(fechaIniStr, fechaFinStr, idema, api_key):
    """
    Funtion used for calling "climatologías diarias" endpoint

    Params:
    -fechaIniStr: string
        Initial date
    
    -fechaFinStr: string
        End date
    
    -idema: string
        indicative value for the desired station
    
    Returns:
    -data: array with dictionaries
        response from calling the API
    
    - api_key: string
        Secret API key, used as a query parameter
    
    """
    format_url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/"\
                +fechaIniStr+"/fechafin/"+fechaFinStr+"/estacion/"+idema

    datos = extract_data(format_url, api_key=api_key)
    return datos

fechaIniStr = "2019-10-01T00:00:00UTC."
fechaFinStr = "2019-10-30T23:59:59UTC."

# datos = call_endpoint(fechaIniStr=fechaIniStr, fechaFinStr=fechaFinStr, idema=idema, api_key=secret_key)
# print(datos)




        