"""
  Implementación del TAD Map (tabla de símbolos) utilizando una tabla de hash
  con manejo de colisiones de tipo Linear Probing (open addressing).
"""

import random

from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def new_map(numelem, factcarga, primo=109345121):
    """
    Crea una nueva tabla de símbolos (map) sin elementos.

    :param numelem: Número de elementos que se desean almacenar en la tabla
    :type numelem: int
    :param factcarga: Factor de carga límite de la tabla antes de hacer un rehash
    :type factcarga: float
    :param primo: Número primo utilizado para el cálculo del hash
    :type primo: int

    :returns: Tabla recién creada
    :rtype: map_linear_probing
    """
    capac = mf.next_prime(numelem / factcarga)
    mapa = {
        "prime": primo,
        "capacity": capac,
        "scale": random.randint(1, primo - 1),
        "shift": random.randint(0, primo - 1),
        "table": al.new_list(),
        "current_factor": 0,
        "limit_factor": factcarga,
        "size": 0,
    }
    for _ in range(capac):
        al.add_last(mapa["table"], me.new_map_entry(None, None))
    return mapa


def put(mapa, llave, valor):
    """
    Ingresa una pareja llave-valor a la tabla. Si la llave ya existe,
    se reemplaza su valor. Si el factor de carga supera el límite se hace rehash.

    :returns: El mapa con la nueva pareja
    :rtype: map_linear_probing
    """
    valhash = mf.hash_value(mapa, llave)
    ocupado, posic = find_slot(mapa, llave, valhash)
    if ocupado:
        me.set_value(al.get_element(mapa["table"], posic), valor)
    else:
        al.change_info(mapa["table"], posic, me.new_map_entry(llave, valor))
        mapa["size"] += 1
        mapa["current_factor"] = mapa["size"] / mapa["capacity"]
        if mapa["current_factor"] > mapa["limit_factor"]:
            mapa = rehash(mapa)
    return mapa


def contains(mapa, llave):
    """
    Valida si la llave ``llave`` se encuentra en el mapa.

    :returns: True si la llave está en el mapa, False en caso contrario
    :rtype: bool
    """
    ocupado, _ = find_slot(mapa, llave, mf.hash_value(mapa, llave))
    return ocupado


def get(mapa, llave):
    """
    Obtiene el valor asociado a la llave ``llave``.

    :returns: Valor asociado a la llave o None si no existe
    :rtype: any
    """
    ocupado, posic = find_slot(mapa, llave, mf.hash_value(mapa, llave))
    if ocupado:
        return me.get_value(al.get_element(mapa["table"], posic))
    return None


def remove(mapa, llave):
    """
    Elimina la pareja llave-valor asociada a ``llave``. La posición se marca
    con ``__EMPTY__`` para no romper las secuencias de sondeo.

    :returns: El mapa sin la llave
    :rtype: map_linear_probing
    """
    ocupado, posic = find_slot(mapa, llave, mf.hash_value(mapa, llave))
    if ocupado:
        al.change_info(mapa["table"], posic, me.new_map_entry("__EMPTY__", "__EMPTY__"))
        mapa["size"] -= 1
        mapa["current_factor"] = mapa["size"] / mapa["capacity"]
    return mapa


def size(mapa):
    """
    Retorna el número de parejas llave-valor en el mapa.
    """
    return mapa["size"]


def find_slot(my_map, key, hash_value):
    """
    Busca la posición de la llave ``key`` a partir de ``hash_value``.

    Si la llave está en la tabla retorna ``(True, pos)`` con su posición.
    Si no está retorna ``(False, pos)`` con la primera posición disponible
    donde podría insertarse.

    :returns: Tupla (ocupado, posición)
    :rtype: tuple
    """
    table = my_map["table"]
    capacity = my_map["capacity"]
    first_avail = None
    pos = hash_value
    for _ in range(capacity):
        entry = al.get_element(table, pos)
        entry_key = me.get_key(entry)
        if entry_key is None:
            
            if first_avail is None:
                first_avail = pos
            return False, first_avail
        if entry_key == "__EMPTY__":
            if first_avail is None:
                first_avail = pos
        elif default_compare(key, entry) == 0:
            return True, pos
        pos = (pos + 1) % capacity
    return False, first_avail


def is_available(table, pos):
    """
    Informa si la posición ``pos`` de la tabla está disponible
    (nunca usada o marcada como ``__EMPTY__``).
    """
    entry = al.get_element(table, pos)
    key = me.get_key(entry)
    return key is None or key == "__EMPTY__"


def default_compare(key, entry):
    """
    Función de comparación por defecto entre una llave y la llave de una entrada.

    :returns: 0 si son iguales, 1 si ``key`` es mayor, -1 si es menor
    :rtype: int
    """
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    if key > entry_key:
        return 1
    return -1


def rehash(my_map):
    """
    Aumenta la capacidad de la tabla al siguiente primo mayor al doble de la
    capacidad actual y reinserta todas las parejas llave-valor.

    :returns: El mapa con la nueva capacidad
    :rtype: map_linear_probing
    """
    old_table = my_map["table"]
    new_capacity = mf.next_prime(2 * my_map["capacity"])
    my_map["capacity"] = new_capacity
    my_map["table"] = al.new_list()
    my_map["size"] = 0
    my_map["current_factor"] = 0
    for _ in range(new_capacity):
        al.add_last(my_map["table"], me.new_map_entry(None, None))
    for entry in old_table["elements"]:
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            put(my_map, key, me.get_value(entry))
    return my_map
