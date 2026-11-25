"""Portfolio reconstruction of Lab 1 numerical PWM experiment.
Original source file was not supplied. This is a host-only mathematical
model, not an electrical measurement or a PiDog calibration setting.
"""
def pulse_width_us(angle):
    if not 0 <= angle <= 180:
        raise ValueError("Angle must be between 0 and 180 degrees")
    return 1000 + angle * (2000 - 1000) / 180


def main():
    period_us = 1_000_000 / 50
    for angle in (0, 45, 90, 135, 180):
        width = pulse_width_us(angle)
        print(f"{angle:3d} deg | {width:.0f} us | {100*width/period_us:.2f}%")


if __name__ == "__main__":
    main()
