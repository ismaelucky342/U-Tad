# **Unit 6: Processor – Part II**

> Advanced Concepts in Assembly & Processor Architecture (Z80 Focused)
> 

---

## 1. Deeper Understanding of the CPU

In Unit 5, we covered registers, memory access, and basic operations. Now, we dive deeper into **how the processor executes instructions**, how the **ALU** works internally, and how **execution timing** is handled.

### Fetch-Decode-Execute Cycle

Every instruction follows this cycle:

1. **Fetch**: CPU reads the next opcode from memory (pointed by PC).
2. **Decode**: Control unit interprets the opcode.
3. **Execute**: ALU and registers perform the operation.

Each step might take several **clock cycles** (also called **T-states**).

---

## 2. Clock Cycles & Machine Cycles

### Clock Cycles (T-states)

- One complete tick of the processor’s clock.
- The Z80 runs instructions in multiple T-states.

### Machine Cycles (M-cycles)

- A group of T-states forming a basic memory operation (e.g., fetch, memory read, memory write).
- Example: Instruction `LD A, B` takes **1 M-cycle (Fetch)** = **4 T-states**.

| Instruction | M-cycles | T-states |
| --- | --- | --- |
| NOP | 1 | 4 |
| LD A, B | 1 | 4 |
| JP addr | 3 | 10 |
| CALL addr | 5 | 17 |

---

## 3. ALU (Arithmetic Logic Unit)

The **ALU** is the part of the processor responsible for **calculations** and **logical operations**. Operations like:

- `ADD`, `SUB`, `AND`, `OR`, `XOR`, `CP`
- Internally uses **binary circuits** to perform these operations
- Affects **flags** in the `F` register (Sign, Zero, Carry, etc.)

### ALU Flags Recap:

| Flag | Purpose |
| --- | --- |
| Z | Zero result? |
| S | Negative result? |
| C | Carry out? |
| P/V | Overflow or Parity |
| H | Half Carry (BCD math) |
| N | Add/Subtract indicator |

---

## 4. Memory Segmentation & Addressing

### Memory Map

- The Z80 uses a **16-bit address bus**, so it can address **64KB** (0x0000 to 0xFFFF).
- Memory is typically divided into:
    - **ROM** (fixed instructions)
    - **RAM** (variable data)
    - **I/O space** (external devices)

### Addressing Modes

| Mode | Example | Description |
| --- | --- | --- |
| Immediate | `LD A, 10H` | Constant value |
| Register | `LD A, B` | From another register |
| Direct | `LD A, (1234H)` | Load from a fixed memory address |
| Indirect | `LD A, (HL)` | Load from address in HL |
| Indexed | `LD A, (IX+2)` | Use index register + displacement |

---

## 5. Subroutines & Context Saving

When the CPU jumps to a subroutine (`CALL`), it must:

- **Save the return address** (push to stack)
- Possibly **save register values** (caller responsibility)
- After finishing, **return** with `RET`

Advanced subroutines might:

- Use **stack frames** for local variables
- Save/restore **AF**, **BC**, **DE**, etc.

```
asm
MYFUNC:
    PUSH AF
    LD A, 5
    ; do stuff
    POP AF
    RET
```

---

## 6. Interrupt Modes and Execution

Z80 supports 3 interrupt modes:

| Mode | Description |
| --- | --- |
| IM 0 | Execute any 8-bit opcode from data bus (risky, flexible) |
| IM 1 | Fixed jump to 0038H (simple and safe) |
| IM 2 | Uses I register and a vector table (advanced, powerful) |

```
asm
IM 1     ; Use mode 1
EI       ; Enable interrupts
; Now the CPU can jump to 0038H when an interrupt is triggered
```

---

## 7. Input/Output (I/O) Operations

Z80 has **dedicated I/O instructions**:

| Instruction | Description |
| --- | --- |
| `IN A, (C)` | Input byte from port in C |
| `OUT (C), A` | Output byte to port in C |

Usually used for communication with peripherals: keyboard, screen, etc.

```
asm
LD C, 0x10   ; Port address
IN A, (C)    ; Read value into A
OUT (C), A   ; Echo it back
```

---

## 8. Sample Program with Subroutine & Loop

```
asm
ORG 0000H

START:
    LD SP, 5000H
    LD A, 10

LOOP:
    CALL PRINT_A
    DEC A
    JP NZ, LOOP
    HALT

PRINT_A:
    PUSH AF
    ; Simulate printing A (e.g., write to screen port)
    POP AF
    RET
```
## 9. Debugging and Optimization Techniques

### Debugging Assembly Code

Debugging assembly programs can be challenging due to the low-level nature of the code. Here are some common techniques:

- **Use Breakpoints**: Pause execution at specific points to inspect register values and memory.
- **Step Through Instructions**: Execute one instruction at a time to observe changes in the CPU state.
- **Inspect Flags**: Check the status of flags in the `F` register to understand the results of operations.
- **Use Comments**: Add detailed comments to explain the purpose of each instruction or block of code.

### Optimization Tips

Optimizing assembly code involves reducing execution time or memory usage:

- **Minimize T-states**: Choose instructions with fewer T-states where possible.
- **Reuse Registers**: Avoid unnecessary memory access by keeping frequently used values in registers.
- **Unroll Loops**: For small, fixed iterations, unroll loops to eliminate branching overhead.
- **Inline Subroutines**: Replace frequently called subroutines with inline code to save the overhead of `CALL` and `RET`.

---

## 10. Advanced Addressing Techniques

### Bank Switching

When the 64KB address space is insufficient, **bank switching** allows access to additional memory:

- Divide memory into banks (e.g., 16KB each).
- Use a special register or I/O port to switch between banks.

```
asm
LD A, 02H       ; Select bank 2
OUT (BANK_REG), A
LD A, (4000H)   ; Access memory in bank 2
```

### Shadow Registers

The Z80 includes an alternate set of registers (`AF'`, `BC'`, `DE'`, `HL'`) that can be swapped with the main registers:

- Useful for fast context switching or interrupt handling.
- Swap using `EXX` and `EX AF, AF'`.

```
asm
EXX             ; Swap BC, DE, HL with BC', DE', HL'
EX AF, AF'      ; Swap AF with AF'
```

---

## 11. Practical Applications of Z80

The Z80 processor has been widely used in various applications:

- **Retro Computers**: ZX Spectrum, MSX, and others.
- **Embedded Systems**: Industrial controllers, calculators, and gaming consoles.
- **Learning Tool**: Ideal for understanding low-level programming and computer architecture.

By mastering the Z80, you gain insights into the foundations of modern processors and assembly programming.
