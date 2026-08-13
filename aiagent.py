# Simple AI Agent with While Loop

def ai_agent(task):
    task = task.lower()

    if "weather" in task:
        print("Agent Action: Check weather information")

    elif "calculate" in task or "math" in task:
        print("Agent Action: Perform calculation")

    elif "search" in task:
        print("Agent Action: Search for information")

    elif "file" in task:
        print("Agent Action: Work with the file")

    else:
        print("Agent Action: I don't know what action to take")


# Main program
while True:
    task = input("\nEnter your task (or type 'exit' to stop): ")

    if task.lower() == "exit":
        print("AI Agent stopped.")
        break

    ai_agent(task)