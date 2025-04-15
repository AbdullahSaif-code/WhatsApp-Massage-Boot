import pyautogui
import time

message = "Hello, this is a test message from Python!"
phone_number = "Number Here"  # Replace with the recipient's phone number

# Instructions for the user
print("Please open WhatsApp Desktop and search for the contact manually.")
input("Press Enter once the chat window is open...")

try:
    while True:
        # Type the message
        pyautogui.typewrite(message)
        pyautogui.press("enter")  # Press Enter to send the message
        print("Message sent!")
        time.sleep(5)  # Wait for 5 seconds before sending the next message
except KeyboardInterrupt:
    print("Program stopped by user.")