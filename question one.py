name = input()
length = int(input())
width = int(input())
height = int(input())
volume = (length*width*height)
volume2 = (3.14*((width // 2)**2))*height
gallon = volume*7.5
gallon2 = volume2*5.875
print(name, gallon)

