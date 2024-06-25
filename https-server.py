import http.server
import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]


def get_ssl_context(certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile, keyfile)
    context.set_ciphers("@SECLEVEL=1:ALL")
    return context

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data.decode("utf-8"))


port = 8080
server_address = ("", port)
httpd = http.server.HTTPServer(server_address, MyHandler)

context = get_ssl_context("server.pem", "key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Server running on https://localhost:{port}")
print(f"Server running on https://{local_ip}:{port}")
httpd.serve_forever()