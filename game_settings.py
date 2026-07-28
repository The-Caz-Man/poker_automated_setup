import csv

from pathlib import Path

def create_game_settings_csv():

    file_name = "csv_files/previous_game_settings.csv"
    field_names = ["Player Count", "Player Names", "Buy-in Amount", "Poker Set", "Chip Values"]
    player_count = get_player_count()
    player_names = get_player_names(player_count)
    buyin = get_buyin()
    poker_set = get_poker_set()
    chip_values = get_chip_values(poker_set)
    settings_data = {
        "Player Count": player_count,
        "Player Names": player_names,
        "Buy-in Amount": buyin,
        "Poker Set": poker_set,
        "Chip Values": chip_values
    }
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(settings_data)


def get_player_count():
    while True:
        try:
            player_count = int(input("Enter the number of players:\n"))
            if player_count > 0:
                return player_count
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return player_count

def get_player_names(player_count):
    player_names = []
    for i in range(player_count):
        name = input(f"Enter name for player {i + 1}:\n")
        player_names.append(name)
    return player_names

def get_buyin():
    while True:
        try:
            buyin = float(input("Enter the buy-in amount:\n"))
            if buyin > 0:
                return buyin
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return buyin

def get_poker_set():
    while True:
        poker_set = input("Enter the poker set name (without .csv):\n")
        poker_set_path = Path(f"csv_files/saved_sets/{poker_set}.csv")
        if poker_set_path.exists():
            return poker_set_path
        else:
            print("Poker set not found. Please enter a valid poker set name.")

def get_chip_values(poker_set):
    chip_values = {}
    poker_set_path = Path(poker_set)
    with open(poker_set_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for color in row:
                while True:
                    try:
                        value = float(input(f"Enter value for {color} chips:\n"))
                        if value % 1 == 0 and value > 0:
                            chip_values[color] = value
                            break
                        elif value == 0.50:
                            chip_values[color] = value
                            break
                        elif value == 0.25:
                            chip_values[color] = value
                            break
                        elif value == 0.10:
                            chip_values[color] = value
                            break
                        elif value == 0.05:
                            chip_values[color] = value
                            break
                        elif value == 0.01:
                            chip_values[color] = value
                            break
                        else:
                            print("Please enter a positive integer or a valid decimal value (0.50, 0.25, 0.10, 0.05, 0.01).")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
    return chip_values

if __name__ == "__main__":
    create_game_settings_csv()
