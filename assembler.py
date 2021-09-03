# A little environment for executing instructions and testing the stack machine
import stackmach as stk
import number as num
import sys

class assembler:
    def __init__(self):
        self.sm = stk.stackMachine()


# helper functions for the environment

    def format(self, inst): # removes comments from files and REPL
        insts = inst.split()
        instList = [] # a list of the actual instructions
        i = 0

        while i < len(insts):
            if insts[i] == "#": # if there is a comment
                break
            else:
                instList.append(insts[i])
            i += 1
        return instList

    def state(self): # print the state of the machine
        print("SYSTEM STATE:")
        print('CSTK: ' + str(self.sm.cstk.mem))
        print('RSTK: ' + str(self.sm.rstk.mem))
        print('PC: ' + str(self.sm.pc))
        print('MAR: ' + str(self.sm.addr))
        print('MEM: ' + str(self.sm.mem))


# Functions to manage the machine

    def start(self): # go through memory and move instructions into CSTK
        self.sm.pc = 0 # set the program counter to the beginning

        while self.sm.pc < len(self.sm.mem):
            self.sm.cpush(self.sm.mem[self.sm.pc])

            # check for jumps and conditional branches
            
            if self.sm.mem[self.sm.pc] == "jmp":
                self.sm.cpop()
                self.sm.jmp()
                continue
            
            # branch if not equal to
            elif self.sm.mem[self.sm.pc] == "bne":
                self.sm.cpop()
                if self.sm.cpop() != self.sm.cpop():
                    self.sm.jmp()
                else:
                    break
                continue
            
            # branch if equal to
            elif self.sm.mem[self.sm.pc] == "beq":
                self.sm.cpop()
                if self.sm.cpop() == self.sm.cpop():
                    self.sm.jmp()
                else:
                    break
                continue
            
            # branch if greater than
            elif self.sm.mem[self.sm.pc] == "bge":
                self.sm.cpop()
                if self.sm.cpop() > self.sm.cpop():
                    self.jmp()
                else:
                    break
                continue

            # branch if less than
            elif self.sm.mem[self.sm.pc] == "ble":
                self.sm.cpop()
                if self.sm.cpop() < self.sm.cpop():
                    self.jmp()
                else:
                    break
                continue
            
            self.sm.exec()
            self.sm.pc += 1 # increment program counter
            

    def eval(self, inst): # put instructions from REPL or file into mem
        for i in inst:
            if num.is_number(i):
                self.sm.mem.append(int(i))
                self.sm.pc += 1
            # helper commands
            elif i == "state":
                self.state()

            elif i == "exec":
                self.start()

            elif i == "peek":
                print(str(self.sm.mem[int(input("which address? "))])) # print the val at specified address
            else:
                self.sm.mem.append(i)
                self.sm.pc += 1


    def interact(self): # REPL
        while True:
            self.eval(self.format(input('[' + str(self.sm.pc) + '> ')))
            print("\nCSTK:", str(self.sm.cpeek()))


    def rfile(self, f): # read a file
        with open(f, 'r') as source: # evaluate line by line
            for line in source:
                self.eval(self.format(line))
        self.start()
        self.state()

asm = assembler()

if len(sys.argv) == 1:
    print("Hello from assembler :)")
    asm.interact()
elif len(sys.argv) == 2:
    f = sys.argv[1]
    asm.rfile(f)
else:
    raise ValueError('Incorrect number of arguments')
