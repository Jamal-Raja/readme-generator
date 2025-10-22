from art import * 
from rich import print
from rich.console import Console
from rich.panel import Panel
from pathlib import Path
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
    # Get README content from user
    title = input('Enter your project title: ')
    description = multiline_input(f'Enter description for your {title} project: ')
    installation_instructions = multiline_input(f'Enter installation instructions for your {title} project: ')
    features = multiline_input(f'Enter features of your {title} project: ')
    tech_stack = multiline_input(f'Enter tech stack used to build {title}: ')
    # Update data with users input
    data_dict.update({
        "title": title,
        "description": description,
        "installation_instructions": installation_instructions,
        "features": features,
        "tech_stack": tech_stack,
    })
    
     # --- Create README content ---
    readme_content = f"""# {data_dict['title'].upper()}

## Description
{data_dict['description']}

## Installation Instructions
{data_dict['installation_instructions']}

## Features
{data_dict['features']}

## Tech Stack
{data_dict['tech_stack']}
"""
    # Create new README.md file and populate with content
    with open("README.md", "w") as f:
        f.write(readme_content)
        console.print(
        Panel.fit(
            f"[bold green]✅ README.md successfully created![/bold green]\n\n"
            f"[cyan]Location:[/cyan] {Path("README.md").resolve()}",
            title="[bold magenta]Success[/bold magenta]",
            border_style="green",
        )
    )
    

if __name__ == "__main__":
    create_readme()
   