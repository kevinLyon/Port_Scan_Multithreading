from threading import Thread
import socket


target = '127.0.0.1'

def scan(port_list):
    for port in port_list:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(2)
        code = client.connect_ex((target, port))
        if code == 0:
            print(f'{port} OPEN!')
        else:
            pass


def threads():
    THREADS = [
        Thread(target=scan, args=[list(range(1, 4370))]),
        Thread(target=scan, args=[list(range(4370, 8739))]),
        Thread(target=scan, args=[list(range(8739, 13108))]),

        Thread(target=scan, args=[list(range(13108, 17477))]),
        Thread(target=scan, args=[list(range(17477, 21846))]),
        Thread(target=scan, args=[list(range(21846, 26215))]),

        Thread(target=scan, args=[list(range(26215, 30584))]),
        Thread(target=scan, args=[list(range(30584, 34953))]),
        Thread(target=scan, args=[list(range(34953, 39322))]),

        Thread(target=scan, args=[list(range(39322, 43691))]),
        Thread(target=scan, args=[list(range(43691, 48060))]),
        Thread(target=scan, args=[list(range(48060, 52429))]),

        Thread(target=scan, args=[list(range(52429, 56798))]),
        Thread(target=scan, args=[list(range(56798, 61167))]),
        Thread(target=scan, args=[list(range(61167, 65536))]),
    ]

    max_threads = 0

    while len(THREADS) != 0:
        for TH in THREADS[0:3]:
            TH.start()
            max_threads += 1

            if max_threads >= 3:
                TH.join()
                TH.join()
                TH.join()

                del(THREADS[0:3])
                
                max_threads = 0





if __name__ == '__main__':

    threads()
    print('fim do scan!')
