import random

print("V téhle hře budete hádat délku náhodně vygenerovaného pole")

životy = 2

def náh_pole(score):
    low = 1
    high = 420
    cols = 1
    lrows = 2
    hrows = 15

    x = [random.choices(range(low,high), k=cols) for _ in range(random.randint(lrows,hrows))]
    print("--------------------------------------------------------------------------------")
    print("Jaká je délka tohohle pole?")
    print("--------------------------------------------------------------------------------")
    print(', '.join(map(repr, x)))
    print("--------------------------------------------------------------------------------")
    odpoved = int(input("Vaše odpověď: "))

    if odpoved == len(x):
        print("Správně!")
        score += 1

    else:
        print("Špatně")

    print(f"Skóre: {score}")
    return score


lroun = 1
hroun = 15

score = 0

while True:
    for i in range(random.randint(lroun, hroun)):
        score = náh_pole(score)

    y = input("Chcete zkusit další hru? (ano/ne): ").strip().lower()
    if y != 'ano':
        print("Děkujeme za hraní!")
        break