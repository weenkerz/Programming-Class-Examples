"""
This program is meant to be used to see if there is a pokemon that meets the specified criteria of learning the 4 moves
specified while also having the ability specified. If you leave a field blank it will simply skip over it.

Side notes:
Some of the abilities and moves won't give any results because they either are a special case for learning that are
implemented into the api simply for completeness’s sake. (ex. something like aqua boost which is exclusive to pokemon
conquest which is a spin-off game)

I don't really know why it says "AttributeError: 'str' object has no attribute 'master'" when scrolling,
but it doesn't seem to effect anything, so I ignored it.
"""

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import requests
import json
import webbrowser
from PIL import Image, ImageTk
from io import BytesIO
import time


# Functions for calling information
def get_win_icon(window: tk.Tk):
    # This function requests an image from the url and then sets the window icon to said image
    img_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png'
    response = requests.request('GET', img_url, stream=True)
    if response.status_code == 200:
        icon = requests.get(img_url).content
        ico = Image.open(BytesIO(icon))
        photo = ImageTk.PhotoImage(ico)
        window.wm_iconphoto(False, photo)


def move_list():
    # This function grabs the entire list of moves from pokeapi and excludes some that are special cases
    moves = []
    url = 'https://pokeapi.co/api/v2/move?limit=1000'
    response = requests.request('GET', url, stream=True)

    if response.status_code == 200:
        response_data = dict(json.loads(response.text))['results']
        for i in range(len(response_data)):
            move = response_data[i]['name']
            if move not in moves and '--physical' not in move and '--special' not in move:
                moves.append(move)

    return sorted(moves)


def ability_list():
    # This function grabs the entire list of abilities from pokeapi
    abilities = []
    url = 'https://pokeapi.co/api/v2/ability?limit=10000'
    response = requests.request('GET', url, stream=True)

    if response.status_code == 200:
        response_data = dict(json.loads(response.text))['results']
        for i in range(len(response_data)):
            ability = response_data[i]['name']
            if ability not in abilities:
                abilities.append(ability)

    return sorted(abilities)


def get_pokemon():
    # This function grabs a list of all pokemon and assigns them the id number that pokeapi uses to refer to them
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    response = requests.request("GET", url, stream=True)
    if response.status_code == 200:
        data = dict(json.loads(response.text))['results']

        POKEMON = {data[i]['name']: i + 1 for i in range(1025)}
        for j in range(1025, 1302):
            POKEMON[data[j]['name']] = j + 8976

        return POKEMON


def filter_pokemon(complete_moves: list, complete_abilities: list, move1='', move2='', move3='', move4='', ability=''):
    # This function filters through all imputed moves and the specified ability
    moves = [move1.casefold().replace(' ', '-'),
             move2.casefold().replace(' ', '-'),
             move3.casefold().replace(' ', '-'),
             move4.casefold().replace(' ', '-')]
    ability.casefold().replace(' ', '-')

    filtered_pokemon = []

    for move in moves:
        if (move != '') and (move != 'None') and move in complete_moves:
            temp_pokemon = []
            url = f'https://pokeapi.co/api/v2/move/{move}'
            response = requests.request('GET', url, stream=True)

            if response.status_code == 200:
                move_info = dict(json.loads(response.text))["learned_by_pokemon"]
                for i in range(len(move_info)):
                    pokemon_name = move_info[i]['name']
                    temp_pokemon.append(pokemon_name)

                if len(filtered_pokemon) == 0:
                    filtered_pokemon = temp_pokemon
                else:
                    filtered_pokemon = [x for x in filtered_pokemon if x in temp_pokemon]
        else:
            pass

    if ability != '' and ability != 'None' and ability in complete_abilities:
        temp_pokemon = []
        url = f'https://pokeapi.co/api/v2/ability/{ability}'
        response = requests.request('GET', url, stream=True)

        if response.status_code == 200:
            ability_info = dict(json.loads(response.text))["pokemon"]
            for i in range(len(ability_info)):
                pokemon_name = ability_info[i]['pokemon']['name']
                temp_pokemon.append(pokemon_name)

            if len(filtered_pokemon) == 0:
                filtered_pokemon = temp_pokemon
            else:
                filtered_pokemon = [x for x in filtered_pokemon if x in temp_pokemon]

    else:
        pass

    return filtered_pokemon


def get_website(i):
    exceptions = ['Nidoran♀', 'Nidoran♂', 'mr-mime', 'ho-oh', 'mime-jr', 'porygon-z', 'type-null', 'jangmo-o',
                  'hakamo-o', 'kommo-o', 'tapu-koko', 'tapu-lele', 'tapu-bulu', 'tapu-fini', 'mr-rime', 'great-tusk',
                  'scream-tail', 'brute-bonnet', 'flutter-mane', 'slither-wing', 'sandy-shocks', 'iron-treads',
                  'iron-bundle', 'iron-hands', 'iron-jugulis', 'iron-moth', 'iron-thorns', 'wo-chien', 'chien-pao',
                  'ting-lu', 'chi-yu', 'roaring-moon', 'iron-valiant', 'walking-wake', 'iron-leaves', 'gouging-fire',
                  'raging-bolt', 'iron-boulder', 'iron-crown']
    if "-" in i and all(x not in i for x in exceptions):
        problem = i.index('-')
        i = i[:problem]

    url = f"https://bulbapedia.bulbagarden.net/wiki/{i}"
    webbrowser.open(url)


# Function for creating frames of Pokemon that meet the requirements
def pokemon_frames(res_window: tk.Frame, pokemon):
    for widget in res_window.winfo_children():
        widget.destroy()
    small_font = tk.font.Font(family='Helvetica', size=7, weight='bold')
    frames = []
    exceptions = ['mega', 'family-of-three', 'gmax', 'plumage', 'segment', 'totem', 'original', 'noice', '-cap',
                  'eternamax', 'minior', 'power-construct']
    for j in pokemon:
        if all(x not in j for x in exceptions) or ('minior-red' in j and 'meteor' not in j):
            i = POKEMON[j]

            try:
                url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{i}.png'
                response = requests.request('GET', url, stream=True)
                if response.status_code == 200:
                    guy = tk.StringVar(root, j)

                    img_data = response.content
                    img = Image.open(BytesIO(img_data))
                    resized = img.resize((30, 30))
                    sprite = ImageTk.PhotoImage(resized)

                    frame = tk.Frame(res_window, width=20, height=30, bg='#000000')
                    frame.pack(padx=4, pady=2, fill='both')

                    label = tk.Label(frame, image=sprite, bg='#000000')
                    label.image = sprite
                    label.pack(side='left')

                    pokemon_name = (j.capitalize().replace('-breed', '').replace('-male', '').replace('-female', '')
                                    .replace('r-red', 'r').replace('-', ' ').title())

                    button = tk.Button(frame, text="info", command=lambda x=guy.get(): get_website(x),
                                       bg=RED, fg='#ffffff', borderwidth=2, font=small_font)
                    button.pack(side='right')

                    name = tk.Label(frame, text=pokemon_name, fg='#ffffff', bg='#000000', font=small_font)
                    name.pack(side='left', pady=(7, 0))
                    frames.append(frame)

            except:
                print("Fail")


def call_results():
    for widget in timer_frame.winfo_children():
        widget.destroy()

    start = time.time()
    check_moves = [str(move1_variable.get()), str(move2_variable.get()), str(move3_variable.get()),
                   str(move4_variable.get())]
    check_ability = ability_variable.get()

    filtered_pokemon = filter_pokemon(MOVES, ABILITIES, check_moves[0], check_moves[1], check_moves[2], check_moves[3],
                                      check_ability)

    if len(filtered_pokemon) == 0:
        for widget in results_frame.winfo_children():
            widget.destroy()
        empty = tk.Label(results_frame, text='No Pokemon', fg='#ffffff', bg='#000000', font=bold_font_small)
        empty.pack(side='top', anchor='center')

    else:
        pokemon_frames(results_frame, filtered_pokemon)

    end = time.time()

    total = round(end - start, 12)
    cool_label = tk.Label(timer_frame, text='Time(sec) =', fg="#ffffff", bg=DARK_GREY, font=cool_font)
    timer = tk.Label(timer_frame, text=total, fg="#ffffff", bg=DARK_GREY, font=cool_font)
    cool_label.pack(side='left', padx=(20, 5))
    timer.pack(side='right', padx=(5, 20))


def clear():
    move1_variable.set('')
    move2_variable.set('')
    move3_variable.set('')
    move4_variable.set('')
    ability_variable.set('')

    for widget in results_frame.winfo_children():
        widget.destroy()


# Universal Vars(?)
RED = '#C71B1B'
BRIGHT_RED = '#E61114'
DARK_GREY = '#1C1B1B'
LIGHTER_GREY = '#1E1E1E'
DARK_FERN = '#0D5C17'
POKEMON = get_pokemon()
MOVES = ['None'] + move_list()
ABILITIES = ['None'] + ability_list()

if __name__ == '__main__':
    # Main Window
    root = tk.Tk()
    root.geometry('825x280+250+150')
    root.title('Pokémon Search')
    root.config(bg=RED)
    root.resizable(False, False)
    get_win_icon(root)
    root.attributes('-topmost', True)  # Make the window as annoying as possible

    # Fonts because I guess they have to be created after a window is created
    bold_font = tk.font.Font(family='Helvetica', size=14, weight='bold')
    bold_font_small = tk.font.Font(family='Helvetica', size=8, weight='bold')
    cool_font = tk.font.Font(family='Impact', size=24, weight='bold')

    # Upper Frame
    main_frame = tk.Frame(root)
    main_frame.config(bg=RED)
    main_frame.grid(row=0, column=0, padx=10, pady=(5, 2))

    # Parameters Frame
    parameters_frame = ctk.CTkFrame(main_frame, fg_color=DARK_GREY, width=500, height=212)
    parameters_frame.grid_propagate(False)
    parameters_frame.grid(row=0, column=0, padx=(10, 5), pady=2)

    # Timer Frame
    timer_frame = ctk.CTkFrame(root, width=500, height=50, fg_color=DARK_GREY)
    timer_frame.pack_propagate(False)
    timer_frame.grid(row=1, column=0, pady=(2, 5))

    # Timer Label
    cool_label = tk.Label(timer_frame, text='Time(sec) =', fg="#ffffff", bg=DARK_GREY, font=cool_font)
    cool_label.pack(side='left', padx=(20, 5))

    # Results Frame
    results_frame = ctk.CTkScrollableFrame(main_frame, width=250, height=50, fg_color="Black",
                                           scrollbar_button_hover_color=LIGHTER_GREY, scrollbar_button_color=DARK_GREY)
    results_frame.grid(row=0, column=1, padx=(5, 10), pady=2)

    # Move and ability entry fields
    # Move 1
    move1_label = tk.Label(parameters_frame, text='Move 1', bg=DARK_GREY, fg='#ffffff', font=bold_font)
    move1_label.grid(row=0, column=0, sticky='ew', padx=(10, 36))

    move1_variable = tk.StringVar(parameters_frame)
    move1_variable.set('')
    move1 = ttk.Combobox(parameters_frame, textvariable=move1_variable, values=MOVES, width=30)
    move1.grid(row=1, column=0, sticky='ew', padx=(10, 36), pady=2)

    # Move 2
    move2_label = tk.Label(parameters_frame, text='Move 2', bg=DARK_GREY, fg='#ffffff', font=bold_font)
    move2_label.grid(row=0, column=3, sticky='ew', padx=(36, 10))

    move2_variable = tk.StringVar(parameters_frame)
    move2_variable.set('')
    move2 = ttk.Combobox(parameters_frame, textvariable=move2_variable, values=MOVES, width=30)
    move2.grid(row=1, column=3, sticky='ew', padx=(36, 10), pady=2)

    # Move 3
    move3_label = tk.Label(parameters_frame, text='Move 3', bg=DARK_GREY, fg='#ffffff', font=bold_font)
    move3_label.grid(row=3, column=0, sticky='ew', padx=(10, 36), pady=(10, 0))

    move3_variable = tk.StringVar(parameters_frame)
    move3_variable.set('')
    move3 = ttk.Combobox(parameters_frame, textvariable=move3_variable, values=MOVES, width=30)
    move3.grid(row=4, column=0, sticky='ew', padx=(10, 36), pady=2)

    # Move 4
    move4_label = tk.Label(parameters_frame, text='Move 4', bg=DARK_GREY, fg='#ffffff', font=bold_font)
    move4_label.grid(row=3, column=3, sticky='ew', padx=(36, 10), pady=(10, 0))

    move4_variable = tk.StringVar(parameters_frame)
    move4_variable.set('')
    move4 = ttk.Combobox(parameters_frame, textvariable=move4_variable, values=MOVES, width=30)
    move4.grid(row=4, column=3, sticky='ew', padx=(36, 10), pady=2)

    # Ability
    ability_frame = tk.Frame(parameters_frame, bg=DARK_GREY, width=200, height=50)
    ability_frame.grid(row=6, column=0, padx=(5, 30), pady=(20, 10))
    ability_frame.grid_propagate(False)
    ability_label = tk.Label(ability_frame, text='Ability', bg=DARK_GREY, fg='#ffffff', font=bold_font)
    ability_label.grid(row=6, column=0, sticky='ew')

    ability_variable = tk.StringVar(ability_frame)
    ability_variable.set('')
    ability = ttk.Combobox(ability_frame, textvariable=ability_variable, values=ABILITIES, width=29,
                           foreground=DARK_GREY)
    ability.grid(row=7, column=0, sticky='ew')

    # Results/Clear Button
    button_frame = tk.Frame(parameters_frame, bg=DARK_GREY)
    button_frame.grid_propagate(False)
    button_frame.grid(row=6, column=3, padx=(30, 15), pady=(25, 0), sticky='se')

    result = tk.Button(button_frame, text='SEARCH', bg=DARK_FERN, fg='#ffffff', width=9, height=2, font=bold_font_small,
                       borderwidth=10, command=call_results)
    result.pack(side='left', padx=(0, 15))

    clear = tk.Button(button_frame, text='CLEAR', bg=BRIGHT_RED, fg='#ffffff', width=9, height=2, font=bold_font_small,
                      borderwidth=10, command=clear)
    clear.pack(side='left')

    # Keep running or something
    tk.mainloop()
