#include<vector>
#include<cstdint>
class StackMachine {
private:
  std::vector<uint16_t> cstk; // Call stack
  std::vector<uint16_t> rstk; // Return stack

  std::vector<uint16_t>::iterator sp = cstk.end(); // first stack pointer (top of stack)
  std::vector<uint16_t>::iterator sp2 = cstk.end() - 1; // second stack pointer (second element)

  uint16_t mem[131072]; // 128K RAM

  uint16_t pc; // Program counter
  uint16_t opcode; // Current opcode
  uint16_t mar; // Memory Address Register

  void init();

public:
  StackMachine();
  ~StackMachine();

  void run(); // run one instruction


  // CSTK Operations
  void cpush(uint16_t item);  // Push an item onto CSTK
  void cpop(); // Pop first element of CSTK
  uint16_t cpeek(); // Look at top of CSTK
  void drop(); // Drop first element of CSTK
  void dup(); // Duplicate first element of CSTK
  void over(); // Push a copy of second element of CSTK
  void swap(); // Swap first and second elements

  
  // RSTK Operations
  void rpush(uint16_t item); // Push an item onto RSTK
  void rpop(); // Pop first element from RSTK

  // Arithmetic
  void add();
  void sub();
  void mul();
  void div();

  // Bitwise Logical Operations
  void ori(); // Bitwise "or" instruction
  void xori(); // Bitwise "xor" instruction
  void andi(); // Bitwise "and" instruction

  // Movement Operations
  void jmp(); // Jump
  void fetch();
  void mov();

  // Conditional Branches
  void beq(); // Branch if equal to
  void bne(); // Branch if not equal to
  void ble(); // Branch if less than
  void bge(); // Branch if greater than

  // Subroutines
  void call(); // call subroutine
  void exit();
};
  
