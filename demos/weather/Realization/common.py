from pyrealb import *

### time generation
def get_term_at(terms, hour):
    if terms is None or len(terms) == 0: return None
    for term in terms:
        if hour <= term.end:
            return term
    return None


def get_fn_term(terms, idx, cmp):
    if terms is None or not terms: return None
    term = terms[0]
    for i in range(1, len(terms)):
        if cmp(terms[i].infos[idx], term.infos[idx]):
            term = terms[i]
    return term


def get_max_term(terms, idx):
    return get_fn_term(terms, idx, lambda x, y: x > y)


def get_min_term(terms, idx):
    return get_fn_term(terms, idx, lambda x, y: x < y)


if __name__ == '__main__':
    from English import English
    from Francais import Francais
    for lang in [English(), Francais()]:
        print(f"-- {lang.code} --")
        load(lang.code)
        for h in range(1, 40, 3):
            print(" %2d : %s : %s" % (h, lang.pyrHour(h).realize(),
                                      lang.pyrDayPeriod(h).realize()))
