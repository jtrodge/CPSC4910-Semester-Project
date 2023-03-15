from ebaysdk.finding import Connection as finding

# Set your API credentials for Sandbox environment
api_key = "JasonRod-APIDev-SBX-ab6a1979d-1d40aa89"
endpoint = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'

# Create a connection to the eBay Finding API
api = finding(appid=api_key, config_file=None, siteid='EBAY-US', domain='svcs.sandbox.ebay.com', endpoint=endpoint)

# Set the search parameters
keywords = "iPhone"  # Enter your search term here
api.execute('findItemsAdvanced', {'keywords': keywords})

# Print the results
for item in api.response.reply.searchResult.item:
    print(item.title)