if __name__ == "__main__":
    #  list food
    food = ['rice', 'beans']
    food.append('broccoli')
    # using extend
    more_food = ('bread', 'pizza')
    food.extend(more_food)
    # printing using slicing notation
    print(food[0:2])
    # using index notation
    print(food[len(food)-1])
    # creating a list called breakfast using split
    breakfast_1= 'eggs, fruit, orange juice'
    breakfast = breakfast_1.split(',')
    print(breakfast)
    print(len(breakfast))

    # promt user
    while True:
     value = float(input('Enter your floating-point value, or enter stop:'))
     if value == "stop":
               break
    minimum = min(value)
    print(f' Your minimum amoun of values is: {minimum}')
    maximum = max(value)
    print(f' Your maximum amount of values is: {maximum}')
    sum_1 = sum(value)
    length = len(value)
    average = sum_1/length
    print(f'Your average amount of values are: {average}')






    
    
    


    


