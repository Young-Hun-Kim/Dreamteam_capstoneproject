import pandas as pd
import random

# Replace 'your_data_file.txt' with the path to your txt file
file_path = 'Capstone _Project\WISDM_ar_v1.1_raw.txt'

# Read the data into a pandas DataFrame
data = pd.read_csv(file_path, header=None, sep='\s+')

# Percentage - x % of the data
Xpercentage = 0.05    

# Calculate the number of rows to extract (Xpercentage of the data)
num_rows_to_extract = int(Xpercentage * len(data))

# Randomly select Xpercentage of the rows
selected_rows = random.sample(range(len(data)), num_rows_to_extract)

# Extract the selected rows
extracted_data = data.iloc[selected_rows]

# Save the extracted data to a new txt file
extracted_data.to_csv('extracted_data.txt', index=False, header=False, sep=' ')

print("Xpercentage of the data has been randomly extracted and saved to 'extracted_data.txt'")

# Read the extracted data from the new txt file
read_extracted_data = pd.read_csv('extracted_data.txt', header=None, sep='\s+')

# Check if the extracted data matches the data in the original dataset
matched = True
for idx, row in read_extracted_data.iterrows():
    if not (data.iloc[selected_rows[idx]] == row).all():
        matched = False
        break

if matched:
    print("The extracted data matches the original dataset.")
else:
    print("The extracted data does not match the original dataset.")
