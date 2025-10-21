from art import * 
from rich import print
from rich.console import Console
from functions import *

# ============ README GENERATOR ============
console = Console()

ascii_art = text2art("Readme Generator", font="small")
console.print(ascii_art, style="bright_magenta")

# console.print("Hiking", style="bold red")

data_dict = {
    "title": "",
    "description": "",
    "installation_instructions": "",
    "features": "",
    "tech_stack": "",    
}



def create_readme ():    
    name = input('Before we can begin, please enter your name: ')
    print (f'welcome {name}, I just wanted to say you have a awesome name!')

    title = input('Enter your project title: ')
    description = input(f'Enter description for your {title} project: ')
    installation_instructions = input(f'Enter installation instructions for your {title} project: ')
    features = input(f'Enter features of your {title} project: ')
    tech_stack = input(f'Enter tech stack used to build {title}: ')

    data_dict.update({
        "title": title,
        "description": description,
        "installation_instructions": installation_instructions,
        "features": features,
        "tech_stack": tech_stack,
    })
    
    return print(data_dict)


create_readme()
