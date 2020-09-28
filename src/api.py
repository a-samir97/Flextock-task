import requests

def get_rate(to_currency, from_currency, date):

    '''
        get the rate of exchange currency from frankfurter api
    '''

    response = requests.get('https://api.frankfurter.app/%s?to=%s&from=%s' % (date, to_currency, from_currency))

    if response.status_code == 200:
        return response.json()['rates'][to_currency]
    else:

        raise Exception("there is an error, status code %s" %response.status_code)