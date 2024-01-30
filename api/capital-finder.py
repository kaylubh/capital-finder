from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        """
        GET endpoint which expects a query parameter of a country name or country capital name. Responds with the capital if given a country and responds with the country if given a capital.
        """

        # extract queries from url and store in a dictionary
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query = dict(parse.parse_qsl(url_components.query))

        # get country or capital depending on query from REST Countries API 
        response = ""
        api_url = "https://restcountries.com/v3.1"

        if "country" in query:

            country_name = query['country'].title()
            raw_capital_response = requests.get(f"{api_url}/name/{country_name}?fields=capital")
            parsed_capital_response = raw_capital_response.json()
            capital_response = parsed_capital_response[0]["capital"][0]
            response = f"The capital of {country_name} is {capital_response}."

        if "capital" in query:

            capital_name = query['capital'].title()
            raw_country_response = requests.get(f"{api_url}/capital/{capital_name}?fields=name")
            parsed_country_response = raw_country_response.json()
            country_response = parsed_country_response[0]["name"]["common"]
            response = f"{capital_name} is the capital of {country_response}."

        # send response
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        return
