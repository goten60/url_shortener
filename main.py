import requests
import os
import time

def shorten_url(url):
    try:
        response = requests.get('https://is.gd/create.php', params={'format': 'json', 'url': url})  
        if response.status_code == 200:  
            data = response.json()  
            if "errorcode" in data:  
                print(f"Error code {data['errorcode']}, Error message: {data['errormessage']}")
                return None
            return data['shorturl']
        else:  
            print(f"Error http {response.status_code}")
            return None 
    except Exception as e:
        print(f"Error shortening URL {url}: {e}")
        return None

def main():
    input_file = "urls.txt"
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return

    with open(input_file, 'r') as file:
        urls = file.read().splitlines()

    unique_urls = set(urls)
    shortened_urls = {}

    for url in unique_urls:
        shortened = shorten_url(url)
        if shortened:
            shortened_urls[shortened] = url

    for short_url, original_url in shortened_urls.items():
        print(f"{short_url}, {original_url}")

if __name__ == "__main__":
    main()