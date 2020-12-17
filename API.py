# Api League of legends


import requests

api_key="RGAPI-a08db10b-1e63-42ef-9eb0-44990fed3535"
flag_campeon=False

def req_summonerdata(region,summonername,api_key):

    url="https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonername+"?api_key="+api_key
    respuesta=requests.get(url)
    return respuesta.json()

def req_machhistory(region,encryptaccountid,api_key):
    url="https://"+region+".api.riotgames.com/lol/match/v4/matchlists/by-account/"+encryptaccountid+"?api_key="+api_key
    respuesta_HistoryMaches=requests.get(url)
    return respuesta_HistoryMaches.json()

def req_machinfo(region,machid,api_key):
    url="https://"+region+".api.riotgames.com/lol/match/v4/matches/"+machid+"?api_key="+api_key
    respuesta_machinfo=requests.get(url)
    return respuesta_machinfo.json()

region=input("En que reguin Juegas? ")
summonername=input("Cual es tu nombre en LoL: ")
responseJSON=req_summonerdata(region,summonername,api_key)

respuesta_campeones=requests.get("http://ddragon.leagueoflegends.com/cdn/10.25.1/data/es_ES/champion.json")
respuesta_campeones=respuesta_campeones.json()

respuesta_maps=requests.get("http://static.developer.riotgames.com/docs/lol/maps.json")
respuesta_maps=respuesta_maps.json()

print("Nombre:",responseJSON['name'])
print("Nivel:",responseJSON['summonerLevel'])



responseJSON_HistoryMaches=req_machhistory(region,responseJSON['accountId'],api_key)
count=0
for i in range(len(responseJSON_HistoryMaches['matches'])):
    count+=1
    flag_campeon = False
    print("------------------------------------------------")
    print("Partida",count)
    print("ID:",responseJSON_HistoryMaches['matches'][i]['gameId'])
    print("Season:",responseJSON_HistoryMaches['matches'][i]['season'])
    print("Linia:", responseJSON_HistoryMaches['matches'][i]['lane'])
    for j in respuesta_campeones['data']:
        if int(respuesta_campeones['data'][j]['key'])==responseJSON_HistoryMaches['matches'][i]['champion']:
            print("Campeon:",j)
            flag_campeon=True
            break
    if not flag_campeon:
        print("Campeon: Uknown")
    responseJSON_MachInfo=req_machinfo(region,str(responseJSON_HistoryMaches['matches'][i]['gameId']),api_key)

    for j in range(len(respuesta_maps)):
        if respuesta_maps[j]['mapId']==responseJSON_MachInfo['mapId']:
            print("Mapa:",respuesta_maps[j]['mapName'])
            break
    print("------------------------------------------------")
    if count==10:
        break