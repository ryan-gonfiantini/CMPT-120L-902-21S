#question 1
def sum_a_range(number):
    total = 0
    for num in range(number + 1):
        total += num
    return total 
if __name__ == "__main__":
    print(sum_a_range(8))


#question 2
def main():
    x = int(input("Enter an integer: 5 + "))
    print(str(x))

main()

