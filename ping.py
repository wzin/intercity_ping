import subprocess
import time
import csv
from datetime import datetime

# Set the interval X (in seconds) between pings
X = 10

# Set the timeout Y (in seconds) for each ping
Y = 10

# address
address = '1.1.1.1'

# Define the CSV file name
csv_file_name = 'ping_results.csv'

# Open the CSV file in write mode
with open(csv_file_name, mode='a', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the header row to the CSV file
    writer.writerow(['Timestamp', 'Response Time (s)'])
    
    # Start the infinite loop to keep pinging at intervals of X seconds
    while True:
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            # Execute the ping command and measure the response time
            print("Ping")
            start_time = time.time()
            subprocess.check_output(['ping', '-c', '1', '-W', str(Y), address])
            response_time = time.time() - start_time
            print(f"Response time: #{response_time}")
        except subprocess.CalledProcessError:
            # If ping command fails (e.g., no internet), set response time to Y seconds
            response_time = Y
        
        # Log the timestamp and response time to the CSV file
        writer.writerow([timestamp, response_time])
        file.flush()
        
        # Sleep for X seconds before the next ping
        time.sleep(X)
