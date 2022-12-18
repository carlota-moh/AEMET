import sys
import re
import time
from urllib.parse import urlparse
import requests
from .utils import input_url, input_date
from .AEMET import run_AEMET, run_extra

def main():
    arguments = sys.argv
    if "MAIN" in arguments:
        run_AEMET()

    elif "EXTRA" in arguments:
        run_extra()

if __name__ == '__main__':
    print('Loading...')
    main()