import json
from datetime import datetime


def save_to_json(data, filename='shiftHistory.json'):
    with open(filename, 'a') as file:
        json.dump(data, file)
        file.write('\n')


def clear_json_file(filename='shiftHistory.json'):
    with open(filename, 'w') as _:
        pass


def read_from_json(filename='shiftHistory.json'):
    with open(filename, 'r') as file:
        loaded_data = []
        for line in file:
            entry = json.loads(line.strip())
            loaded_data.append(entry)

    return loaded_data


def get_total_hours(filename='shiftHistory.json'):
    with open(filename, 'r') as file:
        add_hours_total = 0
        for line in file:
            entry = json.loads(line.strip())
            loaded_hours = float(entry['hours'])
            add_hours_total += loaded_hours

        add_hours_total_rounded = round(add_hours_total, 2)

    return add_hours_total_rounded


def calculate_hours(start, end, break_mins):
    time1 = datetime.strptime(start, '%H:%M')
    time2 = datetime.strptime(end, '%H:%M')

    time_difference = time2 - time1

    total_minutes = time_difference.total_seconds() / 60

    break_mins = int(break_mins)
    total_minutes -= break_mins
    if total_minutes < 0:
        total_minutes = 0

    day_hours_long = total_minutes / 60
    day_hours = round(day_hours_long, 2)

    return day_hours


def get_id(filename='shiftHistory.json'):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            new_id = 1
        else:
            last_line = lines[-1]
            last_entry = json.loads(last_line.strip())
            last_id = last_entry['id']
            new_id = int(last_id) + 1

    return new_id


def remove_id(id_to_remove, filename='shiftHistory.json'):
    selected_id = int(id_to_remove)
    new_data = []
    with open(filename, 'r') as file:
        for line in file:
            entry = json.loads(line.strip())
            current_id = int(entry['id'])
            if current_id < selected_id:
                new_data.append(entry)
            elif current_id == selected_id:
                pass
            else:
                entry['id'] -= 1
                new_data.append(entry)

    with open(filename, 'w') as file:
        for line in new_data:
            json.dump(line, file)
            file.write('\n')
