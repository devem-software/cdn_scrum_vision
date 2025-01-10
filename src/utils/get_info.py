import utils.file_system as fs


def count_empty_by_item(item: str, file_name: str, show_data:bool = False, show_count: bool = True) -> None:
    data: list = fs.load(file_name)
    count_empty: int = 0
    data_empty: set = set()
    for video in data:
        if video[item] == "":
            count_empty += 1
            data_empty.add(video["videoId"])

    if show_data:
        if len(data_empty) > 0:
            print(f"\nRegistros sin {item}: {data_empty}")
        else:
            print(f"\nEl campo {item} esta completo")
    if show_count:
        print(f"Total de registros sin {item}: {count_empty}")


def count_empty_teams(file_name: str, show_data:bool = False, show_count:bool = True) -> None:
    data: list = fs.load(file_name)
    empty: int = 0
    incomplete: int = 0
    complete: int = 0
    data_empty: set = set()
    for video in data:
        if video["teams"][0] == "" or video["teams"][1] == "":
            incomplete += 1
            data_empty.add(video["videoId"])
        if video["teams"][0] == "" and video["teams"][1] == "":
            empty += 1
            data_empty.add(video["videoId"])
        if video["teams"][0] != "" and video["teams"][1] != "":
            complete += 1

    if show_data:
        if len(data_empty) > 0:
            print(f"\nRegistros incompletos: {data_empty}")
        else:
            print(f"\nEl campo teams esta completo")
    if show_count:
        print("Total de registros")
        print(f"Registros completos\t\t{complete}")
        print(f"Registros incompletos \t\t{incomplete}")
        print(f"Registros vacios \t\t{empty}")
