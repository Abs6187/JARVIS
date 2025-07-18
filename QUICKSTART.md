# 🚀 JARVIS Quick Start Guide

Get JARVIS up and running in just a few minutes!

## ⚡ Super Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/Abs6187/JARVIS.git
cd JARVIS

# 2. Run the automated setup
python setup.py

# 3. Start JARVIS
python main.py
```

## 🔧 Manual Setup (Alternative)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
cp config_template.py config.py
# Edit config.py and add your Wolfram Alpha API keys
```

### 3. Test Installation
```bash
python main.py
```

## 🎯 First Steps

1. **Try the Calculator**: Choose option 3 and enter "what is 2 plus 2"
2. **Voice Greeting**: Choose option 2 for time-aware greetings
3. **Play a Game**: Choose option 5 for Rock Paper Scissors
4. **View Features**: Explore the menu to see all available options

## 🔑 Getting API Keys

### Wolfram Alpha (Required for Calculator)
1. Visit [https://developer.wolframalpha.com/](https://developer.wolframalpha.com/)
2. Create a free account
3. Get your API key
4. Add it to `config.py`

## ⚠️ Common Issues

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Voice recognition not working
- Check microphone permissions
- Ensure you have a working microphone
- Try speaking clearly and loudly

### Windows Focus Mode requires admin
- Right-click terminal and "Run as administrator"
- Or run: `python FocusMode.py` as admin

## 🎮 Try These Commands

**Calculator Examples:**
- "what is 15 plus 25"
- "calculate 50 multiply 3"
- "what is the square root of 144"

**App Launcher Examples:**
- Type "chrome" to open Chrome browser
- Type "word" to open Microsoft Word
- Type "facebook.com" to open Facebook

## 📖 Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Visit [GitHub Issues](https://github.com/Abs6187/JARVIS/issues) for support
- Join discussions at [GitHub Discussions](https://github.com/Abs6187/JARVIS/discussions)

## 🌟 What's Next?

Once you have JARVIS running:
1. Customize voice settings in `config.py`
2. Add your own blocked websites for Focus Mode
3. Try the Focus Graph to track productivity
4. Explore the Easter eggs (hint: try option 10!)

---

**Ready to become Tony Stark? Let's get started! 🦾**