import src.utils.file_system as fs
# import difflib

games = fs.load('./dist/games_normalized_clean')

teams = set()
t = dict()

for game in games:
    if game["teams"][0] != "":
        teams.add(game["teams"][0])
    if game["teams"][1] != "":
        teams.add(game["teams"][1])

for (k,v) in enumerate(sorted(teams)):
    t[v]=k

fs.save(t, './databases/teams')



tournaments = set()
t = dict()

for game in games:
    tournaments.add(game["tournament"])

for (k,v) in enumerate(sorted(tournaments)):
    t[v]=k

fs.save(t, './databases/tournaments')


modalities = set()
t = dict()

for game in games:
    modalities.add(str(game["modality"]))

print(modalities)

for (k,v) in enumerate(sorted(modalities)):
    t[v]=k

fs.save(t, './databases/tournaments')


# names = fs.load('./databases/teams')

# normalized = [name.strip().lower() for name in names]

# # Crear un conjunto para los nombres únicos
# unique_names = []

# for name in normalized:
#     # Encontrar nombres similares en la lista única
#     similar = difflib.get_close_matches(name, unique_names, n=1, cutoff=0.9)
#     if not similar:
#         # Si no hay coincidencias similares, añadir el nombre
#         unique_names.append(name)

# unique_names

import re

title ="Mas 15´ - Animals vs Salamandras - TRCB 2021 - Fecha 9"
value = "15´"
item = ""
new_value = 15

pattern = rf'\b{re.escape(value)}\b'
if re.search(pattern, title, re.IGNORECASE) and item == "":
    item = new_value

item

SPECIALS_CHARS = {
    "\u00b4": "'",
    "&#39;": "'",
    "\u00c1": "A",
    "Bogot@": "Bogota",
    "\u00b0": "°",
    "´": ""
}

SPECIALS_CHARS["´"]
