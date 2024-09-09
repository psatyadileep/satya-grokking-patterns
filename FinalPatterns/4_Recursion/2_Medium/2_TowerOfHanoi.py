def tower_of_hanoi_steps(n, source, auxiliary, target):
    if n == 1:
        return 1  # Only one move required for a single disk

    # Calculate the number of steps required
    steps = 0

    # Steps to move top n-1 disks from source to auxiliary
    steps += tower_of_hanoi_steps(n - 1, source, target, auxiliary)

    # One step to move the nth disk from source to target
    steps += 1

    # Steps to move n-1 disks from auxiliary to target
    steps += tower_of_hanoi_steps(n - 1, auxiliary, source, target)

    return steps


# Example usage:
n = 3  # Number of disks
steps_required = tower_of_hanoi_steps(n, 'A', 'C', 'B')
print(f"Total steps required for {n} disks: {steps_required}")
