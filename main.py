# Converts Liter

print("This program converts liter numbers.")
print()


def Volume(value):
    if value >= 1.0:
        print("The value is" + " " + str(value) + " " + "l" + ".")
    elif value >= 0.1:
        print("The value is" + " " + str(value) + "0" + " " + "cl" + ".")
    elif value >= 0.001:
        value = value * 1000
        print("The value is" + " " + str(value) + " " + "ml" + ".")
    elif value < 0.001:
        print("The value is too small.PLease try again.")


# Path: main.py --------------------------------------

Volume(0)
