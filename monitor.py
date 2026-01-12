error_count = 0

logfile = open("server.log", "r")

for line in logfile:
    if "ERROR" in line:
        error_count += 1

logfile.close()

print("Error count:", error_count)

if error_count > 5:
    print("Critical: Too many errors. Sending email..!")
else:
    print("System is stable.")