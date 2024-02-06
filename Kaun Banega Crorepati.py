def yourname():
    global a  # Declare 'a' as a global variable
    a = input("What is your name: ")
    print(f"Welcome {a} to KPC")

def goodbye(x):
    print(f"Goodbye, {x}")

question = [
    ["What is the national bird of our country?", "Falcon", "Kuku", "Doel", "Egle", 3],
    ["What is the national bird of our country?", "Falcon", "Kuku", "Doel", "Egle", 3],
    ["What is the national bird of our country?", "Falcon", "Kuku", "Doel", "Egle", 3],
    ["What is the national bird of our country?", "Falcon", "Kuku", "Doel", "Egle", 3],
    ["What is the national bird of our country?", "Falcon", "Kuku", "Doel", "Egle", 3]
    # Add more questions here...
]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

total_prize = 0
yourname()
lifeline = 3
for i in range(len(question)):
    print(f"{i + 1}. {question[i][0]}")
    print(f"a. {question[i][1]} \t b. {question[i][2]}")
    print(f"c. {question[i][3]} \t d. {question[i][4]}")
    while True:
        print(f"Your remaining lifeline: {lifeline}\n")
        print("If you want to use a lifeline, please enter 5")
        user_choice = int(input("Enter your choice (1-5): "))
        if (user_choice == 5 and lifeline!= 0):
            answer = question[i][5]
            import random
            ran = random.randint(1, 4)
            print("Thank you for choosing 50:50 lifeline!")
            print(f"Your answer is either {answer} or {ran}.")
            lifeline -= 1
        if not (1 <= user_choice <= 5):
            raise ValueError(f"Invalid.\t {user_choice} is not in the range of 1-4")
        if 1 <= user_choice <= 4:
            break

    if user_choice == question[i][5]:
        print("You are right!")
        print(f"You have earned {levels[i]} /- taka")
        total_prize += levels[i]
    else:
        print("You are wrong!")
        break

print(f"Your total prize: {total_prize}")
goodbye(a)