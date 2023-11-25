def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        #correct_guesses += check_answer(questions.get(key), guess) 
        question_num += 1
        
    
    
    #--------------------------------------
    def check_answer(answer,guess):
       
        if answer == guess:
            print("Correct!")
            return 1
        else :
            print("Wrong")
            return 0
     #----------------------------------------   
    def display_score(correct_guesses,guesses):
        print('----------------------------')
        print('Result')    
        print('----------------------------')
        print('Answers:',end=" ")
        for i in questions:
            print(questions.get(i),end = " ")
            print()
        
        print('Guesses: ',end=" ")
        for i in guesses:
            print(i,end = " ")
        print()

        score = int((correct_guesses/len(questions))*100)
        print("your score is: "+str(score)+"%")

        #----------------------------------------
        '''def play_again():
            
            response = input("Do you want to play agian(Yes/No): ")

            response = response.upper() 

            if response == "YES":
                return True
            else :
                return False '''
            
questions = {'Who is the current captain of Indian cricket team':'A' ,
             'Which team won the cricket world cup 2023':'B' ,
             'Who was the highest run scorer in the world cup': 'A' ,
             'Who was the highest wicket taker in the world cup ':'A'
            }

options = [['A. Rohit Sharma','B. Virat Kohli','C. Steve Smith','D. Ms Dhoni'],
           ['A. India','B. Australia','C. Pakistan','D. England'],
           ['A. Virat Kohli','B. Rohit sharma','C. Kane williamson','D. KL Rahul'],
           ['A. Mohammad Shami','B. Jasprit Bumrah','C. Trent Boult ','D. Pat Cummins']]            

new_game()



    


    