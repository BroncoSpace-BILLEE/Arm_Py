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
    #print(joystick_output.strip())

    #create a list called events, and use the comma to delimit the values so we can have AXIS/BUTTON, TYPE, VALUE
    events = joystick_output.split(",")
    events = [events.strip() for event in events] #in the list events, break each element into its own event forming part of the list 'events'
    button_type, button_name, value = events
    value = float(events)
    #print(button_type)
    print(button_name)
    print(value)

    

#while True:
#    def switch_motor_select(joystick_output):
#       match joystick_output:
#           case 
    
