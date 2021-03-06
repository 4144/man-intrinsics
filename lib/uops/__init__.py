def architecture_name(arch_code):
    names = {
        'CFL': 'Coffee Lake',
        #'SNM': '',
        'SNB': 'Sandy Bridge',
        'KBL': 'Kaby Lake',
        'IVB': 'Ivy Bridge',
        'NHM': 'Nehalem',
        'WSM': 'Westmere',
        'SKX': 'SkylakeX',
        'BDW': 'Broadwell',
        'HSW': 'Haswell',
        'SKL': 'Skylake',
    }

    return names.get(arch_code, arch_code)


def normalize(string):
    symbols = set(['CFL',
                   'SNM',
                   'SNB',
                   'KBL',
                   'IVB',
                   'NHM',
                   'SKX',
                   'BDW',
                   'HSW',
                   'SKL'])

    mapping = {
        'COFFEELAKE'    : 'CFL',
        'SANDYBRIDGE'   : 'SNB',
        'KABYLAKE'      : 'KBL',
        'IVYBRIDGE'     : 'IVB',
        'NEHALEM'       : 'NHM',
        'WESTMERE'      : 'WSM',
        'SKYLAKEX'      : 'SKX',
        'BROADWELL'     : 'BDW',
        'HASWELL'       : 'HSW',
        'SKYLAKE'       : 'SKL',
    }

    tmp = string.upper()

    try:
        return mapping[tmp]
    except KeyError:
        if tmp in symbols:
            return tmp
        else:
            raise KeyError("'%s' is not a valid architecture name nor symbol" % string)

