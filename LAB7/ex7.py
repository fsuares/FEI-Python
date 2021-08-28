from math import acos, sin, cos, radians

def distancia(latA, lonA, latB, lonB):
    dist = 6371.01 * acos((sin(radians(latA)) * sin(radians(latB))) + (cos(radians(latA)) * cos(radians(latB))) * cos(
        radians(lonA) - radians(lonB)))
    return dist

def main():
    latA = float(input("Digite a latitude A: "))
    lonA = float(input("Digite a longitude A: "))
    latB = float(input("Digite a latitude B: "))
    lonB = float(input("Digite a longitude B: "))

    print("A distância é {:.2f}km.".format(distancia(latA,lonA,latB,lonB)))


main()
