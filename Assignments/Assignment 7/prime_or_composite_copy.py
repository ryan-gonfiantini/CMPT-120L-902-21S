def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True 
numbers=[1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201] 
for i in numbers:
    if is_prime(i):
        print(i, "is a prime number")
    else:
        print(i, "is a composite number") 