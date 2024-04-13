import requests

res = requests.get('https://api.nbrb.by/exrates/rates/431').json()
print(res)
print(res.get('Cur_OfficialRate'))
