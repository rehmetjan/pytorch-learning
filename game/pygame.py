# nothing here yet
# print "hello world" in deutch (german) using python3
print("Hallo Welt")
# never use python 2 print syntax in python 3
# print "Hallo Welt" # this is python 2 syntax
# print "nice to meet you" in deutch (german) using python3
print("Schön dich kennenzulernen")
# print how many packages are installed in python path
import sys

print(sys.path)
# count the packages in python path
print(len(sys.path))


def find_roots(a, b, c):
    """Return roots of the quadratic equation ax**2 + bx + c = 0."""
    # calculate the discriminant
    import math
    disc = b**2 - 4 * a * c
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        return root1, root2
    elif disc == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return None, None


# test find_roots
print(find_roots(2, 10, 8))
