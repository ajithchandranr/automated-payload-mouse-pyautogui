import tkinter as tk
import pyautogui
import webbrowser
import time

# Set the duration between each mouse movement (in seconds)
movement_duration = 0.7

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Set the number of movements
num_movements = 5

# Calculate the movement distance
move_distance = min(screen_width, screen_height) // num_movements

# Set the starting position
start_x = screen_width // 2
start_y = screen_height // 2

# Define the payload function
def payload():
    # Perform the mouse movements in a pattern
    for i in range(num_movements):
        # Calculate the target position for the mouse movement
        target_x = start_x + move_distance * i
        target_y = start_y - move_distance * i

        # Move the mouse cursor to the target position
        pyautogui.moveTo(target_x, target_y, duration=movement_duration)
        time.sleep(movement_duration)

    # Move the mouse cursor back to the starting position
    pyautogui.moveTo(start_x, start_y, duration=movement_duration)

    # Open the LinkedIn and GitHub links automatically
    webbrowser.open_new("https://www.linkedin.com/in/ajithchandranr/")
    webbrowser.open_new("https://github.com/ajithchandranr")

    # Close the window after a delay
    window.after(2000, window.destroy)

# Create a Tkinter window
window = tk.Tk()
window.title("Payload")
window.geometry("500x180")

# Create a label with the message
message_label = tk.Label(window, text="This is a demonstration of an automated payload.\n\nUpon completion, you will be automatically redirected to my LinkedIn and GitHub profiles.\n\nThank you for your attention!")
message_label.pack(pady=30)

# Function to close the window after a delay
def close_window():
    window.after(2000, window.destroy)

# Execute the payload function after a delay
window.after(3000, payload)
window.after(6000, close_window)

# Start the Tkinter event loop
window.mainloop()