import game_settings
import poker_sets


def create_player_inventory(settings):
    player_inventories = {}
    for player in settings.player_names:
        player_inventories[player] = {}
        for color in settings.chip_values:
            player_inventories[player][color] = 0
        player_inventories[player]["Total Value"] = 0
    return player_inventories


def get_settings(settings):
    settings.display_settings()
    while True:
        try:
            is_current_settings = input("Are these the correct settings? (y/n):\n").lower()
            if is_current_settings == "y":
                print("Settings confirmed.")
                break
            elif is_current_settings == "n":
                game_settings.create_game_settings_csv()
                player_count, player_names, buyin, poker_set, chip_values = game_settings.unpack_settings_csv()
                settings = game_settings.GameSettings(player_count, player_names, buyin, poker_set, chip_values)
                break
            else:
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        except ValueError as e:
            print(e)

def create_stacks_counts(settings):
    stack_counts = {}
    for color, value in settings.chip_values.items():
        if value >= 1:
            stack_counts[color] = 1
        else:
            stack_counts[color] = 1 / value
    return stack_counts

def distribute_chips(player_inventories, stack_counts, settings, poker_set, color = None, player = None):
    
    #Make a list of current players who still need chips
    player_list = [key for key in player_inventories.keys() if player_inventories[key]["Total Value"] != settings.buyin]
    if player == None:
        player = player_list[0]

    #Chip value dict ordered from highest value to lowest.
    r_sorted_chip_values = dict(sorted(settings.chip_values.items(), key=lambda x: x[1], reverse=True))

    #Set the lowest value chip that's still available as current chip
    for color in r_sorted_chip_values:
        if poker_set.chip_data[color] >= stack_counts[color]:
            current_chip = color

    if player_inventories[player]["Total Value"] != settings.buyin:
        player_inventories[player][current_chip] += stack_counts[current_chip]
        player_inventories[player]["Total Value"] += stack_counts[current_chip] * settings.chip_values[current_chip]
        poker_set.chip_data[current_chip] -= stack_counts[current_chip]
    
    if player_list:
        player_index = player_list.index(player)
        if player_index == len(player_list) - 1:
            next_player = player_list[0]
        else:
            next_player = player_list[player_index + 1]
    
        distribute_chips(player_inventories, stack_counts, settings, poker_set, current_chip, next_player)

    else:
        return

    
    


    
        
    
    

if __name__ == "__main__":
    player_count, player_names, buyin, poker_set, chip_values = game_settings.unpack_settings_csv()
    settings = game_settings.GameSettings(player_count, player_names, buyin, poker_set, chip_values)
    poker_set = poker_sets.PokerSet(settings.poker_set)
    player_inventories = create_player_inventory(settings)
    stack_counts = create_stacks_counts(settings)
    distribute_chips(player_inventories, stack_counts, settings, poker_set)
    print(player_inventories)