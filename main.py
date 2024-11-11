def main():

    totalRain = 0.0
    totalWind = 0.0
    days = 0

    while True:

        userInput = input("Enter rain (in inches) and wind (in mph), or type -1.0 to stop: ")


        if userInput == "-1.0":
            break


        try:
            rain, wind = userInput.split()
            rain = float(rain)
            wind = float(wind)


            totalRain += rain
            totalWind += wind
            days += 1
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue


    if days > 0:
        avgRain = totalRain / days
        avgWind = totalWind / days


        severity = (avgRain * 10) + avgWind


        print("The average rain is", round(avgRain, 1), "inches")
        print("The average wind is", round(avgWind, 1), "mph")
        print("The weather severity for these", days, "days is:", round(severity, 1))
    else:
        print("No data was entered.")


if __name__ == "__main__":
    main()