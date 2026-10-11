def hanoi_solver(disks: int):
    start = []
    helper = []
    destination = []
    moves = []
    
    for i in range(disks, 0, -1):
        start += [i]

    moves.append(f"{start} {helper} {destination}\n")
    
    def move(n, source, support, target):
        if n == 1:
            target.append(source.pop())
            moves.append(f"{start} {helper} {destination}\n")
        else:
            move(n - 1, source, target, support)
            move(1, source, support, target)
            move(n - 1, support, source, target)

    move(disks, start, helper, destination)
    return "".join(moves).strip()