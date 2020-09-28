def user_input():
    '''
        this function to get input from user

        return to_currency, from_currency, date
    '''
    
    to_currency = input("what is your to currency code ? \n")
    from_currency = input("what is your from currency code? \n")
    date = input("what is your date? \n")

    return to_currency, from_currency, date
