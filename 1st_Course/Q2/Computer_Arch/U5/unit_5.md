## CHAPTER 5 - PROCESSOR PART I

### 1. Motivation and Need for Machine Language

Programming languages are tools that allow programmers to write and develop applications and computer systems. There are different categories of programming languages, and some of them are specifically used for assembly programming. Some of the relevant programming languages for an assembly course include:

1. **Machine Language**: The most basic programming language, closest to the CPU architecture.
2. **Assembly Language**: A low-level language that allows writing code easily translatable to machine language.
3. **High-Level Languages**: More abstract languages, closer to human language, such as C, Python, Java, etc.
4. **Specific Purpose Languages**: Designed for specific tasks, like SQL for database management, or HTML for web development.

---

### 2. Machine Language

- **Source Program**: A text file that contains code written in a programming language like C, Python, or Java. It cannot be directly executed by the computer; it must be compiled or interpreted first.
- **Assembly Language**: A low-level language that allows writing code easily translated into machine language.
- **Assembler**: The tool responsible for translating assembly language into machine language.
- **Object Program**: A file generated from the source program that contains code translated into a format executable by the CPU. It is produced by a compiler or interpreter and contains machine or assembly instructions.
- **Machine Language**: The instructions executed by the processor. These are native to each processor family and differ by manufacturer.

### High-Level Language

A programming language that uses syntax closer to human language and is based on abstract concepts like variables, control flow structures, and functions. Examples include Python, Java, and C++.

### Assembly Language

Used for programming directly in machine language. It offers fine control over the CPU and system, but requires deep knowledge of CPU architecture and memory.

### Machine Language

Written in binary code (0s and 1s). It is the lowest-level language and not human-readable, so an assembler or compiler is needed to write programs in it.

---

### 3. Machine Instructions

Machine instructions are commands that the CPU can execute directly, written in binary code. These instructions can perform a wide variety of tasks, such as:

- Loading and storing values in memory
- Performing calculations and comparisons
- Jumping to different parts of the code

Each machine instruction consists of a series of bits that represent an **opcode** (operation code), which specifies the operation to perform, and other bits for the **operands** involved. For a 16-bit architecture, a machine instruction would be structured like this:

- **Opcode**: The binary code that defines the operation the CPU must perform
- **Operands**: Can be sources or destinations, located in:
    - Main memory
    - CPU registers
    - I/O devices

For example, a machine instruction to add two numbers could be structured as follows:

The **instruction set** of a CPU is the collection of commands it can execute, including:

- Arithmetic and logical operations
- Data transfer operations
- Control flow operations
- Memory operations

The number and type of instructions supported by a CPU vary by architecture, and the instruction set is essential to the CPU’s speed and efficiency. Each instruction has an associated opcode and a mnemonic (or shorthand).

**Operands** are the values or memory addresses used in instructions. They may be:

- **Memory addresses**: Typically enclosed in parentheses and expressed in hexadecimal
- **Numbers**: Used in calculations; though the ALU operates in binary, numbers may be represented in base 6 or others
- **Characters**: Used in sequences to represent text

---

### ASCII Code

**ASCII** stands for *American Standard Code for Information Interchange*. It defines a character set used to represent text, including uppercase and lowercase letters, numbers, punctuation, and control characters (like newline and tab).

ASCII is widely used and has served as the foundation for other character encodings such as Unicode.

---

### 4. The Z80 Microprocessor

- A **register** is a small area of internal memory in a processor where temporary values are stored and operations are performed.
- Registers are much faster than external RAM and are used by the processor to store and manipulate critical data.
- Registers are key components in processor architecture.
- Each processor has a different number of registers depending on its design, each with specific functions.
- Each register can be read from and written to by the processor in a single clock cycle.

### Z80 Registers

- **16 registers of 8 bits** (1 byte)
- **4 registers of 16 bits** (2 bytes)
    
    These registers are divided into two groups:
    
- **12 General-Purpose Registers**
- **8 Dedicated Registers** (4 of them 16-bit)

**Z80 General-Purpose Registers**

Used to store data for operations without referencing memory. Divided into two sets: normal (no apostrophe) and alternate (with apostrophe):

- B, C, D, E, H, L, B’, C’, D’, E’, H’, L’
- Only one set is accessible at a time
- They are 8-bit registers, but can be paired for 16-bit operations as follows:
    - BC, DE, HL, B’C’, D’E’, H’L’

Use the `EXX` instruction to switch between register sets.

**Z80 Dedicated Registers**

- **A (Accumulator)**: Main register for arithmetic and logic operations. Also used to exchange data with memory and I/O ports.
- **F (Flags)**: Stores status bits after arithmetic and logic operations (e.g., zero, carry, sign).
- **Alternate Registers (A', F', etc.)**: Used for storing temporary values, especially during subroutine calls or interrupts.
- **PC (Program Counter)**: Holds the address of the next instruction to execute. Automatically increments after each instruction.
- **SP (Stack Pointer)**: Points to the current stack position in memory, used in subroutine calls and interrupts.
- **IX, IY (Index Registers)**: Used for indirect addressing, useful for working with data structures like arrays or tables.

---

### Architecture

The Z80 processor architecture is composed of several key parts:

- **Control Unit**: Manages the flow of data and synchronization within the processor.
- **ALU (Arithmetic Logic Unit)**: Performs arithmetic and logic operations on data in the accumulator.
- **Registers**: Include the accumulator, general-purpose, index, segment, and stack registers.
- **Memory Unit**: Responsible for reading and writing to system memory.
- **Interrupt Control**: Handles hardware and software interrupts. The control unit detects them and directs execution to the appropriate handler.
- **Address Bus**: Carries memory or device addresses to be accessed.
- **Data Bus**: Transfers data between the processor, memory, and I/O devices.

---

### 5. Z80 Assembler (continued)

### `LD` Instruction

The most frequently used instruction in Z80 assembly is `LD` (short for **load**). It is used to **transfer data** from one location to another. The syntax is:

```
asm
CopyEdit
LD destination, source

```

This instruction **copies** the value from the source to the destination. The source is **not modified**, and the destination receives the same value.

### Examples:

```
asm
CopyEdit
LD A, B      ; Copies the value in register B into register A
LD B, 45     ; Loads the decimal number 45 into register B
LD A, 3CH    ; Loads the hexadecimal value 3C into register A
LD (3000H), A ; Stores the value of A in memory address 3000H
LD HL, 2100H ; Loads the 16-bit value 2100H into register pair HL

```

### Memory Access

In assembly, accessing memory often involves parentheses. For example:

```
asm
CopyEdit
LD A, (3000H)  ; Loads the value at memory address 3000H into register A
LD (3000H), A  ; Stores the value in register A into memory at 3000H

```

### Using Index Registers (IX and IY)

These are special 16-bit registers used for **indirect addressing**.

```
asm
CopyEdit
LD A, (IX+0)    ; Load from memory at address IX + 0 into A
LD (IY+5), B    ; Store the value of B at the address IY + 5

```

These forms are useful when dealing with data structures like arrays.

---

### 6. Flag Register (`F`)

The **F register** (also called the **Flag Register**) contains several **status bits** that are set or cleared based on the result of operations. These bits are:

| Bit | Flag Name | Description |
| --- | --- | --- |
| 7 | Sign (S) | Set if result is negative |
| 6 | Zero (Z) | Set if result is zero |
| 5 | — | Reserved / Unused |
| 4 | Half Carry (H) | Set if there was a carry from bit 3 |
| 3 | — | Reserved / Unused |
| 2 | Parity/Overflow (P/V) | Set if parity is even or overflow occurred |
| 1 | Subtract (N) | Set if the last operation was subtraction |
| 0 | Carry (C) | Set if there was a carry out (for adds) or borrow (for subs) |

These flags are automatically updated after arithmetic and logic operations and are used for **conditional jumps**, **comparisons**, and **loops**.

---

### 7. Arithmetic and Logic Instructions

| Instruction | Meaning |
| --- | --- |
| `ADD A, r` | Add register `r` to A |
| `SUB r` | Subtract register `r` from A |
| `INC r` | Increment register `r` by 1 |
| `DEC r` | Decrement register `r` by 1 |
| `AND r` | Bitwise AND between A and `r` |
| `OR r` | Bitwise OR between A and `r` |
| `XOR r` | Bitwise XOR between A and `r` |
| `CP r` | Compare A with `r` (like subtraction, but result not stored) |

### Examples:

```
asm
CopyEdit
ADD A, B      ; A ← A + B
SUB C         ; A ← A - C
INC D         ; D ← D + 1
AND E         ; A ← A & E
CP F          ; Compare A with F (sets flags, doesn't store result)

```

---

### 8. Control Flow Instructions

These instructions change the flow of execution:

| Instruction | Description |
| --- | --- |
| `JP addr` | Jump unconditionally to address |
| `JP Z, addr` | Jump if Zero flag is set |
| `CALL addr` | Call a subroutine at address |
| `RET` | Return from a subroutine |
| `JR offset` | Relative jump (short-range) |
| `DJNZ offset` | Decrement B and jump if not zero |

### Examples:

```
asm
CopyEdit
JP 2050H      ; Unconditionally jump to address 2050H
JP Z, 2100H   ; Jump to 2100H if the Zero flag is set
CALL 3000H    ; Call the subroutine at 3000H
RET           ; Return from subroutine
DJNZ LOOP     ; Decrement B and jump to LOOP if not zero

```

### 9. Stack Operations

The **stack** in Z80 is a section of memory used to **store return addresses, temporary values**, and for **subroutine management**. It grows **downwards**, meaning that every time you push a value, the stack pointer (`SP`) decreases.

### Key Stack Instructions:

| Instruction | Description |
| --- | --- |
| `PUSH rp` | Push register pair onto the stack |
| `POP rp` | Pop top two bytes from the stack into a register pair |
| `CALL addr` | Push current PC to stack, then jump |
| `RET` | Pop return address from stack into PC |

### Examples:

```
asm
CopyEdit
LD SP, 4000H   ; Initialize stack pointer
PUSH BC        ; Push BC onto the stack
POP DE         ; Pop two bytes into DE (BC's old value)
CALL 3000H     ; Jump to subroutine at 3000H, saving return addr
RET            ; Return from subroutine

```

Stack is often used in **interrupts and subroutines** to preserve the context.

---

### 10. Interrupts

Interrupts allow the Z80 to **pause current execution** and jump to a specific routine when a certain event occurs. After handling the event, it **returns to where it left off**.

There are **two types**:

- **Maskable Interrupts (INT)** – Can be turned on/off with `EI` (enable interrupts) and `DI` (disable interrupts).
- **Non-maskable Interrupt (NMI)** – Cannot be disabled.

### Related Instructions:

| Instruction | Description |
| --- | --- |
| `EI` | Enable maskable interrupts |
| `DI` | Disable maskable interrupts |
| `RETI` | Return from interrupt (used for both types) |
| `RETN` | Return from NMI |

Interrupt mode is set using:

```
asm
CopyEdit
IM 0          ; Interrupt Mode 0 (most flexible)
IM 1          ; Mode 1 (simplest)
IM 2          ; Mode 2 (advanced, uses vector table)

```