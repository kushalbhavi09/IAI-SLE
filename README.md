# IAI-SLE
# Simple AI Agent with While Loop

## 📌 Overview
This project demonstrates a **basic rule-based AI agent** written in Python.  
The agent takes user input (a task description) and decides what action to perform based on simple keyword matching.

It is not a chatbot — instead, it acts like a **command interpreter** that maps tasks to actions.

---

## 🚀 Features
- Runs continuously in a loop until the user types `exit`.
- Recognizes keywords in tasks:
  - `"weather"` → Check weather information
  - `"calculate"` or `"math"` → Perform calculation
  - `"search"` → Search for information
  - `"file"` → Work with files
- Handles unknown tasks gracefully with a default response.

---

## 🛠️ How It Works
1. The program waits for user input.
2. It checks the input against predefined rules.
3. It prints the corresponding agent action.
4. The loop continues until the user types `exit`.

---

## ▶️ Usage
### Requirements
- Python 3.x installed on your system

### Run the program
```bash
python ai_agent.py
