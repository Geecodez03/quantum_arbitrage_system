# Navigate to your project folder
cd C:\quantum_arbitrage_system

# 1. Create virtual environment called 'venv' if it doesn't exist
if (-not (Test-Path -Path ".\venv")) {
    python -m venv venv
    Write-Host "Virtual environment created."
} else {
    Write-Host "Virtual environment already exists."
}

# 2. Activate the virtual environment (PowerShell)
# Note: This activates for the current session only
& .\venv\Scripts\Activate.ps1
Write-Host "Virtual environment activated."

# 3. Upgrade pip, setuptools, wheel inside venv
pip install --upgrade pip setuptools wheel

# 4. Install your package in editable mode with PEP 517 (modern standard)
pip install -e . --use-pep517

Write-Host "Setup complete! Your package is installed in editable mode inside the venv."
