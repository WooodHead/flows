# PowerShell脚本：从指定地址下载文件并自动解压缩和更新
# 使用方法：
#   1. 右键点击此文件，选择"使用PowerShell运行"
#   2. 或者在PowerShell中运行:
#      .\download_and_update.ps1
#      .\download_and_update.ps1 -Url "http://example.com/file.zip"
#      .\download_and_update.ps1 -SkipIfExists
#      .\download_and_update.ps1 -Url "http://example.com/file.zip" -SkipIfExists
#   3. 从命令行（CMD）或批处理文件中执行（路径包含空格时）:
#      powershell.exe -File "完整路径\download_and_update.ps1"
#      powershell.exe -File "C:\Users\Thinkbook 16 G5\Downloads\download_and_update.ps1"
#   注意：如果路径包含空格，必须使用 -File 参数并用引号包裹路径
#   错误示例：powershell "路径"  （这会导致路径被错误解析）
#   正确示例：powershell.exe -File "路径"
# 参数说明：
#   -Url: 下载地址（可选，有默认值）
#   -OutputDir: 输出目录（可选，默认为脚本目录下的downloads文件夹）
#   -SkipIfExists: 如果文件已存在则跳过下载（可选，使用此参数时如果文件已存在则跳过下载）

param(
    [string]$Url = "",
    [string]$OutputDir = "",
    [switch]$SkipIfExists
)

# 检查是否以管理员身份运行
function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# 如果不是管理员，尝试以管理员身份重新启动
if (-not (Test-Administrator)) {
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host "  需要管理员权限" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "此脚本需要管理员权限才能执行更新操作" -ForegroundColor White
    Write-Host "正在尝试以管理员身份重新启动..." -ForegroundColor Yellow
    Write-Host ""
    
    try {
        $scriptPath = $MyInvocation.MyCommand.Path
        $scriptDir = Split-Path -Parent $scriptPath
        
        # 构建参数数组（使用数组方式可以正确处理路径中的空格）
        $arguments = @(
            "-NoProfile"
            "-ExecutionPolicy"
            "Bypass"
            "-File"
            $scriptPath
        )
        
        if ($Url) {
            $arguments += "-Url"
            $arguments += $Url
        }
        if ($OutputDir) {
            $arguments += "-OutputDir"
            $arguments += $OutputDir
        }
        if ($SkipIfExists) {
            $arguments += "-SkipIfExists"
        }
        
        # 以管理员身份重新启动脚本
        $process = Start-Process powershell.exe -Verb RunAs -ArgumentList $arguments -WorkingDirectory $scriptDir -Wait -PassThru
        
        # 退出当前进程，使用新进程的退出代码
        exit $process.ExitCode
    }
    catch {
        Write-Host "[×] 无法以管理员身份启动: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host ""
        Write-Host "请手动右键点击脚本，选择'以管理员身份运行'" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "按任意键退出..." -ForegroundColor Gray
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        exit 1
    }
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  文件下载与解压工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ====== 关闭正在运行的进程的函数 ======
function Stop-ProcessByName {
    param(
        [string]$ProcessName,
        [bool]$ExitOnError = $false
    )
    
    Write-Host "检查是否有正在运行的 $ProcessName 进程..." -ForegroundColor Yellow
    
    $runningProcesses = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    
    if ($runningProcesses) {
        $processCount = @($runningProcesses).Count
        Write-Host "发现 $processCount 个 $ProcessName 进程正在运行" -ForegroundColor Yellow
        Write-Host "正在关闭进程..." -ForegroundColor Yellow
        
        try {
            $runningProcesses | ForEach-Object {
                $processId = $_.Id
                Write-Host "  正在关闭进程 (PID: $processId)..." -ForegroundColor Gray
                $_ | Stop-Process -Force
            }
            
            # 等待进程完全退出
            Start-Sleep -Seconds 2
            
            # 再次检查是否还有残留进程
            $remainingProcesses = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
            if ($remainingProcesses) {
                Write-Host "[!] 部分进程可能未完全关闭，尝试强制终止..." -ForegroundColor Yellow
                $remainingProcesses | Stop-Process -Force -ErrorAction SilentlyContinue
                Start-Sleep -Seconds 1
            }
            
            Write-Host "[√] 所有 $ProcessName 进程已关闭" -ForegroundColor Green
            return $true
        }
        catch {
            Write-Host "[×] 关闭进程失败: $($_.Exception.Message)" -ForegroundColor Red
            if ($ExitOnError) {
                Write-Host "请手动关闭程序后重试" -ForegroundColor Yellow
                Write-Host ""
                Write-Host "按任意键退出..." -ForegroundColor Gray
                $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
                exit 1
            }
            return $false
        }
    }
    else {
        Write-Host "[√] 没有发现正在运行的 $ProcessName 进程" -ForegroundColor Green
        return $true
    }
}

# ====== 配置参数 ======
# 如果没有通过参数传入，使用默认值
if ([string]::IsNullOrEmpty($Url)) {
    # 在这里配置默认下载地址
    $Url = "https://installer-bty-ai-prod.oss-cn-hangzhou.aliyuncs.com/customer-service/win/BetterYeahCustomerRobot.zip"
}

if ([string]::IsNullOrEmpty($OutputDir)) {
    # 默认解压目录（脚本所在目录的 downloads 子目录）
    $scriptPath = $MyInvocation.MyCommand.Path
    if ($scriptPath) {
        $scriptDir = Split-Path -Parent $scriptPath
        $OutputDir = Join-Path -Path $scriptDir -ChildPath "downloads"
    } else {
        $OutputDir = Join-Path -Path $PWD -ChildPath "downloads"
    }
}
# ====== 配置参数结束 ======

# 从URL中提取文件名
$fileName = [System.IO.Path]::GetFileName($Url)
if ([string]::IsNullOrEmpty($fileName) -or -not $fileName.Contains(".")) {
    $fileName = "downloaded_file.zip"
}

Write-Host "下载地址: $Url" -ForegroundColor Gray
Write-Host "输出目录: $OutputDir" -ForegroundColor Gray
Write-Host "文件名称: $fileName" -ForegroundColor Gray
Write-Host ""

# 创建输出目录（如果不存在）
if (-Not (Test-Path -Path $OutputDir)) {
    Write-Host "输出目录不存在，正在创建: $OutputDir" -ForegroundColor Yellow
    try {
        New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
        Write-Host "[√] 输出目录创建成功" -ForegroundColor Green
    }
    catch {
        Write-Host "[×] 创建输出目录失败: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host ""
        Write-Host "按任意键退出..." -ForegroundColor Gray
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        exit 1
    }
}
else {
    Write-Host "[√] 输出目录已存在: $OutputDir" -ForegroundColor Green
}

Write-Host ""

# 下载文件的完整路径
$downloadPath = Join-Path -Path $OutputDir -ChildPath $fileName

# 检查文件是否已存在
$fileExists = Test-Path -Path $downloadPath
$skipDownload = $false

if ($fileExists) {
    if ($SkipIfExists) {
        $fileSize = (Get-Item $downloadPath).Length
        $fileSizeMB = [math]::Round($fileSize / 1MB, 2)
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "文件已存在，跳过下载" -ForegroundColor Yellow
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "文件路径: $downloadPath" -ForegroundColor Gray
        Write-Host "文件大小: $fileSizeMB MB" -ForegroundColor Gray
        Write-Host "[√] 将使用现有文件继续解压" -ForegroundColor Green
        Write-Host ""
        $skipDownload = $true
    }
    else {
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "文件已存在，但未启用跳过选项" -ForegroundColor Yellow
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "文件路径: $downloadPath" -ForegroundColor Gray
        Write-Host "提示: 如需跳过下载，请使用 -SkipIfExists 参数" -ForegroundColor Gray
        Write-Host ""
    }
}

if (-not $skipDownload) {
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "开始下载文件..." -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""

    try {
        Write-Host "正在下载: $fileName" -ForegroundColor White
        Write-Host "请稍候..." -ForegroundColor Gray
        Write-Host ""
        
        # 使用同步方式下载文件（使用 Invoke-WebRequest 支持进度显示）
        $ProgressPreference = 'Continue'
        
        # 使用 Invoke-WebRequest 同步下载，自动显示进度
        $response = Invoke-WebRequest -Uri $Url -OutFile $downloadPath -UseBasicParsing -TimeoutSec 1800
        
        Write-Progress -Activity "正在下载文件" -Completed
        
        # 检查文件是否下载成功
        if (Test-Path -Path $downloadPath) {
            $fileSize = (Get-Item $downloadPath).Length
            $fileSizeMB = [math]::Round($fileSize / 1MB, 2)
            Write-Host "[√] 文件下载成功" -ForegroundColor Green
            Write-Host "    文件大小: $fileSizeMB MB" -ForegroundColor Gray
        }
        else {
            throw "下载后文件不存在"
        }
    }
    catch {
        Write-Host "[×] 下载失败: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host ""
        Write-Host "可能的原因：" -ForegroundColor Yellow
        Write-Host "  - 网络连接问题" -ForegroundColor Gray
        Write-Host "  - 下载地址无效" -ForegroundColor Gray
        Write-Host "  - 服务器不可用" -ForegroundColor Gray
        Write-Host ""
        Write-Host "按任意键退出..." -ForegroundColor Gray
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        exit 1
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "开始解压文件..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 获取文件扩展名
$extension = [System.IO.Path]::GetExtension($downloadPath).ToLower()

# 解压目录（使用文件名作为子目录名，去掉扩展名）
$extractFolderName = [System.IO.Path]::GetFileNameWithoutExtension($fileName)
$extractPath = Join-Path -Path $OutputDir -ChildPath $extractFolderName

# 如果解压目录已存在，先删除
if (Test-Path -Path $extractPath) {
    Write-Host "解压目录已存在，正在清理: $extractPath" -ForegroundColor Yellow
    try {
        Remove-Item -Path $extractPath -Recurse -Force
        Write-Host "[√] 旧目录已清理" -ForegroundColor Green
    }
    catch {
        Write-Host "[!] 清理旧目录失败，将覆盖现有文件" -ForegroundColor Yellow
    }
}

try {
    # 创建解压目录
    New-Item -ItemType Directory -Path $extractPath -Force | Out-Null
    
    Write-Host "正在解压到: $extractPath" -ForegroundColor White
    Write-Host ""
    
    switch ($extension) {
        ".zip" {
            # 使用 .NET 解压 ZIP 文件
            Add-Type -AssemblyName System.IO.Compression.FileSystem
            [System.IO.Compression.ZipFile]::ExtractToDirectory($downloadPath, $extractPath)
            Write-Host "[√] ZIP 文件解压成功" -ForegroundColor Green
        }
        ".7z" {
            # 需要 7-Zip 支持
            $7zipPath = "C:\Program Files\7-Zip\7z.exe"
            if (Test-Path $7zipPath) {
                & $7zipPath x $downloadPath -o"$extractPath" -y | Out-Null
                Write-Host "[√] 7Z 文件解压成功" -ForegroundColor Green
            }
            else {
                throw "需要安装 7-Zip 才能解压 .7z 文件"
            }
        }
        ".rar" {
            # 需要 WinRAR 或 7-Zip 支持
            $7zipPath = "C:\Program Files\7-Zip\7z.exe"
            $winrarPath = "C:\Program Files\WinRAR\UnRAR.exe"
            
            if (Test-Path $7zipPath) {
                & $7zipPath x $downloadPath -o"$extractPath" -y | Out-Null
                Write-Host "[√] RAR 文件解压成功 (使用7-Zip)" -ForegroundColor Green
            }
            elseif (Test-Path $winrarPath) {
                & $winrarPath x -y $downloadPath $extractPath | Out-Null
                Write-Host "[√] RAR 文件解压成功 (使用WinRAR)" -ForegroundColor Green
            }
            else {
                throw "需要安装 7-Zip 或 WinRAR 才能解压 .rar 文件"
            }
        }
        ".tar" {
            # 使用 tar 命令（Windows 10+ 内置）
            tar -xf $downloadPath -C $extractPath
            Write-Host "[√] TAR 文件解压成功" -ForegroundColor Green
        }
        ".gz" {
            # 使用 tar 命令（Windows 10+ 内置）
            tar -xzf $downloadPath -C $extractPath
            Write-Host "[√] GZ 文件解压成功" -ForegroundColor Green
        }
        ".tar.gz" {
            # 使用 tar 命令（Windows 10+ 内置）
            tar -xzf $downloadPath -C $extractPath
            Write-Host "[√] TAR.GZ 文件解压成功" -ForegroundColor Green
        }
        default {
            # 尝试作为 ZIP 处理
            Write-Host "未知的压缩格式，尝试作为ZIP文件解压..." -ForegroundColor Yellow
            Add-Type -AssemblyName System.IO.Compression.FileSystem
            [System.IO.Compression.ZipFile]::ExtractToDirectory($downloadPath, $extractPath)
            Write-Host "[√] 文件解压成功" -ForegroundColor Green
        }
    }
    
    # 检查是否有嵌套文件夹（解压后可能有一层额外的文件夹）
    $directChildren = Get-ChildItem -Path $extractPath -Directory
    $directFiles = Get-ChildItem -Path $extractPath -File
    
    # 如果解压目录下只有一个子文件夹，且没有直接文件，说明有嵌套结构
    if ($directChildren.Count -eq 1 -and $directFiles.Count -eq 0) {
        $nestedFolder = $directChildren[0]
        Write-Host "[!] 检测到嵌套文件夹结构: $($nestedFolder.Name)" -ForegroundColor Yellow
        Write-Host "    将使用嵌套文件夹作为实际解压目录" -ForegroundColor Gray
        Write-Host ""
        
        # 更新解压路径为嵌套文件夹
        $extractPath = $nestedFolder.FullName
    }
    
    # 统计解压的文件数量
    $extractedItems = Get-ChildItem -Path $extractPath -Recurse
    $fileCount = ($extractedItems | Where-Object { -not $_.PSIsContainer }).Count
    $folderCount = ($extractedItems | Where-Object { $_.PSIsContainer }).Count
    
    Write-Host ""
    Write-Host "解压统计:" -ForegroundColor White
    Write-Host "  文件数量: $fileCount" -ForegroundColor Gray
    Write-Host "  文件夹数量: $folderCount" -ForegroundColor Gray
}
catch {
    Write-Host "[×] 解压失败: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "按任意键退出..." -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "解压完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "下载文件: $downloadPath" -ForegroundColor White
Write-Host "解压目录: $extractPath" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ====== 拷贝文件到安装目录 ======
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "拷贝文件到安装目录..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 配置目标目录
$targetDir = "C:\Program Files\BetterYeahCustomerRobot\CustomerRobot"
$requiredFolderPrefix = "BetterYeah"

# 获取解压目录的文件夹名称
$folderName = Split-Path -Leaf $extractPath

Write-Host "解压目录: $extractPath" -ForegroundColor Gray
Write-Host "文件夹名称: $folderName" -ForegroundColor Gray
Write-Host ""

# 检查文件夹名称是否以 BetterYeah 开头或者名称为 out
$isValidFolder = $folderName.StartsWith($requiredFolderPrefix) -or ($folderName -eq "out")

if (-Not $isValidFolder) {
    Write-Host "[!] 警告：文件夹名称不符合要求" -ForegroundColor Yellow
    Write-Host "    当前文件夹名称: $folderName" -ForegroundColor Gray
    Write-Host "    要求：文件夹名称必须以 '$requiredFolderPrefix' 开头，或者名称为 'out'" -ForegroundColor Gray
    Write-Host "    将继续尝试拷贝文件..." -ForegroundColor Yellow
    Write-Host ""
}

# 检查目标目录是否存在，不存在则创建
if (-Not (Test-Path -Path $targetDir)) {
    Write-Host "目标目录不存在，正在创建: $targetDir" -ForegroundColor Yellow
    try {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        Write-Host "[√] 目标目录创建成功" -ForegroundColor Green
    }
    catch {
        Write-Host "[×] 创建目标目录失败: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "可能需要管理员权限" -ForegroundColor Yellow
        Write-Host ""
    }
}
else {
    Write-Host "[√] 目标目录已存在: $targetDir" -ForegroundColor Green
    
    # 在清空目录前，关闭可能正在运行的进程，确保文件不被占用
    Write-Host ""
    Write-Host "清空目录前，检查并关闭相关进程..." -ForegroundColor Yellow
    Stop-ProcessByName -ProcessName "BetterYeahCustomerRobot" -ExitOnError $false
    Stop-ProcessByName -ProcessName "RobotRPA" -ExitOnError $false
    Write-Host ""
    
    # 等待进程完全退出
    Start-Sleep -Seconds 1
    
    # 清空目标目录
    Write-Host "正在清空目标目录..." -ForegroundColor Yellow
    try {
        # 获取目录中的所有项目
        $itemsToDelete = Get-ChildItem -Path $targetDir -Force -ErrorAction SilentlyContinue
        
        if ($itemsToDelete) {
            $itemCount = @($itemsToDelete).Count
            Write-Host "  发现 $itemCount 个项目需要删除" -ForegroundColor Gray
            
            # 删除所有文件和文件夹
            $itemsToDelete | ForEach-Object {
                try {
                    if ($_.PSIsContainer) {
                        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
                        Write-Host "    [√] 已删除目录: $($_.Name)" -ForegroundColor Gray
                    }
                    else {
                        Remove-Item -Path $_.FullName -Force -ErrorAction Stop
                        Write-Host "    [√] 已删除文件: $($_.Name)" -ForegroundColor Gray
                    }
                }
                catch {
                    Write-Host "    [!] 删除失败: $($_.Name) - $($_.Exception.Message)" -ForegroundColor Yellow
                }
            }
            
            # 等待一下确保删除完成
            Start-Sleep -Milliseconds 500
            
            # 再次检查是否还有残留文件
            $remainingItems = Get-ChildItem -Path $targetDir -Force -ErrorAction SilentlyContinue
            if ($remainingItems) {
                Write-Host "  [!] 部分项目可能未完全删除，尝试强制删除..." -ForegroundColor Yellow
                $remainingItems | ForEach-Object {
                    Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
                }
                Start-Sleep -Milliseconds 300
            }
            
            Write-Host "[√] 目标目录已清空" -ForegroundColor Green
        }
        else {
            Write-Host "[√] 目标目录已经是空的" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "[×] 清空目标目录失败: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "  提示: 可能有些文件正在被使用，请确保相关程序已关闭" -ForegroundColor Yellow
        Write-Host "  将继续尝试拷贝文件（可能会覆盖现有文件）..." -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "开始拷贝文件..." -ForegroundColor Yellow
Write-Host ""

# 统计变量
$successCount = 0
$errorCount = 0
$skipCount = 0

# 获取所有文件和子目录（排除 update_robot.ps1 脚本）
$items = Get-ChildItem -Path $extractPath -Force | Where-Object { $_.Name -ne "update_robot.ps1" }

if ($items.Count -eq 0) {
    Write-Host "没有找到需要拷贝的文件" -ForegroundColor Yellow
}
else {
    Write-Host "找到 $($items.Count) 个项目需要拷贝" -ForegroundColor White
    Write-Host ""
    
    foreach ($item in $items) {
        $sourcePath = $item.FullName
        $destPath = Join-Path -Path $targetDir -ChildPath $item.Name
        
        try {
            if ($item.PSIsContainer) {
                # 是目录，递归拷贝
                Write-Host "正在拷贝目录: $($item.Name)" -ForegroundColor White
                Copy-Item -Path $sourcePath -Destination $destPath -Recurse -Force
                Write-Host "  [√] 目录拷贝成功" -ForegroundColor Green
            }
            else {
                # 是文件
                Write-Host "正在拷贝文件: $($item.Name)" -ForegroundColor White
                Copy-Item -Path $sourcePath -Destination $destPath -Force
                Write-Host "  [√] 文件拷贝成功" -ForegroundColor Green
            }
            $successCount++
        }
        catch {
            $errorMsg = $_.Exception.Message
            Write-Host "  [×] 拷贝失败: $errorMsg" -ForegroundColor Red
            
            # 如果是权限错误，提供更详细的提示
            if ($errorMsg -like "*访问被拒绝*" -or $errorMsg -like "*PermissionDenied*" -or $errorMsg -like "*Unauthorized*") {
                Write-Host "     提示: 这可能是权限问题，请确保以管理员身份运行此脚本" -ForegroundColor Yellow
            }
            
            $errorCount++
        }
    }
}

Write-Host ""
Write-Host "拷贝完成！" -ForegroundColor Green
Write-Host "成功: $successCount 个项目" -ForegroundColor Green
Write-Host "失败: $errorCount 个项目" -ForegroundColor $(if ($errorCount -gt 0) { "Red" } else { "Gray" })
Write-Host ""

# ====== 添加到 Windows 快速访问 ======
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "添加到 Windows 快速访问..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 配置要添加到快速访问的目录
# 使用 Join-Path 和 $env:USERPROFILE 确保正确处理用户名中的空格
$folders = @(
    (Join-Path -Path $env:USERPROFILE -ChildPath "AppData\Local\Bantouyan\qianniu"),
    "C:\Program Files\BetterYeahCustomerRobot\CustomerRobot"
)

Write-Host "准备添加以下目录到快速访问：" -ForegroundColor Yellow
Write-Host ""

# 显示所有目录
for ($i = 0; $i -lt $folders.Count; $i++) {
    Write-Host "[$($i + 1)] $($folders[$i])"
}

Write-Host ""
Write-Host "开始处理..." -ForegroundColor Yellow
Write-Host ""

# 统计变量
$quickAccessSuccessCount = 0
$quickAccessSkipCount = 0
$quickAccessAlreadyPinnedCount = 0
$quickAccessErrorCount = 0

# 创建Shell对象
$shell = New-Object -ComObject shell.application

# 获取快速访问中已固定的目录列表
function Get-QuickAccessPinnedFolders {
    $quickAccessItems = @()
    try {
        # 通过快速访问命名空间获取项目
        $quickAccess = $shell.Namespace("shell:::{679f85cb-0220-4080-b29b-5540cc05aab6}")
        if ($quickAccess) {
            foreach ($item in $quickAccess.Items()) {
                if ($item.Path) {
                    $quickAccessItems += $item.Path.ToLower()
                }
            }
        }
    }
    catch {
        # 如果获取失败，返回空数组
    }
    
    return $quickAccessItems
}

# 获取已固定的目录
$pinnedFolders = Get-QuickAccessPinnedFolders

# 逐个处理
for ($i = 0; $i -lt $folders.Count; $i++) {
    $folderPath = $folders[$i]
    $num = $i + 1
    
    Write-Host "[$num] 正在处理: $folderPath" -ForegroundColor White
    
    # 检查目录是否存在
    if (-Not (Test-Path -Path $folderPath)) {
        Write-Host "    [跳过] 目录不存在" -ForegroundColor DarkYellow
        $quickAccessSkipCount++
    }
    else {
        # 检查是否已经在快速访问中
        $folderPathLower = $folderPath.ToLower()
        $isAlreadyPinned = $pinnedFolders -contains $folderPathLower
        
        if ($isAlreadyPinned) {
            Write-Host "    [已存在] 该目录已在快速访问中，跳过" -ForegroundColor Cyan
            $quickAccessAlreadyPinnedCount++
        }
        else {
            try {
                # 添加到快速访问
                $folder = $shell.Namespace($folderPath).Self
                $folder.InvokeVerb("pintohome")
                
                Write-Host "    [成功] 已添加到快速访问" -ForegroundColor Green
                $quickAccessSuccessCount++
                
                # 短暂延迟，确保操作完成
                Start-Sleep -Milliseconds 100
            }
            catch {
                Write-Host "    [失败] 添加出现错误: $($_.Exception.Message)" -ForegroundColor Red
                $quickAccessErrorCount++
            }
        }
    }
    
    Write-Host ""
}

# 显示统计信息
Write-Host "快速访问处理完成！" -ForegroundColor Green
Write-Host "新增添加:   $quickAccessSuccessCount 个目录" -ForegroundColor Green
Write-Host "已经存在:   $quickAccessAlreadyPinnedCount 个目录" -ForegroundColor Cyan
Write-Host "不存在跳过: $quickAccessSkipCount 个目录" -ForegroundColor Yellow
Write-Host "添加失败:   $quickAccessErrorCount 个目录" -ForegroundColor $(if ($quickAccessErrorCount -gt 0) { "Red" } else { "Gray" })
Write-Host ""

Write-Host ""

# ====== 启动 BetterYeahCustomerRobot.exe ======
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "启动程序..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$exePath = "C:\Program Files\BetterYeahCustomerRobot\CustomerRobot\BetterYeahCustomerRobot.exe"
$exeDir = Split-Path -Parent $exePath

if (Test-Path -Path $exePath) {
    Write-Host "正在启动: $exePath" -ForegroundColor Gray
    
    try {
        # 如果当前是管理员权限，使用计划任务以当前用户身份启动程序
        # 这样可以避免程序继承管理员权限，确保正常显示在系统托盘
        if (Test-Administrator) {
            try {
                # 获取当前登录用户名
                $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
                $taskName = "StartBetterYeahRobot_$(Get-Date -Format 'yyyyMMddHHmmss')"
                
                # 创建临时计划任务，以当前用户身份运行程序
                $taskAction = New-ScheduledTaskAction -Execute $exePath -WorkingDirectory $exeDir
                $taskPrincipal = New-ScheduledTaskPrincipal -UserId $currentUser -LogonType Interactive
                $taskSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
                
                Register-ScheduledTask -TaskName $taskName -Action $taskAction -Principal $taskPrincipal -Settings $taskSettings -Force | Out-Null
                
                # 立即运行任务
                Start-ScheduledTask -TaskName $taskName
                
                # 等待任务启动
                Start-Sleep -Seconds 1
                
                # 删除临时任务
                Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
                
                Write-Host "[√] 程序已启动（以普通用户身份运行，确保显示在系统托盘）" -ForegroundColor Green
            }
            catch {
                # 如果计划任务方法失败，尝试直接启动（虽然可能不会显示在托盘）
                Write-Host "[!] 计划任务方法失败，尝试直接启动..." -ForegroundColor Yellow
                Start-Process -FilePath $exePath -WorkingDirectory $exeDir -ErrorAction Stop
                Write-Host "[√] 程序已启动（注意：如果以管理员身份运行，可能不会显示在系统托盘）" -ForegroundColor Green
            }
        }
        else {
            # 如果不是管理员，直接启动即可
            $process = Start-Process -FilePath $exePath -WorkingDirectory $exeDir -PassThru -ErrorAction Stop
            
            if ($process -and -not $process.HasExited) {
                Write-Host "[√] 程序已启动 (PID: $($process.Id))" -ForegroundColor Green
            }
            else {
                Write-Host "[√] 程序已启动" -ForegroundColor Green
            }
        }
        
        # 等待一小段时间，确保进程启动
        Start-Sleep -Milliseconds 500
    }
    catch {
        Write-Host "[×] 启动程序失败: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "提示: 如果程序没有出现在系统托盘，请手动启动程序" -ForegroundColor Yellow
    }
}
else {
    Write-Host "[×] 程序文件不存在: $exePath" -ForegroundColor Red
    Write-Host "请检查安装路径是否正确" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "全部操作完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

