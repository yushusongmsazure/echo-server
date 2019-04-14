#Yushu Song
#Assignment 02

import socket
import sys
import traceback

def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 20000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    sock.bind(address)
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    buffer_size = 16
                    data = conn.recv(buffer_size)
                    print('received "{0}"'.format(data.decode('utf8')))

                    conn.send(data)
                    print('sent "{0}"'.format(data.decode('utf8')))

                    if(len(data) < buffer_size):
                        break
            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                print(
                    'echo complete, client connection closed', file=log_buffer
                )
                conn.close()

    except KeyboardInterrupt:
        print('quitting echo server', file=log_buffer)
        conn.close()
        sys.exit(1)

if __name__ == '__main__':
    server()
    sys.exit(0)
