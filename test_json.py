import json
import os

def test_json():
    for folder in ['participants', 'mentors']:
        for filename in os.listdir(folder):
            if filename == '.gitkeep':
                continue
            print(filename)
            with open(os.path.join(folder, filename)) as fh:
                data = json.load(fh)
            assert 'name' in data

