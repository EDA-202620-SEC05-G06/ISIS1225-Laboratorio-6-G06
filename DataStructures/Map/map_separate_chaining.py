"""
  Implementación del TAD Map (tabla de símbolos) utilizando una tabla de hash
  con manejo de colisiones de tipo Separate Chaining (encadenamiento separado).
"""

import random

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def new_map(numelem, factorcar, primo=109345121):
    """
    Retorna un mapa vacío.
    """
    capacidad = mf.next_prime(numelem / factorcar)
    mapa = {
        "prime": primo,
        "capacity": capacidad,
        "scale": random.randint(1, primo - 1),
        "shift": random.randint(0, primo - 1),
        "table": al.new_list(),
        "current_factor": 0,
        "limit_factor": factorcar,
        "size": 0,
    }
    for _ in range(capacidad):
        al.add_last(mapa["table"], sl.new_list())
    return mapa


def put(mapa, llave, valor):
    """
    Retorna el mapa con la pareja llave-valor agregada.
    """
    cubeta = al.get_element(mapa["table"], mf.hash_value(mapa, llave))
    entrada = find_entry(cubeta, llave)
    if entrada is not None:
        me.set_value(entrada, valor)
    else:
        sl.add_last(cubeta, me.new_map_entry(llave, valor))
        mapa["size"] += 1
        mapa["current_factor"] = mapa["size"] / mapa["capacity"]
        if mapa["current_factor"] > mapa["limit_factor"]:
            mapa = rehash(mapa)
    return mapa


def contains(mapa, llave):
    """
    Retorna True si la llave está en el mapa, False si no.
    """
    cubeta = al.get_element(mapa["table"], mf.hash_value(mapa, llave))
    return find_entry(cubeta, llave) is not None


def get(mapa, llave):
    """
    Retorna el valor asociado a la llave, o None si no existe.
    """
    cubeta = al.get_element(mapa["table"], mf.hash_value(mapa, llave))
    entrada = find_entry(cubeta, llave)
    if entrada is not None:
        return me.get_value(entrada)
    return None


def remove(mapa, llave):
    """
    Retorna el mapa sin la pareja de la llave dada.
    """
    cubeta = al.get_element(mapa["table"], mf.hash_value(mapa, llave))
    posicion = 0
    nodo = cubeta["first"]
    while nodo is not None:
        if me.get_key(nodo["info"]) == llave:
            sl.delete_element(cubeta, posicion)
            mapa["size"] -= 1
            mapa["current_factor"] = mapa["size"] / mapa["capacity"]
            return mapa
        nodo = nodo["next"]
        posicion += 1
    return mapa


def size(mapa):
    """
    Retorna el número de parejas llave-valor.
    """
    return mapa["size"]


def is_empty(mapa):
    """
    Retorna True si el mapa no tiene parejas, False si tiene.
    """
    return mapa["size"] == 0


def key_set(mapa):
    """
    Retorna un array_list con todas las llaves.
    """
    llaves = al.new_list()
    for cubeta in mapa["table"]["elements"]:
        nodo = cubeta["first"]
        while nodo is not None:
            al.add_last(llaves, me.get_key(nodo["info"]))
            nodo = nodo["next"]
    return llaves


def value_set(mapa):
    """
    Retorna un array_list con todos los valores.
    """
    valores = al.new_list()
    for cubeta in mapa["table"]["elements"]:
        nodo = cubeta["first"]
        while nodo is not None:
            al.add_last(valores, me.get_value(nodo["info"]))
            nodo = nodo["next"]
    return valores


def find_entry(cubeta, llave):
    """
    Retorna la entrada con la llave dada, o None si no está en la cubeta.
    """
    nodo = cubeta["first"]
    while nodo is not None:
        if default_compare(llave, nodo["info"]) == 0:
            return nodo["info"]
        nodo = nodo["next"]
    return None


def default_compare(llave, entrada):
    """
    Retorna 0 si la llave es igual a la de la entrada, 1 si es mayor, -1 si es menor.
    """
    llaveent = me.get_key(entrada)
    if llave == llaveent:
        return 0
    if llave > llaveent:
        return 1
    return -1


def rehash(mapa):
    """
    Retorna el mapa con la capacidad aumentada al primo siguiente al doble.
    """
    tablavie = mapa["table"]
    capacidadnue = mf.next_prime(2 * mapa["capacity"])
    mapa["capacity"] = capacidadnue
    mapa["table"] = al.new_list()
    mapa["size"] = 0
    mapa["current_factor"] = 0
    for _ in range(capacidadnue):
        al.add_last(mapa["table"], sl.new_list())
    for cubeta in tablavie["elements"]:
        nodo = cubeta["first"]
        while nodo is not None:
            put(mapa, me.get_key(nodo["info"]), me.get_value(nodo["info"]))
            nodo = nodo["next"]
    return mapa
