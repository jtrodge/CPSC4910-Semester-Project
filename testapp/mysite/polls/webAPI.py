import requests

# Define the Ebay API endpoint and your Ebay API key
endpoint = "https://api.ebay.com/buy/browse/v1/item/v1|123456789|0"
headers = {'Authorization': 'Bearer <your_ebay_api_key>'}

# Make a GET request to the Ebay API endpoint
response = requests.get(endpoint, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # If the request was successful, print the item information
    item = response.json()
    print("Item ID:", item['itemId'])
    print("Title:", item['title'])
    print("Price:", item['price']['value'])
else:
    # If the request was unsuccessful, print an error message
    print("An error occurred:", response.text)
