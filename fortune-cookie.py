# Copyright (c) 2014 [REDACTED]

# Exercise 3.1 from Dawson's "Python Programming for the Absolute Beginner (3d)"

import random

fortune = random.randrange(5) + 1

if fortune == 1: print("A good friend is hard to find.")
elif fortune == 2: print("Red is your lucky color.")
elif fortune == 3: print("Buy a lottery ticket tomorrow.")
elif fortune == 4: print("Don't go on a boat tomorrow.")
elif fortune == 5: print("True love is right around the corner.")
