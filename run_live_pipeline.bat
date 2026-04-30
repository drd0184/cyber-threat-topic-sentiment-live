@echo off
setlocal

cd /d "%~dp0"

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py scripts\run_live_pipeline.py
    exit /b %ERRORLEVEL%
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python scripts\run_live_pipeline.py
    exit /b %ERRORLEVEL%
)

set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%BUNDLED_PYTHON%" (
    "%BUNDLED_PYTHON%" scripts\run_live_pipeline.py
    exit /b %ERRORLEVEL%
)

echo Python was not found. Install Python or update run_live_pipeline.bat with the correct interpreter path.
exit /b 1
