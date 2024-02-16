# Hanoi's Tower using Recursion
def towerOfHanoi(n, source, target, auxiliary):
    # base case: if only one disk to move, move it directly from fource to target
    if n == 1:
        print("Move disk 1 from peg", source, "to peg", target)
        return
    # moves n-1 disks from source to auxiliary using auxiliary peg has the target
    towerOfHanoi(n-1, source, auxiliary, target) # recursion
    # moves  the remaining disk from source to target
    print("Move disk", n, "from peg", source, "to peg", target)
    #moves n-1 disks from auxiliary to target using source as the auxiliary peg
    towerOfHanoi(n-1, auxiliary, target, source) # recursion

# Example usage
n = 3  # Number of disks
towerOfHanoi(n, 'A', 'C', 'B')  # A, B, and C are the names of the pegs
          