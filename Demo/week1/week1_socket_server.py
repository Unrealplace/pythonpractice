import socket
from threading import Thread

ADDRESS = ('127.0.0.1',8000)
socket_server = None
socket_server_pool = [] #连接池

def initServer():
    global socket_server
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.bind(ADDRESS)
    socket_server.listen(5) #最大排队等待连接数量
    print('服务已经启动，等待客户端连接...')
    pass

def accept_clinet():
    """
    接受新的链接
    :return:
    """
    while True:
        # 阻塞等待客户端连接
        client,_= socket_server.accept()
        socket_server_pool.append(client)
        # 每个客户端创建一个独立的线程进行管理
        thread = Thread(target=message_handle,args=(client,))
        # 设置成守护线程
        thread.setDaemon(True)
        thread.start()
        pass
    pass

def message_handle(client : socket):
    """
    消息处理
    :param client:
    :return:
    """
    client.sendall('链接服务器成功'.encode(encoding='utf-8'))
    while True:
        bytes = client.recv(1024)
        print('来自客户端消息：',bytes.decode(encoding='utf-8'))
        if len(bytes) == 0:
            client.close()
            socket_server_pool.remove(client)
            print('有一个客户端下线了')
        pass
    pass


if __name__ == '__main__':
    initServer()
    thread = Thread(target=accept_clinet)
    thread.setDaemon(True)
    thread.start()
    while True:
        cmd = input("""
        输入1:查看当前在线人数
        输入2:给指定客户端发送消息
        输入3:关闭服务端
        """)
        if cmd == '1':
            print('################')
            print('当前在线人数：',len(socket_server_pool))
            pass
        elif cmd == '2':
            print('################')
            index,msg = input('请输入【索引,消息】的形式:').split(',')
            socket_server_pool[int(index)].sendall(msg.encode(encoding='utf-8'))
            pass
        elif cmd == '3':
            exit()
            pass
        pass
    pass
