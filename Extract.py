from Session import Session
from DataProcessor import DataProcessor
import sys

login_url = "https://community.grainfather.com/login"
data_url = 'https://community.grainfather.com/my-brews/data'

# Assign login credentials
email = sys.argv[1]
password = sys.argv[2]

session_instance = Session.new(email, password,login_url)

# Example usage
if isinstance(session_instance, Session):
    data_processor = DataProcessor(session_instance, data_url)
    all_data = data_processor.fetch_all_brew_data()
    if all_data:
        data_processor.save_data_to_json_and_csv(all_data)
        print("Data saved.")
    else:
        print("Failed to fetch data or no data to save.")
else:
    print(session_instance)  # Login error message
