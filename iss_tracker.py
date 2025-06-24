import requests
import datetime
import os
import turtle
#import geocoder
import time 
from tabulate import tabulate
def get_iss_position(log_func, save_func, gui_output_func=None):
    """Fetches the current position of the International space station, logs the request,
    saves the data to a file, and optionaly displays it in a turtle graphics window."""
    url = "http://api.open-notify.org/iss-now.json"
    module_name = "iss_tracker.py"
    try:
        # Make a http GET request to the ISS API
        response = requests.get(url)    
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        log_func(module_name, url, "SUCCESS")
        timestamp_utc = datetime.datetime.fromtimestamp(data['timestamp'], tz=datetime.timezone.utc)
        # Extract latitude and longitude from the response
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        # Log the fetched data
        table_data = [
            ["Timestamp (UTC)", timestamp_utc.strftime("%Y-%m-%d %H:%M:%S")],
            ["Latitude", f"{latitude}°"],
            ["Longitude", f"{longitude}°"]
        ]
        # Print the data in a table format
        print("\n--- ISS Real-Time Position ---")
        print(tabulate(table_data, tablefmt="plain"))
        print("-----------------------------")
        iss_info_to_save = (
            f"--- ISS Position at {timestamp_utc.strftime('%Y-%m-%d %H:%M:%S')} UTC ---\n"
            f"Latitude: {latitude}°, Longitude: {longitude}°\n"
            f"-----------------------------\n"
        )
        # Optionally display the data in a GUI window
        save_func("data/iss_data.txt", iss_info_to_save)
        def setup_turtle_map(iss_icon_path="images/iss.gif", map_path="images/map.gif"):
            screen = turtle.Screen()
            screen.setup(width=720, height=360)
            screen.title("ISS Tracker")
            screen.setworldcoordinates(-180, -90, 180, 90)
            if os.path.exists(map_path):
                try:
                    screen.bgpic(map_path)
                except turtle.TurtleGraphicsError as e:
                    print(f"Error: Failed to load map image {map_path}. Using default background. Error: {e}")
                screen.bgcolor("lightblue")  # Fallback background color
            else:
                print(f"Map image not found at {map_path}. Using default background.")
                screen.bgcolor("lightblue")
            if os.path.exists(iss_icon_path):
                try:
                    screen.register_shape(iss_icon_path)
                    iss_shape_name = iss_icon_path
                except turtle.TurtleGraphicsError:
                    print(f"Warning: ISS icon not found at {iss_icon_path}. Using default turtle shape.")
                    iss_shape_name = "square"
            else:
                iss_shape_name = "square"
            iss_turtle = turtle.Turtle()    # Create a turtle for the ISS
            iss_turtle.shape(iss_shape_name)    # Set the shape of the turtle to the ISS icon
            iss_turtle.setheading(90)  # Point north
            iss_turtle.penup()  # Don't draw lines
            iss_turtle.speed(0)  # Fastest drawing
            return iss_turtle, screen   
        # Setup the turtle graphics window and draw the ISS position
        iss_turtle, screen = setup_turtle_map()
        iss_turtle.goto(float(longitude), float(latitude))
        #try:
        #    #g = geocoder.osm([float(latitude), float(longitude)], method='reverse')
        #    if g.ok and g.address:
        #        print(f"Approx.Location: {g.address}")
        #except Exception as geo_e:
        #    print(f"Could not reverse geocode location: {geo_e}")
        import time
        time.sleep(5)  # Keep the window open for a while
        turtle.bye()
        return True
    # Handle potential errors during the request and data processing
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS position: {e}")
        log_func(module_name, url, "FAILURE", f"RequestError: {e}")
        return False
    except KeyError as e:
        print(f"Error parsing ISS position data: Missing expected key {e}")
        log_func(module_name, url, "FAILURE", f"KeyError: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while fetching ISS position: {e}")
        log_func(module_name, url, "FAILURE", f"Unexpected Error: {e}")
        return False
if __name__ == "__main__":
    # Example usage
    print("Running iss_tracker.py directly for testing purposes.")
    def dummy_log(*args, **kwargs):
        print(f"Dummy log: {args}")
    def dummy_save(*args, **kwargs):
        print(f"Dummy save: {args}")
    get_iss_position(dummy_log, dummy_save)
    
        
