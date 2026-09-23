from DataStructures.List import list_node as node
from DataStructures.Utils import error as error


def new_list():
    
    """Crea una lista implementada con una Lista Simplemente Encadenada vacía. 

        Define ``first`` y ``last`` como None y el ``size`` en cero

        :returns: Lista creada
        :rtype: linked_list
    """
    newlist = {'first': None,
               'last': None,
               'size': 0,
               }

    return newlist


def add_first(my_list, element):
    """Agrega un elemento en la primera posición de la lista.

    Al agregar un elemento en la primera posición de la lista, se incrementa el tamaño de la lista en uno.
    En caso de que la lista esté vacía, el nuevo elemento se convierte en el primer y último elemento de la lista.


    :param my_list: SingleLinkedList en la que se va a insertar el elemento
    :type my_list: single_linked_list
    :param element: Elemento a insertar
    :type element: any

    :returns: SingleLinkedList con el elemento insertado en la primera posición
    :rtype: single_linked_list
    """
    try:
        new_node = node.new_single_node(element)
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
        if (my_list['size'] == 0):
            my_list['last'] = my_list['first']
        my_list['size'] += 1
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->add_first: ')


def add_last(my_list, element):
    """ Agrega un elemento en la última posición de la lista.

        Al agregar un elemento en la última posición de la lista y se incrementa el tamaño de la lista en uno.
        En caso de que la lista esté vacía, el nuevo elemento se convierte en el primer y último elemento de la lista.
        
        :param my_list: SingleLinkedList en la que se va a insertar el elemento
        :type my_list: single_linked_list
        :param element: Elemento a insertar
        :type element: any

        :returns: SingleLinkedList con el elemento insertado en la última posición
        :rtype: single_linked_list
    """
    try:
        new_node = node.new_single_node(element)

        if my_list['size'] == 0:
            my_list['first'] = new_node
        else:
            my_list['last']['next'] = new_node
        my_list['last'] = new_node
        my_list['size'] += 1
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->add_last: ')


def is_empty(my_list):
    """ Indica si la lista está vacía

        :param my_list: Lista a examinar
        :type my_list: single_linked_list

        :returns: ``True`` si la lista está vacía, ``False`` en caso contrario
        :rtype: bool
    """
    try:
        return my_list['size'] == 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->is_empty: ')


def size(my_list):
    """ Retorna el número de elementos de la lista.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list

        :returns: Número de elementos de la lista
        :rtype: int
    """
    try:
        return my_list['size']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->size: ')


def first_element(my_list):
    """ Retorna el primer elemento de una lista.
        
        Retorna el primer elemento de la lista, si la lista no está vacía.
        Esta funcion NO elimina el elemento de la lista.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list

        :returns: Primer elemento de la lista
        :rtype: any
    """
    try:
        if my_list['first'] is not None:
            return my_list['first']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->first_element: ')


def last_element(my_list):
    """ Retorna el último elemento de una lista.

        Retorna el último elemento de la lista, si la lista no está vacía.
        Esta funcion NO elimina el elemento de la lista.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list

        :returns: Último elemento de la lista
        :rtype: any
    """
    try:
        if my_list['last'] is not None:
            return my_list['last']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->last_element: ')


def get_element(my_list, pos):
    """ Retorna el elemento en la posición ``pos`` de la lista.

        Se recorre la lista hasta el elemento ``pos``, el cual debe ser igual o mayor
        que cero y menor al tamaño de la lista.
        Se retorna el elemento en dicha posición sin eliminarlo.
        La lista no puede ser vacía.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list
        :param pos: Posición del elemento a retornar
        :type pos: int

        :returns: Elemento en la posición ``pos``
        :rtype: any
    """
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']  


def delete_element(my_list, pos):
    """ Elimina el elemento en la posición ``pos`` de la lista.

        La lista no puede estar vacía.
        Elimina el elemento que se encuentra en la posición ``pos`` de la lista.
        ``Pos`` debe ser igual o mayor que cero y menor al tamaño de la lista.
        Se decrementa en un uno el tamaño de la lista.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list
        :param pos: Posición del elemento a eliminar
        :type pos: int

        :returns: Lista con el elemento eliminado
        :rtype: single_linked_list
    """
    try:
        if (my_list['size'] > 0):
            if (pos == 0):
                my_list['first'] = my_list['first']['next']
                if my_list['first'] is None:
                    my_list['last'] = None
                my_list['size'] -= 1
            elif (pos > 0):
                temp = my_list['first']
                searchpos = 1
                while searchpos < pos:
                    temp = temp['next']
                    searchpos += 1
                temp['next'] = temp['next']['next']
                if (pos == my_list['size']-1):
                    my_list['last'] = temp
                my_list['size'] -= 1
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->delete_element: ')


def remove_first(my_list):
    """ Remueve el primer elemento de la lista y lo retorna.

        Elimina y retorna el primer elemento de la lista.
        El tamaño de la lista se decrementa en uno.  Si la lista
        es vacía se retorna ``None``.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list

        :returns: Primer elemento de la lista
        :rtype: any
    """
    try:
        if my_list['first'] is not None:
            temp = my_list['first']['next']
            node = my_list['first']
            my_list['first'] = temp
            my_list['size'] -= 1
            if (my_list['size'] == 0):
                my_list['last'] = my_list['first']
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remove_first: ')


def remove_last(my_list):
    """ Remueve el último elemento de la lista.

        Elimina el último elemento de la lista  y lo retorna en caso de existir.
        El tamaño de la lista se decrementa en 1.
        Si la lista es vacía retorna ``None``.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list

        :returns: Último elemento de la lista
        :rtype: any
    """
    try:
        if my_list['size'] > 0:
            if my_list['first'] == my_list['last']:
                node = my_list['first']
                my_list['last'] = None
                my_list['first'] = None
            else:
                temp = my_list['first']
                while temp['next'] != my_list['last']:
                    temp = temp['next']
                node = my_list['last']
                my_list['last'] = temp
                my_list['last']['next'] = None
            my_list['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')


def insert_element(my_list, element, pos):
    """ Inserta el elemento element en la posición ``pos`` de la lista.

        Inserta el elemento en la posición ``pos`` de la lista.
        La lista puede ser vacía.
        Se incrementa en 1 el tamaño de la lista.
        ``pos`` debe ser mayor o igual que cero y menor al tamaño de la lista.

        :param my_list: La lista en la que se va a insertar el elemento
        :type my_list: single_linked_list
        :param element: El elemento a insertar
        :type element: any
        :param pos: posición en la que se va a insertar el elemento
        :type pos: int

        :returns: Lista con el elemento insertado
        :rtype: single_linked_list
    """
    new_node = node.new_single_node(element)
    if (my_list['size'] == 0):
        my_list['first'] = new_node
        my_list['last'] = new_node

    elif ((my_list['size'] > 0) and (pos == 0)):
        new_node['next'] = my_list['first']
        my_list['first'] = new_node

    else:
        cont = 1
        temp = my_list['first']
        while cont < pos:
            temp = temp['next']
            cont += 1
        new_node['next'] = temp['next']
        temp['next'] = new_node

        if (pos == my_list['size']):
            my_list['last'] = new_node

    my_list['size'] += 1
    return my_list


def is_present(my_list, element, cmp_function):
    """ Informa si el elemento element esta presente en la lista.

        Informa si un elemento está en la lista.
        Si esta presente, retorna la posición en la que se encuentra
        o menos uno (-1) si no esta presente. Se utiliza la función de comparación
        pasada por parámetro para comparar los elementos,
        la cual debe retornan cero si los elementos son iguales.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list
        :param element: El elemento a buscar
        :type element: any
        :param cmp_function: Función de comparación de elementos
        :type cmp_function: function

        :returns: Posición del elemento en la lista
        :rtype: int
    """
    try:
        is_in_array = False
        temp = my_list['first']
        count = 0
        while not is_in_array and temp is not None:
            if cmp_function(element, temp['info']) == 0:
                is_in_array = True
            else:
                temp = temp['next']
                count += 1

        if not is_in_array:
            count = -1
        return count
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->is_present: ')


def change_info(my_list, pos, new_info):
    """ Cambia la información contenida en el nodo de la lista
        que se encuentra en la posición ``pos`` por la información recibida en new_info.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list
        :param pos: posición de la lista con la información a cambiar
        :type pos: int
        :param new_info: Nueva información que se debe poner en el nodo de la posición ``pos``
        :type new_info: any

        :returns: Lista con la información cambiada
        :rtype: single_linked_list
    """
    try:
        current = my_list['first']
        cont = 0
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = new_info
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->ichange_info: ')


def exchange(my_list, pos1, pos2):
    """ Intercambia la información en las posiciones ``pos1`` y ``pos2`` de la lista.

        :param my_list: La lista a examinar
        :type my_list: single_linked_list
        :param pos1: Posición del primer elemento
        :type pos1: int
        :param pos2: Posición del segundo elemento
        :type pos2: int

        :returns: Lista con la información intercambiada
        :rtype: single_linked_list
    """
    try:
        if pos1 == pos2:
            return my_list
        else:
            element_1 = get_element(my_list, pos1)
            element_2 = get_element(my_list, pos2)
            change_info(my_list, pos1, element_2)
            change_info(my_list, pos2, element_1)
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->exchange: ')


def sub_list(my_list, pos, num_elem):
    """ Retorna una sub-lista de la lista recibida.

        Retorna una lista que contiene los elementos a partir de la posición ``pos``,
        con una longitud de ``num_elem`` elementos.
        Se crea una copia de dichos elementos y se retorna una lista nueva.

        :param my_list: La lista origen
        :type my_list: single_linked_list
        :param pos: Posición del primer elemento
        :type pos: int
        :param num_elem: Posición del segundo elemento
        :type pos: int

        :returns: Sub-lista de la lista original
        :rtype: single_linked_list
    """
    try:
        sublst = new_list()
        cont = 0
        loc = pos
        while cont < num_elem:
            elem = get_element(my_list, loc)
            add_last(sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->sub_list: ')


def compare_elements(my_list, element, info, cmp_function):
    """ Compara el elemento ``element`` de la lista ``my_list`` con el elemento ``info``.

        Se utiliza la función de comparación por defecto si key es None o la función provista por el usuario en caso contrario

        :param my_list: La lista con los elementos
        :type my_list: single_linked_list
        :param element: El elemento que se está buscando en la lista
        :type element: any
        :param info: El elemento de la lista que se está analizando\
        :type info: any
        :param cmp_function: Función de comparación de elementos
        :type cmp_function: function

        :returns: 0 si los elementos son iguales, 1 si element > info, -1 si element < info
        :rtype: single_linked_list
    """
    try:
        if (my_list['key'] is not None):
            return my_list['cmpfunction'](element[my_list['key']], info[my_list['key']])
        else:
            return my_list['cmpfunction'](element, info)
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->compare_elements')


def defaultfunction(id1, id2):
    """ Función de comparación por defecto

        Compara dos elementos

        :param id1: Identificador 1
        :type id1: any
        :param id2: Identificador 2
        :type id2: any

        :retuns: 0 si los elementos son iguales, 1 si id1 > id2, -1 si id1 < id2
        :rtype: int
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def selection_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Slection Sort**

        Se recorre la lista y se selecciona el elemento más pequeño
        y se intercambia con el primer elemento de la lista.
        Se repite el proceso con el segundo elemento más pequeño y así sucesivamente.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list
    """

    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            minimum = pos1    # minimun tiene el menor elemento
            pos2 = pos1 + 1
            while (pos2 < n):
                if (sort_crit(get_element(my_list, pos2),
                (get_element(my_list, minimum)))):
                    minimum = pos2  # minimum = posición elemento más pequeño
                pos2 += 1
            if minimum != pos1:
                exchange(my_list, pos1, minimum)  # elemento más pequeño -> elem pos1
            pos1 += 1
    return my_list

def insertion_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Insertion Sort**

        Se recorre la lista y se inserta el elemento en la posición correcta
        en la lista ordenada.
        Se repite el proceso hasta que la lista esté ordenada.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            pos2 = pos1
            while (pos2 > 0) and (sort_crit(
                get_element(my_list, pos2), get_element(my_list, pos2-1))):
                exchange(my_list, pos2, pos2-1)
                pos2 -= 1
            pos1 += 1
    return my_list

def shell_sort(my_list, sort_crit):

    """ Función de ordenamiento que implementa el algoritmo de **Shell Sort**
        Se recorre la lista y se ordena los elementos con un gap determinado.
        Se repite el proceso con un gap menor hasta que la lista esté ordenada.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    if size(my_list) > 1:
        n = size(my_list)
        h = 1
        while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
            h = 3*h + 1
        while (h >= 1):
            for i in range(h, n):
                j = i
                while (j >= h) and sort_crit(
                                    get_element(my_list, j),
                                    get_element(my_list, j-h)):
                    exchange(my_list, j, j-h)
                    j -= h
            h //= 3    # h se decrementa en un tercio
    return my_list

def merge_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Merge Sort**

        Se divide la lista en dos partes, se ordenan las partes y se combinan
        las partes ordenadas.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    n = size(my_list)
    if n > 1:
        mid = (n // 2)
        #se divide la lista original, en dos partes, izquierda y derecha, desde el punto mid.
        left_list = sub_list(my_list, 0, mid)
        right_list = sub_list(my_list, mid, n - mid)

        #se hace el llamado recursivo con la lista izquierda y derecha 
        merge_sort(left_list, sort_crit)
        merge_sort(right_list, sort_crit)

        #i recorre la lista izquierda, j la derecha y k la lista original
        i = j = k = 0

        left_elements = size(left_list)
        righ_telements = size(right_list)

        while (i < left_elements) and (j < righ_telements):
            elem_i = get_element(left_list, i)
            elem_j = get_element(right_list, j)
            # compara y ordena los elementos
            if sort_crit(elem_j, elem_i):   # caso estricto elem_j < elem_i
                change_info(my_list, k, elem_j)
                j += 1
            else:                            # caso elem_i <= elem_j
                change_info(my_list, k, elem_i)
                i += 1
            k += 1

        # Agrega los elementos que no se comprararon y estan ordenados
        while i < left_elements:
            change_info(my_list, k, get_element(left_list, i))
            i += 1
            k += 1

        while j < righ_telements:
            change_info(my_list, k, get_element(right_list, j))
            j += 1
            k += 1
    return my_list

def quick_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Quick Sort**

        Se selecciona un elemento como **pivot** y se ordenan los elementos

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    quick_sort_recursive(my_list, 0, size(my_list)-1, sort_crit)
    return my_list

def quick_sort_recursive(my_list, lo, hi, sort_crit):
    """ Función recursiva que implementa el algoritmo de **quick sort**, esta es llamada por la función ``quick_sort()``

        Se localiza el **pivot**, utilizando la funcion de particion.

        Luego se hace la recursión con los elementos a la izquierda del **pivot**
        y los elementos a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param lo: Posición del primer elemento
        :type lo: int
        :param hi: Posición del último elemento
        :type hi: int
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function
    """
    if (lo >= hi):
        return
    pivot = partition(my_list, lo, hi, sort_crit)
    quick_sort_recursive(my_list, lo, pivot-1, sort_crit)
    quick_sort_recursive(my_list, pivot+1, hi, sort_crit)

def partition(my_list, lo, hi, sort_crit):

    """ Función que implementa la partición de la lista en **quick sort**, esta es llamada por la función ``quick_sort_recursive()``

        Se selecciona un **pivot** y se ordenan los elementos menores a la izquierda del **pivot**
        y los elementos mayores a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param lo: Posición del primer elemento
        :type lo: int
        :param hi: Posición del último elemento
        :type hi: int
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Posición del **pivot**
        :rtype: int
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           get_element(my_list, leader), get_element(my_list, hi)):
            exchange(my_list, follower, leader)
            follower += 1
        leader += 1
    exchange(my_list, follower, hi)
    return follower

def default_sort_criteria(element1, element2):
    """ Función de comparación por defecto para ordenar de manera ascendente.

<<<<<<< HEAD
        Compara dos elementos y retorna ``True`` si el primer elemento es menor al segundo elemento.
=======
        Compara dos elementos y retorna ``True`` si el primer elemento es menor o igual al segundo elemento.
>>>>>>> origin/main

        :param element1: Elemento 1
        :type element1: any
        :param element2: Elemento 2
        :type element2: any

        :returns: ``True`` si el primer elemento es menor al segundo elemento, ``False`` en caso contrario
        :rtype: bool
    """
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted