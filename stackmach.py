# New design features:
# Program Counter
# Seperate Memory address register

# New ISA:

# Movement instructions
# FCH ADDR, mem[ADDR] -> stack
# MOV ADDR N1, stack -> mem[ADDR]
# JMP ADDR, PC = ADDR

# Arithmetic
# ADD N1 N2, N1+N2
# SUB N1 N2, N1-N2
# MUL N1 N2, N1*N2
# DIV N1 N2, N1/N2

# Logical Operators
# OR N1 N2 # do bitwise or
# XOR N1 N2 # do bitwise xor
# AND N1 N2 # do bitwise and

# Stack Operators
# RPUSH N1, push N1 to RSTK from CSTK
# RPOP, pop from RSTK and push to CSTK (like sv)
# DROP, pop whatever is at the top of CSTK
# DUP, Duplicate whatever is at the top of CSTK
# OVER, Pop a second copy of the second element of the stack to the top of CSTK
# SWAP, swap the second and first elements of CSTK

# Conditional Branches
# BEQ ADDR V2 V1, "Branch if equal" if V1=V2, jump to ADDR
# BNE ADDR V2 V1, "Branch if not equal" if V1!=V2 jump to ADDR
# BLE ADDR V2 V1, "Branch if less than" if V1<V2 jump to ADDR
# BGE ADDR V2 V1, "Branch if greater than" if V1>V2 jump to ADDR

# Subroutines
# CALL ADDR, "call subroutine at ADDR", push current PC to RSTK and set new value to ADDR
# EXIT, set PC to value at RSTK

class stack:
    def __init__(self):
        self.mem = []
    def push(self, item):
        self.mem.append(item)
    def pop(self):
        return self.mem.pop()
    def peek(self):
        if not self.mem:
            return []
        else:
            return self.mem[-1]
    def size(self):
        return len(self.mem)
    def look(self):
        print(self.mem)


class stackMachine:
    def __init__(self):
        self.cstk = stack()
        self.rstk = stack()
        self.mem = []
        self.addr = 0 # now the memory address register
        self.pc = 0 # program counter

    # Stack Operations
    def cpush(self, inst):
        self.cstk.push(inst)

    def cpop(self):
        return self.cstk.pop()

    def cpeek(self):
        return self.cstk.peek()

    def rpush(self): # push from the top of CSTK to RSTK 
        self.rstk.push(self.cpop())

    def rpop(self): # push to CSTK from RSTK (replaces sv)
        self.cpush(self.rstk.pop())

    def drop(self): # drop the value at the top of the stack
        self.cpop()

    def dup(self): # duplicate the value at the top of the stack
        self.cpush(self.cpeek())

    def over(self): # make a copy of the second element of the stack at the top of the stack
        self.cpush(self.cstk.mem[-2])

    def swap(self): # swap the first and second elements of the stack
        self.over()
        del self.cstk.mem[-3]

    # Arithmetic
    def add(self):
        self.cpush(self.cpop() + self.cpop())

    def sub(self):
        self.cpush(self.cpop() - self.cpop())

    def mul(self):
        self.cpush(self.cpop() * self.cpop())

    def div(self):
        self.cpush(self.cpop() / self.cpop())

    # Bitwise Logical Operators
    def ori(self):
        self.cpush(self.cpop() | self.cpop())

    def xor(self):
        self.cpush(self.cpop() ^ self.cpop())

    def andi(self):
        self.cpush(self.cpop() & self.cpop())

    # Movement Operators
    def jmp(self): # sets the program counter
        self.pc = self.cpop()
        
    def fetch(self): # Pushes the contents of memory address to stack
        self.addr = self.cpop()
        self.cpush(self.mem[self.addr])

    def mov(self):
        self.addr = self.cpop()
        self.mem[self.addr] = self.cpop()

    # Conditional Branches
    def beq(self): # Branch if equal to
        if self.cpop() == self.cpop():
            self.jmp()
        else:
            pass

    def bne(self): # Branch if not equal to
        if self.cpop() != self.cpop():
            self.jmp()
        else:
            pass

    def ble(self): # Branch if less than
        if self.cpop() < self.cpop():
            self.jmp()
        else:
            pass

    def bge(self): # Branch if greater than
        if self.cpop() > self.cpop():
            self.jmp()
        else:
            pass

    # Subroutines
    def call(self): # save the current address to RSTK and jump to new address
        self.rstk.push(self.pc)
        self.jmp()

    def exit(self): # revert to the previous address
        self.pc = self.rstk.pop()

    # helper functions
    def exec(self): # execute an instruction
       if self.cpeek() == "rpush":
           self.cpop()
           self.rpush()
       elif self.cpeek() == "rpop":
           self.cpop()
           self.rpop()
       elif self.cpeek() == "drop":
           self.cpop()
           self.drop()
       elif self.cpeek() == "dup":
           self.cpop()
           self.dup()
       elif self.cpeek() == "over":
           self.cpop()
           self.over()
       elif self.cpeek() == "swap":
           self.cpop()
           self.swap()
       elif self.cpeek() == "add":
           self.cpop()
           self.add()
       elif self.cpeek() == "sub":
           self.cpop()
           self.sub()
       elif self.cpeek() == "mul":
           self.cpop
           self.mul()
       elif self.cpeek() == "div":
           self.cpop()
           self.div()
       elif self.cpeek() == "or":
           self.cpop()
           self.ori()
       elif self.cpeek() == "xor":
           self.cpop()
           self.xor()
       elif self.cpeek() == "and":
           self.cpop()
           self.andi()
       elif self.cpeek() == "fetch":
           self.cpop()
           self.fetch()
       elif self.cpeek() == "mov":
           self.cpop()
           self.mov()
       elif self.cpeek() == "jmp":
           self.cpop()
           self.jmp()
       elif self.cpeek() == "beq":
           self.cpop()
           self.beq()
       elif self.cpeek() == "bne":
           self.cpop()
           self.bne()
       elif self.cpeek() == "ble":
           self.cpop()
           self.ble()
       elif self.cpeek() == "bge":
           self.cpop()
           self.bge()
       else:
           pass
