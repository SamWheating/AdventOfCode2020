def transform(subject, loops):
    value = 1
    for i in range(loops):
        value = (value * subject) % 20201227
    return value

def find_loops(subject, pubkey):
    value = 1
    for i in range(1, 20201227):
        value = (value * subject) % 20201227
        if value == pubkey:
            return i

def part1():

    pubkey1 = 11404017
    pubkey2 = 13768789
    subject_number = 7

    num_loops = find_loops(subject_number, pubkey1)
    return transform(pubkey2, num_loops)
    

if __name__ == "__main__":

    print(f"Part 1 solution: {part1()}")
