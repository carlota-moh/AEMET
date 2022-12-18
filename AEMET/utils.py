from urllib.parse import urlparse
import re

def input_url(url):
    """
    Function used to check whether an input URL is valid or not. Where it not valid,
    the function will call itself recursively until a valid URL is provided.

    Params:
    -url: string
        url to check
    
    Returns:
    -url: string
        valid url
    
    """
    def valid_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    if valid_url(url):
        return url
    else:
        print('Invalid URL. Please try again')
        return input_url(url=input('Please paste the url you want to extract data from: '))

def input_date(date):
    """
    Function used to check whether an input date has the format "YYYY-MM-DDTHH:MM:SSUTC". 
    Where it not the case, the function will call itself recursively until a valid date is provided.

    Params:
    -date: string 
        date to check
    
    Returns:
    -date: string
        valid date, formatted as "YYYY-MM-DDTHH:MM:SSUTC"
    
    """

    def valid_date(date):
        date_regex = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}UTC$"
        if re.search(date_regex, date):
            return True
        else:
            return False

    if valid_date(date):
        return date
    else:
        print('Invalid date. Please try again')
        return input_date(date=input('Please enter a valid date: '))

def write_json(dic, file_path):
    """
    Function used to write data to JSON in a specified file_path

    Params:
    -dic: dictionary
        Python dictionary to be written to file

    -file_path: string
        final location of the file

    """
    import json
    with open(file_path, "w") as f:
        json.dump(dic, f)