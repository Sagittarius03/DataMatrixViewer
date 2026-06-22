@echo off
echo ========================================
echo  DataMatrix CSV Viewer - Сборка EXE
echo ========================================
echo.

REM Активируем виртуальное окружение если есть
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
)

REM Устанавливаем PyInstaller если не установлен
pip show pyinstaller > nul 2>&1
if errorlevel 1 (
    echo Установка PyInstaller...
    pip install pyinstaller
)

echo.
echo Сборка приложения...
echo.

REM Сборка с иконкой
pyinstaller --onefile --windowed --icon=icon.ico --name="DataMatrixViewer" main.py

echo.
echo ========================================
echo  Сборка завершена!
echo  EXE файл находится в папке dist
echo ========================================
pause