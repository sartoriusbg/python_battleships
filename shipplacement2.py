import server
import client
import time

client.send_until_success('hi', '127.0.0.1', 12346)
server.start_server()
time.sleep(5)
