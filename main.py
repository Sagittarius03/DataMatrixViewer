"""
DataMatrix CSV Viewer Pro
Главный файл для запуска приложения
"""
import tkinter as tk
from viewer import DataMatrixCSVViewer
import single_instance
import sys
import os


def main():
    """Точка входа в приложение"""
    # Получаем аргументы командной строки
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # Проверяем, есть ли файл для открытия
    file_to_open = None
    for arg in args:
        if os.path.exists(arg) and arg.lower().endswith('.csv'):
            file_to_open = os.path.abspath(arg)
            break
    
    # Проверяем, запущен ли уже экземпляр
    if single_instance.is_already_running():
        if file_to_open:
            # Отправляем файл запущенному экземпляру
            if single_instance.send_file_to_running_instance(file_to_open):
                print(f"📤 Файл отправлен в существующий экземпляр: {file_to_open}")
                sys.exit(0)
            else:
                print("⚠️ Не удалось отправить файл существующему экземпляру")
        else:
            # Если нет файла, просто выходим
            print("📌 Приложение уже запущено")
            sys.exit(0)
    
    # Создаем новое окно
    root = tk.Tk()
    
    # Устанавливаем иконку (если есть)
    try:
        # Ищем файл иконки в папке программы
        icon_paths = ['icon.ico', '../icon.ico', './icon.ico']
        for path in icon_paths:
            if os.path.exists(path):
                root.iconbitmap(path)
                break
    except:
        pass
    
    # Создаем приложение
    app = DataMatrixCSVViewer(root, file_to_open)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Завершение работы...")
        sys.exit(0)


if __name__ == "__main__":
    main()