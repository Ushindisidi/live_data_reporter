# Live Data Reporter

## Project Overview

The Live Data Reporter is a Python-based command-line interface (CLI) application designed to fetch and display real-time or near real-time data from various public APIs. This project demonstrates how to interact with external web services, process JSON data, display information in a user-friendly, tabulated format, and even visualize data using Python's turtle graphics module.

Currently, the application supports:

* Astronaut Tracking: Fetches and displays the number of astronauts currently in space and their names.
* ISS Real-Time Position: Retrieves the International Space Station's current latitude, longitude, and timestamp, displaying it in the console and visualizing its position on a world map using turtle graphics.
* Top U.S. Business Headlines: Fetches and displays the latest top U.S. business news headlines from the NewsAPI.

## Features

* API Integration: Connects to Open-Notify API (for ISS and astronauts) and NewsAPI.
* Tabulated Output: Presents data in a clean, readable table format using the tabulate library.
* Environmental Variables: Securely manages API keys using .env files and python-dotenv.
* Data Logging: Logs API interactions and potential errors to a logs.txt file.
* Data Saving: Saves ISS position data to iss_data.txt.
* Interactive Menu: Provides a simple command-line menu for easy navigation.
* Graphical Visualization: Uses turtle graphics to display the ISS position on a world map.

## Technologies Used

* Python 3.13.5
* requests library: For making HTTP requests to APIs.
* python-dotenv library: For loading environment variables from .env files.
* tabulate library: For pretty-printing data in table format.
* turtle module: Python's built-in graphics module for visualization.

## Setup and Installation

Follow these steps to get the Live Data Reporter running on your local machine.

### 1. Clone the Repository

https://github.com/Ushindisidi/live_data_reporter.git

### 2. Create a Virtual Environment (Recommended)

It's good practice to use a virtual environment to manage project dependencies.

```bash
python -m venv venv

3. Activate the virtual environment
```bash
source venv/scripts/activate

4. Install dependencies
Install the required python libraries using pip:
``` bash
pip install -r requirements.text

5. Set up API Keys
This project uses NewsAPI, which requires an API key.
   Go to NewsAPI.org and sign up for a free developer account to get your API key.
   In the root directory of your project (e.g., live-data-reporter/), create a new file named .env.
   Add your NewsAPI key to this file in the following format:
   NEWS_API_KEY=your_news_api_key_here

   (Replace your_news_api_key_here with the actual key you obtained).
6. Prepare Images for ISS Tracker (Important!)
The ISS tracker uses image files for the world map and the ISS icon.
  In the root of your project, create a new directory named images/.
  Find or create two .gif image files:
    map.gif: A world map image.
    iss.gif: An icon for the International Space Station.
  Place these .gif files inside the live-data-reporter/images/ directory.
   Your project structure should look like this:
   live-data-reporter/
├── data/
│   └── iss_data.txt
├── images/
│   ├── iss.gif
│   └── map.gif
├── .env
├── astronauts.py
├── iss_tracker.py
├── main.py
├── news_or_stock.py
├── logs.txt
├── README.md
└── requirements.txt

   Note: Ensure map.gif and iss.gif are actual, non-animated .gif files, as the turtle module can be particular about image formats.
How to Run
  Make sure your virtual environment is activated.
  Navigate to the root directory of the live-data-reporter project in your terminal.
  Run the main application script:
   python main.py

Project Structure
live-data-reporter/
├── data/
│   └── iss_data.txt        # Saved ISS position data
├── images/
│   ├── iss.gif             # ISS icon for turtle visualization
│   └── map.gif             # World map background for turtle visualization
├── .env                    # Environment variables (e.g., API keys)
├── astronauts.py           # Module to fetch and display astronaut data
├── iss_tracker.py          # Module to track ISS position and display on map
├── main.py                 # Main application entry point and menu
├── news_or_stock.py        # Module to fetch and display business headlines
├── logs.txt                # Log file for API interactions
├── README.md               # This README file
└── requirements.txt        # Python dependencies

Troubleshooting
  NEWS_API_KEY not found error: Ensure you have a .env file in the root directory with NEWS_API_KEY=your_key inside it.
  Images not displaying for ISS Tracker:
    Confirm map.gif and iss.gif are in the images/ directory within your project root.
    Ensure they are true .gif files (not just renamed .png or .jpg). turtle can be picky.
    Run python in your project root and test import os; print(os.path.exists("images/map.gif")) to verify the path. Both should print True.
  Network errors: Check your internet connection. API endpoints might also have rate limits or be temporarily down.
  Status code 403 from nominatim.openstreetmap.org: This error occurs if the geocoder library is used without proper authentication or if the service is blocking requests. The current iss_tracker.py has this part commented out to avoid issues.
AUTHOR
Ushindi Sidi❤
