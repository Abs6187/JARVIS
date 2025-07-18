#!/usr/bin/env python3
"""
JARVIS Setup Script
Automated setup for the JARVIS voice assistant
"""

import subprocess
import sys
import os
import shutil

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🤖 JARVIS Setup Script")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    print("✅ Python version check passed")
    
    # Install requirements
    print("\n📦 Installing dependencies...")
    if os.path.exists("requirements.txt"):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            print("Please run manually: pip install -r requirements.txt")
    else:
        print("⚠️  requirements.txt not found, installing core packages...")
        packages = ["pyttsx3", "SpeechRecognition", "Pillow", "pygame", "wolframalpha", "pyautogui", "matplotlib"]
        for package in packages:
            if install_package(package):
                print(f"✅ Installed {package}")
            else:
                print(f"❌ Failed to install {package}")
    
    # Setup configuration
    print("\n⚙️  Setting up configuration...")
    if not os.path.exists("config.py"):
        if os.path.exists("config_template.py"):
            shutil.copy("config_template.py", "config.py")
            print("✅ Configuration file created from template")
            print("📝 Please edit config.py and add your Wolfram Alpha API keys")
            print("🔑 Get free API keys from: https://developer.wolframalpha.com/")
        else:
            print("❌ config_template.py not found")
    else:
        print("✅ Configuration file already exists")
    
    # Initialize data files
    print("\n📁 Initializing data files...")
    if not os.path.exists("focus.txt"):
        with open("focus.txt", "w") as f:
            f.write("0")
        print("✅ Created focus.txt")
    
    if not os.path.exists("Alarmtext.txt"):
        with open("Alarmtext.txt", "w") as f:
            f.write("")
        print("✅ Created Alarmtext.txt")
    
    print("\n🎉 Setup completed successfully!")
    print("\n🚀 To start JARVIS, run:")
    print("   python main.py")
    print("\n📖 For more information, see README.md")

if __name__ == "__main__":
    main()