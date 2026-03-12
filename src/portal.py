import http.server
import socketserver
import subprocess
from socketserver import ThreadingMixIn

PORT = 80
SECRET_PATH = "YOUR_SECRET_URL_HERE" # Change this before deploying!
SUCCESS_URL = "https://www.google.com"

class ThreadedHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

class HardenedPortalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == f"/{SECRET_PATH}":
            client_ip = self.client_address[0]
            try:
                subprocess.run(["nft", "add", "element", "inet", "custom_portal", "allowed_clients", f"{{ {client_ip} timeout 2h }}"], check=True)
                self.send_response(302)
                self.send_header('Location', SUCCESS_URL)
                self.end_headers()
            except Exception as e:
                self.send_error(500, f"Firewall Error: {e}")
        elif self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f"""
            <html>
            <body style="text-align:center; padding-top:100px; font-family:sans-serif; background:#f4f4f4;">
                <div style="background:white; display:inline-block; padding:50px; border-radius:10px; shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <h1>Guest Network Access</h1>
                    <p>Click 'Accept' for 2 hours of internet access.</p>
                    <form action="/{SECRET_PATH}" method="GET">
                        <button type="submit" style="padding:15px 30px; background:#007bff; color:white; border:none; border-radius:5px; cursor:pointer;">Accept & Connect</button>
                    </form>
                </div>
            </body>
            </html>"""
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Not Found")

if __name__ == '__main__':
    server = ThreadedHTTPServer(('', PORT), HardenedPortalHandler)
    print(f"Portal running on port {PORT}...")
    server.serve_forever()
