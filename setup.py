import subprocess
import sys

print("Installing requirements...")
subprocess.run([
    sys.executable, "-m", "pip", "install",
    "--user", "--break-system-packages",
    "-r", "requirements.txt"
], check=True)


print("Installing Playwright browsers...")
try:
    subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
except subprocess.CalledProcessError:
    print("\n⚠️ Note: Playwright browser downloads were interrupted or failed.")
    print("This is normal if you have a weak network or connection resets.")
    print("MARK XLVI can still run using your locally installed Chrome/Firefox/Safari browsers.")

print("\n✅ Setup complete! Run 'python main.py' to start MARK XXV.")

