import subprocess
import threading

def read_output(proc):
    for line in proc.stdout:
        print(f"Captured: {line.strip()}")  # You can store it too

# Launch the other program
proc = subprocess.Popen(['./Gamepad.py'], stdout=subprocess.PIPE, text=True)

# Start reading in a separate thread
thread = threading.Thread(target=read_output, args=(proc,))
thread.start()

# Your main script can now run in parallel
while True:
    # Do your thing here
    print("Main script running...")
    print(read_output)
    time.sleep(1)