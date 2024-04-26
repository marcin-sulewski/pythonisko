red = int(input("Wpisz wartość czerwonego (0 - 255): "))
green = int(input("Wpisz wartość zielonego (0 - 255): "))
blue = int(input("Wpisz wartość niebieskiego (0 - 255): "))


hex_color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)

print("Kolor w kodzie hexadecymalnym to: ", hex_color_code)
