import requests
import json

# URL for the Flask API endpoint
url = "http://ddos-detection-service.eastus.azurecontainer.io:5000/score"


# Example payload with dummy data for all features
data = [
    {
        " Destination Port": 80,
        " Flow Duration": 5000,
        " Total Fwd Packets": 20,
        "Total Length of Fwd Packets": 1500,
        " Fwd Packet Length Max": 800,
        " Fwd Packet Length Min": 200,
        "Bwd Packet Length Max": 600,
        " Bwd Packet Length Min": 100,
        "Flow Bytes/s": 1000000,
        " Flow Packets/s": 200,
        " Flow IAT Mean": 300,
        " Flow IAT Min": 100,
        " Fwd IAT Mean": 250,
        " Fwd IAT Min": 150,
        "Bwd IAT Total": 400,
        " Bwd IAT Mean": 200,
        " Bwd IAT Std": 50,
        " Bwd IAT Max": 250,
        " Bwd IAT Min": 100,
        "Fwd PSH Flags": 0,
        " Fwd URG Flags": 0,
        "Fwd Packets/s": 300,
        " Bwd Packets/s": 150,
        " Min Packet Length": 100,
        " Max Packet Length": 1200,
        "FIN Flag Count": 1,
        " SYN Flag Count": 0,
        " RST Flag Count": 0,
        " PSH Flag Count": 1,
        " ACK Flag Count": 1,
        " URG Flag Count": 0,
        " CWE Flag Count": 0,
        " ECE Flag Count": 0,
        " Down/Up Ratio": 1,
        "Subflow Fwd Packets": 10,
        " Subflow Fwd Bytes": 500,
        "Init_Win_bytes_forward": 3000,
        " Init_Win_bytes_backward": 2000,
        " act_data_pkt_fwd": 5,
        " min_seg_size_forward": 32,
        "Active Mean": 200,
        " Active Std": 50,
        "Idle Mean": 400,
        " Idle Std": 75,
        " Idle Min": 200
    }
]

# Send POST request
response = requests.post(url, json=data)

# Output response
print(f"Response Status Code: {response.status_code}")
if response.status_code == 200:
    print("Response JSON:")
    print(response.json())
else:
    print("Error occurred:", response.text)
