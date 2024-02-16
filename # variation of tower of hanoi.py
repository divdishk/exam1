# variation of tower of hanoi
def towerOfHanoi(n, source, target, auxiliaryPegs):
    # base case: if only one disk to move, move it directly from fource to target
    if n == 1:
        print("Move disk 1 from peg", source, "to peg", target)
        return
    # Chooses an auxiliary peg not equal to source or target
    auxiliary = (set(range(len(auxiliaryPegs))) - {source, target}).pop()
    # moves n-1 disks from source to auxiliary using auxiliary peg has the target
    towerOfHanoi(n-1, source, auxiliary, auxiliaryPegs)
    # moves  the remaining disk from source to target
    print("Move disk", n, "from peg", source, "to peg", target)
    #moves n-1 disks from auxiliary to target using source as the auxiliary peg
    towerOfHanoi(n-1, auxiliary, target, auxiliaryPegs)

numPegs = 5 # no. of pegs
n = 4 # no. of disks
# calls the towerOfHanoi function 
towerOfHanoi(n, 0, numPegs -1, list(range(1, numPegs)))  