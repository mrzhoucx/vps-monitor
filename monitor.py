#!/usr/bin/env python3
"""
Simple VPS System Monitor
Check CPU, memory, disk usage and print a report.
Requires: psutil (pip install psutil)
"""

import psutil
import datetime

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"=== VPS Monitor Report ({now}) ===")
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    print(f"CPU: {cpu_percent}% ({cpu_count} cores)")
    mem = psutil.virtual_memory()
    print(f"Memory: {mem.percent}% used ({mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB)")
    disk = psutil.disk_usage('/')
    print(f"Disk (/): {disk.percent}% used ({disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB)")
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    print(f"Uptime: {uptime.days} days, {uptime.seconds // 3600} hours")

if __name__ == "__main__":
    main()
