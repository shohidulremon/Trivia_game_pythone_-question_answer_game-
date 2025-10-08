import random
questions = {
    "What is the key value to define a funtion in Python":"def",
    "Which data Type is used to store True or False velue":"boolean",    #dictionary Function
    "What is the correct file extention for python files" : ".Py",
    "What will be the value of the following Python expression? 'print(4 + 3 % 5)'": "7",
    "What are the values of the following Python expressions?\nprint(2**(3**2))\nprint((2**3)**2)\nprint(2**3**2)": "512, 64, 512",
    "Which of the following is the truncation division operator in Python?":"/"
}
def python_q():
    question_list = list(questions.keys())
    total_question =  6
    score = 0
    selected_questions = random.sample(question_list,total_question)
    #print(selected_questions)
    
    for indx, question in enumerate(selected_questions):  #emurate - will give the question with its index 
        print(f"{indx + 1}. {question}")
        user_answer = input("Type your answer: ").lower().strip() #.strip - will remove spacing from begining or end of string 
        correct_answer = questions[question]
        if user_answer==correct_answer.lower():
            print("Correct!!\n")
            score += 1
        else:
            print(f"The Answer is Wrong!!.\nThe correct answer is: {correct_answer}.\n")
    print(f"Your Total Score is {score}/{total_question}")
            
                


python_q()
