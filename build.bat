@echo off
echo ========================================
echo  DataMatrix CSV Viewer - Build Script
echo ========================================
echo.

:: Проверяем наличие pyinstaller
pip show pyinstaller > nul 2>&1
if errorlevel 1 (
    echo Установка pyinstaller...
    pip install pyinstaller
    echo.
)

:: Создаем папку для сборки
if not exist dist mkdir dist

:: Собираем приложение
echo Сборка приложения...
pyinstaller --onefile --windowed --name "DataMatrixViewer" --icon=NONE --add-data "logo.py;." main.py

if errorlevel 1 (
    echo.
    echo [ОШИБКА] Сборка не удалась!
    pause
    exit /b 1
)

echo.
echo [ГОТОВО] Приложение собрано в папке dist\
echo Файл: dist\DataMatrixViewer.exe
echo.
pause