"""Conceptual example transcribed from Lab 1 report.
No hardware control. Not represented as the original executed script.
"""
servo_count = 12
robot_ready = False
actions = ["stand", "sit", "wag_tail"]
for action in actions:
    if robot_ready:
        print("Execute:", action)
    else:
        print("Simulation only:", action)
