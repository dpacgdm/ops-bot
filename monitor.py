import sys

def analyze_log(filename):
    try:
        # Open the file provided in the argument
        logfile = open(filename, "r")
        
        error_count = 0
        
        for line in logfile:
            # Change "ERROR" to be case-insensitive (optional bonus)
            if "ERROR" in line:
                error_count += 1
        
        logfile.close()
        
        print(f"Analyzing {filename}...")
        print(f"Total Errors: {error_count}")
        
        if error_count > 5:
            print("CRITICAL: High error rate detected!")
        else:
            print("Status: Stable")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if the user actually provided a filename argument
    if len(sys.argv) < 2:
        print("Usage: python3 monitor.py <filename>")
    else:
        # The filename is the second item in the list (index 1)
        log_file_name = sys.argv[1]
        analyze_log(log_file_name)