import sys
import os
from fetcher import fetch_all
from parser import parse_all
from checker import check_proxies
from saver import save_proxies


try:
    def main():
        try:
            clear = int(input("Очистить файл valid_proxies.csv?\n1. Да\n2. Нет\n3. Выход\nВаш выбор: "))
            if clear == 1 and os.path.exists("valid_proxies.csv"):
                os.remove("valid_proxies.csv")
            elif clear == 2 and os.path.exists("valid_proxies.csv"):
                pass
            elif clear == 3 and os.path.exists("valid_proxies.csv"):
                print("Выход из программы.")
            sys.exit(0)


        except ValueError:
            print("Ошибка: Введите 1 или 2.")
            return

        print("Начинаем сбор прокси...")
        fetched_data = fetch_all()
        
        print("Извлекаем прокси из полученных данных...")
        proxies = parse_all(fetched_data)

        print(f"Найдено {len(proxies)} прокси. Проверяем их...")
        valid_proxies = check_proxies(proxies)

        if valid_proxies:
            print(f"Сохранение {len(valid_proxies)} валидных прокси в файл...")
            save_proxies(valid_proxies, "valid_proxies.csv")
            print("Готово!")
        else:
            print("Не было найдено валидных прокси.")

    if __name__ == "__main__":
        main()


except KeyboardInterrupt:
    print("\nПрограмма остановлена пользователем.")
    sys.exit(0)
except Exception as e:
    print(f"\nПроизошла ошибка: {e}")
    sys.exit(1)

print("Программа завершена успешно.")
sys.exit(0)