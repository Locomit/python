#guess the word
import random
words=['namita','manita','netra','terna']
score=0
while True:
    for wr in range(3):
        lett=list(random.choice(words))
        print("Guess Correct Word By given word:=>","".join(lett))
        user = input("Enter correct word or '(quit)':")
        if user == 'quit':
            break

        if user != "".join(lett):
            valid = True
            for letter in user:
                if letter in lett:
                    lett.remove(letter)
                else:
                    valid=False
                    break

            if valid and user in words:
                score = score + len(user)
                print(f"correct and your score is {score}")
            else:
                print("Wrong Word Enter by You")
            if user != "".join(lett):
                break
        else:
            print("You Enter same name.....")
    else:
        score=score-len(user)
        print(f"We have reduse your {len(user)} score because you enter same word 3 time your total score is {score}")
    print("Thank You for Playing this Game :>")


