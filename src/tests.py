import unittest
import requests

class TestExchangeCurrency(unittest.TestCase):

    def test_with_valid_data(self):
        to_currency = 'USD'
        from_currency = 'EUR'
        date = '2020-01-01'
        rate = 1.1234

        response = requests.get('https://api.frankfurter.app/%s?to=%s&from=%s' % (date, to_currency, from_currency))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['rates'][to_currency], rate)
    
    def test_with_invalid_data(self):
        to_currency = "AAA"
        from_currency = 'EUR'
        date = '2020-01-01'
        
        response = requests.get('https://api.frankfurter.app/%s?to=%s&from=%s' % (date, to_currency, from_currency))

        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    
    unittest.main()