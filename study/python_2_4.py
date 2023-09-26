#홀수, 짝수 판별
for n in range(1,11):
    match n % 2:
        case 0:
            print(f"{n} is even.")
        case 1:
            print(f"{n} is odd.")

#FIZZBUZZ
for n in range(1,101):
    match (n%3, n%5) :
        case(0,0):
            print("FIZZBUZZ")
        case(0,_):
            print("FIZZ")
        case(_,0):
            print("BUZZ")
        case(_,_):
            print(n)
