if __name__ == '__main__':



    while True:

        value = (input('Enter your floating-point value, or enter stop:'))
        value = float(value)
        if value == 'stop':
            break
        
    
    minimum = min(value)
    print(f' Your minimum amoun of values is: {minimum}')
    maximum = max(value)
    print(f' Your maximum amount of values is: {maximum}')
    sum_1 = sum(value)
    length = len(value)
    average = sum_1/length
    print(f'Your average amount of values are: {average}')