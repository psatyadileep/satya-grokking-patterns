"""
Find th epossible combinations of dice thrown for a given target
"""
def Dice(target):
    def helper(p, target):
        if target == 0:
            print(p)
            return

        for i in range(1, 7):
            if target - i >= 0:
                helper(p + str(i), target - i)

    helper("", target)

# Call the function without using print because the function already prints the combinations
Dice(5)