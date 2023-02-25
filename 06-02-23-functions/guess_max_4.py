import random

def main():
    target, lives_left = setup()
    result = play(target, lives_left)

def setup():
    target = random.randrange(1, 100)
    lives_left = 6
    return target, lives_left

def play(target, lives_left):
    guess = int(input("Guess a number: "))
    result = assess(target, lives_left, guess)
    print(result["message"])
    return result if "game_over" in result else play(target, lives_left - 1) 

def assess(target, lives_left, guess):
    for fn in guess_correct, failed, too_low, too_high:
        result = fn(target, lives_left, guess)
        if result:
            return result

def guess_correct(target, lives_left, guess):
    return {
    	"game_over": True,
    	"message": f"You guessed correctly with {lives_left} lives left!"
    	} if guess == target else None

def failed(target, lives_left, guess):
    return {
    	"game_over": True,
    	"message": f"Sorry, you failed :( The correct answer was {target}"
    } if target != guess and lives_left == 0 else None

def too_low(target, lives_left, guess):
    return {
    	"message": f"Too low! Try again, you have {lives_left} lives left!"
    } if guess < target else None

def too_high(target, lives_left, guess):
    return {
    	"message": f"Too high! Try again, you have {lives_left} lives left!"
    } if guess > target else None

if __name__ == '__main__':
    main()
