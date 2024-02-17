import server
import client

client.send_until_success("hi")
server.start_server()
