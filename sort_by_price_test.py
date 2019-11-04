"""

Created by aditya on 25/12/18 at 5:24 PM

"""

from ast import literal_eval


class Products:

    @staticmethod
    def sort_by_price_ascending(json_string):

        l1 = literal_eval(json_string)
        p = []
        for i in l1:
            p.append(i['price'])

        p = p.sort()
        l2 = []
        for k in p:
            l2.append(d['prices'] = k)

            return None

    print(Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))

    '''
    sort by price, if same price then sort by name, then finally return in the same format as input(str)
    hint: use google (eval) (direct sort using lambda) method
    '''
