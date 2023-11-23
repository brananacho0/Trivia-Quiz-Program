# Brandon Choo
# 1254798

# Function provides the user with a question and it's possible answers
def ask_question(question_number, question_list, possible_answers_list):
    print("Question", question_number)
    question_index = question_number - 1  # Indexing in a list starts from zero
    print(question_list[question_index])
    answer_num = 1  # Used to assign a number to each possible answer
    for answer in possible_answers_list[question_index]:  # Used to iterate through list within list and print the possible answers for the question
        print(answer_num, answer)
        answer_num = answer_num + 1
    print("")
    return


# Function asks the user for their answer and checks whether the answer is given in the correct format
def check_user_answer_validity():
    valid_answer = False
    while (valid_answer == False):
        user_answer = (input("Enter your answer as a number 1/2/3: ")).strip()  # Receives user input and removes trailing whitespace using the strip() function
        if (user_answer in ["1", "2", "3"]):  # Checks if the user entered a valid number from 1 - 3
            valid_answer = True  # This ensures that if the user enters a valid number, the while loop is exited
        else:
            print("Invalid Answer! Please enter a valid number, 1 or 2 or 3")  # User is notified of their incorrect input and subsequently asked to input an answer again
        print("")
    return user_answer  # The user's answer is returned and used as an input for the check_correct_answer() function


# Function checks if the user's answer is correct or wrong
def check_correct_answer(question_number, user_answer, correct_answer_list):
    question_index = question_number - 1
    correct_answer = correct_answer_list[question_index]  # Accesses the correct answer for the particular question
    if (user_answer == correct_answer):  # Compares user's answer against correct answer
        print("CORRECT! Wow, you're smarter than I thought!")  # User is notified if their answer is correct
        result = True
    else:
        print("WRONG! Guess you're not smarter than a 5th grader!")  # User is notified if their answer is wrong
        print("The correct answer is", possible_answers_list[question_index][int(correct_answer) - 1])  # Correct answer is revealed to the user
        result = False
    return result  # The Boolean values returned are appended to a list and used for score calculation


# Function is used to ask the user if they would like to move on to the next question or stop playing (Not called upon after the last question)
# and also checks whether they have responded in the correct format
# Follows same logic as check_user_answer_validity()
def check_user_decision_after_question_validity():
    print("")
    valid_answer = False
    while (valid_answer == False):
        user_decision = (input("Do you wish to continue? Y/N: ")).strip()
        if (user_decision in ["Y", "N"]):  # Checks if the user entered a valid response, "Y" or "N"
            valid_answer = True
        else:
            print("Invalid Answer! Please enter Y or N")
        print("")
    return user_decision  # User response is returned and used to control flow of the program


# Function calculates the user's score
def score_calculator(result_list):
    no_of_correct_answers = result_list.count(True)  # Counts the number of True values (Correct Answers) appended in the result_list
    total_score = no_of_correct_answers * 100  # Each correct answer is awarded 100 points, Incorrect answers are not awarded any points
    return total_score


# Function is used to ask the user if they would like to play the quiz again after they have completed all the questions
# and also checks whether they have responded in the correct format
# Follows same logic as check_user_answer_validity()
def check_user_decision_after_quiz_completion_validity():
    print("")
    valid_answer = False
    while (valid_answer == False):
        user_decision = (input("Do you wish to play again? Y/N: ")).strip()
        if (user_decision in ["Y", "N"]):  # Checks if the user entered a valid response, "Y" or "N"
            valid_answer = True
        else:
            print("Invalid Answer! Please enter Y or N")
        print("")
    return user_decision  # User response is returned and used to control flow of the program




# Lists of questions, possible answers, correct answers and results
question_list = ["What is the name of the Princess in Mario games?", "Which fruit is known as the 'King of fruits'?", "What is the capital of Singapore?"]
possible_answers_list = [["Princess Peach", "Princess Banana", "Princess Pineapple"], ["Jackfruit", "Rambutan", "Durian"], ["Caldecott", "Kent Ridge", "Singapore"]]
correct_answers_list = ["1", "3", "3"]  # Items saved as strings rather than integers for easier comparison with user input
result_list = []  # Used to collect Boolean values returned from check_correct_answer() function


# Setting initial values for variables that control the while loops
play_again = "Y"
continue_quiz = "Y"
question_number = 1  # This can be changed to start from a different question
total_number_of_questions_to_be_asked = 3  # This can be changed to vary the total number of questions asked


# Quiz Program
while (play_again == "Y"):
    while ((continue_quiz == "Y") and (question_number <= total_number_of_questions_to_be_asked)):  # Questions are continuously presented as long as user answers "Y" to "Do you wish to continue? Y/N: " and until all questions are presented
        ask_question(question_number, question_list, possible_answers_list)
        user_answer = check_user_answer_validity()
        result = check_correct_answer(question_number, user_answer, correct_answers_list)
        result_list.append(result)  # Saves result (Boolean Values) of user's answer in a list
        if (question_number <= total_number_of_questions_to_be_asked - 1):  # After the last question, this ensures that the user is not asked "Do you wish to continue? Y/N: " and that their score is not printed as "current score" but as "FINAL SCORE" later
            print("Your current score is ...", score_calculator(result_list), "Points!")
            continue_quiz = check_user_decision_after_question_validity()
        question_number = question_number + 1  # Helps to iterate through the list of quiz questions
    if (continue_quiz == "Y"):  # Ensures that only when the user completes all questions is "FINAL SCORE" printed and the user is asked "Do you wish to play again? Y/N: "
        print("Your FINAL SCORE is ...", score_calculator(result_list), "Points!")
        play_again = check_user_decision_after_quiz_completion_validity()
        result_list = []  # Prepares quiz to be played again, Erases user's old score
        question_number = 1  # Prepares quiz to be played again, Resets question_number so that the program can enter the inner while loop again
    else:
        break  # If user answers "N" to "Do you wish to continue? Y/N: ", the outer while loop is broken and the quiz programme closes

print("Quiz programme terminated, HASTA LA VISTA BABY!")  # Informs user that the quiz program has been closed