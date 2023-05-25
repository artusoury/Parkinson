import time
import datetime
import logging
import keyboard

# Logging setup to capture keyboard events
logging.basicConfig(filename="key_events.log", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# list to store the time between key press and release
key_intervals = []

# counter to keep track of number of keys pressed
key_count = 0
key_press_time = 0

# variable to store the final average typing speed
avg_typing_speed = 0

# flag to keep track of when to stop the keyboard listener
stop_listening = False

# function to log the key press and release events
def on_press(key):
    global key_press_time
    logging.info("Key {} pressed".format(key))
    key_press_time = time.time()

def on_release(key):
    global key_count, avg_typing_speed, stop_listening
    logging.info("Key {} released".format(key))
    key_count += 1
    key_intervals.append(time.time() - key_press_time)
    if key_count % 5 == 0:
        avg_time = sum(key_intervals) / len(key_intervals)
        logging.info("5 keys pressed. Average time for a key to be pressed and then released: {:.2f} seconds".format(avg_time))
        with open("average_speed.log", "a") as f:
            f.write("\n{}: Average typing speed: {:.2f} seconds per key".format(datetime.datetime.now(), avg_time))
    if key_count >= 21:
        avg_time = sum(key_intervals) / len(key_intervals)
        avg_typing_speed = avg_time
        stop_listening = True

# start the keyboard event listener
keyboard.on_press(on_press)
keyboard.on_release(on_release)

# wait for the keyboard events
while not stop_listening:
    keyboard.wait()

# Logging setup to capture average typing speeds
logging.basicConfig(filename="average_speed.log", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# write the final average typing speed to the terminal
print("Final average typing speed: {:.2f} seconds per key".format(avg_typing_speed))
