# start-quantum.ps1
# Launch PowerShell with bypass, activate venv, and stay in your project folder

# Bypass Execution Policy for this session
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Activate your virtual environment
. .\venv\Scripts\Activate.ps1

# Optional: Confirm environment is active
Write-Host "Virtual environment activated. Ready to go!" -ForegroundColor Green

# Optional: Open VS Code in current folder (uncomment if you want)
# code .

# Keep PowerShell window open
