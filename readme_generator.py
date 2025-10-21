# ============ README GENERATOR ============
import numpy as np

print(f'NumPY Version: {np.__version__}')
print("Welcome to Jamal's Readme Generator \n")

def create_readme ():
    name = input('Before we can begin, please enter your name: ')
    print (f'welcome {name}, I just wanted to say you have a awesome name!')

    title = input('Enter your project title: ')
    description = input(f'Enter description for your {title} project: ')
    installation_instructions = input(f'Enter installation instructions for your {title} project: ')
    features = input(f'Enter features of your {title} project: ')
    tech_stack = input(f'Enter tech stack used to build {title}: ')
    return 


create_readme()
