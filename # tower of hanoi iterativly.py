# tower of hanoi iterativly
def towerOfHanoiIterative(n, source, target, auxiliary):
    if n % 2 == 0:
        auxiliary, target = target, auxiliary
    pegs = [source, auxiliary, target]
    moves = [(0, 1), (0, 2), (1, 2)]
    for i in range(1, 2 ** n):
        move = moves[(i & (i - 1)) % 3]
        print("Move disk from peg", pegs[move[0]], "to peg", pegs[move[1]])

# Example usage
n = 3  # Number of disks
towerOfHanoiIterative(n, 'A', 'C', 'B')  # A, B, and C are the names of the pegs
