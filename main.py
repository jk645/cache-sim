def main():
    print("Hello, this is the CPU Simulator.")
    mode = input("Select mode (1: Read, 2: Write): ")
    replacement_policy = input("Select replacement policy (1: FIFO, 2: LRU): ")
    associativity = input("Select associativity (1: Direct Mapped, 2: 2-Way Set Associative, 3: Fully Associative): ")
    if mode == '2':
        # Only ask for write policy if the mode is Write
        write_policy = input("Select write policy (1: Write Through, 2: Write Back): ")

    print_rectangles_ascii_art()
    print(f"You selected mode {mode}.")
    print(f"You selected replacement policy {replacement_policy}.")
    print(f"You selected associativity {associativity}.")
    if mode == '2':
        print(f"You selected write policy {write_policy}.")


def print_rectangles_ascii_art():
    print(" Cache (4)    |   Memory (16)")
    double_rectangle = [
        "+----+----+       +----+----+",
        "|    |    |       | XX |    |",
        "+----+----+       +----+----+"
    ]
    rectangle = [
        "                  +----+----+",
        "                  | XX |    |",
        "                  +----+----+"
    ]
    for i in range(7):
        for j in range(3):
            if i != 0 and j == 0:
                continue
            line = double_rectangle[j] if i < 4 else rectangle[j]
            if j == 1:
                if i == 3:
                    label = '..'
                elif i > 3:
                    label = str(i + 9)
                else:
                    label = ' ' + str(i)
                line = line.replace("XX", label)
            print(line)


if __name__ == "__main__":
    main()
