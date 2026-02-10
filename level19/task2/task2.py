
import requests
import codes


id = input("select crypto id: (example: bitcoin, ethereum, tether, binancecoin, solana, ripple, usd-coin, cardano, avalanche-2, dogecoin, tron):\n")

headers = {"x-cg-demo-api-key": codes.key}

url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={id}"


response = requests.get(url, headers=headers)
result = response.json()

status_code = response.status_code


if status_code==200 and len(result) == 1:
    price = result[id]["usd"]
    print(f"1 {id} = {price} USD")
else:
    print("Такої криптовалюти неіснує")