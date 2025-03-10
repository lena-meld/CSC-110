'''
Magdalena Sammut
CSC 110-002
Project -3
This script contains four functions, each one a different statistical calculation.
Each of these four functions accepts a list of numbers as an argument.
    The first function calculates the average of the list by summing the provided
        values, and dividing this sum by the length of the list
    The second function uses the first function to calculate the variance of
        the list of numbers. This function sums the squares of the mean subtracted
        from each value of the list, and divides this sum by the length of the list
        minus one. The variance is returned as a float rounded to two decimal places
    The third function calculates the standard deviation of the list of numbers using
        the second function. To accomplish this, the function simply takes the square
        root of the list's standard deviation.
    The fourth function calculates the range of the list by subtracting the lowest
        value of the list from the highest value.
'''

def mean(numbers):
    '''
    This function determines the average value of a list of numbers
    To accomplish this, the function finds the sum of all the values
    in the list, and divides this by the total number of values in the list.
    The average is returned as a float rounded to two decimal places
    Arg:
        numbers: this argument represents a list of numbers
    Return:
        This function will return the mean of the argument as a float
        rounded to two decimal places
        If the list is empty, 0 will be returned
    '''
    # initialize index variable
    index = 0
    # create a temporary variable for the resulting average
    mean = 0
    # establish while loop to iterate over each item of the list
    while index < len(numbers):
        # add the value of the list item to the temporary variable, mean
        mean += numbers[index]
        # check the next item in the list
        index += 1
    # calculate the average of the list
    if len(numbers) > 0:
        # return the mean of the list
        return round(mean / len(numbers),2)
    # determine if there are any items in the list
    if len(numbers) == 0:
        # if there are no items in the list, return zero
        return mean

def variance(numbers):
    '''
    This function determines the variance of a list of numbers. 
    To accomplish this, it calls the previously created function, 
    mean. The variance is calculated by summing the square of the 
    difference between each item of the list and the mean of the list,
    then dividiging by the number of items in the list minus one.
    Arg:
        numbers: this argument represents a list of numbers
    Return:
        This function will return the variance of the argument as
        a float rounded to two decimal places
        If the list is empty, return 0
    '''
    # call the mean function to determine the argument's average
    # also, save the argument's average to a variable
    x = mean(numbers)
    # initialize index variable
    index = 0
    # create a temporary variable for the resulting variance
    result = 0
    # check if the list is empty
    if len(numbers) == 0:
        # return 0 if above condition met
        return 0
    # establish a while loop to iterate over each item of the list
    while index < len(numbers):
        # save the item of the list at a given index to a variable
        value = numbers[index]
        # calculate the variance for each value, and add them to the temporary
        # 'result' variable to find the variance of the list
        result += ((value - x)**2) / (len(numbers) - 1)
        # perform calculation with next item in the list
        index += 1
    # return the summation rounded to two decimal places
    return round(result, 2)

def sd(numbers):
    '''
    This function calculates the standard deviation of the list argument,
    numbers. The function calls the previous function, variance, to determine
    the variance of the list, and then takes the square root of the variance
    to calculate the standard deviation
    Arg:
        numbers: this argument represents a list of numbers
    Return:
        The calculated standard deviation rounded to two decimal places
        If the list is empty, return 0
    '''
    # calculate the variance of the argument and save it to a variable
    v = variance(numbers)
    # check if list is empty
    if len(numbers) == 0:
        # return 0 if above condition met
        return 0
    # calculate the standard deviation by taking the square root
    # of the argument's variance
    standard_deviation = (v) ** (1/2)
    # return the standard deviation rounded to two decimal places
    return round(standard_deviation,2)

def list_range(numbers):
    '''
    This function calculates the range of a list of numbers by subtracting
    the minimimm value of the list from the maximum
    Arg:
        numbers: this argument represents a list of numbers
    Return: The calculated range of the list
    '''
    # intiialize index variable
    index = 0
    # check if there are any items in the lsit
    if len(numbers) == 0:
        # if the list is empty, the range equals zero. Therefore, return zero
        return 0
    # create a temporary variable for the maximum value
    max = numbers[0]
    # create a temporary variable for the minimum value
    min = numbers[0]
    # create a while loop to iterate over each item of the list
    while index < len(numbers):
        # save the item of the list at a given index to a variable
        value = numbers[index]
        # determine if the value being tested is greater than the current
        # maximum value
        if value >= max:
            # if above condition met, the max equals the value being tested
            max = value
        # determine if the value being tested is less than the current
        # minimum value
        if value <= min:
            # if above condition met, the min equals the value being tested
            min = value
        # repeat the while loop with every item in the lsit
        index +=1
    # calculate the range of the argument by subtracting the minimum value
    # from the maximum
    range = max - min
    # reeturn the range
    return range