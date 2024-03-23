import json
import pandas as pd

class DataProcessor:
    def __init__(self, session_instance, data_url):
        self.session_instance = session_instance
        self.data_url = data_url

    def fetch_all_brew_data(self):
        all_data = []
        next_url = self.data_url

        while next_url:
            data = self.session_instance.fetch_brew_data(next_url)

            if isinstance(data, dict) and data.get("data"):
                all_data.extend(data.get("data"))  # Assuming the relevant data is under "data" key
                next_url = data.get("next_page_url", None)
                if not next_url:
                    break  # Exit loop if there's no next page
                print(f"next:{next_url}")
            else:
                print("Failed to fetch or parse data")
                return None

        return all_data

    def save_data_to_json_and_csv(self, data, json_filename='brew_data.json', csv_filename='brew_data.csv'):
        # Save to JSON
        with open(json_filename, 'w') as jsonfile:
            json.dump(data, jsonfile)

        # Convert to DataFrame and save to CSV
        df = pd.DataFrame(data)
        columns = [
            "id", "batch_number", "session_name", "original_gravity", "final_gravity",
            "created_at", "updated_at", "fermentation_start_date", "recipe_id",
            "notes", "name", "status"
        ]
        df_filtered = df[columns]
        df_filtered.to_csv(csv_filename, index=False)

# Example usage (assuming session_instance and data_url are defined)
# data_processor = DataProcessor(session_instance, 'https://community.grainfather.com/my-brews/data')
# all_data = data_processor.fetch_all_brew_data()
# if all_data:
#     data_processor.save_data_to_json_and_csv(all_data)
#     print("Data saved.")
