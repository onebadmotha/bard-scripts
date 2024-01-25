import requests
import json

def fetch_and_extract_ips(url):
    response = requests.get(url)
    data = response.json()

    ips = []
    for entry in data['prefixes']:
        if 'ipv4Prefix' in entry:
            ips.append(entry['ipv4Prefix'])
        elif 'ipv6Prefix' in entry:
            ips.append(entry['ipv6Prefix'])

    return ips

def save_ips_to_file(ips, filename):
    with open(filename, 'w') as file:
        for ip in ips:
            file.write(ip + '\n')

def main():
    url = 'https://www.gstatic.com/ipranges/goog.json'
    ips = fetch_and_extract_ips(url)
    save_ips_to_file(ips, 'extracted_ips.txt')
    print("IP addresses have been extracted and saved to extracted_ips.txt")

if __name__ == "__main__":
    main()

