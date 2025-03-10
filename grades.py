'''
Magdalena Sammut
CSC 110-002
Project -2
This script contains four functions:
    The first accepts a float argument, grade, that finds the grade the student received as a letter. The function returns
    either A, B, C, D, or E. If an invalid argument is provided (such as a negative grade, or one greater than 100), it will
    return X.
    The second accepts a string argument, letter_grade, that determines whether or not the student passed the assignment. The 
    function first confirms that the length of the string is only one character. If there is more than one character present,
    the function will return Error. If the value for the argument is A, B, C, or D, the function returns Pass. If the value is
    E, the function returns Fail.
    The third accepts two float arguments, score and total_points, that determines the grade the student received on an assignment
    by dividing the score by the total_points. This value is returned, rounded to two decimal places.
    The final function accepts two float arguments, score and total_points, that calls the three preceding functions to provide 
    the user with a breakdown of their score. The arguments provided to this function by the user are used in the point_grade
    function to find the grade as a percentage, which is saved to a variable. The percentage grade is used as an argument by 
    the letter_grade function to find this percentage as a letter grade, which is also saved to a variable. The calculated 
    letter grade is used as an argument is used by the pass_or_fail function to determine whether or not the student passed, and, 
    again, is saved to a variable. Each variable is called in order to concatenate a string providing a grade summary, which is 
    then returned.
'''

def letter_grade(grade):
    '''
    This function accepts a float argument, representing a number grade.
    The function will convert the number grade to a letter grade (A, B, C, D, E).
    Args:
        grade: a float representing the score in question.
    Returns:
        The function will return a letter grade( A, B, C, D, or E) corresponding
        to the argument. 
        If an invalid argument is entered (negative or greater than 100), "X" will be returned.
    '''
    # test if grade is between 90 and 100, inclusive
    if grade >= 90 and grade <= 100:
        # return equivalent letter grade
        return "A"
    # test if grade is greater than or equal to 80 and less than 90
    if grade >= 80 and grade < 90:
        # return equivalent letter grade
        return "B"
    # test if grade is greater than or equal to 70 and less than 80
    if grade >= 70 and grade < 80:
        # return equivalent letter grade
        return "C"
    # test if grade is greater than or equal to 60 and less than 70
    if grade >= 60 and grade <70:
        # return equivalent letter grade
        return "D"
    # test if grade is between 0 and 60, not inclusive
    if grade < 60 and grade >= 0:
        # return equivalent letter grade
        return "E"
    # test if the argument is negative or greater than 100
    else:
        # return X, indicating the argument is invalid for this particular function
        return "X"
    
def pass_or_fail(letter_grade):
    '''
    This function accepts a string argument, representing a letter grade.
    The function will determine if the individual passed or failed the assignment in question.
    Arg:
        letter_grade: a string representing the score in question
    Returns:
        If the grade is A, B, C, or D, the function will return "Pass"
        If the grade is E, the function will return "Fail"
        If the number of characters in the argument is greater than 1, the function will return "Error"
    '''
    # determine if there is more than one character in the argument
    if len(letter_grade) > 1:
        # return Error
        return "Error"
    # determine if the student passed
    if letter_grade == "A" or letter_grade == "B" or letter_grade == "C" or letter_grade == "D":
        # return Pass
        return "Pass"
    # This statement is executed only if the student did not receive and A, B, C, or D
    else:
        # return Fail
        return "Fail"
    
def point_grade(score, total_points):
    '''
    This function accepts two float arguments. It will determine the student's grade as a percentage by dividing
    the score (score) on the assignment by the total points (total_points) available, and multiply this value by 100
    Arg:
        score: A float representing the score the individual received on an assignment
        total_points: A float representing the total number of points avaialable on an assignment
    Return:
        Returns the grade the student received as a percentage
    '''
    # calculate the score as a percentage
    percentage = (score/total_points) * 100
    # return the percent score rounded to two decimal places
    return round(percentage, 2)

def get_grade_results(score, total_points):
    '''
    This function accepts two float arguments. It calls the previous three functions, point_grade, letter_grade,
    and pass_or_fail. The arguments the user provides are plugged back into the point_grade function to find the grade
    on an assignment as a percent. This percentage then becomes its equivalent as a letter_grade using the letter_grade
    function. Then the found grade as a letter is used to determine whether the student passed or failed. The function
    returns a string providing the score breakdown of the assingment.
    Args:
        score: A float representing the score an individual received on an assignment
        total_points: A float representing the total points available on an assignment
    Return:
        Returns a string breaking down the student's score
    '''
    # calculate the percent grade using the point_grade function using the same arguments for this function
    percentage = point_grade(score, total_points)
    # convert the calculated grade as a percent to a letter grade
    grade = letter_grade(percentage)
    # using the letter grade, determine if the student passed or failed the assingment
    result = pass_or_fail(grade)
    # save a string describing the components of the student's score
    grade_summary = "Your grade is " + str(percentage) + " (" + grade + " - " + result + ")"
    # return the aforementioned string
    return grade_summary
