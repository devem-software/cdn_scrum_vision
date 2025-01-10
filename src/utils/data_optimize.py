import utils.file_system as fs

def item(item:str,data:list, data_base:dict, file_name:str)->None:
    for (index,video) in enumerate(data):
        video[item] = data_base[str(video[item])]
    fs.save(data, file_name)

def teams(data: list, data_base:dict, file_name:str)->None:
    for video in data:
        video["teams"][0] = data_base[video["teams"][0]]
        video["teams"][1] = data_base[video["teams"][1]]
    fs.save(data, file_name)
