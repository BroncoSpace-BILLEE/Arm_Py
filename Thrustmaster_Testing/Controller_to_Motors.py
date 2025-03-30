import subprocess

# Start Gamepad.py as a subprocess
process = subprocess.Popen(
    ["python3", "Gamepad.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True  # so that output is decoded as text
)

# Read output continuously
while True:
    line = process.stdout.readline()
    if not line:
        break  # process ended
    # Process the output from Gamepad.py
    print("Controller output:", line.strip())
    # You can add your logic here to generate other outputs based on the line
