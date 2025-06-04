# List of question
questions = [
    ["Who is Shah Rukh Khan", "WWE wrestler", "Actor", "Astrounaut", "plumber", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Iron", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the boiling point of water?", "100°C", "0°C", "50°C", "200°C", 1],
    ["Which language is used to create web pages?", "Python", "HTML", "C++", "Java", 2],
    ["What is the currency of Japan?", "Dollar", "Euro", "Yen", "Rupee", 3]
]
prize=[1000,234343,24344,2234343,2343434,34343434,2343324,55444345,3454543]
i=0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    # check whether the answer is correct or not
    ans = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d: "))

    if(question[5]==ans):
        print("correct Answer")
    else:
        print(f"Incorrect, the correct answer is {question[5]}" )
        print("better luck next time")
        break
 
    print(f"you won {prize[i]}")
    i +=1