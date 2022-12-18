import sys
import re
import time
from urllib.parse import urlparse
import requests
from .utils import input_url, input_date
from .AEMET import extract_data, get_indicative, call_endpoint

def main():
    arguments = sys.argv
    if "MAIN" in arguments:
        try:
            url = input_url(url=input('Please paste the url you want to extract data from: '))
            time.sleep(1)
            api_key = input('Please paste here your api key: ')
            time.sleep(1)
            station_data = extract_data(url=url, api_key=api_key)
            station_name = input('Which station would you like to get data from? ')
            print('Fetching data from station...')
            time.sleep(2)
            idema = get_indicative(station_data=station_data, station_name=station_name)
            fechaIniStr = input_date(date=input('Please paste here the starting date: '))+'.'
            fechaFinStr = input_date(date=input('Please paste here the ending date: '))+'.'
            datos = call_endpoint(fechaIniStr=fechaIniStr, fechaFinStr=fechaFinStr, idema=idema, api_key=api_key)
            print(datos)
        except TypeError as e:
            print(e)

    elif "EXTRA" in arguments:
        pass

if __name__ == '__main__':
    print('Loading...')
    main()