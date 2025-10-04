import random

questions = {
    "What is the capital of France?": {"options": ["a) London", "b) Paris", "c) Berlin"], "answer": "b"},
    "Which planet is known as the Red Planet?": {"options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b"},
    "What is the powerhouse of the cell?": {"options": ["a) Nucleus", "b) Mitochondria", "c) Ribosome"], "answer": "b"},
    "Who wrote 'Romeo and Juliet'?": {"options": ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare"], "answer": "c"},
    "What is the chemical symbol for gold?": {"options": ["a) Au", "b) Ag", "c) Cu"], "answer": "a"},
    "What is the largest mammal in the world?": {"options": ["a) Elephant", "b) Blue Whale", "c) Giraffe"], "answer": "b"},
    "In what year did the Titanic sink?": {"options": ["a) 1905", "b) 1912", "c) 1920"], "answer": "b"},
    "What is the square root of 64?": {"options": ["a) 6", "b) 7", "c) 8"], "answer": "c"},
    "What is the main ingredient in guacamole?": {"options": ["a) Tomato", "b) Onion", "c) Avocado"], "answer": "c"},
    "Which gas do plants absorb during photosynthesis?": {"options": ["a) Oxygen", "b) Nitrogen", "c) Carbon Dioxide"], "answer": "c"}
}

questions_list = list(questions.items())
random.shuffle(questions_list)

incorrect_answers = 0
score=0
for question, data in questions_list:
    options = "\n".join(data["options"])
    user_answer = input(f"\n{question}\n{options}\nEnter the letter corresponding to your answer: ").lower()
    if user_answer == data["answer"]:
        print("Correct!")
        score=score+1
    else:
        print(f"Incorrect! The correct answer is: {data['answer']}")
        incorrect_answers += 1

    if incorrect_answers == 3:
        print("\nYou've reached 3 incorrect answers. Quiz over.")
        break
print('score is' ,score,'out of 10')
if score == 10:
    print("Excellent job!")
elif score >= 7:
    print("Good work!")
elif score >=4:
	print("try harder")
else:
    print("weak in general knowledge!")

print("\nQuiz Completed!")
Z=input('do you want to see credits\n')
if Z=='yes':
	print("Made by Nikhil Asthana  ")
	print("Questions suggested by Shourya Srivastava" )
else:
	print ('fine!')