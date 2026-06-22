"""
Модуль для работы с CSV файлами
Содержит функции для чтения и записи CSV с правильными окончаниями строк
"""
import os
import re


def normalize_line_endings(text):
    """
    Нормализация окончаний строк для Windows (CRLF)
    Преобразует LF в CRLF
    
    Args:
        text (str): Исходный текст
    
    Returns:
        str: Текст с Windows окончаниями строк
    """
    if not text:
        return text
    
    # Сначала удаляем все CR, потом заменяем LF на CRLF
    text = text.replace('\r\n', '\n')  # Убираем дублирование
    text = text.replace('\r', '')       # Удаляем одиночные CR
    text = text.replace('\n', '\r\n')   # Заменяем LF на CRLF
    
    return text


def read_csv_with_encoding(file_path):
    """
    Читает CSV файл с определением кодировки
    
    Args:
        file_path (str): Путь к файлу
    
    Returns:
        tuple: (data, encoding) - список строк и использованная кодировка
    """
    encodings = ['utf-8-sig', 'utf-8', 'cp1251', 'cp866', 'latin-1', 'koi8-r']
    data = []
    used_encoding = None
    
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                content = f.read()
            
            lines = []
            for line in content.split('\n'):
                line = line.strip()
                if line:
                    lines.append(line)
            
            if lines:
                data = lines
                used_encoding = enc
                break
        except:
            continue
    
    # Если не удалось прочитать ни одной кодировкой
    if not data:
        try:
            with open(file_path, 'rb') as f:
                content = f.read().decode('utf-8', errors='ignore')
            data = [line.strip() for line in content.split('\n') if line.strip()]
            used_encoding = 'utf-8 (с игнором ошибок)'
        except:
            raise Exception("Не удалось прочитать файл ни в одной кодировке")
    
    return data, used_encoding


def save_csv_with_crlf(file_path, data):
    """
    Сохраняет данные в CSV с Windows окончаниями строк
    
    Args:
        file_path (str): Путь для сохранения
        data (list): Список строк
    
    Returns:
        bool: True если успешно
    """
    try:
        with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
            for line in data:
                normalized_line = normalize_line_endings(line)
                f.write(normalized_line + '\r\n')
        return True
    except Exception as e:
        print(f"Ошибка при сохранении CSV: {e}")
        return False