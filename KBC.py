# It will be a 5 question game
# 1st qs 
# -> if right then (add money and) go for next qs. 
# -> repeat the same until the ans is wrong 
# -> if any ans gets wrong (do show  "GAME ENDED") and give the total money as output
# -> if all 5 ans is right then show you won (amount)

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. New York", "D. Tokyo"],
        "correct_answer": "B"
    },
    {
        "question": "Which gas is most abundant in the Earth's atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "C"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Leo Tolstoy"],
        "correct_answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Go", "B. Au", "C. Ag", "D. Fe"],
        "correct_answer": "B"
    }
]

def kbc_game():
    score = 0
    print("Welcome to Kaun Banega Crorepati!")

    i = 0
    for i in range(5):
        ques = questions[i]['question']

        print(f"Your first question is: {ques}")

        op = questions[i]['options']
        print(f"Your options are: {' ,'.join(op)}")

        # User input
        user_answer = input("Your answer (A/B/C/D): ").upper()

        correct = questions[i]['correct_answer']

        if (user_answer == correct ):
            print(f"You are right, you win for the {i+1} level!!!")
            score += 10
        else:
            print("SORRY!!!! You didn't win")
            break
    print(f"\nCongratulations! You've won Rs. {score} in Kaun Banega Crorepati!")

kbc_game()
