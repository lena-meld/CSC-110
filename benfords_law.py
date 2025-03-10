'''
Magdalena Sammut
CSC 110-002
Project -5
This script is used to determine if a .csv file follows Benford's Law. To
    accomplish this, this script uses 5 functions:
    The first function accepts one string argument and returns a boolean
        regarding whether or not the argument is also a float
    The second function accepts the name of a .csv file and returns the numeric
        and float values found within the file
    The third function accepts a list of strings, where each string in the list
        will also be a number. This function counts the occurences of the first
        digit of each numeric string being the first digit and returns this in
        the form of a dictionary.
    The fourth function accepts a dictionary where the key is a digit between
        1 and 9 and the value is the number of times that digit appears as the
        first value. The function determines the percent of the time a digit
        appears as the first value and returns this in the form of a dictionary
    The fifth function accepts a dictionary where the key is a digit and the
        frequency that digit appears as the first number of a value in the .csv
        file. It will return a boolean representing whether or not the file
        is in accordance with Benford's law
'''
def is_float(string):
    '''
    This function is used to check if a string is also a float
    Arg:
        string: this function accepts one string argument
    Returns:
        If the argument is not also a float, the function will return False
        If the argument is also a float, the function will return True
    '''
    # create a for loop to iterate over each character of the string
    for char in string:
        # check if the character is a digit or a decimal point
        if char not in "0123456789.":
            # if the argument is not a float, return False
            return False
    # if the arugment is not a float, return True
    return True

def csv_to_list(file_name):
    '''
    This function is used to create a list of the numeric or float values of a
        .csv file in a list
    Arg:
        file_name: this function accepts a string argument that correlates to
            the name a location of a .csv file
    Return:
        This function will return a list of the numeric and float values found
            within the .csv file
    '''
    # create an empty list to hold the integers and floats found in the file
    new_list = []
    # open the file in question
    f = open(file_name, "r")
    # use a for loop to iterate over each line of the file
    for line in f:
        # remove the whitespace from every line of code, and create a list where
        # the words and numbers of the line are their own element, not including
        # commas. Save this list to a variable
        value = line.strip().split(",")
        # iterate through every element of the value list
        for v in value:
            # determine if the element is an integer or a float
            if v.isnumeric() or is_float(v):
                # if above condition met, append the element to the list created
                # at the beginning of the function
                new_list.append(str(v))
    # return the list of integer and float values
    return new_list
            
def count_start_digits(numbers):
    '''
    This function counts the occurence of the first digit of each number found 
        within the .csv file
    Arg:
        numbers: one list composed of strings. Each string within this list
            will be a number
    Return:
        This function will return the number of times a value appears as the
            first digit of a number
    '''
    # create an empty dictionary
    counts = {}
    # iterate through each element of the argument
    for i in range(len(numbers)):
        # check if the first number of the element being tested is in counts.
        #Additionaly, ensure this first number is not zero
        if int(numbers[i][0]) in counts and int(numbers[i][0]) != 0:
            # if above condition met, add 1 to key's value
            counts[int(numbers[i][0])] += 1
        # check if the first number of the element being tested is not found in
        # counts. Additionally, ensure the first number of the element is not
        # zero
        if int(numbers[i][0]) not in counts and int(numbers[i][0]) != 0:
            # if above conditions met, create a key value pair where the first
            # number of the element being tested is the key and its value is 1
            counts[int(numbers[i][0])] = 1
    # return the new dictionary
    return counts

def digit_percentages(counts):
    '''
    This function determines what percent of the time a value appears as the
        first digit of a number
    Arg:
        counts: this function accepts a dictionary where the key will be the
            digit in question and its associated value will be the number of
            times it appears as the first digit of a number
    Return:
        This function will return a dictionary where the key will be a digit
            in between 1 and 9 (inclusive) and its associated value will 
            represent the percentage of how often that value appears as the
            first digit of the number in the .csv file
    '''
    # create an empty dictionary
    percentage = {}
    # start with a sum of zero
    sum = 0
    # iterate through each key of the argument
    for c in counts:
        # add each value associated with the key of the argument being tested 
        # to the sum
        sum += counts[c]
    # iterate through each key of the argument again
    for c in counts:    
        # determine what percent of digits in the .csv file start with a given
        # number by dividing the number of times the value appears by the sum of
        # all the values. Multiply this quotient by 100, and round to two
        # decimal places
        percentage[c] = round((counts[c]/sum) * 100, 2)
    # return the percentages of each number's appearance as the first digit
    return percentage

def check_benfords_law(percentages):
    '''
    This function determines whether or not the values found within the .csv 
        file are in accordance with Benford's Law
    Arg:
        percentages: this function accept a dictionary where the key is the
            digit in question and its associated value will be a percentage
            representing how often that digit appear as the first value of a
            number in the .csv file
    Return:
        This function will return True if the percentages are in accordance with
            Benford's Law
        This function will return False if the percentages are not in accordance
            with Benford's law
    '''
    
    # iterate through every key of percentages and check if its associated
    # value is in accordance with Benford's Law
    for p in percentages:
        if p == 1:
            if percentages[p] > 40 or percentages[p] < 25:
                return False
        if p == 2:
            if percentages[p] > 27 or percentages[p] < 12:
                return False
        if p == 3:
            if percentages[p] > 22 or percentages[p] < 7:
                return False
        if p == 4:
            if percentages[p]> 19 or percentages[p] < 4:
                return False
        if p == 5:
            if percentages[p] > 17 or percentages[p] < 2:
                return False
        if p == 6:
            if percentages[p] > 16 or percentages[p] < 1:
                return False
        if p == 7:
            if percentages[p]  > 15 or percentages[p] < 0:
                return False
        if p == 8:
            if percentages[p] > 15 or percentages[p] < 0:
                return False
        if p == 9:
            if percentages[p] > 14 or percentages[p] < 0:
                return False
    return True