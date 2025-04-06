import ssl
import requests
from concurrent.futures import ThreadPoolExecutor

# Создаем кастомный SSL-контекст
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = True

def check_proxy(proxy_str):
    """Проверяет работоспособность одного прокси, переданного в виде строки 'IP:PORT'."""
    try:
        ip, port = proxy_str.split(":")  # Разбираем строку на IP и порт
        test_url = "https://www.google.com"

        proxies = {
            "http": f"http://{ip}:{port}",
            "https": f"http://{ip}:{port}"
        }

        response = requests.get(test_url, proxies=proxies, timeout=5, verify=True)
        if response.status_code == 200:
            return proxy_str  # Если прокси рабочий, возвращаем строку

    except Exception:
        return None  # Если ошибка, возвращаем None

def check_proxies(proxy_list):
    """Проверяет список прокси в многопоточном режиме."""
    valid_proxies = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_proxy, proxy_list)

    for proxy in results:
        if proxy:
            valid_proxies.append(proxy)

    return valid_proxies  # Возвращаем список валидных прокси
