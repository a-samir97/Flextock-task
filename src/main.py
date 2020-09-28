from database import database_connection, get_data
from input import user_input
from api import get_rate

if __name__ == "__main__":

    # get input from user
    to_currency, from_currency, date = user_input()

    # get data from database 
    get_data(to_currency, from_currency, date)
