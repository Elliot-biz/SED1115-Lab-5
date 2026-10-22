import matplotlib.pyplot as plt

times = []

# Read the recorded times from the log file
with open("log.txt", "r") as file:
    for line in file:
        times.append(float(line.strip()))

# Create the histogram
plt.hist(times)

plt.xlabel("Time taken to count 15 seconds")
plt.ylabel("Number of attempts")
plt.title("15 Second Timing Game Results")

plt.savefig("histogram.png")
plt.show()
