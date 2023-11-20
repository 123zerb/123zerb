
# Specify the paths to your JSON files
# json_file_path1 = '/Users/mac/Desktop/connect/alpaca_gpt4_data_zh_100.json'
# json_file_path2 = '/Users/mac/Desktop/connect/medical_train_zh_0_300.json'

# Function to mix the data from two files with a 1:3 ratio

import json

# Specify the paths to your JSON files
json_file_path1 = '/Users/mac/Desktop/connect/alpaca_gpt4_data_zh_100.json'
json_file_path2 = '/Users/mac/Desktop/connect/medical_train_zh_0_300.json'
output_json_file = '/Users/mac/Desktop/connect/mixed_data.json'

# Function to mix the data from two files with a 1:3 ratio
def mix_data(file1_data, file2_data):
    mixed_data = []

    # Mix data based on a 1:3 ratio
    for i in range(min(len(file1_data), 3 * len(file2_data))):
        if i % 4 == 0:
            mixed_data.append(file1_data.pop(0))
        else:
            mixed_data.append(file2_data.pop(0))

    # Add any remaining data from both files
    mixed_data.extend(file1_data)
    mixed_data.extend(file2_data)

    return mixed_data

# Open and load data from the first JSON file
with open(json_file_path1, 'r') as file1:
    data1 = json.load(file1)

# Open and load data from the second JSON file
with open(json_file_path2, 'r') as file2:
    data2 = json.load(file2)

# Mix the data from the two files
mixed_data = mix_data(data1, data2)

# Write the mixed data to a new JSON file
with open(output_json_file, 'w') as output_file:
    json.dump(mixed_data, output_file, indent=2 ,ensure_ascii=False)

print(f"Mixed data has been written to {output_json_file}")

