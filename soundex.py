##################################
# soundex without soundex module #
##################################

from unidecode import unidecode

map_dict = {1: ['b', 'f', 'p', 'v'],
            2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
            3: ['d', 't'],
            4: ['l'],
            5: ['m', 'n'],
            6: ['r']}


def find_key(value):
    
  for key, val in map_dict.items():
    if value in val:
        
      return str(key)


def soundex(string):

    res = unidecode(string).upper()[0]

    for i in unidecode(string).lower()[1:]:
        try:
            if res[-1] != find_key(i):
                res += find_key(i)
        except:
            pass

    return res[:4]