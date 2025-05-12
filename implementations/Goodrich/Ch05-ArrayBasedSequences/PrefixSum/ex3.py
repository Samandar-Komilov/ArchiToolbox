# Given a list of timestamps and user visit counts, compute cumulative visits over time.

activity_logs = [
    {"timestamp": "2024-05-10 09:00:00", "visits": 10},  # Opening time
    {"timestamp": "2024-05-10 09:15:00", "visits": 5},   # After 15 mins
    {"timestamp": "2024-05-10 09:30:00", "visits": 20},   # Peak traffic
    {"timestamp": "2024-05-10 09:45:00", "visits": 3},    # Dip
    {"timestamp": "2024-05-10 10:00:00", "visits": 15},    # Next hour
]


def get_cumulative_visits(logs: list) -> list:
    # In place update of activity_logs
    ln = len(logs)
    prefixSum = [None] * ln
    prefixSum[0] = logs[0]["visits"]
    logs[0]["cumulative_visits"] = prefixSum[0]

    for i in range(1, ln):
        prefixSum[i] = prefixSum[i-1] + logs[i]["visits"]
        logs[i]["cumulative_visits"] = prefixSum[i]

    return None

get_cumulative_visits(activity_logs)
print("Logs after prefix summed:", activity_logs)

import datetime
def find_num_visits(logs: list, timestamp_from: str, timestamp_to: str) -> int:
    format = "%Y-%m-%d %h:%m:%s"
    timestamp_dt_from = datetime.datetime.strptime(timestamp_from, format)
    timestamp_dt_to = datetime.datetime.strptime(timestamp_to, format)

    # I should research:
    #   - Binary Search
    #   - File operations in Python & C