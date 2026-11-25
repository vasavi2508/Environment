
# Environmental Monitoring Data Analyzer

def classify_reading(value, warning_limit, critical_limit):
    if value <= warning_limit:
        return "Normal"
    elif value <= critical_limit:
        return "Warning"
    else:
        return "Critical"


def analyze_data(stations, readings, warning_limit, critical_limit):

    total_readings = 0
    total_sum = 0

    print("\n========== ENVIRONMENTAL MONITORING REPORT ==========")

    for i in range(len(stations)):

        print("\nMonitoring Station:", stations[i])

        station_readings = readings[i]

        average = sum(station_readings) / len(station_readings)
        maximum = max(station_readings)
        minimum = min(station_readings)

        print("Readings:", station_readings)
        print("Average Reading:", round(average, 2))
        print("Maximum Reading:", maximum)
        print("Minimum Reading:", minimum)

        print("\nObservation Classification:")

        for value in station_readings:
            category = classify_reading(
                value, warning_limit, critical_limit
            )

            print(value, "->", category)

        total_sum += sum(station_readings)
        total_readings += len(station_readings)

    overall_average = total_sum / total_readings

    print("\n========== OVERALL SUMMARY ==========")
    print("Total Monitoring Stations:", len(stations))
    print("Total Readings:", total_readings)
    print("Overall Average:", round(overall_average, 2))


# Main Program

print("ENVIRONMENTAL MONITORING DATA ANALYZER")

stations = ["Station A", "Station B", "Station C"]

# Nested list containing environmental readings
readings = [
    [25, 30, 35, 28],
    [45, 55, 60, 50],
    [70, 80, 65, 90]
]

print("\nEnter the threshold values")

warning_limit = float(input("Enter warning threshold: "))
critical_limit = float(input("Enter critical threshold: "))

if warning_limit >= critical_limit:
    print("Invalid thresholds! Warning must be less than critical.")
else:
    analyze_data(
        stations,
        readings,
        warning_limit,
        critical_limit
    )
