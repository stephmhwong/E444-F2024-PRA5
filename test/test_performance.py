import requests
import time
import pandas as pd

# Change this to your actual endpoint
url = 'http://serve-sentiment-env.eba-qjvk43at.us-east-1.elasticbeanstalk.com/predict'

# Test cases
test_cases = [
    "The moon landing was staged by NASA.",
    "Aliens have been living among us for years.",
    "The president signed a new bill into law.",
    "Scientists discover a new species of frog in the Amazon."
]

# Prepare DataFrame to record the results
results = []

for text in test_cases:
    for _ in range(100):
        start_time = time.time()
        response = requests.post(url, json={"text": text})
        end_time = time.time()
        
        if response.status_code == 200:
            latency = end_time - start_time
            results.append({"text": text, "latency": latency})

# Create a DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv('latency_results.csv', index=False)
print("Latency results saved to 'latency_results.csv'")
