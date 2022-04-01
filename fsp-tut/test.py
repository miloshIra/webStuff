import json
from PIL import Image
import requests

######### GET CHAMPIONS DATA #######################
# response = requests.get('https://ddragon.leagueoflegends.com/cdn/12.5.1/data/en_US/champion.json')


########## GET USER PUUID BY ACCOUNT NAME #####################
# get_user = requests.get('https://europe.api.riotgames.com/lol/summoner/v4/summoners/by-name/sevenxblades?api_key=RGAPI-2ac767af-3454-453b-a638-360bfbd8fefe')

########## GET MATCH DATA BY PUUID ############################
match_data = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/YA8Rdc9B5E_2pRPTryQS3oMsJI3gNWH1MJhnCPdMgITv3wckL25NUrycnw1JoSOksj84P2jjeCqrmw/ids?api_key=RGAPI-2ac767af-3454-453b-a638-360bfbd8fefe')
# print(get_user.text) /lol/match/v5/matches/by-puuid/YA8Rdc9B5E_2pRPTryQS3oMsJI3gNWH1MJhnCPdMgITv3wckL25NUrycnw1JoSOksj84P2jjeCqrmw/ids


#json_data = json.loads(response.text)
#json_user_data = json.loads(get_user.text)
print(match_data.text)

# print(json_user_data['puuid'])

# print(json_data['data']['Graves'])

{'version': '12.5.1', 'id': 'Graves', 'key': '104', 'name': 'Graves', 'title': 'the Outlaw',
 'blurb': 'Malcolm Graves is a renowned mercenary, gambler, and thief—a wanted man in every city and empire he has visited. Even though he has an explosive temper, he possesses a strict sense of criminal honor, often enforced at the business end of his...',
 'info': {'attack': 8, 'defense': 5, 'magic': 3, 'difficulty': 3},
 'image': {'full': 'Graves.png', 'sprite': 'champion1.png', 'group': 'champion', 'x': 336, 'y': 0, 'w': 48, 'h': 48},
 'tags': ['Marksman'], 'partype': 'Mana',
 'stats': {'hp': 555, 'hpperlevel': 92, 'mp': 325, 'mpperlevel': 40, 'movespeed': 340, 'armor': 33,
           'armorperlevel': 3.4, 'spellblock': 32, 'spellblockperlevel': 1.25, 'attackrange': 425, 'hpregen': 8,
           'hpregenperlevel': 0.7, 'mpregen': 8, 'mpregenperlevel': 0.7, 'crit': 0, 'critperlevel': 0,
           'attackdamage': 68, 'attackdamageperlevel': 4, 'attackspeedperlevel': 2.6, 'attackspeed': 0.475}}

# champion_id = json_data['data']['Graves']['id']
# print(champion_id)
#
# image = json_data['data']['Graves']['image']['full']
# print(type(image))
# im = Image.open(image)
# im.show()