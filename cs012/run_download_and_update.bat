@echo off
REM 批处理文件：正确执行 download_and_update.ps1 脚本
REM 此文件演示了如何正确处理包含空格的路径

REM 获取当前批处理文件所在目录
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_PATH=%SCRIPT_DIR%download_and_update.ps1"

REM 方法1：使用 -File 参数（推荐，可以正确处理路径中的空格）
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_PATH%"

REM 如果需要传递参数，可以这样：
REM powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_PATH%" -SkipIfExists
REM powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_PATH%" -Url "http://example.com/file.zip"

pause

