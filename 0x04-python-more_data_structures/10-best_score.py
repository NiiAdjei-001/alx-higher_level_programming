#!/usr/bin/python3
def best_score(a_dictionary):
    """Gets the key with the biggest integer value

        Args:
        a_dictionary: A dictionary

        Returns:
        returns the key with the biggest integer value
    """
    _bestkey = ""
    _bestscore = 0
    if a_dictionary:
        keys = set(list(a_dictionary))
        for key in keys:
            if a_dictionary[key] > _bestscore:
                _bestscore = a_dictionary[key]
                _bestkey = key
        return _bestkey
    return "None"
