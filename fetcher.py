# Модуль для загрузки списка прокси

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_spys_one():
    """Получает HTML с сайта spys.one и возвращает содержимое"""
    url = "https://spys.one/ru/"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при обработке spys_one: {e}")
        return None

def fetch_free_proxy_list():
    """Получает HTML с free-proxy-list.net"""
    url = "https://www.free-proxy-list.net/"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при обработке free-proxy-list: {e}")
        return None

def fetch_proxyscrape():
    """Получает текстовый список прокси с ProxyScrape"""
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text.strip().split("\n")  # Разбиваем построчно
    except requests.RequestException as e:
        print(f"Ошибка при обработке ProxyScrape: {e}")
        return None

def fetch_geonode():
    """Получает JSON-список прокси с Geonode"""
    url = "https://proxylist.geonode.com/api/proxy-list?protocols=http"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return [f"{proxy['ip']}:{proxy['port']}" for proxy in data['data']]
    except requests.RequestException as e:
        print(f"Ошибка при обработке Geonode: {e}")
        return None

def fetch_all():
    """Собирает прокси со всех источников"""
    proxies = []
    
    sources = {
        "spys_one": fetch_spys_one,
        "free_proxy_list": fetch_free_proxy_list,
        "proxyscrape": fetch_proxyscrape,
        "geonode": fetch_geonode
    }

    for name, fetch_function in sources.items():
        print(f"Получение прокси из {name}...")
        result = fetch_function()
        if result:
            proxies.append((name, result))

    return proxies
