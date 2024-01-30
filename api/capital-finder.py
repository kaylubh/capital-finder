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
        queries = dict(parse.parse_qsl(url_components.query))

        response = ""

        if "country" in queries:
            response += queries["country"]
        elif "capital" in queries:
            response += queries["capital"]

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        return
