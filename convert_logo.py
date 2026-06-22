import base64

def convert_logo_to_base64():
    """Конвертирует logo.png в base64 строку"""
    try:
        with open('logodeveloper.png', 'rb') as f:
            image_data = f.read()
            base64_data = base64.b64encode(image_data).decode('utf-8')
        
        print("LOGO_BASE64 = \"\"\"")
        # Разбиваем на строки по 100 символов для читаемости
        for i in range(0, len(base64_data), 100):
            print(base64_data[i:i+100])
        print("\"\"\"")
        print("\n# Вставьте этот код в переменную LOGO_BASE64 в основном файле")
        return base64_data
    except FileNotFoundError:
        print("Ошибка: файл logo.png не найден!")
        print("Поместите файл logo.png в текущую папку")
        return None

if __name__ == "__main__":
    convert_logo_to_base64()
 