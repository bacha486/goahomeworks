completed = 0
cancelled = 0
total_income = 0
total_km = 0
highest = 0
lowest = 0
over_20 = 0

while True:
    print ("""======= TAXI SYSTEM =======
    1. მგზავრობის შეკვეთა
    2. შემოსავლის ნახვა
    3. მგზავრობების სტატისტიკა
    4. გასვლა
    ===========================""")

    choice = input("Choose an option: ")

    if choice == "1":
        km = float(input("Distance (km): "))
        while km <= 0:
            print("Distance must be positive.")
            km = float(input("Distance (km): "))

        passengers = int(input("Number of passengers (1-4): "))
        while passengers < 1 or passengers > 4:
            print("Passengers must be from 1 to 4.")
            passengers = int(input("Number of passengers (1-4): "))

        night = input("Night ride? (yes/no): ")
        while night != "yes" and night != "no":
            print("Please type yes or no.")
            night = input("Night ride? (yes/no): ")

        base_and_distance = 2.50 + km * 0.70
        if passengers >= 3:
            base_and_distance += 3

        if night == "yes":
            night_extra = base_and_distance * 0.20
        else:
            night_extra = 0

        price = base_and_distance + night_extra

        print("====== Ride details ======")
        print("Distance: " + str(km) + " km")
        print("Passengers: " + str(passengers))
        print("Night ride: " + night)
        print("Base + distance: " + str(base_and_distance) + " GEL")
        print("Night extra: " + str(night_extra) + " GEL")
        print("Final price: " + str(price) + " GEL")
        print("==========================")

        confirm = input("Confirm the ride? (yes/no): ")
        while confirm != "yes" and confirm != "no":
            print("Please type yes or no.")
            confirm = input("Confirm the ride? (yes/no): ")

        if confirm == "yes":
            total_income += price
            total_km += km
            if completed == 0:
                highest = price
                lowest = price
            if price > highest:
                highest = price
            if price < lowest:
                lowest = price
            if price > 20:
                over_20 += 1
            completed += 1
            print("Ride completed successfully!")
        else:
            cancelled += 1
            print("Ride cancelled.")

    elif choice == "2":
        print("Total income: " + str(total_income) + " GEL")
        print("Completed rides: " + str(completed))
        if completed == 0:
            print("No completed rides yet.")
        else:
            print("Average price: " + str(total_income / completed) + " GEL")

    elif choice == "3":
        print("Completed rides: " + str(completed))
        print("Cancelled rides: " + str(cancelled))
        print("Total km: " + str(total_km))
        print("Total income: " + str(total_income) + " GEL")
        if completed == 0:
            print("No completed rides yet.")
        else:
            print("Average price: " + str(total_income / completed) + " GEL")
            print("Most expensive ride: " + str(highest) + " GEL")
            print("Cheapest ride: " + str(lowest) + " GEL")
            print("Rides over 20 GEL: " + str(over_20))

    elif choice == "4":
        break

    else:
        print("Invalid choice.")

print("Goodbye!")