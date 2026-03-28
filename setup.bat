@echo off
title InstantCMD Setup
echo.
echo  ===================================
echo   InstantCMD - Setup
echo  ===================================
echo.

:: Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python is not installed or not in PATH.
    echo  Please install Python 3.8+ from https://python.org
    echo.
    pause
    exit /b 1
)

echo  [1/2] Installing dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo  [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)

echo  [2/2] Setup complete!
echo.
echo  ===================================
echo   To launch InstantCMD, run:
echo     python instantcmd.py
echo   Or double-click: run.bat
echo  ===================================
echo.
pause
