from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re


try:
    html = urlopen("https://empresas.americanas.com.br/hotsite/empresas-dell-infoacess?chave="
                    "hmem_banner1_dell&pfm_carac=dell&pfm_page=home&pfm_pos=contentmiddle1&pfm_type=vit_spacey")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")

    if res.title is None:
        print("T&iacute;tulo n&atilde;o encontrado")
    else:
        print("Link Fixo - " + res.title.getText() + "\n")

    tags = res.findAll("h2", {"class": "TitleUI-bwhjk3-15 jfuFNN TitleH2-sc-1wh9e1x-1 gYIWNc"})
    preco = res.findAll("span", {"class": "PriceUI-bwhjk3-11 jtJOff PriceUI-sc-1q8ynzz-0 dHyYVS TextUI-sc-12tokcy-0 bLZSPZ"})

    numTags = len(tags)
    numPreco = len(preco)

    qtdLinks = 0
    itemSelecionado = 0

    while qtdLinks < numTags:
        if re.search('notebook\\b', tags[qtdLinks].getText(), re.IGNORECASE):
            print("(" + preco[qtdLinks].getText() + ") " + tags[qtdLinks].getText())
            itemSelecionado += 1
        qtdLinks += 1

    print("\nTotal de " + str(numTags) + " links encontrados!")
    print("Exibindo " + str(itemSelecionado) + " links com notebook!")