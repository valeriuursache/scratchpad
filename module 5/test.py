 while True:
     value = (input('Enter your floating-point value, or enter stop:'))
     if value == 'stop':
         break
        value = float(value)
    
    minimum = min(value)
    print(f' Your minimum amoun of values is: {minimum}')
    maximum = max(value)
    print(f' Your maximum amount of values is: {maximum}')
    sum_1 = sum(value)
    length = len(value)
    average = sum_1/length
    print(f'Your average amount of values are: {average}')