import random


def selectrand(a, b=1):
    # Allow for user to specify how many elements they want to choose but default to 1
    if b == 1:
        element = random.choice(a)
    else:
        element = random.choices(a, k=b)
    return element