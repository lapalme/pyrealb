from datetime import datetime
from pyrealb import *

# language independent realization algorithm
class Realizer:
    def __init__(self): # called by __init__() in subclasses after setting the language
        pass

    def realize(self,fields,phrase_type):
        def no_undef(struct):
            return struct.realize() if struct is not None else ""

        if phrase_type == 1:
            return no_undef(CP(self.and_conj,
                               self.advice(fields),
                               self.customer_rating(fields),
                               self.family_friendly(fields)))
        elif phrase_type == 2:
            return no_undef(CP(self.and_conj,
                               self.advice(fields),
                               self.customer_rating(fields)).a("."))\
                  + no_undef(self.family_friendly(fields))
        elif phrase_type == 3:
            return no_undef(self.advice(fields)) \
                   + no_undef(self.customer_rating(fields)) \
                   + no_undef(self.family_friendly(fields))

