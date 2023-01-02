import math

def draw_circle_filled_wrong(R):
    pixels = set()
    def draw_circle_perimeter(R):
        for x in range(-R, R+1): 
            y = round(math.sqrt(R * R - x * x))   # round to nearest integer, breaking ties towards zero
            pixels.add((x,y))
            pixels.add((x,-y))
            pixels.add((y,x))
            pixels.add((-y,x))
    for r in range(0, R+1):
        draw_circle_perimeter(r)
    return pixels

def draw_circle_filled_correct(R):
    pixels = set()
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if round(math.sqrt(x * x + y * y)) <= R:
                pixels.add((x, y))
    return pixels

def print_diff(R):
    correct = len(draw_circle_filled_correct(R))
    wrong = len(draw_circle_filled_wrong(R))
    print(R, correct, wrong, correct - wrong)

for i in range(1,21):
    print_diff(i)