import csv

def save_proxies(proxies, filename):
    """Сохраняет список прокси в CSV"""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Port", "Type", "Latency"])  # Заголовки CSV
        for proxy in proxies:
            writer.writerow([proxy["ip"], proxy["port"], proxy["type"], proxy["latency"]])
