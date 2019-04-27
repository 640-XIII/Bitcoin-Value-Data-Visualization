import matplotlib.pyplot as plt
from time import sleep as s
from requests import get
from bs4 import BeautifulSoup

time = int(1)

plt.style.use("ggplot")
plt.figure("Bitcoin Value")
plt.title("Value")

for i in range(4):
    htmlDataRaw = get("https://www.coinbase.com/price/bitcoin").text
    soup = BeautifulSoup(htmlDataRaw, features = "html.parser")

    bitcoinValue = soup.find("div", "ChartPriceHeader__BigAmount-eVkcaL fyHSnf").text
    bitcoinValue = bitcoinValue.replace(",", ""); bitcoinValue = bitcoinValue.replace(".", "")

    plt.scatter(i, int(bitcoinValue[1:]))

    time += 1
    plt.pause(1)