# GUI of TOH
import sys
import time

class TowerOfHanoi:
    def __init__(self, numDiscs, speed):
        # intializes the no. of discs and speed
        self.numDiscs = numDiscs
        self.speed = speed

    def moveDisc(self, source, target):
        # move disc from source peg to target peg
        print(f"Move disc from peg {source} to peg {target}")
        time.sleep(self.speed)

    def towerOfHanoi(self, n, source, target, auxiliary):
        # function uses recursion to solve tower of hanoi
        if n == 0:
            return
        self.towerOfHanoi(n - 1, source, auxiliary, target)
        self.moveDisc(source, target)
        self.towerOfHanoi(n - 1, auxiliary, target, source)

    def start(self):
        # starts TOH with specifed discs and pegs
        self.towerOfHanoi(self.numDiscs, 'A', 'C', 'B')

def main(numDiscs, speed):
    print("Tower of Hanoi")

    hanoi = TowerOfHanoi(numDiscs, speed)
    hanoi.start()

if __name__ == "__main__":
    # checks if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <num_discs> <speed>")
        sys.exit(1)
    
    numDiscs = int(sys.argv[1])
    speed = float(sys.argv[2])

    main(numDiscs, speed)

