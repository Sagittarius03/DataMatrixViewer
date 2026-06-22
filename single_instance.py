"""
Модуль для обеспечения единственного экземпляра приложения
Использует сокет для межпроцессного взаимодействия
"""
import socket
import sys
import os
import time

PORT = 25715  # Порт для сокета


def is_already_running():
    """
    Проверяет, запущен ли уже другой экземпляр приложения
    
    Returns:
        bool: True если другой экземпляр запущен, иначе False
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect(('127.0.0.1', PORT))
        sock.close()
        return True
    except socket.error:
        return False


def send_file_to_running_instance(file_path):
    """
    Отправляет путь к файлу уже запущенному экземпляру
    
    Args:
        file_path (str): Путь к файлу для открытия
    
    Returns:
        bool: True если успешно отправлено, иначе False
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', PORT))
        sock.send((file_path + '\n').encode('utf-8'))
        response = sock.recv(1024).decode('utf-8')
        sock.close()
        return response == 'OK'
    except Exception:
        return False


def start_server(handler_func):
    """
    Запускает сервер для приема команд от других экземпляров
    
    Args:
        handler_func: Функция-обработчик, принимающая file_path
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', PORT))
    server.listen(1)
    server.settimeout(0.5)
    
    while True:
        try:
            conn, addr = server.accept()
            data = conn.recv(4096).decode('utf-8').strip()
            if data:
                handler_func(data)
                conn.send(b'OK')
            conn.close()
        except socket.timeout:
            continue
        except Exception:
            break