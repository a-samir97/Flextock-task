import psycopg2
import asyncio

from api import get_rate

POSTGRES_CONFIG = {
    'database': 'flextock',
    'host': 'localhost',
    'user': 'ahmedsamir',
    'password': 'postgres'
}

def database_connection():
    '''
        function that connect to database

        if: 
            the database connected successfully return connection object 
        else:
            return None
    '''
    try:
        connection = psycopg2.connect(**POSTGRES_CONFIG)
        return connection
    except:
        return None


async def insert_data(cur, to_currency, from_currency, date, rate):
    '''
        To Insert data into our database
    '''
    cur.execute('''
                INSERT INTO exchange_currency(to_currency, from_currency, date, rate)
                VALUES('%s', '%s', '%s', '%s')
                ''' % (to_currency, from_currency, date, rate))



def get_data(to_currency, from_currency, date):
    '''
        To get data from database 
        if 
            exist, 
        else 
            insert new row for data,   
        Finally
            print data to the user
    '''
    conn = database_connection()
    
    if conn is not None:
        
        cur = conn.cursor()

        cur.execute('''SELECT rate from exchange_currency WHERE date='%s' and
                    to_currency='%s' and  from_currency='%s';''' % (date, to_currency, from_currency))

        get_data = cur.fetchone()

        if get_data is not None:
            
            cur.close()
            conn.close()

            print("Rate: %s" %get_data[0])

        else:
            rate = get_rate(to_currency, from_currency, date)
    
            asyncio.run(insert_data(cur, to_currency, from_currency,date, rate))

            # to save change 
            conn.commit()

            print("Rate: %s" % rate)

    else:
        print('there is an error in database connection')