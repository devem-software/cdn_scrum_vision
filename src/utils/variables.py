import operator

DATA_PATH = './dist'
SRC_PATH = './src'
DATA_FILE = 'games'
DATA_FILE_EXT = 'json'
DATA_FILE_FULL = f'{DATA_FILE}.{DATA_FILE_EXT}'
DATA_FILE_BACKUP = f'{DATA_FILE}_backup'
DATA_FILE_CLEAN = f'{DATA_FILE}_clean'
DATA_FILE_OPTIMIZED = f'{DATA_FILE}_optimized'
DATA_FILE_MINIFIED = f'{DATA_FILE}_minified'

BLACKLIST = ["8QhhaZKWmMs", "zyQZwL6dLk4", "3naQnHCvbNY", "5hhS5HyaSTg", "7-0nEMVwrcY", "J56qof2Y7-M", "bC7Uz3Q9tLU", "hvuvPyqCZzo",
             "naGkWvia1Fo", "5No1xzb6MMk", "8b05Yvz7Sr4", "M9_2DzpN5go", "7gc1kYEECz4", "eTxJfMYhVyo"]

SPECIALS_CHARS = {
    "\u00b4": "'",
    "&#39;": "'",
    "\u00c1": "A",
    "Bogot@": "Bogota",
    "\u00b0": "°",
    "´": ""
}

COMPARES = {
    "<": operator.lt,
    ">": operator.gt,
    "=": operator.eq,
    ">=": operator.ge,
    "<=": operator.le
}


EVENTS = {
    'scrums': [],
    'lineouts': [],
    'rucks': [],
    'infractions': {
        'fouls': [],
        'cards': {
            'yellow': [],
            'red': []
        }
    },
    "score": {
        "try": [],
        "convertion": [],
        "drop": [],
        "penal": []
    }
}


CLEAN_WORDS = [
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "rugby",
    "club",
    "rc",
    "r.c",
    "premier",
    "oro",
    "plata",
    "bronce",
    "semifinales",
    "r.c.",
    "bogota",
    "(bogota)",
    "d.c",
    "d.c.",
    "torneo",
    "lrb",
    "copa",
    "clubes",
    "desarrollo",
    "des",
    ".",
    " .",
    "mac",
    "regionales",
    "capital",
    "juvenil",
    "interligas",
    "del",
    "super",
    "tcrb",
    "seven",
    "20",
    "fecha1",
    "fecha2",
    "fecha3",
    "11",
    "y",
    "lugar",
    "20192",
    "20224",
    "f16",
    "rv",
    "16",
    "madera",
    "s",
    "52",
    "15",
    "12",
    "10",
    "7",
    "local",
    "final",
    "semifinal",
    "semifianles",
    "masculino",
    "maculino",
    "masculina",
    "m",
    "mas",
    "masc",
    "m15´s",
    "ranking",
    "femenino",
    "femenina",
    "equipo",
    "resto",
    "juveniles",
    "encuentro",
    "primer",
    "partido",
    "f",
    "fem",
    "fem12´s",
    "fem-12´s",
    "A",
    "B",
    "15´s",
    "12´s",
    "10´s",
    "7´s",
    "-",
    " -",
    "nacional",
    "- ",
    " - ",
    "-  ",
    "torneo",
    "trcb",
    "apertura",
    "clausura",
    "seleccion",
    "fecha",
    "sevens",
    "plano",
    "general",
    "cerrado",
    "internacional",
    "xiv",
    "xix",
    "en",
    "xx",
    "m18",
    "r. ",
    "c",
    "rv",
    "i",
    "c. ",
    "()",
    "rv",
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13", "f14", "f15",
    "´s",
    "ma", "mb",
    "ii",
    "ok",
    "cerra",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "primera",
    "segunda",
    "tercera",
    "cuarta",
    "quinta",
    "sexta",
    "séptima",
    "septima",
    "octava",
    "novena",
    "decima",
    "fecha",
    "festival",
    "playa",
    "de",
    "verano",
    "amistoso",
]
