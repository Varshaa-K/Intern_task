
# Task 2 - IP Geolocation & Logging

## Overview
This project reads IP addresses from a text file, retrieves their geolocation details using the ipinfo.io API, and saves the results into a CSV file.

## Technologies Used
- Requests
- CSV
- Logging


## Installation

Install the required dependency:

```bash
pip install requests
```

## How to Run

1. Add the IP addresses to `ips.txt`.
2. Run the Python script:

python ip_lookup.py

3. The script fetches geolocation information.
4. Results are saved in `ip_locations.csv`.
5. Request details and errors are recorded in `ip_lookup.log`.

## Error Handling

- Handles request timeouts.
- Handles HTTP errors.
- Handles invalid JSON responses.
- Handles missing city information.
- Uses `Unknown` when the city cannot be resolved.
- Continues processing the remaining IP addresses.

## Output

### ip_locations.csv

Contains two columns:

- ip
- city

### ip_lookup.log

Records:
- Timestamp
- IP address
- HTTP status code
- Resolved city or error reason

## API Reference

https://ipinfo.io/
