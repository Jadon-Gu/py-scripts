def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
try:
      n = int(input('Enter number:'))
      while n != 1:
            n = collatz(n)
            print(n)
except ValueError:
    print('Please type an integer.')