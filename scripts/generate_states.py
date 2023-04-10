import os
import json


# Path to the folder containing the subfolders with JSON files
root_folder = "../jsons/india"

# Iterate through all subfolders inside the root folder
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)

    # Create a dictionary to store the results
    results = {"name": folder_name, "pincodes": [], "districts": []}

 # Check if the subfolder is a directory
    if os.path.isdir(folder_path):

        # Iterate through all JSON files inside the subfolder
        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                jsonPath = os.path.join(folder_path, filename)

                # Open the JSON file and extract the pincode and place values
                with open(jsonPath) as f:
                    data = json.load(f)
                    for value in data:
                        if (value["pincode"].lower() != "pincode"):
                            results["districts"].append(value)
                            results["pincodes"].append(value["pincode"])

        # Count the total number of pincodes in each state
        results["totalPincodesCount"] = len(results["pincodes"])

        # Save the results to a new JSON file
        states_path = '../jsons/states'
        if not os.path.exists(states_path):
            os.makedirs(states_path)

        output_file = '../jsons/states/{output}.json'.format(
            output=folder_name)
        with open(output_file, "w") as f:
            json.dump(results, f)
