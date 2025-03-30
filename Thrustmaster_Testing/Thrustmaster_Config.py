class T16000M(Gamepad):
    # This class must have self.axisNames with a map
    # of numbers to capitalised strings. Follow the
    # conventions the other classes use for generic
    # axes, make up your own names for axes unique
    # to your device.
    # self.buttonNames needs the same treatment.
    # Use python Gamepad.py to get the event mappings.
    fullName = 'T16000M_Joystick'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'AXIS0',
            1: '2ND_AXIS', # 0 to -1 is forward, 0 to 1 is backward 
            2: '1ST_AXIS', # 0 to -1 is left, 0 to 1 is right
            3: 'AXIS_SPEED',# 0 to -1 is down, 0 to 1 is up
            4: '4TH_AXIS', # -1 is left, 0 is no movement, 1 is right
            5: '5TH_AXIS' # -1 is up, 0 is no movement, 1 is down
        }
        self.buttonNames = {
            0: 'GRIPPER_CLOSE', 
            1: 'GRIPPER_OPEN',
            2: '3RDAXIS_DOWN',
            3: '3RDAXIS_UP',




        }
        self._setupReverseMaps()