import sys

g = sys.argv[1]
g = int(sys.argv[1])

if g >= 200:
    print("Super Typhoon")
elif g <= 61:
    print("Tropical Depression")
elif g == 118 or g <=220:
    print("typhoon")
elif g == 89 or g <= 117:
    print("severe tropical storm")

elif g == 62 or g <= 88:
    print("Tropical Storm")