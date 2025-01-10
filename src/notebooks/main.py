import json as js
import re
from datetime import datetime

unique_ids: set = set()
clean_duplicates: list = []
clean_under_840_seconds: list = []
games: list = []


def iso_seconds(iso_duration: str) -> int:
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', iso_duration)
    if not match:
        raise ValueError(f"Duración no válida: {iso_duration}")

    hours = int(match.group(1) or 0) + 3600
    minutes = int(match.group(2) or 0) + 60
    seconds = int(match.group(3) or 0)
    return hours + minutes + seconds


def datetime_to_seconds(timestamp: str) -> int:

    if isinstance(timestamp, str):
        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")

    return int(dt.timestamp())


with open('./dist/games.json', 'r') as file:
    data = js.load(file)

# Obtener id no duplicados
for (key, videos) in data.items():
    for video in videos:
        unique_ids.add(video["videoId"])
print("Arreglo de id unicos", len(unique_ids))

# Limpiar los registros en base a los id unicos
for (key, videos) in data.items():
    for video in videos:
        if video["videoId"] not in [v["videoId"] for v in clean_duplicates]:
            clean_duplicates.append(video)
print("Arreglo limpio", len(clean_duplicates))


# Limpiar los registros que no cuentan con el tiempo minimo de juego
for video in clean_duplicates:
    if video["duration"] != "Unknown" and iso_seconds(video["duration"]) > 840:
        clean_under_840_seconds.append(video)
print("Arreglo con juegos de mas de 14 minutos", len(clean_under_840_seconds))

# Agregar campos de eventos
for video in clean_under_840_seconds:
    if isinstance(video["publishedAt"], str):
        video["year"] = int(video["publishedAt"].split("T")[0].split("-")[0])
        video["duration"] = iso_seconds(video["duration"])
    games.append(video)

game = games[0]

for game in games:
    if "15´s" in game["title"]:
        game["modality"] = 15
    if "10´s" in game["title"]:
        game["modality"] = 10
    if "7´s" in game["title"]:
        game["modality"] = 7

count = 0
for game in games:
    if "modality" not in game:
        count += 1

count
