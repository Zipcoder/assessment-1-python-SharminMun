
def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for keys in keylist:
        if keys in datadict:
            del datadict[keys]
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    minimun_value = min(ddd.values())
    for key, value in ddd.items():
        if value == minimun_value:
            return key

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    maximum_value = max(ddd.values())
    for key, value in ddd.items():
        if value == maximum_value:
            return key

def letterfreq(word):
    '''
    # Write a function that returns a dictionary of letter frequencies from a word
    '''
    frequencies = {}

    for letter in word:
        
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return frequencies