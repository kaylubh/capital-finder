from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        """
        
        """

        # extract queries from url and store in a dictionary
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query = dict(parse.parse_qsl(url_components.query))

        # get country or capital depending on query from REST Countries API 
        response = ""

        api_url = "https://restcountries.com/v3.1"

        if "country" in query:

            raw_capital_response = requests.get(f"{api_url}/name/{query['country']}?fields=capital")
            parsed_capital_response = raw_capital_response.json()
            # capital_response = raw_capital_response[0]["capital"]
            # response = f"The capital of {query['country']} is {capital_response}."
            response = parsed_capital_response

        if "capital" in query:
            response += query["capital"]

        # send response
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        return
