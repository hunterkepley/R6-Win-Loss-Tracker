import csv
# R6 WL Tracker 2020

class Site:
    def __init__(self, name):
        self.name = name
        self.aWins = 0
        self.aLosses = 0
        self.dWins = 0
        self.dLosses = 0

maps = [
    "Clubhouse", 
    "Coastline", 
    "Consulate",
    "Kafe Dostoyevsky", 
    "Oregon", 
    "Theme Park", 
    "Villa"
]
mapSites = {
    maps[0]: [Site("Bedroom/Gym"), Site("Bar/Stock"), Site("Cash/CCTV"), Site("Church/Arsenal")], 
    maps[1]: [Site("Billiards/Hookah"), Site("Theater/Penthouse"), Site("Kitchen/Service"), Site("Blue/Sunrise")], 
    maps[2]: [Site("Meeting/Consulate"), Site("Press/Lobby"), Site("Archives/Tellers"), Site("Cafeteria/Garage")],
    maps[3]: [Site("Cocktail"), Site("Fireplace/Mining"), Site("Reading/Fireplace"), Site("Kitchen")], 
    maps[4]: [Site("Kids/Dorms"), Site("Kitchen/Dining"), Site("Meeting/Kitchen"), Site("Laundry/Supply")], 
    maps[5]: [Site("Initiation/Office"), Site("Bunk/Day Care"), Site("Armory/Throne"), Site("Lab/Storage")], 
    maps[6]: [Site("Aviator/Games"), Site("Trophy/Statuary"), Site("Living Room/Library"), Site("Dining Room/Kitchen")]
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
                        print("{}: {}".format(i, m.name))
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
                with open('winloss.csv', 'a+') as f:
                    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
                    l = [mapChoice, siteChoice, side, outcome]
                    wr.writerow(l)
                
                print("Enter another round on {}? (y/n)\n: ".format(maps[mapChoice]), end='')

                c = input()

                if c.lower() == 'n':
                    break
        elif programChoice == 1:
            displayStats()
        elif programChoice == 2:
            break

def displayStats():

    # Local variables
    mapChoice = 0

    # Reset stats in memory
    mapSites = {
        maps[0]: [Site("Bedroom/Gym"), Site("Bar/Stock"), Site("Cash/CCTV"), Site("Church/Arsenal")], 
        maps[1]: [Site("Billiards/Hookah"), Site("Theater/Penthouse"), Site("Kitchen/Service"), Site("Blue/Sunrise")], 
        maps[2]: [Site("Meeting/Consulate"), Site("Press/Lobby"), Site("Archives/Tellers"), Site("Cafeteria/Garage")],
        maps[3]: [Site("Cocktail"), Site("Fireplace/Mining"), Site("Reading/Fireplace"), Site("Kitchen")], 
        maps[4]: [Site("Kids/Dorms"), Site("Kitchen/Dining"), Site("Meeting/Kitchen"), Site("Laundry/Supply")], 
        maps[5]: [Site("Initiation/Office"), Site("Bunk/Day Care"), Site("Armory/Throne"), Site("Lab/Storage")], 
        maps[6]: [Site("Aviator/Games"), Site("Trophy/Statuary"), Site("Living Room/Library"), Site("Dining Room/Kitchen")]
    }


    # Open and gather data
    with open('winloss.csv', 'r') as f:
        for _, line in enumerate(f): 
            r = line.replace('"', '')
            s = r.split(',')
            map = maps[int(s[0])]
            site = mapSites[map][int(s[1])]
            side = int(s[2])
            outcome = int(s[3])

            if side == 0:
                if outcome == 0:
                    site.aWins += 1
                else:
                    site.aLosses += 1
            else:
                if outcome == 0:
                    site.dWins += 1
                else:
                    site.dLosses += 1

    # Pick map
    while True:
        for i, m in enumerate(maps):
            print("{}: {}".format(i, m))
        print("\nWhich map # would you like to view stats of?\n: ", end='')

        mapChoice = int(input())
        if mapChoice >= 0 and mapChoice < len(maps):
            break
    print()

    for _, site in enumerate(mapSites[maps[mapChoice]]):
        aWinrate = -1
        dWinrate = -1
        totalARounds = site.aWins+site.aLosses
        totalDRounds = site.dWins+site.dLosses
        if site.aWins > 0:
            aWinrate = 100
        if site.dWins > 0:
            dWinrate = 100
        if site.aLosses > 0:
            aWinrate = (site.aWins/(site.aWins+site.aLosses)) * 100
        if site.dLosses > 0:
            dWinrate = (site.dWins/(site.dWins+site.dLosses)) * 100
        
        # Print results
        print("\t{} - Attack: {}% ({} Rounds) | Defense: {}% ({} Rounds)".format(site.name, aWinrate, totalARounds, dWinrate, totalDRounds))

            

if __name__ == "__main__":
    main()
