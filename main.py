# Exercise 3
from pathlib import Path
from collections import Counter
import pandas as pd
# import functions from utils here

data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]
subdir = data_dir/"cars.txt"
print(subdir)

dir_exist = subdir.exists()
print("Filepath exists: {}".format(dir_exist))

# 2. Read the text file [2P]
with open (subdir, "r") as file:
    models = file.read().splitlines()

print(models)
models = models[1:]

# 3. Count the occurences of each item in the text file [2P]
items = list(set(models))
print(items)

occurence = list(Counter(models).values())
print(occurence)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]
output_dir.mkdir(parents = True, exist_ok = True)

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
df = pd.DataFrame({"item":items, "count":occurence})

print(df.head())

solutionFile = output_dir/"counts.csv"
print(solutionFile)

df.to_csv(solutionFile, sep = "\t")