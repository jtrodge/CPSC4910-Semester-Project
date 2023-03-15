from ebaysdk.finding import Connection as Finding

# Set the Ebay API Sandbox credentials
APP_ID = "MarkFabi-4910proj-PRD-5cd6d2723-b325ca86"
DEV_ID = "cac0d703-8005-41e6-8a52-b07008b4ab53"
CERT_ID = "PRD-cd6d27237ff4-d167-41a2-98ef-8671"

# Create a connection to the Ebay API Sandbox
api = Finding(appid=APP_ID, devid=DEV_ID, certid=CERT_ID, config_file=None, domain='svcs.ebay.com')

# Set the search parameters
keywords = "hat"
sort_order = "BestMatch"
pagination_input = {"entriesPerPage": 100, "pageNumber": 1}

# Search for products
response = api.execute("findItemsByKeywords", {"keywords": keywords, "sortOrder": sort_order, "paginationInput": pagination_input})

# Get the results
items = response.reply.searchResult.item
# items = response.reply
# print(items)
# Print the results
for item in items:
    
    print(item.title)
    print(item.viewItemURL)
    print(item.sellingStatus.currentPrice.value)