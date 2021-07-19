import json


default_filename = 'settings.json'
default_setting = {
    'Level': 'Medium',
    'Size': 3,
    'Who first': 'Random',
}


def read_setting(filename=default_filename):
    settings = default_setting
    try:
        with open(filename) as json_file:
            settings = json.load(json_file)
    except:
        save_settings(settings)
    finally:
        return settings


def save_settings(settings, filename=default_filename):
    with open(filename, 'w') as json_file:
        json.dump(settings, json_file)
