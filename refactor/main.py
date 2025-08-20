def main():
    print("Running simulation...")
    result = simulation()
    print("Simulation complete. Results:")
    show_cache(result[0])
    print(f"Cache misses: {result[1]}")
    print(f"Cache hits: {result[2]}")

def simulation():
    cache = {0: None, 1: None, 2: None, 3: None}
    first_in = 0
    misses = 0
    hits = 0
    addresses = [8, 3, 4, 12, 10, 7, 3, 2, 6, 3, 1, 7, 8, 6]
    for address in addresses:
        for (line, tag) in cache.items():
            if tag == address:
                hits += 1
                break
        else:
            misses += 1
            cache[first_in] = address
            first_in = (first_in + 1) % len(cache)
    return (cache, misses, hits)

def show_cache(cache):
    print(f"Line| Tag")
    print(f"+---+-----")
    for (line, tag) in cache.items():
        print(f"| {line} | {tag} ")
        print(f"+---+-----")

if __name__ == "__main__":
    main()
