print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    result = ""
    if "3" in str(num) and num % 3 != 0 and num % 7 != 0:
        return "Almost Fizz"
    if num % 3 == 0 and num % 7 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 7 == 0:
        return "Buzz"
    else:
        return str(num)

num = int(input())
for i in range(1, num + 1):
    print(fizzbuzz(i))
