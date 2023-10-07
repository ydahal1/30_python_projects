import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_pth : str) -> list[str]:
    websits : list[str] = []
    with open(csv_pth, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if "https://" not in row[0]:
                websits.append(f"https://{row[0]}")
            else:
                websits.append(row[0])

    return websits

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:

    for status in HTTPStatus:        
        if(status.value == status_code):
            description : str = f"({status} {status.name}) {status.description}"
            return description
    else: 
        return '(???) Unknown status code'

def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={'User-Agent' : user_agent}).status_code
        print(f"'{website}' {get_status_description(code)}")
    except Exception:
        print(f"**Could not get information for website - '{website}'")

def main():
    sites : list[str] = get_websites('/Users/yadhapdahal/Desktop/python/30_python_projects.py/websites.csv')
    user_agent: str = get_user_agent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == "__main__":
    main()
