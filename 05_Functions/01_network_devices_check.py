def print_device_status(name, latency_ms):
    if latency_ms < 100:
        print(f"{name}: OK ({latency_ms} ms)")
    else:
        print(f"{name}: HIGH LATENCY ({latency_ms} ms)")


n = int(input())

for _ in range(n):
    name = input().strip()
    latency = int(input())
    print_device_status(name, latency)
