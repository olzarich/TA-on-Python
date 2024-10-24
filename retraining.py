import json
import random
from datetime import datetime

class JsonEdit:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def load_json(self):
        with open(self.json_file_path, 'r') as file:
            return json.load(file)

    def edit_json_format(self):
        data = self.load_json()

        for user in data:
            if "birth_date" in user:
               old_date = user['birth_date']
               date_obj = datetime.strptime(old_date, '%m/%d/%Y')
               user['birth_date'] = date_obj.date().isoformat()
            user.pop('id')
        # print(data)
        # return data

# json_editor = JsonEdit("test.json")
# json_editor.edit_json_format()

def get_random_value(list_name):
    used_values = set()

    while len(used_values) < len(list_name):
        value = random.choice(list_name)
        if value not in used_values:
            used_values.add(value)
            yield value

test_list = [1, 2, 3, 4, 5]
rand_value = get_random_value(test_list)

for test_value in rand_value:
    print(test_value)


