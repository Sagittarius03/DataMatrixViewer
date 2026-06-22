"""
Модуль для регистрации программы в Windows как обработчика CSV файлов
"""
import os
import sys
import winreg
import subprocess


def register_file_association():
    """
    Регистрирует программу как обработчик для .csv файлов в Windows
    """
    try:
        # Получаем путь к текущему исполняемому файлу
        if getattr(sys, 'frozen', False):
            # Если запущено как .exe
            app_path = sys.executable
        else:
            # Если запущено как скрипт
            app_path = f'"{sys.executable}" "{__file__}"'
        
        # Регистрируем программу
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'.csv') as key:
            winreg.SetValueEx(key, None, 0, winreg.REG_SZ, 'DataMatrixCSVViewer.csv')
        
        # Создаем команду открытия
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv\shell\open\command') as key:
            winreg.SetValueEx(key, None, 0, winreg.REG_SZ, f'{app_path} "%1"')
        
        # Устанавливаем иконку
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv\DefaultIcon') as key:
            winreg.SetValueEx(key, None, 0, winreg.REG_SZ, f'{app_path},0')
        
        print("✅ Программа зарегистрирована как обработчик .csv файлов")
        return True
        
    except Exception as e:
        print(f"⚠️ Не удалось зарегистрировать программу: {e}")
        print("   Запустите программу от имени администратора для регистрации")
        return False


def unregister_file_association():
    """
    Удаляет регистрацию программы как обработчика
    """
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv\shell\open\command')
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv\shell\open')
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv\shell')
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv\DefaultIcon')
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DataMatrixCSVViewer.csv')
        winreg.DeleteValue(winreg.HKEY_CLASSES_ROOT, r'.csv', None)
        print("✅ Регистрация программы удалена")
        return True
    except Exception:
        print("⚠️ Не удалось удалить регистрацию")
        return False


def show_association_menu():
    """Показывает меню для регистрации/отмены регистрации"""
    print("\n=== Регистрация обработчика .csv файлов ===")
    print("1 - Зарегистрировать программу как обработчик .csv")
    print("2 - Отменить регистрацию")
    print("3 - Выход")
    
    choice = input("\nВыберите действие: ").strip()
    
    if choice == '1':
        register_file_association()
    elif choice == '2':
        unregister_file_association()
    elif choice == '3':
        return
    else:
        print("Неверный выбор")
    
    if choice in ['1', '2']:
        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    show_association_menu()