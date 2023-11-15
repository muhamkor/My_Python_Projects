import requests

api_key = 'ENTER BITLY ACCESS TOKEN'
api_url = 'https://api-ssl.bitly.com/v4/shorten'

def shorten_url(long_url):
	headers = {
	    'Authorization': f'Bearer {apikey}',
	    'Content-Type': 'application/json'
	}

	data = {
	    'long_url': long_url,
	    'group_guid': None  
	}

	try:
		response = requests.post(api_url, headers=headers, json=data, verify=False)
		response.raise_for_status()  # Check for HTTP errors
		short_url = response.json()['link']
		return short_url
	except requests.exceptions.RequestException as e:
		print(f'An error occurred: {e}')
		return None

if __name__ == '__main__':
	long_url = input('Enter the URL you want to shorten: ')
	shortened_url = shorten_url(long_url)

	if shortened_url:
		print(f'Shortened URL: {shortened_url}')
