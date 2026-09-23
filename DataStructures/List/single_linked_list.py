from DataStructures.List import list_node as node
from DataStructures.Utils import error as error


def new_list():
    
    newlist = {'first': None,
               'last': None,
               'size': 0,
               }

    return newlist


def add_first(my_list, element):
    
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
   
    try:
        return my_list['size'] == 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->is_empty: ')


def size(my_list):
    
    try:
        return my_list['size']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->size: ')


def first_element(my_list):
    
    try:
        if my_list['first'] is not None:
            return my_list['first']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->first_element: ')


def last_element(my_list):
    
    try:
        if my_list['last'] is not None:
            return my_list['last']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->last_element: ')


def get_element(my_list, pos):
    
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']  


def delete_element(my_list, pos):
    
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
    
    try:
        if (my_list['key'] is not None):
            return my_list['cmpfunction'](element[my_list['key']], info[my_list['key']])
        else:
            return my_list['cmpfunction'](element, info)
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->compare_elements')


def defaultfunction(id1, id2):
    
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def selection_sort(my_list, sort_crit):
    

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
    
    quick_sort_recursive(my_list, 0, size(my_list)-1, sort_crit)
    return my_list

def quick_sort_recursive(my_list, lo, hi, sort_crit):
    
    if (lo >= hi):
        return
    pivot = partition(my_list, lo, hi, sort_crit)
    quick_sort_recursive(my_list, lo, pivot-1, sort_crit)
    quick_sort_recursive(my_list, pivot+1, hi, sort_crit)

def partition(my_list, lo, hi, sort_crit):

    
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
    
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted