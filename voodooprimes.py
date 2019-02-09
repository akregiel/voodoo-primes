def if_prime(p): #a function that checks and tells if the number is prime
    for i in range(2,p):
        if i*i<=p and p%i==0: #we can limit the search of the factors to the square root of the p number
            print("your number is not prime. Try another input")
            break
    else:
        print("your number is prime")
        reciprocal(p)

def reciprocal(n): #we look for decimal expansion and check if our number is in the expansion
    rec=(1/(n))
    print("reciprocal: ", rec)

    if str(n) in str(rec):
        print("your number is a voodoo prime :) ")
    else:
        print("your number is not a voodoo prime :( ")
    
print("input a number")
number=int(input())

if_prime(number)