import csv

def create_set_csv():
    file_name = get_set_name()
    file_name = f"csv_files/saved_sets/{file_name}"
    colors = get_chip_colors()
    chip_data = get_chip_data(colors)

    
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = colors
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(chip_data)

def get_set_name():
    csv_forbidden_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    while True:
        file_name = input("Enter poker set name:\n")
        for char in csv_forbidden_chars:
            if char in file_name:
                print(f"Error: The character '{char}' is not allowed in the set name.")
                break
        else:
            break
    if " " in file_name:
        file_name = file_name.replace(" ", "_")
    file_name = f"{file_name}.csv"
    return file_name

def get_chip_colors():
    while True:
        try:
            num_of_colors = int(input("Enter the number of chip colors:\n"))
            if num_of_colors > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    colors = []
    for i in range(num_of_colors):
        color = input(f"Enter color {i + 1}:\n")
        colors.append(color)
    return colors

def get_chip_data(colors):
    chip_data = {}
    for color in colors:
        while True:
            try:
                value = int(input(f"Enter inventory for {color} chips:\n"))
                if value > 0:
                    chip_data[color] = value
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return chip_data

def unpack_set_csv(file_name):
    chip_data = {}
    with open(file_name, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for color in row:
                chip_data[color] = int(row[color])
    return chip_data

class PokerSet:
    def __init__(self, file_name):
        self.file_name = file_name
        self.chip_data = unpack_set_csv(file_name)

if __name__ == "__main__":
    create_set_csv()