from ebaysdk.finding import Connection as Finding

# Set the Ebay API Sandbox credentials
APP_ID = "JasonRod-APIDev-SBX-ab6a1979d-1d40aa89"
DEV_ID = "20fcf12b-62c7-4ed7-88fc-2fecd2d8b3b1"
CERT_ID = "SBX-b6a1979df2b8-569b-4787-adb3-9ca9"

# Create a connection to the Ebay API Sandbox
api = Finding(appid=APP_ID, devid=DEV_ID, certid=CERT_ID, config_file=None, domain='svcs.sandbox.ebay.com')

# Set the search parameters
keywords = "iPhone"
sort_order = "BestMatch"
pagination_input = {"entriesPerPage": 100, "pageNumber": 1}

# Search for products
response = api.execute("findItemsByKeywords", {"keywords": keywords, "sortOrder": sort_order, "paginationInput": pagination_input})

# Get the results
items = response.reply.searchResult.item

# Print the results
for item in items:
    print(item.title)
    print(item.viewItemURL)
    print(item.sellingStatus.currentPrice.value)
