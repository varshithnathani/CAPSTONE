import numpy as np
import time

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
    'Heart Rate': (60, 100),      # Normal range: 60-100 bpm
    'Pulse': (60, 100),            # Normal range: 60-100 bpm
    'Hemoglobin': (13.0, 17.0),    # Normal range: 13-17 g/dL
    'Platelets': (150, 450)        # Normal range: 150-450 x 10^9/L
}

def check_deviations(data):
    """Check for deviations from normal health ranges."""
    deviations = []
    for entry in data:
        heart_rate, pulse, hemoglobin, platelets = entry
        
        if not (NORMAL_RANGES['Heart Rate'][0] <= heart_rate <= NORMAL_RANGES['Heart Rate'][1]):
            deviations.append(('Heart Rate', heart_rate))
        
        if not (NORMAL_RANGES['Pulse'][0] <= pulse <= NORMAL_RANGES['Pulse'][1]):
            deviations.append(('Pulse', pulse))
        
        if not (NORMAL_RANGES['Hemoglobin'][0] <= hemoglobin <= NORMAL_RANGES['Hemoglobin'][1]):
            deviations.append(('Hemoglobin', hemoglobin))
        
        if not (NORMAL_RANGES['Platelets'][0] <= platelets <= NORMAL_RANGES['Platelets'][1]):
            deviations.append(('Platelets', platelets))

    return deviations

# Continuous monitoring
def continuous_monitoring(interval=10):
    """Monitor health parameters continuously."""
    while True:
        deviations = check_deviations(data)
        if deviations:
            print("Deviations detected:")
            for metric, value in deviations:
                print(f"{metric}: {value}")
        else:
            print("All parameters are within normal ranges.")

        time.sleep(interval)  # Wait for the specified interval before checking again

# Start monitoring
continuous_monitoring(10)  # Checks every 10 seconds
