import urllib.request
import json
import ssl

# Set your API credentials for Sandbox environment
api_key = "JasonRod-APIDev-SBX-ab6a1979d-1d40aa89"
endpoint = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'

# Set the search parameters
keywords = "iPhone"  # Enter your search term here
url = f'{endpoint}?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME={api_key}&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords={keywords}'

# Disable SSL verification
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Make a request to the eBay Finding API
with urllib.request.urlopen(url, context=context) as f:
    response = json.loads(f.read().decode())

# Print the results
for item in response['findItemsAdvancedResponse'][0]['searchResult'][0]['item']:
    print(item['title'][0])
