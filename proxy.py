import http.server
import socketserver

# Define the proxy server's address and port
proxy_host = 'localhost'
proxy_port = 8080

# Define the target server's address and port
target_host = 'example.com'
target_port = 80

# Create a proxy handler class
class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Forward the request to the target server
        self.headers['Host'] = target_host
        self.send_header('Host', target_host)
        self.send_header('X-Forwarded-For', self.client_address[0])
        self.send_header('X-Forwarded-Host', self.headers['Host'])
        self.send_header('X-Forwarded-Server', proxy_host)
        self.send_header('Connection', 'close')
        self.end_headers()

        # Send the request to the target server
        with socketserver.TCPServer(("", 0), http.server.SimpleHTTPRequestHandler) as httpd:
            httpd.timeout = 5  # Set a timeout for the proxy server
            httpd.server_name = self.headers['Host']
            httpd.handle_request()

# Start the proxy server
with socketserver.ThreadingTCPServer((proxy_host, proxy_port), ProxyHandler) as httpd:
    print(f"Proxy server is running on {proxy_host}:{proxy_port}")
    httpd.serve_forever()
