def try_me(usernumber):
    '''The function will take a random integer number and create a list of numbers
       according to the Collatz problem, that is always going to end with the numbers
       ..., 4, 2, 1
    '''
    def collatz(number):
        if int(number) % 2 == 0:
            return int(number) // 2
        elif int(number) % 2 == 1:
            return 3 * int(number) +1

    start_number=usernumber
    try:
        int(start_number)
        collatz_series = []
        while int(start_number) > 1:
            start_number=collatz(start_number)
            collatz_series.append(start_number)
        print('''
            You will see a list of numbers created according to the Collatz problem,
            that is always going to end with the numbers [..., 4, 2, 1] no matter 
            what number you choose. 
            Try to find the rule for creating those numbers starting from the one you chose!
       ''')
        return collatz_series
    except:
        return 'Sorry, your input was invalid! Please use an integer number!'