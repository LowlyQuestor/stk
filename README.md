# stk
Simulated stack machine architecture that hopefully can be implemented in hardware.

# How the system works so far
The main components of the machine are the Call Stack (cstk), Return Stack (rstk) and Memory.
CSTK contains all the instructions and data that the system processes. CSTK obtains these instructions from memory.

Take a simple example:

1 2 ADD

Here, inside CSTK is the instruction ADD and the operands 1 and 2. CSTK first pops the ADD inst first (as it is in the top of the stack).
It then knows to pop out the next two elements from CSTK and push the addition of the two.

 - CSTK {1 2 ADD}
- CSTK {1 2}
- CSTK {3}

RSTK simply saves results and addresses that could be needed for later.

Memory contains all the instructions of the program, a program counter goes through memory and pushs the pointed to instruction into CSTK.
