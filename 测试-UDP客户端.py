import socket

clientSocket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
)  # AF_INET是ipv4,SOCK_STREAM是tcp
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # 设置端口复用
clientSocket.sendto("谭清文很帅".encode("utf-8"), ("localhost", 8080))  # 发送数据
data = clientSocket.recv(1024)  # 接收数据
dataNature = data.decode("utf-8")
print(dataNature)  # 打印接收到的数据
