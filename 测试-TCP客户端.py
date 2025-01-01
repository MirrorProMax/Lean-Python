import socket

clientSocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # AF_INET是ipv4,SOCK_STREAM是tcp
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # 设置端口复用
clientSocket.connect(("localhost", 8000))  # 也是一个元组
clientSocket.send("哈哈".encode("utf-8"))
recData = clientSocket.recv(1024)
print(recData.decode("utf-8"))
clientSocket.close()
