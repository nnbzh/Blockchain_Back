import json

from django.http import JsonResponse
from requests import Session

from api.models import CurrencyRecord

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '2fc80347-66d7-46dc-a236-627ce9e249a4',
}
session = Session()
session.headers.update(headers)


def get_eth(request):
    eth = {
        'start': '2',
        'limit': '1',
        'convert': 'USD'
    }
    try:
        data = session.get(api_url, params=eth)
        exchange_rates = data.json()
        return JsonResponse({'name': exchange_rates['data'][0]['name'],
                             'symbol': exchange_rates['data'][0]['symbol'],
                             'USD': exchange_rates['data'][0]['quote']['USD']['price']})
    except Exception as e:
        print(e)


def get_etc(request):
    etc = {
        'start': '31',
        'limit': '1',
        'convert': 'USD'
    }
    try:
        data = session.get(api_url, params=etc)
        exchange_rates = data.json()
        return JsonResponse({'USD': exchange_rates['data'][0]['quote']['USD']['price']})
    except Exception as e:
        print(e)
