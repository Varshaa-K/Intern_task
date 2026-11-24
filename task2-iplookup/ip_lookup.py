
import requests
import csv
import logging
from datetime import datetime
from pathlib import Path

# Get the current project folder
BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "ips.txt"
OUTPUT_FILE = BASE_DIR / "ip_locations.csv"
LOG_FILE = BASE_DIR / "ip_lookup.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)


def get_ip_location(ip):
    url = f"https://ipinfo.io/{ip}/geo"

    status_code = "N/A"

    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code

        if response.status_code != 200:
            reason = f"HTTP error: {status_code}"
            logging.info(
                "IP: %s | HTTP Status: %s | Error: %s",
                ip, status_code, reason
            )
            return "Unknown"

        data = response.json()

        city = data.get("city")

        if not city or not city.strip():
            reason = "City field missing"
            logging.info(
                "IP: %s | HTTP Status: %s | Error: %s",
                ip, status_code, reason
            )
            return "Unknown"

        logging.info(
            "IP: %s | HTTP Status: %s | City: %s",
            ip, status_code, city
        )

        return city

    except requests.exceptions.Timeout:
        reason = "Request timed out"

    except requests.exceptions.RequestException as error:
        reason = f"Request error: {error}"

    except ValueError:
        reason = "Invalid JSON response"

    except Exception as error:
        reason = f"Unexpected error: {error}"

    logging.info(
        "IP: %s | HTTP Status: %s | Error: %s",
        ip, status_code, reason
    )

    return "Unknown"


def main():

    # Read IP addresses from the input file
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        ip_addresses = [
            line.strip()
            for line in file
            if line.strip()
        ]

    # Write results to CSV
    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8"
    ) as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(["ip", "city"])

        for ip in ip_addresses:
            city = get_ip_location(ip)

            writer.writerow([ip, city])

            print(f"{ip} -> {city}")

    print("\nIP lookup completed successfully.")
    print(f"CSV saved to: {OUTPUT_FILE}")
    print(f"Log saved to: {LOG_FILE}")


if __name__ == "__main__":
    main()
