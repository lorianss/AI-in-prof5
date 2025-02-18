import os
import time
from concurrent.futures import ThreadPoolExecutor


def find_log_files_multithreaded(root_dir):
    log_files = []

    def process_directory(directory):
        try:
            with os.scandir(directory) as entries:
                for entry in entries:
                    if entry.is_file() and entry.name.lower().endswith('.log'):
                        log_files.append(entry.path)
                    elif entry.is_dir():
                        process_directory(entry.path)
        except PermissionError:
            print(f"Нет доступа к директории: {directory}")
        except FileNotFoundError:
            print(f"Директория не существует: {directory}")
        except OSError as e:
            print(f"Ошибка при обработке директории '{directory}': {e}")

    with ThreadPoolExecutor(max_workers=8) as executor:  # 8 потоков
        executor.submit(process_directory, root_dir)

    return log_files


# Пример использования
if __name__ == "__main__":
    root_directory = r"D:\one\2\3\4\55\6\7\8\9\10\2\Новая папка"

    if os.path.exists(root_directory) and os.path.isdir(root_directory):
        print("Начинаем поиск...")
        start_time = time.time()

        log_files = find_log_files_multithreaded(root_directory)

        end_time = time.time()
        print(f"Поиск завершён за {end_time - start_time:.2f} секунд.")

        print("Найденные .log файлы:")
        for file in log_files:
            print(file)
    else:
        print(f"Указанный путь '{root_directory}' не существует или не является директорией.")