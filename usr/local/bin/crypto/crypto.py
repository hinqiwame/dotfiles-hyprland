# Self coded
from sys import exc_info, argv
import requests.exceptions

help = f"""My self-coded tool to fetch prices of cryptocurrencies that I use.

Usage: {argv[0]} <coin>
Example usage: {argv[0]} eth

Git: https://github.com/hinqiwame/dotfiles-hyprland/tree/main/usr/local/bin/crypto
"""

def main(coin):
    """Fetches price of a specified coin using coingecko API."""

    import requests
    import colorama
    colorama.init()

    # Format the arguments specified
    if coin  == "eth":
        coin = "ethereum"
    elif coin == "sol":
        coin = "solana"
    elif coin == "trx":
        coin = "tron"
    elif coin == "ltc":
        coin = "litecoin"
    elif coin == "btc":
        coin = "bitcoin"

    coinpretty = coin.capitalize()
    bold  = "\033[1m"
    reset = "\033[0m"

    # Main url
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,eur"
    response = requests.get(url)
    data = response.json()
    if coin in data:
        coindata = data[coin]
        usdprice = coindata.get("usd")
        eurprice = coindata.get("eur")
        print(f"{bold}Price for {coinpretty}{reset}: {usdprice}$ / {eurprice}€")
    else:
        print(f"Couldn't fetch {coinpretty} price.")

if __name__ == "__main__":
    try:
        if argv[1] == "--help":
            print(help)
        else:
            main(argv[1])
    except IndexError:
        print(f"Not enough arguments provided. See {argv[0]} --help to see how to use it.")
    except requests.exceptions.RequestException:
        print("No internet connection, cannot fetch coingecko API.")
    except:
        print("Error: ", exc_info())
