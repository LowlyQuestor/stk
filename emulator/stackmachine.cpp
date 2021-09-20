#include<stdio.h>
#include<stdlib.h>
#include<iostream>

#include "stackmachine.hpp"

StackMachine::StackMachine() {}
StackMachine::~StackMachine() {}

// Initialize
void StackMachine::init() {
pc         = 0x0; // Set program counter to beginning of memory
opcode     = 0;
mar        = 0;



// Clear CSTK
for (auto it = cstk.begin(); it != cstk.end(); ++it) {
        *it = 0;
}

// Clear RSTK
for (auto it = rstk.begin(); it != rstk.end(); ++it) {
        *it = 0;
}

// Clear Memory
for (int i = 0; i < 131072; ++i) {
        mem[i] = 0;
}
}

// Stack Operations
void StackMachine::cpush(uint16_t item) { // Push item onto CSTK
        cstk.push_back(item);
}

void StackMachine::cpop() { // Pop first element from CSTK
        cstk.pop_back();
}

uint16_t StackMachine::cpeek() { // Look at top element from CSTK
        return *cstk.end();
}

void StackMachine::drop() { // Drop first element from CSTK
        cpop();
}

void StackMachine::dup() { // Duplicate first element from CSTK 
	cpush(*cstk.end());
}

void StackMachine::over() { // Push a copy of second element of CSTK
	cpush(*(cstk.end()-1));
}

void StackMachine::swap() { // Swap two elements of CSTK
	std::iter_swap(cstk.end(),cstk.end()-1);
}

// RSTK Operations
void StackMachine::rpush(uint16_t item) { // Push an item onto RSTK
rstk.push_back(item);
}

void StackMachine::rpop() { // Pop an item from RSTK
rstk.pop_back();
}

// Arithmetic
void StackMachine::add() {
  auto temp = *(sp) + *(sp2); // store the addition in a temp var
  cpop(); // pop out the two elements
  cpop();
  cpush(temp);
}

void StackMachine::sub() {
  auto temp = *(sp) - *(sp2);
  cpop();
  cpop();
  cpush(temp);
}

void StackMachine::mul() {
  auto temp = *(sp) * *(sp2); // store multiplication in a temp var
  cpop();
  cpop();
  cpush(temp);
}

void StackMachine::div() {
  auto temp = *(sp) / *(sp2);
  cpop();
  cpop();
  cpush(temp);
}

// Bitwise Logical Operations
void StackMachine::ori() {
  auto temp = *(sp) | *(sp2);
  cpop();
  cpop();
  cpush(temp);
}

void StackMachine::xori() {
  auto temp = *(sp) ^ *(sp2);
  cpop();
  cpop();
  cpush(temp);
}

void StackMachine::andi() {
  auto temp = *(sp) & *(sp2);
  cpop();
  cpop();
  cpush(temp);
}

// Movement Operations
void StackMachine::jmp() {
  pc = *(sp); // set the program counter to the value at the top of stack
  cpop();
}

void StackMachine::fetch() {
  mar = *(sp); // set the MAR to the value at the top of the stack
  cpop();
  cpush(mem[mar]); // push the contents of memory at MAR
}

void StackMachine::mov() { // First arg is address second is data
  mar = *(sp);
  cpop();
  mem[mar] = *(sp2);
  cpop();
}

// Conditional Branches
void StackMachine::beq() { // Branch if equal to
  if ( *(sp) == *(sp2) ) {
    cpop();
    cpop();
    jmp();
  } else {} // do nothing
}

void StackMachine::bne() { // Branch if not equal to
  if ( *(sp) != *(sp2) ) {
    cpop();
    cpop();
    jmp();
  } else {}
}

void StackMachine::ble() { // Branch if less than
  if ( *(sp) < *(sp2) ) {
    cpop();
    cpop();
    jmp();
  } else {}
}

void StackMachine::bge() { // Branch if greater than
  if ( *(sp) > *(sp2) ) {
    cpop();
    cpop();
    jmp();
  } else {}
}

// Subroutine Calls
void StackMachine::call() {
  rpush(pc); // save the current address to RSTK
  jmp(); // jump to new address
}

void StackMachine::exit() {
  pc = *(rstk.end()); // set the program counter back
  rpop(); // take out that value
}

