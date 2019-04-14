#Yushu Song
#Assignment 02

import socket
import sys
import traceback

def client(msg, log_buffer=sys.stderr):
    server_address = ('127.0.0.1', 20000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)

    msg_recv = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf-8'))

        received_message = sock.recv(16)
        msg_recv += received_message.decode('utf-8')

        while(len(received_message) >= 16):
            chunk = received_message
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

            received_message = sock.recv(16)
            msg_recv += received_message.decode('utf-8')

        chunk = received_message
        print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

    finally:
        print('closing socket', file=log_buffer)
        sock.close()
        return msg_recv


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
