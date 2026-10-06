print("-----MOBILE SHOP MENU-----")

print("1. iPhone 15")
print("2. Samsung Galaxy S24")
print("3. OnePlus 12")
print("4. Google Pixel 8")
print("5. Redmi Note 13")

option = int(input("Enter your choice: "))

match option:

    case 1:
        print("Item        : iPhone 15")
        print("Price       : 70000")
        print("Description : Apple smartphone with A16 Bionic chip.")

    case 2:
        print("Item        : Samsung Galaxy S24")
        print("Price       : 65000")
        print("Description : Samsung smartphone with AMOLED display.")

    case 3:
        print("Item        : OnePlus 12")
        print("Price       : 60000")
        print("Description : OnePlus smartphone with powerful performance.")

    case 4:
        print("Item        : Google Pixel 8")
        print("Price       : 55000")
        print("Description : Google smartphone with an advanced camera.")

    case 5:
        print("Item        : Redmi Note 13")
        print("Price       : 20000")
        print("Description : Affordable smartphone with a high-quality display.")

    case _:
        print("Invalid Choice")

print("-----TELUGU MOVIE MENU-----")

print("1. Baahubali")
print("2. RRR")
print("3. Pushpa")
print("4. Arjun Reddy")
print("5. Jersey")

option = int(input("Enter your choice: "))

match option:

    case 1:
        print("Movie       : Baahubali")
        print("Price       : 250")
        print("Description : Historical action drama movie.")

    case 2:
        print("Movie       : RRR")
        print("Price       : 300")
        print("Description : Action drama movie about two freedom fighters.")

    case 3:
        print("Movie       : Pushpa")
        print("Price       : 250")
        print("Description : Action drama movie based on red sandalwood smuggling.")

    case 4:
        print("Movie       : Arjun Reddy")
        print("Price       : 200")
        print("Description : Romantic drama movie about a medical student.")

    case 5:
        print("Movie       : Jersey")
        print("Price       : 220")
        print("Description : Sports drama movie about a former cricketer.")

    case _:
        print("Invalid Choice")