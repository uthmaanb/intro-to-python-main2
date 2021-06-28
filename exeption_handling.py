try:                            # start with try when using exception handling.
    x = int(input('enter number: '))
except Exception:               # not recommended, it's GENERIC error exception. whenever an error occurs it will appear
    print('An error occurred')
except ZeroDivisionError:
    print('You can\'t divide by zero!')
except ValueError:
    print('enter a valid integer')
else:                   # 'finally' can also be used, but cannot be used with else and vice versa.
    print('Arigato')
