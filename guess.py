import random

def guess_game():
    secret = random.randint(1,100)
    guesses = []# guesses.append(guess)定义上把guess全部罗列出来
    print('Guess a number between 1 and 100 (you have 7 chances).')
    for i in range(1,8):
        guess = input(f'Chance {i}/7: ').strip()
        if not guess.isdigit():
            print('Please enter an integer.')
            continue
        guess = int(guess)
        guesses.append(guess)

        if guess == secret:
            print(f'You got it in {i} guesses! History: {guesses}')
            return
# elif 否则如果是带有条件的
        elif guess < secret:
            print('Too low')
        else:
            print('Too high')

    print(f'Game over! The number was {secret}. Your guesses: {guesses}')

# ===== 启动游戏 =====
if __name__ == '__main__':
    guess_game()
