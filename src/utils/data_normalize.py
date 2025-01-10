import re
import utils.variables as VARS
import utils.file_system as fs
import utils.parse_time as pt
import utils.data_clean as clean


def playlist_to_videos(data: list, file_name: str) -> None:

    unique_ids = set()
    clean_duplicates: list = []

    # Obtener id no duplicados
    for videos in data:
        for video in data[videos]:
            unique_ids.add(video["videoId"])

    # Limpiar los registros en base a los id unicos
    for videos in data:
        for video in data[videos]:
            if video["videoId"] not in [v["videoId"] for v in clean_duplicates]:
                clean_duplicates.append(video)

    data = add_year(clean_duplicates)
    data = add_events(data)
    data = add_teams(data)
    data = white_spaces(data)
    data = set_team_special_case(data, "bogota vs", "bogota", 0)
    data = set_team_special_case(data, "bogota d.c. vs", "bogota", 0)
    data = set_team_special_case(data, "vs bogota", "bogota", 1)
    data = set_team_special_case(data, "vs bogota d.c.", "bogota", 1)
    data = set_team_special_case(data, "vs equipo", "bogota", 1)
    data = set_team_special_case(data, "lrb vs", "lrb", 0)
    data = set_team_special_case(data, "vs lrb", "lrb", 1)

    fs.save(data, file_name)


def white_spaces(data: list) -> list:
    for video in data:
        video["title"] = " ".join(video["title"].split())
    return data


def add_year(data: list) -> list:

    for video in data:
        if isinstance(video["publishedAt"], str):
            video["year"] = int(video["publishedAt"].split("T")[0].split("-")[0])
            video["duration"] = pt.iso_time_to_seconds(video["duration"])
    return data


def add_events(data: list) -> list:

    event = {
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

    for video in data:
        video["modality"] = ""
        video["category"] = ""
        video["tournament"] = ""
        video["teams"] = ["", ""]
        video["events"] = [event, event]

    return data


def parse_special_characters(item: str, data: list, file_name: str) -> None:
    # Recorremos todos los caracteres especiales
    for special_char, replacement in VARS.SPECIALS_CHARS.items():
        for video in data:
            # Reemplazamos cada ocurrencia del caracter especial por su reemplazo
            video[item] = video[item].replace(special_char, replacement)
    
    # Guardamos los cambios en el archivo
    fs.save(data, file_name)


def parse_item_by_title(item: str, value: str, new_value: str | int | bool | float, data: list, file_name: str) -> None:

    for video in data:
        pattern = rf'\b{re.escape(value)}\b'
        if re.search(pattern, video["title"], re.IGNORECASE) and video[item] == "":
            video[item] = new_value

    fs.save(data, file_name)


def parse_item_by_duration(item: str, beetwen: list, new_value: str | int | bool | float, data: list, file_name: str) -> None:
    for (index, video) in enumerate(data):
        if beetwen[0] < video["duration"] < beetwen[1] and video[item] == "":
            video[item] = new_value
    fs.save(data, file_name)


def add_teams(data: list) -> list:
    cleaned_data: list = []
    step: int = 0
    for video in data:
        title = video["title"].lower()
        match = re.match(r"(.*)vs(.*)", title)
        if match:
            groups = match.groups()
            cleaned_teams = clean.team_names(groups)
            cleaned_data.append(cleaned_teams)
            step += 1
            video["teams"] = cleaned_teams
    return data


def set_team_special_case(data: list, text:  str, value: str, position: int) -> list:
    for game in data:
        if text.lower() in game["title"].lower():
            game["teams"][position] = value.lower()
    return data
