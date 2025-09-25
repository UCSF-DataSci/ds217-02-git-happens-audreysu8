import time

def count_sheep(n):
    for i in range(1, n + 1):
        print(f"We have sheep {i} which jumps over the fence")
        time.sleep(0.5)  # pause for effect
    print("All sheep have finished jumping. Now, time to sleep!")

if __name__ == "__main__":
    count_sheep(10)