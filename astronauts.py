import requests
import datetime
from tabulate import tabulate
def get_astronauts(log_func, save_func): # Function to fetch current astronauts in space from Open Notify API
    url = "http://api.open-notify.org/astros.json"
    module_name = "astronauts.py"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        log_func(module_name, url, "SUCCESS")
        headers = ["Name", "Craft"]
        table_data = []
        current_time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        astronaut_info_to_save = f"--- Astronauts in space at {current_time_str} ---\n"
        if data and 'people' in data: # Check if 'people' key exists in the response
            for p in data['people']: # Iterate through each astronaut
                name = p.get('name', 'N/A')
                craft = p.get('craft', 'N/A')
                table_data.append([name, craft])
                astronaut_info_to_save += f"- {name} is currently on the {craft} spacecraft.\n"
            astronaut_info_to_save += "-----------------------------\n"
        else: # If no astronaut data is found, append a message to the table
            table_data.append(["No astronaut data found", "N/A"])
            astronaut_info_to_save += "No astronaut data found.\n------------------------------\n"
        print("\n--- Astronauts currently in Space ---")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("-----------------------------")
        save_func("data/iss_data.txt", astronaut_info_to_save)
        print("Astronaut data saved to data/iss_data.txt")
        return True # Successfully fetched and displayed astronaut data
    # Handle specific exceptions
    except requests.exceptions.RequestException as e:
        print(f"Error fetching astronaut data: {e}")
        log_func(module_name, url, "FAILURE", f"JSONDecodeError: {e}")
        return False
    except KeyError as e:
        print(f"Error parsing astronaut data: Missing expected key {e}")
        log_func(module_name, url, "FAILURE", f"KeyError: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while fetching astronaut data: {e}")
        log_func(module_name, url, "FAILURE", f"Unexpected Error: {e}")
        return False


    
    
