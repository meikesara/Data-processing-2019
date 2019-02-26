# Meike Kortleve
# 10773576

import json
import csv

input_file = r"D:\Meike\Documenten\Universiteit\Master\DataProcessing\Data-processing-2019\Homework\week3\KNMI_20190225.csv"

# Set path for JSON file
output_file = r"D:\Meike\Documenten\Universiteit\Master\DataProcessing\Data-processing-2019\Homework\week3\converted.json"

with open(input_file,'r') as input:
    reader = csv.DictReader(input)
    data = list(reader)


with open(path, 'w') as output:
    json.dump(data, output)
