import utils.variables as VARS
import utils.get_info as info
import utils.file_system as fs
import utils.get_videos as get
import utils.data_normalize as norm
import utils.data_clean as clean
import utils.data_optimize as opt
import os
import sys
import json
from dotenv import load_dotenv
sys.path.append(os.getcwd())


load_dotenv()

# Claves de la API
api_key = os.getenv("YOUTUBE_API_KEY")
channel_id = os.getenv("YOUTUBE_CHANNEL_ID")

# --------------------------------------------------------
# Para ejecutar solo en la primera lectura del canal
# Obtener videos y guardar en JSON
# --------------------------------------------------------
# playlists_videos = get.all_playlists_videos(channel_id, api_key)
# fs.save(playlists_videos, './dist/games')

# --------------------------------------------------------
# Normalizar datos y limpiar registros
# --------------------------------------------------------
data = fs.load('./dist/games')
norm.playlist_to_videos(data, './dist/games_normalized')

normalized = fs.load('./dist/games_normalized')
normalized = clean.blacklist(normalized, VARS.BLACKLIST)

file_clean = './dist/games_normalized_clean'
clean.all(normalized, file_clean)
clean.by_title(normalized, 'Bob Hosty', file_clean)

normalized_clean = fs.load(f"./dist/games_normalized_clean")

# Normalizando modalidades
norm.parse_special_characters("title", normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'F12', 12, normalized_clean, file_clean)
norm.parse_item_by_title('modality', '15s', 15, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'Mas 15', 15, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'super 10', 15, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'super 20', 15, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'mb', 15, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'ma', 15, normalized_clean, file_clean)
# --
norm.parse_item_by_title('modality', "12's", 12, normalized_clean, file_clean)
norm.parse_item_by_title('modality', '12s', 12, normalized_clean, file_clean)
norm.parse_item_by_title('modality', '10s', 10, normalized_clean, file_clean)
# --
norm.parse_item_by_title('modality', "7's", 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', '7s', 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'playa', 'playa', normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'verano', 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'seven', 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'sevens', 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'Gatorade', 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'Ciudad Bolivar', 7, normalized_clean, file_clean)
norm.parse_item_by_title('modality', 'zeppelin rosas', 7, normalized_clean, file_clean)
# --
norm.parse_item_by_title('modality', 'regionales cali', 7, normalized_clean, file_clean)

# --


# Normalizando categorias
norm.parse_item_by_title('category', 'playa m', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'super 20', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'super 10', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'm15s', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'masc', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'masculino', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'masculina', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'mas', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'ma', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'mb', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'm ', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'desarrollo', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'premier', 'M', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'zeppelin', 'M', normalized_clean, file_clean)
# --
norm.parse_item_by_title('category', 'femenino', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'femenina', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'fem', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'fe', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'F ', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'F - ', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'F12', 'F', normalized_clean, file_clean)
norm.parse_item_by_title('category', 'Cachacas', 'F', normalized_clean, file_clean)
# --

# Normalizando torneo
norm.parse_item_by_title('tournament', '15´s Masculino', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'LRB', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'TRCB', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'TCRB', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', '12´s Femenino', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'Torneo Capital', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'Torneo Local', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'Copa de Clubes', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'torneo apertura', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'torneo clausura', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', '15´s Femenino', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', '10´s', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'Desarrollo', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'Premier', 'liga de bogota', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'interligas', 'interligas', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'regionales', 'regionales', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'amistoso', 'amistoso', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'encuentro juvenil', 'amistoso', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'super 10', 'nacional de clubes', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'super 20', 'super 20', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'playa', 'rugby playa', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'festival de verano', 'festival de verano', normalized_clean, file_clean)
norm.parse_item_by_title('tournament', 'internacional de sevens',
                         'internacional de sevens', normalized_clean, file_clean)

norm.parse_item_by_duration("modality", [714, 1200], 7, normalized_clean, file_clean)

tournaments = fs.load('./databases/tournaments')
teams = fs.load('./databases/teams')
modalities = fs.load('./databases/modalities')
categories = fs.load('./databases/categories')

# Optimzacion de la base datos
opt.item("tournament", normalized_clean, tournaments, file_clean)
opt.item("modality", normalized_clean, modalities, file_clean)
opt.item("category", normalized_clean, categories, file_clean)
opt.teams(normalized_clean, teams, file_clean)

opt.minify(file_clean)

info.count_empty_by_item('modality', file_clean, show_data=1)
info.count_empty_by_item('category', file_clean, show_data=1)
info.count_empty_by_item('tournament', file_clean, show_data=1)
info.count_empty_teams(file_clean, show_data=1)
