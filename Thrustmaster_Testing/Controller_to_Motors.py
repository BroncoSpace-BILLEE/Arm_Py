import subprocess

# Start Gamepad.py as a subprocess
process = subprocess.Popen( #
    ["python3", "-u", "Gamepad.py"], #run the subprocess with python 3, -u means unbuffered so we get instant output, the program to run is Gamepad.py
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True  # so that output is decoded as text
    
    #stdout=subprocess.PIPE: This tells Python to capture the standard output (stdout) of the subprocess. 
    #Instead of letting the output go directly to the terminal or console, 
    #it creates a pipe so your main program can read the output programmatically (e.g., using process.stdout.readline()).

    #stderr=subprocess.PIPE: Similarly, this captures the standard error (stderr) output of the subprocess. 
    #Any error messages or diagnostics that would normally be printed to the console are instead captured in a pipe, 
    #which allows your program to process or log them as needed.
    
)

# Read output continuously
while True:
    joystick_output = process.stdout.readline()
     # Process the output from Gamepad.py

    joystick_output = joystick_output.strip()
    #print(joystick_output.strip())

    if len(events) == 3:
        button_type, button_name, value = events
        try:
            value = float(value)
        except ValueError:
    print("Could not convert value to float:", value)
    print("Button Type:", button_type)
    print("Button Name:", button_name)
    print("Value:", value)
    else:
        print("Unexpected format. Expected 3 elements but got:", len(events))
    

#while True:
#    def switch_motor_select(joystick_output):
#       match joystick_output:
#           case 
    
