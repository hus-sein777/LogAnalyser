with open("honeypot_log.txt", "r") as log:
    lines = log.readlines()

print("Lines read:", len(lines))

counts = {}

for line in lines:
    start = line.find("('") + 2
    end = line.find("'", start)
    ip = line[start:end]
    
    if ip in counts:
        counts[ip] = counts[ip] + 1
    else:
        counts[ip] = 1

print(counts)

print("\n=== Honeypot Log Analysis ===")
print("Total connections:", len(lines))
print("Unique IP addresses:", len(counts))
print("\nConnections per IP:")

for ip in counts:
    print(" ", ip, "-", counts[ip], "connection")
    if counts[ip] > 5:
        print("      WARNING: HIGH CONNECTION COUNT - POSSIBLE SCANNING ACTIVITY")
        