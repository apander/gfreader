# Brew Data Extractor

This tool extracts brewing data and saves it into both JSON and CSV formats for easy analysis and review.

## Dependencies

The script relies on the `pyarrow` and `pandas` libraries for data processing and serialization. Ensure you have Python installed on your system before proceeding, v3.1x recommended.

To install the necessary Python package, run the following command in your terminal:

```bash
pip install pyarrow
pip install pandas
```

## Running the Script
Once the dependencies are installed, you can run the script to extract brewing data. Make sure you're in the same directory as the Extract.py script, then execute it with Python:

```bash
python Extract.py 'username' 'password'
```

The Grainfather username is typically an email address, remeber to escape special characters on the command line for the password.

## Output
Upon successful execution, the script generates two files in the current directory:
```bash
brew_data.csv: Contains the extracted brewing data in CSV format.
brew_data.json: Contains the extracted brewing data in JSON format.
```

These files can be used for further data analysis or review as needed.

##Customizing Extracted Columns
If you wish to extract more or different columns than the default, please modify the columns list in **DataProcessor.py** to include the column names you're interested in. For example:
```bash
columns = [
"id", "batch_number", "session_name", "original_gravity", "final_gravity",
"created_at", "updated_at", "fermentation_start_date", "recipe_id",
"notes", "name", "status"
]
```
