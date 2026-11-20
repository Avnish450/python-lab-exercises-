from pathlib import Path

log_file = Path(__file__).parent / "Data" / "sample.log"

if not log_file.exists():
    print("Log file not found:", log_file)
else:
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    print("Reading log file:", log_file.name)

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
            for level in counts:
                if f"[{level}]" in line:
                    counts[level] += 1

    print("\nLog Summary")
    for level, count in counts.items():
        print(f"{level}: {count}")
