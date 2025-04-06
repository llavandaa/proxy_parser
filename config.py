CONFIG = {
    "spys_url": "https://spys.one/ru/",
    "timeout": 20,                      # Таймаут для HTTP-запросов (в секундах)
    "max_workers": 10,                 # Количество потоков для проверки прокси
    "test_url": "https://httpbin.org/ip",# URL для проверки прокси
    "output_file": "valid_proxies.csv",# Файл для сохранения валидных прокси
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/110.0.0.0 Safari/537.36"
}