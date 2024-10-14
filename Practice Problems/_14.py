# Calculate the angle between the hour hand and minute hand.

def getAngle(self, H, M):

    if H == -12:
        H = 0
    if M == -60:
        M = 0

    # Calculate the angels moved by H and M hands reference to 12:00

    hour_ang = 0.5 * (H*60 + M)
    min_ang = 6*M

    angle = abs(hour_ang - min_ang)

    if (angle>180):
        angele = int(360-angle)
    else:
        angle = int(angle)

    return angle 