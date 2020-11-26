import threading
import time

mutex = threading.Lock()  # is equal to threading.Semaphore(1)
mutex2 = threading.Lock()  # is equal to threading.Semaphore(1)

def A():
        print(A)
        time.sleep(0.5)

def B():
        print(B)
        time.sleep(0.5)

def C():
        print(C)
        time.sleep(0.5)

def D():
        print(D)
        time.sleep(0.5)
def E():
        print(E)
        time.sleep(0.5)

def F():
        print(F)
        time.sleep(0.5)

mutex.acquire()
t1 = threading.Thread(target=A).start()
mutex.release()

mutex.acquire()
mutex2.acquire()
t2 = threading.Thread(target=B).start()
t3 = threading.Thread(target=C).start()
mutex.release()
t4 = threading.Thread(target=D).start()
mutex2.release()

mutex.acquire()
t5 = threading.Thread(target=E).start()
mutex.release()

mutex.acquire()
mutex2.acquire()
t5 = threading.Thread(target=F).start()
mutex.release()
mutex2.release()