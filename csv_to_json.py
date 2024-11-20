import pandas as pd
import json

# name and data path
# name = 'Internship'
# csv_path = 'Internship Data/internship.csv'

name = 'Training'
csv_path = 'Training Program Data/data.csv'

# Load the CSV file
df = pd.read_csv(csv_path)

# Strip whitespace and newline characters from each cell
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Capitalize names and convert IDs to lowercase
for col in df.columns:
    if 'name' in col.lower():
        # Ensure that the column is of string type before applying str.title()
        if df[col].dtype == 'object':
            df[col] = df[col].str.title()  # Capitalize each word in names
    elif 'id' in col.lower():
        # Ensure that the column is of string type before applying str.lower()
        if df[col].dtype == 'object':
            df[col] = df[col].str.lower()  # Convert IDs to lowercase

if name.lower() == 'training':
    path_to_store_json = 'Training Program Data/training_info.json'
    # Select relevant columns
elif name.lower() == 'internship':
    path_to_store_json = 'Internship Data/internship_info.json'

# Convert to JSON
students_json = df.to_dict(orient='records')

# Print or save JSON to a file
with open(path_to_store_json, 'w') as f:
    json.dump(students_json, f, indent=4)
