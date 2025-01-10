import json
import os


def load(file_name: str, encoding: str = "utf-8") -> list:
    if exists(file_name):
        with open(f"{file_name}.json", "r", encoding=encoding) as file:
            data = json.load(file)
    return data


def save(data: list, file_name: str, encoding: str = "utf-8") -> None:
    if not isinstance(data, (list, dict)):
        raise ValueError(
            "Los datos a guardar deben ser una lista o un diccionario.")

    try:
        with open(f"{file_name}.json", "w", encoding=encoding) as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")


def exists(file_name: str) -> bool:
    return os.path.exists(f"{file_name}.json")
