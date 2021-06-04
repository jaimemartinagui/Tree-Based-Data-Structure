"""
    Algorithm that generates a tree-based data structure (dictionary) from a list of lists of data.
"""

def generate_tree_based_data_structure(data):
    """Function that creates a tree-based data structure from a list of lists."""

    list_of_dicts = [list_to_dict(d) for d in data]

    general_dict = {}
    for dict_ in list_of_dicts:
        general_dict = join_two_dicts(general_dict, dict_)

    return general_dict

def join_two_dicts(general_dict, new_dict):
    """Recursive function that merges two dictionaries in a nested one."""

    if isinstance(general_dict, dict) and isinstance(new_dict, dict):

        if set(new_dict).issubset(set(general_dict)):
            key = list(new_dict)[0]
            new_dict = {key: join_two_dicts(general_dict[key], new_dict[key])}

        return {**general_dict, **new_dict}

    elif isinstance(general_dict, dict) or isinstance(new_dict, dict):

        raise Exception('There is some leaf node missing!')

    else:

        return list(set(general_dict + new_dict))

def list_to_dict(list_):
    """Recursive function that generates a (nested) dictionary from a list."""

    if len(list_) == 0:
        dict_ = {}
    elif len(list_) == 1:
        dict_ = {list_[0]: []}
    elif len(list_) == 2:
        dict_ = {list_[0]: [list_[1]]}
    else:
        dict_ = {list_[0]: list_to_dict(list_[1:])}

    return dict_
