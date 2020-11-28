# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    value = raw_input()
    desired_area = float(value)
    import math
    if desired_area <= math.sqrt(2):
        theta = -math.acos(desired_area/math.sqrt(2)) + math.pi/4
        x = (0.5*math.cos(theta), 0.5*math.sin(theta), 0)
        y = (-0.5*math.sin(theta), 0.5*math.cos(theta), 0)
        z = (0, 0, 0.5)
        print "Case #{}:".format(i)
        print "{} {} {}".format(x[0], x[1], x[2])
        print "{} {} {}".format(y[0], y[1], y[2])
        print "{} {} {}".format(z[0], z[1], z[2])

    else:
        theta = math.asin(desired_area/math.sqrt(3)) - 0.955316618

        x = (0.5*math.cos(math.pi/4), 0.5/math.sqrt(2)*math.cos(theta), 0.5/math.sqrt(2)*math.sin(theta))
        y = (-0.5*math.sin(math.pi/4), 0.5/math.sqrt(2)*math.cos(theta), 0.5/math.sqrt(2)*math.sin(theta))
        z = (0, -0.5*math.sin(theta), 0.5*math.cos(theta))

        print "Case #{}:".format(i)
        print "{} {} {}".format(x[0], x[1], x[2])
        print "{} {} {}".format(y[0], y[1], y[2])
        print "{} {} {}".format(z[0], z[1], z[2])
