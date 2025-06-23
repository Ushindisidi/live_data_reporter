import sys
import os
import datetime
from dotenv import load_dotenv
from astronauts import get_astronauts
from iss_tracker import get_iss_position
from news_or_stock import get_business_headlines
def log_api_interaction(module_name, endpoint, status, message=""):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Module: {module_name}, Endpoint: {endpoint}, Status: {status}, Message: {message}\n"
    try:
        with open("logs.txt", "a") as f:
            f.write(log_entry)
    except IOError as e:
        print(f"Error writing to log file: {e}")
def save_data(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "a") as f:
            f.write(f"{data}\n")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
def display_menu():
    print("Welcome to to Live Data Reporter!")
    print("Please choose an option:")
    print("1. View Astronauts in space")
    print("2. Track ISS Position")
    print("3. view top U.S. Business Headlines")
    print("4. Exit")
    print("-------------------------------")
def main():
    load_dotenv()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            print("Fetching astronauts in space...")
            get_astronauts(log_api_interaction, save_data)
        elif choice == "2":
            print("Fetching ISS position...")
            get_iss_position(log_api_interaction, save_data)
        elif choice == "3":
            print("Fetching top U.S. business headlines...")
            get_business_headlines(log_api_interaction)
        elif choice == "4":
            print("Exiting the live data reporter. Goodbye!")
            break
        else:
            print("Invalid choice. please enter a number between 1 and 4.")
        print("-------------------------------")
if __name__ == "__main__":
    main()







