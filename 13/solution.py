with open('13/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")
    departure = int(inputlines[0])
    busses = [bus for bus in inputlines[1].split(",")]

def part1():
    bus_times = [int(bus) for bus in busses if bus != "x"]
    delays = []
    for bus in bus_times:
        delays.append(((int(departure/bus)+1) * bus) - departure)
    return bus_times[delays.index(min(delays))] * min(delays)

# finds the generating function which encapsulates two other generating functions
# i.e generating function which provides all numbers x such that x = Ax + B = Cy + D
def find_new_generator(period1, offset1, period2, offset2):
    i = 0
    initial = None
    period = None
    while True:
        if (i*period1 + offset1 - offset2) % period2 == 0:
            if initial is None:
                initial = i*period1 + offset1
            else:
                return i*period1 + offset1 - initial, initial
        i += 1

def part2():
    period = int(busses[0])
    offset = 0
    for i, bus in enumerate(busses[1:]):
        if bus != "x":
            period, offset = find_new_generator(period, offset, int(bus), -(i+1))
    return offset

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
