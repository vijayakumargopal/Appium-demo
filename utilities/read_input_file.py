import json
import os


def read_data(*key):
    current_path = os.path.dirname(os.getcwd())
    file_path = os.path.join(current_path, "base_datas\\inputs.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    if len(key) == 1:
        return data[key[0]]
    list_of_data = {val: data[val] for val in key}
    return list_of_data
