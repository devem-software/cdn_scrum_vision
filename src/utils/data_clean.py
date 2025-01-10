import re
import utils.variables as VARS
import utils.file_system as fs
import utils.parse_time as time


def duplicates(data: list) -> list:
    unique_ids = set()
    filtered_data = []

    for video in data:
        if video["videoId"] not in unique_ids:
            unique_ids.add(video["videoId"])
            filtered_data.append(video)

    return filtered_data


def blacklist(data: list, blacklist: list) -> list:
    filtered_data = []
    for video in data:
        if video["videoId"] not in blacklist:
            filtered_data.append(video)

    return filtered_data


def under_time(data: list) -> list:
    clean_under_840_seconds = []
    for video in data:
        if video["duration"] != "Unknown" and video["duration"] > 840:
            clean_under_840_seconds.append(video)

    return clean_under_840_seconds


def all(data: list, file_path: str) -> None:
    data = duplicates(data)
    data = under_time(data)
    data = blacklist(data, VARS.BLACKLIST)
    fs.save(data, file_path)


def by_title(data: list, title: str, file_path: str) -> None:
    filtered_data = []
    for video in data:
        if title not in video["title"]:
            filtered_data.append(video)

    fs.save(filtered_data, file_path)


# FIXME: This function is not working properly
# TODO: Add more characters to the list

def replace_characters(data: list, char_list: list) -> None:
    for video in data:
        for key in video:
            if key == "title":
                for char in char_list:
                    video[key] = video[key].replace(char, "")


def team_names(groups: tuple) -> list:
    """
    Limpia los nombres de equipos eliminando las palabras no deseadas según clear_words.

    Args:
        groups (tuple): Contiene los nombres de los equipos extraídos.
        clear_words (list): Lista de palabras a eliminar de los nombres.

    Returns:
        list: Nombres limpios de los equipos.
    """
    # Crear un patrón regex con las palabras en clear_words
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in VARS.CLEAN_WORDS) + r')\b', re.IGNORECASE)

    cleaned_teams = []
    for group in groups:
        # Eliminar palabras de clear_words
        cleaned_group = pattern.sub('', group)
        # Eliminar puntos y espacios adicionales
        cleaned_group = re.sub(r'[^\w\s]', '', cleaned_group)  # Elimina todo excepto letras, números y espacios
        cleaned_group = re.sub(r'\s+', ' ', cleaned_group).strip()  # Compacta múltiples espacios en uno
        cleaned_teams.append(cleaned_group)

    return cleaned_teams
