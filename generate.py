import json
import os


def main():
    if not os.path.exists("_site"):
        os.makedirs("_site")
    with open("_site/index.html", "w") as fh:
        fh.write("OSDC Skeleton")

def read_json_files(folder):
    people = []
    for filename in os.listdir(folder):
        if filename == '.gitkeep':
            continue
        #print(filename)
        with open(os.path.join(folder, filename)) as fh:
            person = json.load(fh)
        people.append(person)
    return people

if __name__ == "__main__":
    main()
