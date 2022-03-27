
from bs4 import BeautifulSoup
import requests
import re






CdKeysUrl = 'https://www.cdkeys.com/elden-ring-pc-steam'
SteamUrl = 'https://store.steampowered.com/app/1245620/ELDEN_RING/'

CdKeysRequest = requests.get(CdKeysUrl).text
SteamRequest = requests.get(SteamUrl).text



CdKeysResults = re.search('"price":\d\d\d', CdKeysRequest).group(0)
SteamResults = re.search('final="\d\d\d', SteamRequest).group(0)

print('Elden Ring is','R' + CdKeysResults.split(':')[1], 'On CdKeys')
print('Elden Ring is','R' + SteamResults.split('=')[1].strip('"'), 'On Steam')

ey =  input("----")