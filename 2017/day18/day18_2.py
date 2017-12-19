import threading
from queue import Queue, Empty
from collections import defaultdict

global q, r
global count

class Worker(threading.Thread):

    def __init__(self, pid, inq, outq):
        threading.Thread.__init__(self)
        self.pid = pid
        self.registers = defaultdict(int)
        self.registers["p"] = pid
        self.registers["b"] = 3
        self.inq = inq
        self.outq = outq

    def __str__(self):
        return "Me " + str(self.pid) + " am " + str(self.registers)

    def run(self):
        global count
        insns = []
        with open("day18.txt", "r") as f:
            insns = [x.strip().split(" ") for x in list(f)]
        x = 0
        while x >= 0 and x < len(insns):
            insn = insns[x]
            typ = insn[0]
            if typ == 'set':
                val = self.registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                self.registers[insn[1]] = val
            elif typ == 'add':
                val = self.registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                self.registers[insn[1]] += val
            elif typ == 'mul':
                val = self.registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                self.registers[insn[1]] *= val
            elif typ == 'mod':
                val = self.registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                self.registers[insn[1]] %= val
            elif typ == 'jgz':
                branch = self.registers[insn[1]] if insn[1].isalpha() else int(insn[1])
                if branch > 0:
                    val = self.registers[insn[2]] if insn[2].isalpha() else int(insn[2])
                    x += val
                    continue
            elif typ == 'snd':
                val = self.registers[insn[1]] if insn[1].isalpha() else int(insn[1])
                self.outq.put(val)
                if self.pid == 1:
                    count += 1
            elif typ == 'rcv':
                try:
                    self.registers[insn[1]] = self.inq.get(True, 5)
                except Empty as e:
                    print(self.pid, "empty")
                    break
            x += 1
 
def main():
    global count
    count = 0
    global q, r
    q = Queue()
    r = Queue()
    a = Worker(0, q, r)
    b = Worker(1, r, q)
    a.start()
    b.start()
    a.join()
    b.join()
    print(count)


if __name__ == '__main__':
    main()