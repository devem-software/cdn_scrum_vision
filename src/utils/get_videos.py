import json
from googleapiclient.discovery import build


def playlists(channel_id: str, api_key: str) -> list:
    """
    Obtiene todas las listas de reproducción de un canal de YouTube.

    Args:
        channel_id (str): El ID del canal de YouTube.
        api_key (str): Clave de la API de YouTube.

    Returns:
        list: Lista de listas de reproducción con su título e ID.
    """
    youtube = build("youtube", "v3", developerKey=api_key)
    playlists_data = []

    next_page_token = None
    while True:
        try:
            playlist_response = youtube.playlists().list(
                part="snippet",
                channelId=channel_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            for item in playlist_response["items"]:
                playlists_data.append({
                    "title": f"{item["id"]}%DIVIDER%{item['snippet']['title']}",
                    "playlistId": item["id"]
                })
            next_page_token = playlist_response.get("nextPageToken")
            if not next_page_token:
                break
        except Exception as e:
            print(f"Error al obtener las listas de reproducción: {e}")
            break

    return playlists_data


def video_duration(video_id: str, api_key: str) -> str:
    """
    Obtiene la duración de un video.

    Args:
        video_id (str): El ID del video.
        api_key (str): Clave de la API de YouTube.

    Returns:
        str: La duración del video en formato ISO 8601 (por ejemplo, 'PT5M33S').
    """
    youtube = build("youtube", "v3", developerKey=api_key)

    try:
        video_response = youtube.videos().list(
            part="contentDetails",
            id=video_id
        ).execute()

        if video_response["items"]:
            return video_response["items"][0]["contentDetails"]["duration"]
    except Exception as e:
        print(f"Error al obtener la duración del video {video_id}: {e}")

    return "Unknown"


def videos_from_playlist(playlist_id: str, api_key: str) -> list:
    """
    Obtiene todos los videos de una lista de reproducción.

    Args:
        playlist_id (str): El ID de la lista de reproducción.
        api_key (str): Clave de la API de YouTube.

    Returns:
        list: Lista de videos con su título, ID, fecha de publicación y duración.
    """
    youtube = build("youtube", "v3", developerKey=api_key)
    videos = []

    next_page_token = None
    while True:
        try:
            playlist_items_response = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            for item in playlist_items_response["items"]:
                video_id = item["snippet"]["resourceId"]["videoId"]
                duration = video_duration(video_id, api_key)  # Obtener duración del video

                videos.append({
                    "title": item["snippet"]["title"],
                    "videoId": video_id,
                    "publishedAt": item["snippet"]["publishedAt"],
                    "duration": duration
                })

            next_page_token = playlist_items_response.get("nextPageToken")
            if not next_page_token:
                break
        except Exception as e:
            print(f"Error al obtener los videos de la lista {playlist_id}: {e}")
            break

    return videos


def all_playlists_videos(channel_id: str, api_key: str) -> dict:
    """
    Obtiene todas las listas de reproducción y los videos dentro de cada una de ellas.

    Args:
        channel_id (str): El ID del canal de YouTube.
        api_key (str): Clave de la API de YouTube.

    Returns:
        dict: Un diccionario con las listas de reproducción como claves y los videos correspondientes como valores.
    """
    playlists_data = playlists(channel_id, api_key)
    playlists_videos = {}

    for playlist in playlists_data:
        print(f"Obteniendo videos de la lista de reproducción: {playlist['title']}")
        videos = videos_from_playlist(playlist["playlistId"], api_key)
        playlists_videos[playlist["title"]] = videos

    return playlists_videos


def count_videos(data: dict) -> None:
    """
    Cuenta el número total de videos en un archivo JSON.

    Args:
        file_path (str): Ruta al archivo JSON.

    Returns:
        int: Número total de videos.
    """
    try:
        print(f"Número total de videos: {len(data)}")
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")
