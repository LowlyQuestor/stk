import stackmach as stk
import number as num
import sys

# TODO: Labels
# TODO: Comments
class assembler: # an interface to the stack machine
    def __init__(self):
        self.sm = stk.stackMachine()

    def state(self): 
         print("SYSTEM STATE:")
         print('CSTK: ' + str(self.sm.cstk.mem))
         print('RSTK: ' + str(self.sm.rstk.mem))
         print('PC: ' + str(self.sm.pc))
         print('MAR: ' + str(self.sm.addr))
         print('MEM: ' + str(self.sm.mem))

    def start(self): # go through memory and move instructions into CSTK
        self.sm.pc = 0
        while self.sm.pc < len(self.sm.mem):
            self.sm.cpush(self.sm.mem[self.sm.pc]) # push whatever the PC points to into the stack
            if self.sm.mem[self.sm.pc] == "jmp":
                self.sm.cpop()
                self.sm.jmp()
                continue
            elif self.sm.mem[self.sm.pc] == "bne":
                self.sm.cpop()
                if self.sm.cpop() != self.sm.cpop():
                    self.sm.jmp()
                else:
                    break
                continue
            self.state()
            self.sm.exec()
            self.sm.pc += 1 # increment program counter

    def eval(self,inst): # push all values it recieves into memory
        for i in inst.split():
            if num.is_number(i):
                self.sm.mem.append(int(i))
                self.sm.pc += 1
            elif i == "state": # print the values in all stacks and memory
                self.state()
            elif i == "exec":
                self.start()
            elif i == "#":
                self.state()
                pass
            elif i == "peak":
                add = input("which address? ")
                print(str(self.sm.mem[int(add)]))
            else:
                self.sm.mem.append(i)
                self.sm.pc += 1
    
    def interact(self):
        while True:
            self.eval(input('[' + str(self.sm.pc) + '> '))
            print("\nCSTK:", str(self.sm.cpeek()))
            
    def fileeval(self, f):
        with open(f, 'r') as source: # evaluate file line by line
            for line in source:
                self.eval(line)
        self.start()
        self.state()

asm = assembler()

if len(sys.argv) == 1:
    print("Hello from assembler :)")
    asm.interact()
elif len(sys.argv) == 2: # if a file is provided, open the file and evaluate the code inside it
    f = sys.argv[1]
    asm.fileeval(f)
else:
    raise ValueError('Incorrect number of arguments')
