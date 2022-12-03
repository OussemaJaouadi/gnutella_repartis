from utils import UI_colors
import pyfiglet as figlet
TAB = '\t'*3
projet = figlet.figlet_format(text="Project Repartis",font="big")
authors = figlet.figlet_format(text=f"{TAB}Presented By :\n{TAB}{TAB} Oussema Jaouadi\n{TAB}{TAB} Taha Mediouni",font="smslant")
def print_art():
    UI_colors.print_yellow(projet,end=' ')
    UI_colors.print_violet(authors)