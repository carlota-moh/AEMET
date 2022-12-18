from urllib.parse import urlparse
import re

def input_url(url):
    
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

# print(input_url(url=input('Please paste the url you want to extract data from: ')))

def input_date(date):

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

# print(input_date(date=input('Please paste here the starting date: ')))

