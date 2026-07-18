# Honeypot Log Analyser

A Python tool that reads and analyses log files produced by my honeypot project.

## What it does
- Reads the honeypot log file line by line
- Extracts the source IP address from each logged connection
- Counts how many connections came from each unique IP
- Reports total connections, unique addresses, and a per-IP breakdown
- Flags any IP with an unusually high connection count as possible scanning activity

## How to run
python loganalyser.py

Expects honeypot_log.txt in the same directory. Works with logs produced by:
github.com/hus-sein777/Honeypot

## What I learned
- Reading files in Python and the difference between read and append modes
- Using dictionaries to count occurrences, and why dictionary keys are unique
- String slicing and find() to extract structured data from raw log lines
- Setting detection thresholds and what repeated connections from one source can indicate

## Built as part of my BSc Computer Science with Cyber Security# LogAnalyser
