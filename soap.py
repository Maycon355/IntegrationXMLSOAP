from ast import For
from time import sleep
from suds import client
import pprint
import xml.etree.ElementTree as ET
from json import loads
from dicttoxml import dicttoxml
import json
import xmltodict
import xml.etree.cElementTree as e
from bs4 import BeautifulSoup
import zeep
from zeep import xsd
from zeep.exceptions import Fault, TransportError, XMLSyntaxError
import xml.etree.ElementTree as ET
from zeep import Client, Settings, xsd
from zeep.exceptions import Fault, TransportError, XMLSyntaxError

# Set Connection
settings = Settings(strict=False, xml_huge_tree=True)

wsdl = "http://192.168.3.52:7080/ws/W0405101.apw?WSDL"
client = zeep.Client(wsdl=wsdl, settings=settings)


Cabec = {
    "NFECAB": {
        "CCHVNFE": "41220503933842000194550010000839881774493908",
        "CCOND": "009",
        "CDOC": "83988",
        "CDTDIGIT": "20220505",
        "CEMISSAO": "20220504",
        "CESPECIE": "SPED",
        "CESTPRES": "PR",
        "CFILSF1": "01087",
        "CFORMUL": "",
        "CFORNECE": "03933842000194",
        "CLOJA": "01",
        "CMUNPRES": "4118402",
        "CNATU": "611001",
        "CORIGLAN": "",
        "CSERIE": "1",
        "CSTATUS": "",
        "CTIPO": "N",
        "NDESCONT": "0",
        "NDESPESA": "0",
        "NFRETE": "0",
        "NMOEDA": "1",
        "NSEGURO": "0",
        "NTXMOEDA": "0"
    },
    "NFEIT": {
        "NFENTRADAITEM": {
            "CCCUSTO": "",
            "CCOD": "COMPOS000234",
            "CCODISS": "",
            "CDTDIGITD1": "",
            "CITEM": "1",
            "CITEMCTA": "",
            "CLOCAL": "000999",
            "COPER": "",
            "CTES": "210",
            "CTRIBMUN": "",
            "CUM": "UN",
            "NDESPESA": "0",
            "NQUANT": "5000",
            "NSEGURO": "0",
            "NTOTAL": "30800",
            "NVALDESC": "0",
            "NVALFRE": "0",
            "NVUNIT": "6,16"
        }
    }
}

response = client.service.NFENTRADA(Cabec)
print(response)


# with open('C:\\Users\\maycon.silva1\\Documents\\exemplo.json', 'r', encoding='utf-8') as f:
#    data = f.read()
#    data = json.loads(data)


# Cabec = {
#    "NFECAB": {
#        "CCHVNFE": "41220534274233025946550000005447421672179336",
#        "CCOND": "025",
#        "CDOC": "544742",
#        "CDTDIGIT": "20220517",
# "CEMISSAO": "20220517",
#      "CESPECIE": "SPED",
#      "CESTPRES": "PR",
#      "CFILSF1": "01096",
#      "CFORMUL": "",
#      "CFORNECE": "34274233025946",
#      "CLOJA": "01",
#      "CMUNPRES": "4115200",
#      "CNATU": "611001",
#      "CORIGLAN": "",
#      "CSERIE": "0",
#      "CSTATUS": "",
#      "CTIPO": "N",
#      "NDESCONT": 0,
#      "NDESPESA": 0,
#      "NFRETE": 0,
#      "NMOEDA": 1,
#      "NSEGURO": 0,
#      "NTXMOEDA": 0,#

#       "NFEIT": {
#           "CCCUSTO": "",
#           "CCOD": "COMPOS000234",
#           "CCODISS": "",
#        "CDTDIGITD1": "",
#        "CITEM": "1",
#    "CITEMCTA": "",
#       "CLOCAL": "000999",
#        "COPER": "",
#         "CTES": "210",
#         "CTRIBMUN": "",
#          "CUM": "UN",
#        "NDESPESA": "0",
#        "NQUANT": "5000",
#         "NSEGURO": "0",
#      "NTOTAL": "32100",
#          "NVALDESC": "0",
#          "NVALFRE": "0",
#            "NVUNIT": "6,42"}
#  }
# }


response = client.service.NFENTRADA(Cabec)
print(response)


# url = "http://192.168.3.52:7080/ws/W0405101.apw?WSDL"
# soap = client.Client(url)


# with open("C:\\Users\\maycon.silva1\\Documents\\exemplo.xml", encoding='utf-8') as meu_json:
#    dados = meu_json
#    print(dados)

# with open('C:\\Users\\maycon.silva1\\Documents\\exemplo.xml', 'r', encoding='utf-8') as f:
#    data = f.read()
#    print(data)


# xmlstr = ET.tostring(data, encoding='utf-8', method='xml')

# resposta = soap.service.NFENTRADA(xmlstr)
# pprint.pprint(resposta)

# python -mzeep http://192.168.3.52:7080/ws/W0405101.apw?WSDL
