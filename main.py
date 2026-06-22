"""
DataMatrix CSV Viewer Pro
Главный файл для запуска приложения
"""
import tkinter as tk
from viewer import DataMatrixCSVViewer


def main():
    """Точка входа в приложение"""
    root = tk.Tk()
    app = DataMatrixCSVViewer(root)
    root.mainloop()


if __name__ == "__main__":
    main()