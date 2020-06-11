from sys import argv

def main():
    source_file = open(argv[1])
    source = source_file.read()
    source_file.close()

    memory = [ 0 ]
    memory_pointer = 0
    source_index = 0

    while source_index < len(source):
        char = source[source_index]
        if char == '+':
            memory[memory_pointer] += 1
        elif char == '-':
            memory[memory_pointer] -= 1
        elif char == '>':
            if memory_pointer == len(memory) - 1:
                memory.append(0)
            memory_pointer += 1
        elif char == '<':
            if memory_pointer == 0:
                memory.insert(0, 0)
            else:
                memory_pointer -= 1
        elif (char == '[' and memory[memory_pointer] == 0) or (char == ']' and memory[memory_pointer] != 0):
            depth = 1
            direction = 1 if char == '[' else -1
            while True:
                source_index += direction
                char = source[source_index]
                if char in "][":
                    depth += (1 if char == '[' else -1) * direction
                if depth == 0:
                    break
        elif char == '.':
            print(chr(memory[memory_pointer]), end = '', flush = True)
        elif char == ',':
            memory[memory_pointer] = ord(input()[0])

        source_index += 1

main()

