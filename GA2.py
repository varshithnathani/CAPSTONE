import numpy as np
import time
import pandas as pd
import os

# Data: [Heart Rate, Pulse, Hemoglobin, Platelets]
data = np.array([
    [72, 75, 14.5, 250],
    [80, 78, 13.0, 300],
    [65, 70, 15.2, 220],
    [90, 85, 12.5, 280],
    [75, 77, 14.0, 350],
    [68, 72, 13.8, 275],
    [82, 80, 12.0, 290],
    [78, 79, 15.0, 260],
    [70, 74, 14.3, 230],
    [85, 82, 13.5, 310]
])

# Normal ranges for health metrics
NORMAL_RANGES = {
    'Heart Rate': (60, 100),
    'Pulse': (60, 100),
    'Hemoglobin': (13.0, 17.0),
    'Platelets': (150, 450)
}

# New dataset to store entries with deviations
deviation_data = []

def check_deviations(data):
    """Check for deviations from normal health ranges."""
    deviations = []
    for entry in data:
        heart_rate, pulse, hemoglobin, platelets = entry
        entry_deviation = False
        
        if not (NORMAL_RANGES['Heart Rate'][0] <= heart_rate <= NORMAL_RANGES['Heart Rate'][1]):
            deviations.append(('Heart Rate', heart_rate))
            entry_deviation = True
        
        if not (NORMAL_RANGES['Pulse'][0] <= pulse <= NORMAL_RANGES['Pulse'][1]):
            deviations.append(('Pulse', pulse))
            entry_deviation = True
        
        if not (NORMAL_RANGES['Hemoglobin'][0] <= hemoglobin <= NORMAL_RANGES['Hemoglobin'][1]):
            deviations.append(('Hemoglobin', hemoglobin))
            entry_deviation = True
        
        if not (NORMAL_RANGES['Platelets'][0] <= platelets <= NORMAL_RANGES['Platelets'][1]):
            deviations.append(('Platelets', platelets))
            entry_deviation = True
        
        if entry_deviation:
            deviation_data.append(entry)

    return deviations

def save_deviation_data():
    """Save the deviation data to a CSV file in the Downloads folder."""
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_path, 'deviation_data.csv')
    
    if deviation_data:
        df = pd.DataFrame(deviation_data, columns=['Heart Rate', 'Pulse', 'Hemoglobin', 'Platelets'])
        df.to_csv(file_path, index=False)
        print(f"Deviation data saved to '{file_path}'.")
        print(df)
    else:
        print("No deviation data to save.")

def continuous_monitoring(interval=10):
    """Monitor health parameters continuously."""
    print("Starting continuous monitoring...")  # Debug statement
    while True:
        print("Checking deviations...")  # Debug statement
        deviations = check_deviations(data)
        if deviations:
            print("Deviations detected:")
            for metric, value in deviations:
                print(f"{metric}: {value}")
            print("Entries with deviations stored in deviation_data.")
            save_deviation_data()
        else:
            print("All parameters are within normal ranges.")

        time.sleep(interval)

# Start monitoring
continuous_monitoring(10)  # Checks every 10 seconds
