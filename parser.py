from bs4 import BeautifulSoup
import re

def parse_spys_one(html):
    """Извлекает прокси из HTML spys.one"""
    soup = BeautifulSoup(html, "html.parser")
    proxies = []
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 2:
            ip_port = cells[0].text.strip()
            if re.match(r"\d+\.\d+\.\d+\.\d+:\d+", ip_port):
                proxies.append(ip_port)
    return proxies

def parse_free_proxy_list(html):
    """Извлекает прокси из HTML free-proxy-list.net"""
    soup = BeautifulSoup(html, "html.parser")
    proxies = []
    for row in soup.select("table tbody tr"):
        cells = row.find_all("td")
        if len(cells) >= 2:
            ip = cells[0].text.strip()
            port = cells[1].text.strip()
            proxies.append(f"{ip}:{port}")
    return proxies

def parse_proxyscrape(proxy_list):
    """Просто возвращает список прокси из ProxyScrape"""
    return proxy_list

def parse_geonode(proxy_list):
    """Просто возвращает список прокси из Geonode"""
    return proxy_list

def parse_all(fetched_data):
    """Парсит данные из всех источников"""
    parsed_proxies = []
    
    parsers = {
        "spys_one": parse_spys_one,
        "free_proxy_list": parse_free_proxy_list,
        "proxyscrape": parse_proxyscrape,
        "geonode": parse_geonode
    }

    for source_name, data in fetched_data:
        print(f"Парсим {source_name}...")
        if data:
            parsed_proxies.extend(parsers[source_name](data))
    
    return parsed_proxies
