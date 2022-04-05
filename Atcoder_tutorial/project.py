import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 50000))  # IPとポート番号を指定します
s.listen(5)
out_data=1

while True:
    clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established!")
    msg = s.recv(8192)#4行のデータを取得
    print(msg)


#out_data=tensorflowのプログラム

    clientsocket.send(out_data)
    clientsocket.close()
