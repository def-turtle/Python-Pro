import random
game_history = []
def play_once():
    print("Угадай число от 1 до 10!")
    num = input("Игра с подсказками? (y/n): ").strip().lower()
    secret = random.randint(1, 10)
    guesses = []
    attempts_left = 3

    if num == "y":
        middle = 5
        if secret <= middle:
            print(f"Подсказка: число не больше {middle}.")
        else:
            print(f"Подсказка: число больше {middle}.")

    while attempts_left > 0:
        print(f"\nОсталось попыток: {attempts_left}")
        raw = input("Введи число от 1 до 10 (или 'q' чтобы выйти из игры): ").strip()

        if raw.lower() == "q":
            print("Число было:", secret)
            game_history.append({'secret': secret, 'guesses': guesses, 'result': 'QUIT'})
            return

        try:
            guess = int(raw)
        except ValueError:
            print("Ошибка: нужно ввести ЦЕЛОЕ число.")
            continue

        if guess < 1 or guess > 10:
            print("Число вне диапазона 1–10, попробуй ещё.")
            continue
        attempts_left -= 1

        if guess == secret:
            print(f"Ты угадал! Число было {secret}.")
            game_history.append({'secret': secret, 'guesses': guesses, 'result': 'WON'})
            return
        else:
            print("Не угадал.")
            if num == "y":
      
            if guess < secret:
                    print("Подсказка: моё число БОЛЬШЕ.")
                else:
                    print("Подсказка: моё число МЕНЬШЕ.")

    
    print(f"\nПопытки закончились. Я загадал число {secret}.")
    game_history.append({'secret': secret, 'guesses': guesses, 'result': 'LOSE'})
#hello this is pull request


# def show_history():
#     if not game_history:
#         print("История игр пуста.")
#         return
#     print("\nИстория игр:")
#     for i, game in enumerate(game_history, 1):
#         result = game['result']
#         if result == 'WON':
#             outcome = "Выигрыш"
#         elif result == 'LOSE':
#             outcome = "Проигрыш"
#         else:
#             outcome = "Выход"
#         guesses_str = ', '.join(str(g) for g in game['guesses'] else "Нет попиток")

def main():
    print("Привет! Это игра 'Угадай число'")

    while True:
        play_once()
        again = input("\nСыграть ещё раз? (y/n): ").strip().lower()
        if again != "y":
            print("Пока")
            break

main()

