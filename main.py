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
    "Clubhouse": [""], 
    "Coastline": [""], 
    "Consulate": [""],
    "Kafe": [""], 
    "Oregon": [""], 
    "Theme Park": [""], 
    "Villa": [""]
}

def main():
    while True:
        print("Welcome to R6 WL Tracker\n")
        print("Maps:\t", end='')
        for i, m in enumerate(maps):
            print("{}: {}".format(i, m), end='; ')
        print("\nWhich map # did you play?\n: ", end='')

        mapChoice = int(input())
        if mapChoice >= 0 and mapChoice < len(maps):
            break
    print(maps[mapChoice])

if __name__ == "__main__":
    main()
