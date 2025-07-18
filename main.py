#!/usr/bin/env python3
"""
JARVIS - Just A Rather Very Intelligent System
A Python-based voice assistant with multiple capabilities

Author: Abs6187
Repository: https://github.com/Abs6187/JARVIS
"""

import sys
import os

def show_menu():
    """Display the main menu with available options"""
    print("\n" + "="*50)
    print("    JARVIS - Just A Rather Very Intelligent System")
    print("="*50)
    print("1. 🎬 Play Intro Animation")
    print("2. 👋 Greeting Mode")
    print("3. 🧮 Calculator")
    print("4. 🧮 Number Calculator (Alternative)")
    print("5. 🎮 Rock Paper Scissors Game")
    print("6. ⏰ Set Alarm")
    print("7. 🎯 Focus Mode (Windows Only)")
    print("8. 📊 View Focus Graph")
    print("9. 🚀 Launch Apps/Websites")
    print("10. 📁 File Manager (Easter Egg)")
    print("11. 📦 Install Dependencies")
    print("0. ❌ Exit")
    print("="*50)

def main():
    """Main function to run JARVIS"""
    print("🤖 Welcome to JARVIS!")
    print("Initializing system...")
    
    # Check if config file exists
    if not os.path.exists("config.py"):
        print("\n⚠️  Warning: config.py not found.")
        print("📝 Using config_template.py. Please copy it to config.py and update your API keys.")
        print("🔑 Get Wolfram Alpha API key from: https://developer.wolframalpha.com/")
    
    while True:
        try:
            show_menu()
            choice = input("\n🎯 Enter your choice (0-11): ").strip()
            
            if choice == "0":
                print("👋 Goodbye! JARVIS is shutting down...")
                sys.exit(0)
                
            elif choice == "1":
                print("🎬 Starting intro animation...")
                try:
                    import INTRO
                except Exception as e:
                    print(f"❌ Error running intro: {e}")
                    
            elif choice == "2":
                print("👋 Starting greeting mode...")
                try:
                    from GreetMe import greetMe
                    greetMe()
                except Exception as e:
                    print(f"❌ Error in greeting mode: {e}")
                    
            elif choice == "3":
                print("🧮 Starting calculator...")
                try:
                    from Cal import calc
                    query = input("Enter calculation (e.g., 'what is 2 plus 2'): ")
                    calc(query)
                except Exception as e:
                    print(f"❌ Error in calculator: {e}")
                    
            elif choice == "4":
                print("🧮 Starting number calculator...")
                try:
                    from Calculatenumbers import Calc
                    query = input("Enter calculation: ")
                    Calc(query)
                except Exception as e:
                    print(f"❌ Error in number calculator: {e}")
                    
            elif choice == "5":
                print("🎮 Starting Rock Paper Scissors game...")
                try:
                    from game import game_play
                    game_play()
                except Exception as e:
                    print(f"❌ Error in game: {e}")
                    
            elif choice == "6":
                print("⏰ Starting alarm...")
                try:
                    from alarm import run_alarm
                    run_alarm()
                except Exception as e:
                    print(f"❌ Error in alarm: {e}")
                    
            elif choice == "7":
                print("🎯 Starting focus mode...")
                if os.name != 'nt':
                    print("❌ Focus mode only works on Windows systems.")
                else:
                    try:
                        from FocusMode import focus_mode
                        focus_mode()
                    except Exception as e:
                        print(f"❌ Error in focus mode: {e}")
                        
            elif choice == "8":
                print("📊 Showing focus graph...")
                try:
                    from FocusGraph import focus_graph
                    focus_graph()
                except Exception as e:
                    print(f"❌ Error showing focus graph: {e}")
                    
            elif choice == "9":
                print("🚀 App/Website launcher...")
                try:
                    from Dictapp import openappweb, closeappweb
                    action = input("Type 'open' or 'close': ").lower()
                    query = input("Enter app/website name: ")
                    if action == "open":
                        openappweb(query)
                    elif action == "close":
                        closeappweb(query)
                    else:
                        print("❌ Invalid action. Use 'open' or 'close'.")
                except Exception as e:
                    print(f"❌ Error in app launcher: {e}")
                    
            elif choice == "10":
                print("📁 File manager easter egg...")
                try:
                    import file
                except Exception as e:
                    print(f"❌ Error in file manager: {e}")
                    
            elif choice == "11":
                print("📦 Installing dependencies...")
                try:
                    from Installer import install_package
                    package = input("Enter package name to install: ")
                    install_package(package)
                except Exception as e:
                    print(f"❌ Error installing package: {e}")
                    
            else:
                print("❌ Invalid choice. Please enter a number between 0-11.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! JARVIS is shutting down...")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("🔄 Returning to main menu...")

if __name__ == "__main__":
    main()