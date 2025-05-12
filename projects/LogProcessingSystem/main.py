from datetime import datetime, timedelta, timezone
from typing import Generator


def process_logs(filepath):
    timestamps = [e[0] for e in read_file(filepath)]
    visits = [int(e[1]) for e in read_file(filepath)]

    t1 = input("Enter timestamp: ")
    
    res_id = binary_search(timestamps, t1)

    return res_id

def read_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            line_tup = line.split()
            print(" ".join(line_tup[:2]), line_tup[4])
            yield " ".join(line_tup[:2]), line_tup[4]


def binary_search(lst: list, timestamp: str) -> int:
    print(f"lst={lst} | timestamp={timestamp}")
    length = len(lst)
    start, end = 0, length - 1
    closest_bigger = None
    
    timestamp_searched = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    
    while start <= end:
        mid = (start + end) // 2
        timestamp_current = datetime.strptime(lst[mid].split()[0], "%Y-%m-%d %H:%M:%S")
        
        if timestamp_current == timestamp_searched:
            return mid
        elif timestamp_current > timestamp_searched:
            closest_bigger = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return closest_bigger if closest_bigger is not None else -1


print(process_logs("server.log"))