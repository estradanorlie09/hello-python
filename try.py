# for c in "hello!":
#     print (c)
numbers = []
for x in range(10):
    
    numbers.append(x)
    print(numbers)

    numbers2 =[x for x in range(10)]
    print(numbers2)
import sys

Wind = sys,argv[1]
Wind = int(sys.argv[1])


if windintensity == 200:
    print("Super Typhoon")
elif windintensity == 89 or windintensity == 177:
    print("severiral tropical storm")
elif windintensity == 62 or windintensity == 88:
    print("Tropical Storm")
elif windintensity >= 61:
    print("Tropical Depression")
elif windintensity >= 118 or windintensity <= 220:
    print("typhoon")