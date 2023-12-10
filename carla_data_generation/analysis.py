import json
import numpy
from matplotlib import pyplot as plt

json_folder = r'/projectnb/ec523kb/students/jylu29/dataset2/v1.14/'

with open(json_folder + 'category.json', 'r') as f:
    category = json.load(f)
with open(json_folder + 'instance.json', 'r') as f:
    instance = json.load(f)
with open(json_folder + 'sample_annotation.json', 'r') as f:
    sample_annotation = json.load(f)
with open(json_folder + 'sample.json', 'r') as f:
    sample = json.load(f)

instance = {i['token']: i for i in instance}
category = {c['token']: c for c in category}
count_per_sample = {}
for a in sample_annotation:
    instance_token = a['instance_token']
    category_token = instance[instance_token]['category_token']
    category_name = category[category_token]['name']
    if 'vehicle' in category_name:
        if a['sample_token'] in count_per_sample.keys():
            count_per_sample[a['sample_token']] += 1
        else:
            count_per_sample[a['sample_token']] = 1

count = [v for k, v in count_per_sample.items()]
plt.hist(count)
plt.xlabel('Vehicles Per Sample')
plt.ylabel('Count')
plt.show()