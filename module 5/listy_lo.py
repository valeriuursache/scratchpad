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
    numlist = []
    while True:

        inp = input('Enter your number, (\"done\" to finish):')
        if (inp == 'done'):
            break
           
        numlist.append(float(inp))
    
    
    minimum = min(numlist)
    print(f' Your minimum amoun of values is: {minimum}')
    maximum = max(numlist)
    print(f' Your maximum amount of values is: {maximum}')
    average = sum(numlist) / len(numlist)
    print(f'Your average amount of values are: {average}')






    
    
    


    


