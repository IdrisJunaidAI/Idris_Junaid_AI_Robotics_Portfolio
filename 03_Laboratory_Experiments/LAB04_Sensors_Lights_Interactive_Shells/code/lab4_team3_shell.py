"""TEAM 3 Lab 4 shell. Hardware validation remains pending.
Transcribed from submitted report, pages 6 and 7.
Run only on a calibrated, supervised PiDog with mechanical clearance.
"""
from time import monotonic, sleep
from pidog import Pidog

MENU = """0 Stop motion | 1 Breath | 2 Listen | 3 Boom
4 Solid blue | 5 IMU | 6 Distance | 7 Touch
8 Sound direction | 9 Tail trial | q Quit"""


def light(dog, style, color):
    dog.rgb_strip.set_mode(style, color,
                           bps=1, brightness=0.3)


def imu(dog):
    print("Acceleration raw:", list(dog.accData))
    print("Gyroscope raw:", list(dog.gyroData))


def distance(dog):
    print("Distance cm:", dog.read_distance())


def touch(dog):
    print("Touch status:", dog.dual_touch.read())


def sound(dog):
    deadline = monotonic() + 3
    detected = False
    while monotonic() < deadline:
        if dog.ears.isdetected():
            print("Sound degrees:", dog.ears.read())
            detected = True
            break
        sleep(0.05)
    if not detected:
        print("No sound event within three seconds")


def tail_trial(dog):
    dog.body_stop()
    dog.tail_move([[10], [-10], [0]],
                  immediately=False, speed=20)
    print("Queued one tail trial; 0 stops motion")


def run_menu(dog):
    commands = {
        "0": dog.body_stop,
        "1": lambda: light(dog, "breath", "pink"),
        "2": lambda: light(dog, "listen", "cyan"),
        "3": lambda: light(dog, "boom", "red"),
        "4": lambda: light(dog, "monochromatic", "blue"),
        "5": lambda: imu(dog),
        "6": lambda: distance(dog),
        "7": lambda: touch(dog),
        "8": lambda: sound(dog),
        "9": lambda: tail_trial(dog),
    }
    print(MENU)
    while True:
        choice = input("TEAM 3 > ").strip().lower()
        if choice == "q":
            return
        if choice not in commands:
            print("Choose 0 through 9, or q")
            continue
        try:
            commands[choice]()
        except Exception as exc:
            dog.body_stop()
            print(f"Command {choice} failed: {exc}")


def main():
    dog = None
    try:
        dog = Pidog()
        sleep(0.5)
        run_menu(dog)
    except (KeyboardInterrupt, EOFError):
        print("Exit requested")
    finally:
        if dog is not None:
            try:
                dog.body_stop()
            finally:
                dog.close()


if __name__ == "__main__":
    main()
