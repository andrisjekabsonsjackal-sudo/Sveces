import os
import re

# Šis skripts atradīs jebkuru failu, kurā ir vārds "amberflames"
files = [f for f in os.listdir() if "amberflames" in f.lower() and f.endswith(".jpg")]
files.sort() # Sakārtojam, lai numuri iet pēc kārtas

for i, filename in enumerate(files, 1):
    # Uztaisām ideālo nosaukumu, ko gaida tavs HTML kods
    new_name = f"amberflames_{i}.jpg"
    os.rename(filename, new_name)
    print(f"Saremontēts: {filename} -> {new_name}")
    