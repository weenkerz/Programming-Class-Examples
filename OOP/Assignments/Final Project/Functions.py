import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import requests
import json
from PIL import Image, ImageTk
from io import BytesIO


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


def filter_pokemon(complete_moves: list, complete_abilities: list, move1='', move2='', move3='', move4='', ability=''):
    moves = [move1, move2, move3, move4]
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


# Function for creating frames of Pokemon that meet the requirements
def pokemon_frames(res_window: tk.Frame, pokemon):
    for widget in res_window.winfo_children():
        widget.destroy()
    small_font = tk.font.Font(family='Helvetica', size=12, weight='bold')
    frames = []
    exceptions = ['mega', 'family-of-three', 'gmax', 'plumage', 'segment', 'totem', 'original', 'noice', '-cap',
                  'eternamax']
    for j in pokemon:
        if all(x not in j for x in exceptions):
            url = f'https://pokeapi.co/api/v2/pokemon/{j}'
            response = requests.request('GET', url, stream=True)
            if response.status_code == 200:
                pokemon_data = dict(json.loads(response.text))
                i = pokemon_data['id']

                try:
                    url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{i}.png'
                    response = requests.request('GET', url, stream=True)
                    if response.status_code == 200:
                        img_data = response.content
                        img = Image.open(BytesIO(img_data))
                        resized = img.resize((30, 30))
                        sprite = ImageTk.PhotoImage(resized)

                        frame = tk.Frame(res_window, width=20, height=30, bg='#000000')
                        frame.pack(padx=4, pady=2, fill='both')

                        label = tk.Label(frame, image=sprite, bg='#000000')
                        label.image = sprite
                        label.pack(side='left')

                        pokemon_name = (j.capitalize().replace('-breed', '').replace('-male', '').replace('female', '')
                                        .replace('-', ' ').title())
                        name = tk.Label(frame, text=pokemon_name, fg='#ffffff', bg='#000000', font=small_font)
                        name.pack(side='left', pady=(7, 0))
                        frames.append(frame)

                except:
                    print("Fail")


if __name__ == '__main__':
    moves = move_list()
    abilities = ability_list()

    root = tk.Tk()
    root.geometry('300x210+250+150')
    root.title('test')

    main_frame = ctk.CTkScrollableFrame(root, width=275, height=200, fg_color='black')
    main_frame.grid(row=0, column=0)

    check_mons = filter_pokemon(moves, abilities, ability='technician')
    pokemon_frames(main_frame, check_mons)

    root.mainloop()

    # print(move_list())
