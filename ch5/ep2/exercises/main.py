"""Create a docker image that prints the loaded_potato_salad for making potato salad.

Create a main.py script that reads and prints the loaded_potato_salad using data/potato_salad.yml
Use the pypi colored package to add colors to your loaded_potato_salad. ie: print each ingredient or step in a different color
Create a Dockerfile for your image and include your files
Create a default CMD for your image that runs your script by default
Additional points: use the pypi tabulate package to print the nutritional facts in a table format"""


import colored
from colored import bg, fg
import yaml
from pprint import pprint
from random import randint

with open('potato_salad.yml', 'r') as yaml_tato_salad:
    loaded_potato_salad = yaml.safe_load(yaml_tato_salad)
    for key in loaded_potato_salad:
        print(f'{key}', fg(randint(1,249)))
        value_list = loaded_potato_salad[key]
        for i in value_list: 
            print(f'{i}', fg(randint(1, 249)))
            

            


            nutch_list = loaded_potato_salad[key]
            deets = nutch_list[key]
            if deets in nutch_list:
                # nutch_list = value_list[key]
                for deets in nutch_list:
                    print(f'{deets}', fg(randint(1,249)))


# pprint(loaded_potato_salad)