import InsectClass as i

def main():

    mosquito = i.Insect("mosquito", 2, 4)
    houseFly = i.Insect("housefly", 2, 4)

    mosquito.flight_length()
    houseFly.flight_length()

    print(f"the {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles")
    print(f"the {houseFly.get_name()} can fly up to {houseFly.get_miles()} miles")


main()