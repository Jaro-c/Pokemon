from django.contrib.auth import authenticate
from django.shortcuts import redirect, render

from django.contrib import messages
from .formulario import UserRegisterForm

from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

import requests
import json

def home(request):
    return render(request, 'index.html')

def pokedex(request):
    if request.method=='POST':
        errores = {}
        # Identificar errores
        try:
            pokemon_id = int(request.POST['pokemon-id'])
            if pokemon_id < 1 or pokemon_id > 150:
                errores.setdefault('errorID', 'Número del pokemon entre 1 y 150')
            
        except:
            errores.setdefault('errorID', 'No es un número')

        # Enviar errores o pokemon
        if len(list(errores.keys())) > 0:
            return render(request, 'pokedex.html', {'errores':errores})
        else:
            #https://some-random-api.ml/pokedex?id=1
            URL = f"https://some-random-api.ml/pokedex?id={pokemon_id}"
            response = requests.get(URL).json()
            name = response['name']
            id = response['id']
            hp = response['stats']['hp']
            attack = response['stats']['attack']
            defense = response['stats']['defense']
            sp_atk = response['stats']['sp_atk']
            sp_def = response['stats']['sp_def']
            speed = response['stats']['speed']
            total = response['stats']['total']
            type = get_url(response['type'])
            sprites = response['sprites']['normal']

            data = {
                'name': name, 
                'id': id, 
                'hp':hp,
                'attack': attack, 
                'defense':defense, 
                'sp_atk':sp_atk, 
                'sp_def':sp_def, 
                'speed':speed, 
                'total':total, 
                'type': type,
                'sprites': sprites
            }

            return render(request, 'pokedex.html', data)
    else:
        return render(request, 'pokedex.html')

def get_url(type):
    respuesta = []
    for i in type:
        if (i=="Steel"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Pok%C3%A9mon_Steel_Type_Icon.svg/120px-Pok%C3%A9mon_Steel_Type_Icon.svg.png")
        elif (i=="Water"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Pok%C3%A9mon_Water_Type_Icon.svg/120px-Pok%C3%A9mon_Water_Type_Icon.svg.png")
        elif (i=="Bug"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Pok%C3%A9mon_Bug_Type_Icon.svg/120px-Pok%C3%A9mon_Bug_Type_Icon.svg.png")
        elif (i=="Dragon"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Pok%C3%A9mon_Dragon_Type_Icon.svg/120px-Pok%C3%A9mon_Dragon_Type_Icon.svg.png")
        elif (i=="Electric"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Pok%C3%A9mon_Electric_Type_Icon.svg/120px-Pok%C3%A9mon_Electric_Type_Icon.svg.png")
        elif (i=="Ghost"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Pok%C3%A9mon_Ghost_Type_Icon.svg/120px-Pok%C3%A9mon_Ghost_Type_Icon.svg.png")
        elif (i=="Fire"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Pok%C3%A9mon_Fire_Type_Icon.svg/120px-Pok%C3%A9mon_Fire_Type_Icon.svg.png")
        elif (i=="Fairy"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Pok%C3%A9mon_Fairy_Type_Icon.svg/120px-Pok%C3%A9mon_Fairy_Type_Icon.svg.png")
        elif (i=="Ice"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Pok%C3%A9mon_Ice_Type_Icon.svg/120px-Pok%C3%A9mon_Ice_Type_Icon.svg.png")
        elif (i=="Fighting"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Pok%C3%A9mon_Fighting_Type_Icon.svg/120px-Pok%C3%A9mon_Fighting_Type_Icon.svg.png")
        elif (i=="Normal"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Pok%C3%A9mon_Normal_Type_Icon.svg/120px-Pok%C3%A9mon_Normal_Type_Icon.svg.png")
        elif (i=="Grass"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pok%C3%A9mon_Grass_Type_Icon.svg/120px-Pok%C3%A9mon_Grass_Type_Icon.svg.png")
        elif (i=="Psychic"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Pok%C3%A9mon_Psychic_Type_Icon.svg/120px-Pok%C3%A9mon_Psychic_Type_Icon.svg.png")
        elif (i=="Rock"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Pok%C3%A9mon_Rock_Type_Icon.svg/120px-Pok%C3%A9mon_Rock_Type_Icon.svg.png")
        elif (i=="Dark"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Pok%C3%A9mon_Dark_Type_Icon.svg/120px-Pok%C3%A9mon_Dark_Type_Icon.svg.png")
        elif (i=="Ground"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Pok%C3%A9mon_Ground_Type_Icon.svg/120px-Pok%C3%A9mon_Ground_Type_Icon.svg.png")
        elif (i=="Poison"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Pok%C3%A9mon_Poison_Type_Icon.svg/120px-Pok%C3%A9mon_Poison_Type_Icon.svg.png")
        elif (i=="Flying"): respuesta.append("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Pok%C3%A9mon_Flying_Type_Icon.svg/120px-Pok%C3%A9mon_Flying_Type_Icon.svg.png")
    return respuesta

def validacion(request):
    if request.method=='POST':
        pokemon_id = request.POST['pokemon-id']
        errores = {}
        # Identificar errores
        if pokemon_id == '1':
            errores.setdefault('errorID', 'Número del pokemon entre 1 y 150')
        else:
            errores.setdefault('errorID', '-Número del pokemon entre 1 y 150')
        if len(list(errores.keys())) > 0:
            return render(request, 'pokemon.html', {'errores':errores})
        else:
            datos = pokemon_id
            return render(request, 'pokedex.html', {'datos':datos})
    else:
        return render(request, 'pokedex.html')


def batalla(request):
    seleccionados = False
    if request.method=='POST':
        # Identificar errores
        errores = {}
        try:
            pokemon1 = int(request.POST['pokemon1'])
            pokemon2 = int(request.POST['pokemon2'])
            if (pokemon1 < 1 or pokemon1 > 150) or (pokemon2 < 1 or pokemon2 > 150):
                errores.setdefault('errorID', 'Número de los pokemones entre 1 y 150')
        except:
            errores.setdefault('errorID', 'No es un número')

        # Enviar errores o pokemon
        if len(list(errores.keys())) > 0:
            return render(request, 'batalla.html', {'errores':errores, 'seleccionados':False})
        else:
            #https://some-random-api.ml/pokedex?id=1
            URL1 = f"https://some-random-api.ml/pokedex?id={pokemon1}"
            response1 = requests.get(URL1).json()
            name = response1['name']
            id = response1['id']
            hp = response1['stats']['hp']
            attack = response1['stats']['attack']
            defense = response1['stats']['defense']
            sp_atk = response1['stats']['sp_atk']
            sp_def = response1['stats']['sp_def']
            speed = response1['stats']['speed']
            total = response1['stats']['total']
            sprites = response1['sprites']['normal']

            data1 = {
                'name': name, 
                'id': id, 
                'hp':hp,
                'attack': attack, 
                'defense':defense, 
                'sp_atk':sp_atk, 
                'sp_def':sp_def, 
                'speed':speed, 
                'total':total, 
                'sprites': sprites
            }

                        #https://some-random-api.ml/pokedex?id=1
            URL2 = f"https://some-random-api.ml/pokedex?id={pokemon2}"
            response2 = requests.get(URL2).json()
            name2 = response2['name']
            id2 = response2['id']
            hp2 = response2['stats']['hp']
            attack2 = response2['stats']['attack']
            defense2 = response2['stats']['defense']
            sp_atk2 = response2['stats']['sp_atk']
            sp_def2 = response2['stats']['sp_def']
            speed2 = response2['stats']['speed']
            total2 = response2['stats']['total']
            sprites2 = response2['sprites']['normal']

            data2 = {
                'name': name2, 
                'id': id2, 
                'hp':hp2,
                'attack': attack2, 
                'defense':defense2, 
                'sp_atk':sp_atk2, 
                'sp_def':sp_def2, 
                'speed':speed2, 
                'total':total2, 
                'sprites': sprites2
            }

            desarrollo = comentarios_batalla(nombre1=name, nombre2=name2, vida1=1000, vida2=1000, ataque1=int(attack), ataque2=int(attack2))

            pokemones = {'pokemon1': data1, 'pokemon2': data2, 'seleccionados':True, 'desarrollo': desarrollo}
            return render(request, 'batalla.html', pokemones)
        
    else:
        return render(request, 'batalla.html', {'selescionados': False})

def comentarios_batalla(nombre1, nombre2, vida1, vida2, ataque1, ataque2):
    comentarios = ""
    contador = 1
    turno = 1
    while vida1 >= 0 and vida2 >= 0:
        if turno == 1:
            vida2 = vida2 - ataque1
            comentarios += "Jugada %i: %s atacó, %s recibio un daño de %i. Su vida quedó %i \n" % (contador, nombre1, nombre2, ataque1, vida2)
            contador += 1
            turno = 2
        else:
            vida1 = vida1 - ataque2
            comentarios += "Jugada %i: %s atacó, %s recibio un daño de %i. Su vida quedó %i \n" % (contador, nombre2, nombre1, ataque2, vida1)
            contador += 1
            turno = 1
    if vida1 <= 0:
        comentarios += "GANÓ %s" % nombre2
    else:
        comentarios += "GANÓ %s" % nombre1
    return comentarios





def registrar(request):
    if request.method=='POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            messages.success(request, "Entrenador %s creado" % username)
    else:
        formulario = UserRegisterForm()
    return render(request, 'registrar.html', {'formulario': formulario})

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "El usuario %s ha iniciado sesión" % nombre_usuario)
                return redirect('home')
            else:
                messages.error(request, "El usuario o la contraseña son incorrectos")
        else:
            messages.error(request, "El usuario o la contraseña son incorrectos")
    else:
        formulario = AuthenticationForm()
    return render(request, 'ingresar.html', {'formulario':formulario})

def salir(request):
    logout(request)
    messages.success(request, "Sesion cerrada")
    return redirect('home')