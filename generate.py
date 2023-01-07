import os

os.makedirs("_site")
with open("_site/index.html", "w") as fh:
    fh.write("OSDC Skeleton")

