# How to implement Python APIs
- There are several ways to implement Python APIs, including using popular web frameworks such as Flask and Django.

- Here is a simple example using Flask:

    - from flask import Flask, jsonify, request

    - app = Flask(__name__)
    
    - @app.route('/api/sum', methods=['POST'])
    - def add_numbers():
        - data = request.get_json()
        - result = data.get('a') + data.get('b')
        - return jsonify(result=result)
    
    - if __name__ == '__main__':
        - app.run(debug=True)

- In this example, we create a Flask application and define a single endpoint, /api/sum, which takes in two parameters a and b as a JSON object and returns the sum of the two numbers.
- This is just a simple example, but Flask and Django provide many more features for building full-fledged APIs, including authentication, database access, and more.
- You may also use other libraries such as FastAPI, which is a more modern and fast alternative to Flask, and provides several advanced features out of the box.

# Where to find Python APIs
- There are several sources to find existing Python APIs, including:
    1. Public APIs - There are many public APIs available on the web, which provide access to a wide range of data and services, such as weather information, financial data, and more. Some popular websites for finding public APIs include RapidAPI, ProgrammableWeb, and Public APIs.
    2. Python Package Index (PyPI) - PyPI is the official package repository for Python and contains thousands of packages, many of which provide APIs. You can search PyPI for packages that provide the functionality you need.
    3. Github - Github is a popular platform for open-source projects and you can find many open-source Python projects that provide APIs.
    4. Company websites - Many companies provide APIs for their products and services, and you can find these APIs on the company's website.
    5. Online tutorials and forums - You can find many tutorials and forums online that provide information and examples of how to use specific APIs, or you can ask other developers for recommendations.

- Once you have found an API that you would like to use, you can usually find documentation and code examples on the API provider's website to help you get started.

# Ebay API 
- Getting Started 
    - Create an account (Takes a day to get verified): ** https://developer.ebay.com/ **
    - Under your Account name:
        - Hover over your account name
        - Click Application Keysets
        - Create an Sandbox or Production Environment Keyset (Professor Recommendends Sandbox Environment)
            - Production: The Production environment is the eBay website, where eBay members buy and sell items.
            - Sandbox: The Sandbox environment is a test version of the eBay website, where developers can simulate buying and selling items.
    - Generate a User token (Auth'n'Auth)

- Resources 
    **  https://github.com/iurigo/Ebay-API-with-python-ebaysdk ** 




