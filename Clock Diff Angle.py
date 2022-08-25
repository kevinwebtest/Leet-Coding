def calcAngle(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    if (h < 0 or m < 0 or h > 12 or m > 60):
      return "Wrong Input"

    if (h == 12):
      h = 0
    if(h>12):
      h = h-12
		
    hour_angle = (h + m/60)*30
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)

    return angle

time = "5:01"
print('Angle ', calcAngle(time))
