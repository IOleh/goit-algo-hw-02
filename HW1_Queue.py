import queue
import random
import time

# Створюємо чергу для заявок
requests_queue = queue.Queue()

# Лічильник для генерації унікальних ідентифікаторів заявок
request_id = 0

# Функція для генерації нових заявок
def generate_request():
    global request_id
    request_id += 1
    new_request = f"Request-{request_id}"
    requests_queue.put(new_request)
    print(f"Заявку {new_request} додано до черги.")

# Функція для обробки заявок
def process_request():
    if not requests_queue.empty():
        current_request = requests_queue.get()
        print(f"Обробляється {current_request}...")
        # Імітація часу обробки заявки
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{current_request} успішно оброблено.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Основний цикл програми
def main():
    try:
        while True:
            # Імітація генерації нових заявок (одна заявка кожні 1-3 секунди)
            if random.choice([True, False]):
                generate_request()

            # Імітація обробки заявки (кожні 1-2 секунди)
            process_request()

            # Затримка між ітераціями
            time.sleep(random.uniform(1, 2))
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

if __name__ == "__main__":
    main()
