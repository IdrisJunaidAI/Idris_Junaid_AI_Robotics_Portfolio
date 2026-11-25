"""Source transcribed from the submitted Lab 3 report, page 6.
Adapted from SunFounder 2_legs_control.py. Physical validation pending.
Run only on a calibrated, supervised PiDog with mechanical clearance.
"""
from pidog import Pidog
import time

half_stand = [[45, 10, -45, -10,
               45, 10, -45, -10]]
prepare = [[45, 35, -45, -35,
            80, 70, -80, -70]]
push_up = [
    [90, -30, -90, 30, 80, 70, -80, -70],
    [45, 35, -45, -35, 80, 70, -80, -70]
]

dog = None
try:
    dog = Pidog()
    dog.legs_move(half_stand, speed=30)
    dog.wait_legs_done()
    dog.legs_move(prepare, speed=20)
    dog.wait_legs_done()
    for cycle in range(3):
        dog.legs_move(push_up,
                      immediately=False, speed=30)
        dog.wait_legs_done()
        time.sleep(0.5)
    dog.legs_move(half_stand, speed=30)
    dog.wait_legs_done()
except KeyboardInterrupt:
    pass
finally:
    if dog is not None:
        dog.close()
