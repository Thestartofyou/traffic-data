import random

# Simulating traffic data
def generate_traffic_data():
    # Generate random traffic values for each hour (0 to 23)
    traffic_data = [random.randint(10, 100) for _ in range(24)]
    return traffic_data

def analyze_traffic(traffic_data):
    peak_hours = []
    non_peak_hours = []

    for hour, traffic in enumerate(traffic_data):
        if traffic >= 80:  # Adjust threshold as per your definition of a traffic spike
            peak_hours.append(hour)
        else:
            non_peak_hours.append(hour)

    return peak_hours, non_peak_hours

# Example usage
traffic = generate_traffic_data()
peak_hours, non_peak_hours = analyze_traffic(traffic)

print("Peak Traffic Hours:")
for hour in peak_hours:
    print(f"Hour {hour}:00 - {hour+1}:00")

print("\nNon-Peak Traffic Hours:")
for hour in non_peak_hours:
    print(f"Hour {hour}:00 - {hour+1}:00")
