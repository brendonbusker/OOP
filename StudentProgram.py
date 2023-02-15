import StudentClass as s

def main():
    person1 = s.Student(69, "Sally", "5/21/2001", "Sr")

    person1.determine_age()
    person1.determine_register()

    print(f"{person1.get_name()}'s register time is: {person1.get_register()}")

    print(f"{person1.get_name()}'s age is: {person1.get_age()}")
    #print(person.get_age())


main()