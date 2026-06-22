"""
Тестовый скрипт для проверки CSV файлов на совместимость с OpenLabel
"""
import os
import sys


def test_csv_file(file_path):
    """Проверяет CSV файл на проблемные символы"""
    print(f"Проверка файла: {file_path}")
    
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # Проверяем наличие проблемных символов
    problem_chars = []
    for i, byte in enumerate(content):
        # NUL, управляющие (кроме CR, LF, TAB)
        if byte < 32 and byte not in [9, 10, 13]:
            problem_chars.append((i, byte))
    
    if problem_chars:
        print(f"⚠️ Найдено {len(problem_chars)} проблемных символов:")
        for pos, code in problem_chars[:10]:
            print(f"  Позиция {pos}: HEX {hex(code)}")
    else:
        print("✅ Файл чист, проблемных символов нет")
    
    # Проверяем окончания строк
    crlf_count = content.count(b'\r\n')
    lf_count = content.count(b'\n') - crlf_count
    
    print(f"📊 Окончания строк: CRLF={crlf_count}, LF={lf_count}")
    
    if lf_count > 0:
        print("⚠️ Есть LF (Unix) окончания строк, рекомендуется CRLF (Windows)")
    else:
        print("✅ Все окончания строк в формате CRLF (Windows)")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_csv_file(sys.argv[1])
    else:
        print("Использование: python test_csv.py <путь_к_csv_файлу>")