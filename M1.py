
import socket

'''Initialize the webserver with a port and IP
and return socket
@params IP, Port
'''



def init(IP, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((IP, port))
	return s


'''
start server to listen for connections
@params socket
'''
def start_server(socket):
	s.listen(5)

'''
to accept the connection, read request and send response
@params socket
'''
def serve_clients(socket):

	while True:

		clientSocket, clientAddress = socket.accept()

		print(f'\n\nConnection to {clientAddress} established\n')


		httpRequest = clientSocket.recv(1024) # @ rate of 1024 bytes per communication


		print(httpRequest)
		# a click on google, ex search term
		httpResponse = handle_request(httpRequest) # Passing request to be handled
		# handling search term : like finding info

		clientSocket.send(httpResponse)            # sending response to show

		# clientSocket.send(bytes("Socket programming", "utf-8"))

		if(input() == "X"):
			break

		clientSocket.close()


'''
handle http request and return response data
'''
def handle_request(request):

	try:

		# In case of rendering a .html file------------------------Reading sample HTML file

		# filename = 'sample.html'
		# file = open(filename, 'r')
		# htmlCode = "HTTP/1.1 Content-Type: text/html" + file.read()
		# file.close()
		# return bytes(htmlCode, "utf-8")


		return b"""\
		HTTP/1.1 200 OK
		Content-Type: html

		<html>
		<body>
			<h1>Website is under construction</h1>
		</body>
		</html>
		"""


	except IOError:
		print("Error reading file", filename)



ip = input("IP Address: ")
port = int(input("port : "))

s = init(ip, port) # create socket for given ip,port
start_server(s)    # run server on ip, port
serve_clients(s)   # serves clients on running server
