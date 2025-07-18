# pip install matplotlib
import matplotlib.pyplot as pt
import os
try:
    from config import FOCUS_DATA_FILE
except ImportError:
    print("Warning: config.py not found. Using default values.")
    FOCUS_DATA_FILE = "focus.txt"

def focus_graph():
    if not os.path.exists(FOCUS_DATA_FILE):
        print(f"Error: {FOCUS_DATA_FILE} not found. No focus data to display.")
        return
        
    file = open(FOCUS_DATA_FILE, "r")
    content = file.read()
    file.close()

    content = content.split(",")
    # Remove empty strings
    content = [x for x in content if x.strip()]
    
    if not content:
        print("No focus data available to display.")
        return
        
    x1 = []
    for i in range(0, len(content)):
        content[i] = float(content[i])
        x1.append(i)

    print(content)
    y1 = content

    pt.plot(x1, y1, color="red", marker="o")
    pt.title("YOUR FOCUSED TIME", fontsize=16)
    pt.xlabel("Times", fontsize=14)
    pt.ylabel("Focus Time", fontsize=14)
    pt.grid()
    pt.show()


    
   
