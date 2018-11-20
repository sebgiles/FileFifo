from threading import Lock

class FileFifo:
    def __init__(self, filename):
        self.filename = filename
        self.lock = Lock()
        try:
            f = open(filename,'w')
            f.close()
        except:
            print("impossibile aprire o creare il file")
            raise

    def append(self, line):
        self.lock.acquire()
        try:
            with open(self.filename, "a+") as f:  # Apre il file di testo
                f.write(line + "\r\n")
        finally:
            self.lock.release()

    def popleft(self):
        self.lock.acquire()
        try:
            with open(self.filename, "r") as f:  # Apre il file di testo
                lines = f.readlines()
            if len(lines) > 0:
                line = lines.pop(0).strip()
            else:
                line = None
            filestring = "".join(lines)
            with open(self.filename, "w") as f:  # Apre il file di testo
                f.write(filestring)
        finally:
            self.lock.release()
        return line

    def peekleft(self):
        self.lock.acquire()
        try:
            with open(self.filename, "r") as f:  # Apre il file di testo
                line = f.readline()
        finally:
            self.lock.release()
        if line == "":
            line = None
        return line

    def appendleft(self, line):
        self.lock.acquire()
        try:
            with open(self.filename, "r") as f:  # Apre il file di testo
                lines = f.readlines()
            lines.insert(0, line+"\r\n")
            filestring = "".join(lines)
            with open(self.filename, "w") as f:  # Apre il file di testo
                f.write(filestring)
        finally:
            self.lock.release()



def test():
    tau = 0.5
    import threading
    import random
    import time
    ff = FileFifo("prova.txt")
    random.seed()
    def prod():
        while True:
            x = random.random()
            time.sleep(x * 2 * tau)
            ff.append("x = " + str(x))
    def cons():
        while True:
            time.sleep(tau)
            value = ff.popleft()
            if value is None:
                print("ran out of lines")
            else:
                coin = random.random() - 0.5
                if coin > 0:
                    ff.appendleft(value)
                    print("putting back: " + value)
                else:
                    print("I got: " + value)

    p = threading.Thread(target = prod)
    p.daemon = True
    c = threading.Thread(target = cons)
    c.daemon = True
    p.start()
    c.start()
    while True:
        pass


if __name__ == "__main__":
   test()
