import random


def play_game():
    answer = random.randint(1, 100)
    attempts = 0

    print("1から100までの数字を当ててください!")

    while True:
        guess_input = input("数字を入力: ")

        if not guess_input.isdigit():
            print("数字を入力してください。")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < answer:
            print("もっと大きい数字です。")
        elif guess > answer:
            print("もっと小さい数字です。")
        else:
            print(f"正解!{attempts}回目で当てました。")
            break


def main():
    while True:
        play_game()
        again = input("もう一度プレイしますか? (y/n): ")
        if again.lower() != "y":
            print("ゲームを終了します。")
            break


if __name__ == "__main__":
    main()
