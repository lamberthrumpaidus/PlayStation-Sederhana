import random
import time

# Fungsi untuk menampilkan loading


def loading():
    print("Loading", end="")
    for _ in range(3):
        print(".", end="")
        time.sleep(1)
    print()

# Fungsi untuk mendapatkan input valid


def get_valid_choice(min_value, max_value):
    while True:
        try:
            choice = int(input(f"Pilih antara {min_value} dan {max_value}: "))
            if min_value <= choice <= max_value:
                return choice
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

# Permainan 1: Tebak Angka


def play_guess_number():
    loading()
    print("Permainan Tebak Angka")
    number = random.randint(1, 100)
    while True:
        guess = get_valid_choice(1, 100)
        if guess == number:
            print("Selamat! Anda menebak angka!")
            break
        elif guess < number:
            print("Terlalu rendah! Coba lagi.")
        else:
            print("Terlalu tinggi! Coba lagi.")

# Permainan 2: Batu, Kertas, Gunting


def play_rock_paper_scissors():
    loading()
    print("Permainan Batu, Kertas, Gunting")
    choices = ["batu", "kertas", "gunting"]
    user_choice = input("Pilih batu, kertas, atau gunting: ").lower()
    computer_choice = random.choice(choices)

    print(f"Anda memilih: {user_choice}, Komputer memilih: {computer_choice}")
    if user_choice == computer_choice:
        print("Seri!")
    elif (user_choice == "batu" and computer_choice == "gunting") or \
         (user_choice == "gunting" and computer_choice == "kertas") or \
         (user_choice == "kertas" and computer_choice == "batu"):
        print("Anda menang!")
    else:
        print("Anda kalah!")

# Permainan 3: Tic Tac Toe


def play_tic_tac_toe():
    loading()
    print("Permainan Tic Tac Toe")
    board = [' ' for _ in range(9)]

    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def check_winner():
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return board[combo[0]]
        return None

    current_player = 'X'
    for _ in range(9):
        print_board()
        choice = get_valid_choice(1, 9) - 1
        if board[choice] != ' ':
            print("Posisi sudah terisi. Coba lagi.")
            continue

        board[choice] = current_player
        winner = check_winner()
        if winner:
            print_board()
            print(f"Pemain {winner} menang!")
            return
        current_player = 'O' if current_player == 'X' else 'X'

    print_board()
    print("Permainan seri!")

# Permainan 4: Snake


def play_snake():
    loading()
    print("Permainan Snake")
    snake_length = 3
    snake = [(5, 5)]
    food = (random.randint(0, 9), random.randint(0, 9))
    direction = 'R'

    while True:
        print(f"Ular: {snake}, Makanan: {food}, Panjang: {snake_length}")
        move = input(
            "Gerak (w/a/s/d untuk atas/kiri/bawah/kanan, q untuk keluar): ").lower()

        if move == 'q':
            break
        elif move == 'w':
            direction = 'U'
        elif move == 's':
            direction = 'D'
        elif move == 'a':
            direction = 'L'
        elif move == 'd':
            direction = 'R'

        head_x, head_y = snake[0]
        if direction == 'U':
            head_y -= 1
        elif direction == 'D':
            head_y += 1
        elif direction == 'L':
            head_x -= 1
        elif direction == 'R':
            head_x += 1

        if (head_x, head_y) == food:
            snake_length += 1
            food = (random.randint(0, 9), random.randint(0, 9))

        snake.insert(0, (head_x, head_y))
        if len(snake) > snake_length:
            snake.pop()

        if head_x < 0 or head_x >= 10 or head_y < 0 or head_y >= 10:
            print("Ular keluar dari layar!")
            break

# Permainan 5: Balap Mobil


def play_car_racing():
    loading()
    print("Permainan Balap Mobil")
    position = 0
    finish_line = 100

    while True:
        command = input(
            "Tekan 'f' untuk mempercepat, 'q' untuk keluar: ").lower()
        if command == 'q':
            break
        elif command == 'f':
            position += random.randint(5, 15)
            print(f"Posisi Anda: {position}")
            if position >= finish_line:
                print("Anda menang!")
                break

# Permainan 6: Tebak Kata


def play_guess_word():
    loading()
    print("Permainan Tebak Kata")
    words = ["apel", "jeruk", "pisang", "mangga"]
    word = random.choice(words)
    guessed = ['_' for _ in word]

    while '_' in guessed:
        print(" ".join(guessed))
        letter = input("Tebak huruf: ").lower()
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter

    print(f"Selamat! Anda menebak kata: {word}")

# Permainan 7: Mencocokkan Warna


def play_color_matching():
    loading()
    print("Permainan Mencocokkan Warna")
    colors = ["merah", "biru", "hijau", "kuning"]
    color_to_match = random.choice(colors)

    print(f"Cocokkan warna: {color_to_match}")
    guess = input("Masukkan warna yang cocok: ").lower()

    if guess == color_to_match:
        print("Anda menang!")
    else:
        print("Anda kalah!")

# Permainan 8: Bingo


def play_bingo():
    loading()
    print("Permainan Bingo")
    numbers = list(range(1, 26))
    random.shuffle(numbers)
    choice = get_valid_choice(1, 25)

    if numbers[choice - 1] == choice:
        print("Anda menang!")
    else:
        print("Anda kalah!")

# Permainan 9: Memori


def play_memory():
    loading()
    print("Permainan Memori")
    cards = [1, 2, 1, 2, 3, 4, 3, 4]
    random.shuffle(cards)

    print("Tebak pasangan kartu (1-4): ")
    first_choice = get_valid_choice(1, 4)
    second_choice = get_valid_choice(1, 4)

    if cards[first_choice - 1] == cards[second_choice - 1]:
        print("Anda menang!")
    else:
        print("Anda kalah!")

# Permainan 10: Ular Tangga


def play_snakes_and_ladders():
    loading()
    print("Permainan Ular Tangga")
    position = 0

    while position < 100:
        input("Tekan 'd' untuk melempar dadu: ")
        roll = random.randint(1, 6)
        position += roll
        print(f"Anda mendapatkan {roll}, posisi Anda sekarang: {position}")

        if position == 10:
            print("Anda mendapatkan ular! Posisi Anda sekarang: 5")
            position = 5
        elif position == 20:
            print("Anda mendapatkan tangga! Posisi Anda sekarang: 30")
            position = 30

        if position >= 100:
            print("Selamat! Anda menang!")
            break

# Permainan 11: Hitung Mundur


def play_countdown():
    loading()
    print("Permainan Hitung Mundur")
    countdown = 10
    while countdown > 0:
        print(countdown)
        time.sleep(1)
        countdown -= 1
    print("Waktu habis!")

# Permainan 12: Undian


def play_draw():
    loading()
    print("Permainan Undian")
    participants = input(
        "Masukkan nama peserta (pisahkan dengan koma): ").split(',')
    winner = random.choice(participants).strip()
    print(f"Pemenang undian adalah: {winner}")

# Menu Utama


def main():
    password = input("Masukkan kata sandi: ")
    if password != "lam":
        print("Kata sandi salah!")
        return

    games = [
        play_guess_number,
        play_rock_paper_scissors,
        play_tic_tac_toe,
        play_snake,
        play_car_racing,
        play_guess_word,
        play_color_matching,
        play_bingo,
        play_memory,
        play_snakes_and_ladders,
        play_countdown,
        play_draw,
    ]

    while True:
        print("\nPilih permainan yang ingin dimainkan:")
        for i, game in enumerate(games, 1):
            print(f"{i}. {game.__name__}")
        print("0. Keluar")

        choice = get_valid_choice(0, len(games))
        if choice == 0:
            break

        games[choice - 1]()


if __name__ == "__main__":
    main()
