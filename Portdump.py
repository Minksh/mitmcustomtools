from mitmproxy import http
from mitmproxy import ctx

class SimpleProxy:
    def request(self, flow: http.HTTPFlow) -> None:
        # Log each request URL
        ctx.log.info(f"Request: {flow.request.method} {flow.request.url}")

    def response(self, flow: http.HTTPFlow) -> None:
        # Log each response status code
        ctx.log.info(f"Response: {flow.response.status_code} {flow.request.url}")
        
        # Log basic connection info
        if flow.client_conn:
            connection_info = (
                f"Connection Info - Host: {flow.client_conn.address[0]}, "
                f"Port: {flow.client_conn.address[1]}"
            )
            ctx.log.info(connection_info)
            
            # Optionally, dump connection info into a log file
            with open("connection_info.log", "a") as f:
                f.write(f"{connection_info}\n")

addons = [
    SimpleProxy()
]
