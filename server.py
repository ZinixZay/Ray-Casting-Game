import socket
import threading
import sys
from time import sleep


class GameServer:
    def __init__(self):
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        try:
            self.s.bind((self.server, self.port))

        except socket.error as e:
            print(str(e))
            return

        self.s.listen(2)
        print("Waiting for a connection")

        currentId = "0"
        pos = ["0:50,50", "1:100,100"]

        while True:
            conn, addr = self.s.accept()
            print("Connected to: ", addr)

            threading.Thread(target=self.threaded_client, args=(conn)).start()

    @staticmethod
    def threaded_client(conn):
        global currentId, pos
        conn.send(str.encode(currentId))
        currentId = "1"
        reply = ''
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode('utf-8')
                if not data:
                    conn.send(str.encode("Goodbye"))
                    break
                else:
                    print("Recieved: " + reply)
                    arr = reply.split(":")
                    id = int(arr[0])
                    pos[id] = reply

                    if id == 0:
                        nid = 1
                    if id == 1:
                        nid = 0

                    reply = pos[nid][:]
                    print("Sending: " + reply)

                conn.sendall(str.encode(reply))
            except:
                break

        print("Connection Closed")
        conn.close
