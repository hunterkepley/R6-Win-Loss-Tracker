import csv
# R6 WL Tracker 2020

maps = [
    "Clubhouse", 
    "Coastline", 
    "Consulate",
    "Kafe", 
    "Oregon", 
    "Theme Park", 
    "Villa"
]
mapSites = {
    "Clubhouse": ["Bedroom/Gym", "Bar/Stock", "Cash/CCTV", "Church/Arsenal"], 
    "Coastline": ["Billiards/Hookah", "Theater/Penthouse", "Kitchen/Service", "Blue/Sunrise"], 
    "Consulate": ["Meeting/Consulate", "Press/Lobby", "Archives/Tellers", "Cafeteria/Garage"],
    "Kafe": ["Cocktail", "Fireplace/Mining", "Reading/Fireplace", "Kitchen"], 
    "Oregon": ["Kids/Dorms", "Kitchen/Dining", "Meeting/Kitchen", "Laundry/Supply"], 
    "Theme Park": ["Initiation/Office", "Bunk/Day Care", "Armory/Throne", "Lab/Storage"], 
    "Villa": ["Aviator/Games", "Trophy/Statuary", "Living Room/Library", "Dining Room/Kitchen"]
}

def main():
    print("Welcome to R6 WL Tracker\n")

    mapChoice = 0
    siteChoice = 0
    side = 0 # 0 is attack, 1 is defense
    outcome = 0 # 0 is win, 1 is loss
    inProgram = True
    programChoice = 0 # 0 is round entry, 1 is stats, 2 is quit

    while inProgram:
        print("\nPick from the choices:")
        print("0: Enter rounds\n1: View stats\n2: Quit\n: ", end='')
        programChoice = int(input())
        print()

        if programChoice == 0:
            # Pick map
            while True:
                for i, m in enumerate(maps):
                    print("{}: {}".format(i, m))
                print("\nWhich map # did you play?\n: ", end='')

                mapChoice = int(input())
                if mapChoice >= 0 and mapChoice < len(maps):
                    break
            print()

            while True:
                # Pick site
                while True:
                    for i, m in enumerate(mapSites[maps[mapChoice]]):
                        print("{}: {}".format(i, m))
                    print("\nWhich site # did you play?\n: ", end='')

                    siteChoice = int(input())
                    if siteChoice >= 0 and siteChoice < len(mapSites[maps[mapChoice]]):
                        break
                print()

                # Attack/Def
                while True:
                    print("\nWhich side were you on? (a/d)\n: ", end='')
                    
                    c = input()

                    if c.lower() == 'a':
                        side = 0
                        break
                    elif c.lower() == 'd':
                        side = 1
                        break
                print()

                # Win/Loss
                while True:
                    print("\nDid you win or lose that round? (w/l)\n: ", end='')

                    c = input()

                    if c.lower() == 'w':
                        outcome = 0
                        break
                    elif c.lower() == 'l':
                        outcome = 1
                        break

                # Write round to CSV
                with open('winloss.csv', 'w') as myfile:
                    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                    l = [mapChoice, siteChoice, side, outcome]
                    wr.writerow(l)
                
                print("Enter another round? (y/n)\n: ", end='')

                c = input()

                if c.lower() == 'n':
                    break
        elif programChoice == 1:
            print('e')
        elif programChoice == 2:
            break

if __name__ == "__main__":
    main()
