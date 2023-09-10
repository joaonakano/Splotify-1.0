@echo off
rem Verificar se o Python e o pip estão instalados
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python não está instalado. Por favor, instale o Python e tente novamente.
    exit /b 1
)

pip --version > nul 2>&1
if %errorlevel% neq 0 (
    echo pip não está instalado. Por favor, instale o pip e tente novamente.
    exit /b 1
)

rem Instalar o Pygame
pip install pygame

rem Verificar se a instalação foi bem-sucedida
pip show pygame > nul 2>&1
if %errorlevel% neq 0 (
    echo A instalação do Pygame falhou. Verifique se você está conectado à internet e tente novamente.
    exit /b 1
)

echo Instalação do Pygame concluída com sucesso.
exit /b 0