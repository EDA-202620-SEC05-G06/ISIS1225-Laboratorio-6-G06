
def new_single_node(element):
    
    node = {'info': element, 'next': None}
    return (node)


def get_element(node):
    
    return node['info']


def new_double_node(element):
    
    node = {'info': element,
            'next': None,
            'prev': None
            }
    return node
