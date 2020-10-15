import requests
from bs4 import BeautifulSoup
import json
try:
    with open("config.json") as json_data_files:
        json_data = json.load(json_data_files)
        print("open config.json is successful")
    cookies = json_data["cookie"]
except:
    print("open file error")
    pass


def getURL(cookies):

    response = requests.get(
        'https://simaster.ugm.ac.id/akademik/mhs_evaluasi_dosen/periode',  cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.find(
        "a", {"class": "btn btn-warning btn-sm xhr dest_subcontent-element"})
    href = mydivs['href']

    response = requests.get(
        href,  cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.findAll(
        "a", {"class": "btn btn-warning btn-xs xhr dest_subcontent-element"})
    urls = []
    for a in mydivs:
        urls.append(a['href'])
    return urls


def execute(url, nilai='2'):

    response = requests.get(
        url,  cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    simastertoken = soup.find(
        "input", {"name": "simasterUGM_token"})['value']
    sesiId = soup.find(
        "input", {"name": "sesiId"})['value']
    mkKelasId = soup.find(
        "input", {"name": "mkKelasId"})['value']
    mkKelasGabunganId = soup.find(
        "input", {"name": "mkKelasGabunganId"})['value']
    dosenId = soup.find(
        "input", {"name": "dosenId"})['value']

    data = [
        ('simasterUGM_token', simastertoken),
        ('simasterUGM_token', simastertoken),
        ('sesiId', sesiId),
        ('mkKelasId', mkKelasId),
        ('mkKelasGabunganId', mkKelasGabunganId),
        ('dosenId', dosenId),
        ('jawabanInstrumenPilihan[1]', nilai),
        ('jawabanInstrumenPilihan[2]', nilai),
        ('jawabanInstrumenPilihan[3]', nilai),
        ('jawabanInstrumenPilihan[4]', nilai),
        ('jawabanInstrumenPilihan[5]', nilai),
        ('jawabanInstrumenPilihan[6]', nilai),
        ('jawabanInstrumenPilihan[7]', nilai),
        ('jawabanInstrumenPilihan[8]', nilai),
        ('jawabanInstrumenPilihan[9]', nilai),
        ('jawabanInstrumenPilihan[10]', nilai),
        ('jawabanInstrumenPilihan[11]', nilai),
        ('jawabanInstrumenPilihan[12]', nilai),
    ]

    response = requests.post('https://simaster.ugm.ac.id/akademik/mhs_evaluasi_dosen/quesioner',
                              cookies=cookies, data=data)
    return response.status_code


for url in getURL(cookies):
    print(execute(url))
