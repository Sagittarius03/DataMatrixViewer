"""
Модуль для построения интерфейса
Содержит конфигурацию стилей и построение элементов UI
"""
import tkinter as tk
from tkinter import ttk


def setup_styles(root):
    """
    Настройка стилей для всего приложения
    
    Args:
        root: Корневое окно Tk
    """
    style = ttk.Style()
    style.theme_use('clam')
    
    # Цветовая схема
    bg_primary = '#0a0e17'
    bg_secondary = '#141b2d'
    bg_input = '#1a2338'
    fg_primary = '#e8edf5'
    fg_secondary = '#8899bb'
    accent = '#4f8cf7'
    accent_hover = '#6a9df8'
    accent_dark = '#3a6fd4'
    success = '#00cc66'
    
    # Настройка палитры Tk
    root.tk_setPalette(
        background=bg_primary,
        foreground=fg_primary,
        selectBackground=accent,
        selectForeground='white'
    )
    
    # Отключаем красное подчеркивание
    root.option_add('*Text.redisplay', False)
    root.option_add('*Entry.redisplay', False)
    root.option_add('*TButton.redisplay', False)
    root.option_add('*TLabel.redisplay', False)
    root.option_add('*TEntry.redisplay', False)
    
    # Стили кнопок
    style.configure('Accent.TButton',
        background=accent,
        foreground='white',
        borderwidth=0,
        focuscolor='none',
        font=('Segoe UI', 9, 'bold')
    )
    style.map('Accent.TButton',
        background=[('active', accent_hover), ('pressed', accent_dark)]
    )
    
    style.configure('Success.TButton',
        background=success,
        foreground='white',
        borderwidth=0,
        focuscolor='none',
        font=('Segoe UI', 9, 'bold')
    )
    style.map('Success.TButton',
        background=[('active', '#00dd77'), ('pressed', '#00bb55')]
    )
    
    style.configure('Secondary.TButton',
        background=bg_secondary,
        foreground=fg_secondary,
        borderwidth=1,
        relief='solid',
        font=('Segoe UI', 9)
    )
    style.map('Secondary.TButton',
        background=[('active', bg_input)],
        foreground=[('active', fg_primary)]
    )
    
    # Стили фреймов
    style.configure('Primary.TFrame', background=bg_primary)
    style.configure('Secondary.TFrame', background=bg_secondary)
    
    # Стили меток
    style.configure('Title.TLabel',
        background=bg_primary,
        foreground=fg_primary,
        font=('Segoe UI', 12, 'bold')
    )
    style.configure('Info.TLabel',
        background=bg_primary,
        foreground=fg_secondary,
        font=('Segoe UI', 9)
    )


def create_header(parent, logo_image):
    """
    Создание заголовка с логотипом
    
    Args:
        parent: Родительский виджет
        logo_image: Изображение логотипа
    
    Returns:
        ttk.Frame: Фрейм заголовка
    """
    header_frame = ttk.Frame(parent, style='Primary.TFrame')
    header_frame.pack(fill=tk.X, pady=(0, 15))
    
    # Левая часть - логотип и название
    logo_frame = ttk.Frame(header_frame, style='Primary.TFrame')
    logo_frame.pack(side=tk.LEFT)
    
    # Логотип
    if logo_image:
        logo_label = tk.Label(
            logo_frame,
            image=logo_image,
            bg='#0a0e17',
            borderwidth=0
        )
        logo_label.pack(side=tk.LEFT, padx=(0, 10))
    else:
        # Запасной вариант - эмодзи
        logo_label = tk.Label(
            logo_frame,
            text="📊",
            font=('Segoe UI', 32),
            bg='#0a0e17',
            fg='#4f8cf7'
        )
        logo_label.pack(side=tk.LEFT, padx=(0, 5))
    
    # Название
    title_frame = ttk.Frame(logo_frame, style='Primary.TFrame')
    title_frame.pack(side=tk.LEFT)
    
    title_label = tk.Label(
        title_frame,
        text="DataMatrix CSV Viewer",
        font=('Segoe UI', 18, 'bold'),
        bg='#0a0e17',
        fg='#e8edf5'
    )
    title_label.pack(anchor='w')
    
    subtitle_label = tk.Label(
        title_frame,
        text="Просмотр и разбивка CSV файлов с кодами Data Matrix",
        font=('Segoe UI', 10),
        bg='#0a0e17',
        fg='#8899bb'
    )
    subtitle_label.pack(anchor='w')
    
    # Правая часть - горячие клавиши
    shortcuts = ttk.Label(header_frame,
        text="Ctrl+O Открыть | Ctrl+S Сохранить | Ctrl+C Копировать | Ctrl+F Найти | Ctrl+B Разбить",
        style='Info.TLabel')
    shortcuts.pack(side=tk.RIGHT)
    
    return header_frame

def create_toolbar(parent, commands):
    """
    Создание панели инструментов
    """
    toolbar = ttk.Frame(parent, style='Secondary.TFrame')
    toolbar.pack(fill=tk.X, pady=(0, 10))
    toolbar.configure(relief='solid', borderwidth=1)
    
    inner = ttk.Frame(toolbar, style='Secondary.TFrame')
    inner.pack(fill=tk.X, padx=10, pady=8)
    
    left_group = ttk.Frame(inner, style='Secondary.TFrame')
    left_group.pack(side=tk.LEFT)
    
    buttons = [
        ("📂 Открыть", commands['open'], 'Accent.TButton'),
        ("📊 Сохранить Excel", commands['save_excel'], 'Accent.TButton'),
        ("🔀 Разбивка по коду", commands['split'], 'Success.TButton'),
        ("📋 Копировать", commands['copy'], 'Secondary.TButton'),
        ("🔍 Найти", commands['find'], 'Secondary.TButton'),
        ("🧹 Очистить", commands['clear'], 'Secondary.TButton'),
    ]
    
    for text, cmd, style_name in buttons:
        btn = ttk.Button(left_group, text=text, command=cmd, style=style_name)
        btn.pack(side=tk.LEFT, padx=3)
    
    separator = ttk.Frame(inner, style='Secondary.TFrame', width=1)
    separator.pack(side=tk.LEFT, padx=10, fill=tk.Y)
    separator.configure(relief='solid', borderwidth=1)
    
    right_group = ttk.Frame(inner, style='Secondary.TFrame')
    right_group.pack(side=tk.RIGHT)
    
    ttk.Label(right_group, text="🔍 Фильтр:", 
             style='Info.TLabel').pack(side=tk.LEFT, padx=(0, 5))
    
    filter_var = tk.StringVar()
    filter_entry = ttk.Entry(right_group, 
        textvariable=filter_var,
        width=25,
        font=('Segoe UI', 9))
    filter_entry.pack(side=tk.LEFT, padx=(0, 5))
    
    clear_filter_btn = ttk.Button(right_group, 
        text="✕", 
        command=commands['clear_filter'],
        style='Secondary.TButton',
        width=3)
    clear_filter_btn.pack(side=tk.LEFT)
    
    return filter_var, filter_entry

def create_stats_bar(parent):
    """
    Создание панели статистики
    
    Args:
        parent: Родительский виджет
    
    Returns:
        dict: Словарь с метками статистики
    """
    stats_frame = ttk.Frame(parent, style='Secondary.TFrame')
    stats_frame.pack(fill=tk.X, pady=(0, 10))
    stats_frame.configure(relief='solid', borderwidth=1)
    
    inner = ttk.Frame(stats_frame, style='Secondary.TFrame')
    inner.pack(fill=tk.X, padx=10, pady=6)
    
    stats_labels = {}
    stats = [
        ("📄 Строк:", "total", "0"),
        ("⚠️ Особых:", "special", "0"),
        ("📁 Файл:", "file", "Не загружен")
    ]
    
    for label, key, default in stats:
        frame = ttk.Frame(inner, style='Secondary.TFrame')
        frame.pack(side=tk.LEFT, padx=15)
        
        ttk.Label(frame, text=label, style='Info.TLabel').pack(side=tk.LEFT)
        stats_labels[key] = ttk.Label(frame, 
            text=default, 
            style='Title.TLabel',
            font=('Segoe UI', 9, 'bold'))
        stats_labels[key].pack(side=tk.LEFT, padx=(3, 0))
    
    return stats_labels