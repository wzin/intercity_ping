import argparse
import subprocess
import time
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


class PingTester:
    def __init__(self, interval, timeout, address, csv_file_name='ping_results.csv'):
        self.interval = interval
        self.timeout = timeout
        self.address = address
        self.csv_file_name = csv_file_name

    def run(self):
        with open(self.csv_file_name, mode='a', newline='') as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(['Timestamp', 'Response Time (s)'])

            while True:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                try:
                    start_time = time.time()
                    subprocess.check_output(['ping', '-c', '1', '-W', str(self.timeout), self.address])
                    response_time = time.time() - start_time
                except subprocess.CalledProcessError:
                    response_time = self.timeout

                print(f"Response time: {response_time}")
                writer.writerow([timestamp, response_time])
                file.flush()
                time.sleep(self.interval)


def plot_results(csv_file_name):
    timestamps = []
    response_times = []
    with open(csv_file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            timestamps.append(row[0])
            response_times.append(float(row[1]))

    plt.plot(timestamps, response_times, marker='o')
    plt.xticks(rotation=45)
    plt.ylabel('Response Time (s)')
    plt.title('Ping Response Times')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ping Tester')
    parser.add_argument('--interval', type=int, default=10, help='Interval between pings in seconds')
    parser.add_argument('--timeout', type=int, default=10, help='Timeout for each ping in seconds')
    parser.add_argument('--address', type=str, default='1.1.1.1', help='Remote server address')
    parser.add_argument('--plot', action='store_true', help='Plot results using matplotlib and numpy')

    args = parser.parse_args()

    tester = PingTester(args.interval, args.timeout, args.address)

    if args.plot:
        plot_results(tester.csv_file_name)
    else:
        tester.run()

