import json
import random

# Specify the paths to your JSON files
json_file_path1 = '/Users/mac/Desktop/connect/alpaca_gpt4_data_zh_100.json'
json_file_path2 = '/Users/mac/Desktop/connect/medical_train_zh_0_300.json'
output_json_file = '/Users/mac/Desktop/connect/merged_and_shuffled.json'

# Function to shuffle the data
def shuffle_data(data):
    random.shuffle(data)
    return data

# Open and load data from the first JSON file
with open(json_file_path1, 'r') as file1:
    data1 = json.load(file1)

# Open and load data from the second JSON file
with open(json_file_path2, 'r') as file2:
    data2 = json.load(file2)

# Combine the data from the two files
combined_data = data1 + data2

# Shuffle the combined data
shuffled_data = shuffle_data(combined_data)

# Write the shuffled data to a new JSON file
with open(output_json_file, 'w',encoding='utf-8') as output_file:
    json.dump(shuffled_data, output_file, indent=2,ensure_ascii=False)

print(f"Merged and shuffled data has been written to {output_json_file}")
