# CHAPTER 2 - BOOLEAN ALGEBRA, LOGIC, AND DIGITAL CIRCUITS
### Logic Gates

Logic gates are the fundamental building blocks of digital circuits. They perform basic logical functions that are essential for digital computation. The most commonly used logic gates are NOT, OR, and AND gates. These gates operate based on Boolean Algebra rules and can be combined to create more complex circuits. Below is a detailed explanation of these gates, including their symbols, algebraic notations, and truth tables.

| Gate Name | Symbol | Algebraic Notation | Truth Table |
| --- | --- | --- | --- |
| NOT | ¬ | NOT(x) | 0 → 1, 1 → 0 |
| AND | ∧ | x . y | 0 . 0 = 0, 0 . 1 = 0, 1 . 0 = 0, 1 . 1 = 1 |
| OR | ∨ | x + y | 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, 1 + 1 = 1 |

The NOT gate, also known as an inverter, flips the input signal. The AND gate outputs true only when all inputs are true, while the OR gate outputs true if at least one input is true.

**Other Gates:**

In addition to the basic gates, there are other gates like NOR, NAND, and XOR, which are combinations of the basic gates. These gates are widely used in digital systems for various purposes.

| Gate Name | Symbol | Algebraic Notation | Truth Table |
| --- | --- | --- | --- |
| NOR | ¬(x + y) | NOT(x + y) | 0 + 0 = 1, 0 + 1 = 0, 1 + 0 = 0, 1 + 1 = 0 |
| NAND | ¬(x . y) | NOT(x . y) | 0 . 0 = 1, 0 . 1 = 1, 1 . 0 = 1, 1 . 1 = 0 |
| XOR | x ⊕ y | x ⊕ y | 0 ⊕ 0 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1, 1 ⊕ 1 = 0 |

The NOR gate is the negation of the OR gate, while the NAND gate is the negation of the AND gate. The XOR gate outputs true only when the inputs are different. These gates can be used to implement more complex logical functions and circuits.

### 2. Combinational Circuits

Combinational circuits are a type of digital circuit where the output is determined solely by the current inputs. Unlike sequential circuits, they do not have memory elements and do not depend on past inputs. These circuits are widely used in digital systems for tasks like data selection, decoding, and arithmetic operations.

**Truth Table Representation:**
Combinational circuits are often defined by their truth table, symbol, and Boolean function. Simplifying the Boolean function using Karnaugh maps and algebraic methods is essential to reduce the circuit's complexity and improve efficiency.

| Circuit Type | Inputs | Outputs | Example Truth Table |
| --- | --- | --- | --- |
| Multiplexer (MUX) | n | 1 | Selects one of n inputs based on control signals |
| Demultiplexer (DEMUX) | 1 | n | Routes a single input to one of n outputs |
| Decoder | n | 2^n | Activates one output based on n inputs |
| Adder | 2 | 2 (Sum, Carry) | Adds two binary numbers |

**Typical Combinational Circuits:**

- **Multiplexer (MUX):** A multiplexer is a circuit that selects one of several input signals and forwards it to a single output. The selection is controlled by additional input signals called select lines. Multiplexers are used in applications like data routing and signal selection.
- **Demultiplexer (DEMUX):** The demultiplexer performs the inverse operation of a multiplexer. It takes a single input signal and routes it to one of several outputs based on control signals. Demultiplexers are used in applications like data distribution and signal demultiplexing.
- **Decoder:** A decoder is a circuit with n input signals and 2^n output signals. It activates one specific output based on the binary value of the inputs. Decoders are commonly used in memory addressing and data selection.
- **Adder:** Adders are circuits used for binary addition. A half-adder adds two binary digits and produces a sum and a carry output. A full-adder extends this functionality to include a carry input, enabling multi-bit addition.

**Building Boolean Functions with Decoders and Multiplexers:**
Decoders and multiplexers can be used to implement Boolean functions efficiently. For example, a decoder can generate minterms for a given function, while a multiplexer can directly implement the function by selecting appropriate inputs.

### 3. Sequential Circuits

Sequential circuits are a type of digital circuit where the output depends not only on the current inputs but also on the history of inputs. These circuits have memory elements that store information about past states, making them suitable for applications like counters, registers, and state machines.

| Circuit Type | Description | Example |
| --- | --- | --- |
| Flip-Flop | Stores a single bit of data | S-R Latch, J-K Latch |
| Register | Stores multiple bits of data | Shift Register |
| Counter | Generates a sequence of outputs | Upward, Downward, Reversible |

**Bistables (Flip-Flops):**
Bistables are the basic building blocks of sequential circuits. They are capable of storing a single bit of information and can retain their state indefinitely until triggered by an input signal.

- **Characteristics:**
    - Two complementary outputs: Q and NOT(Q).
    - Time-dependent behavior, meaning the state changes based on input signals and clock pulses.
    - The current state is denoted as Qt, and the next state is denoted as Qt+1.

**Types of Latches:**

- **S-R Latch (Set-Reset Latch):** An asynchronous bistable circuit with two inputs (S and R) and two outputs (Q and NOT(Q)). It is used to store a single bit of data.
- **S-R Latch with Clock:** A variant of the S-R latch that operates in synchronization with a clock signal, ensuring controlled state changes.
- **J-K Latch with Clock:** An advanced version of the S-R latch that resolves the invalid state issue. When both inputs are 1, the state toggles.

**Registers:**
Registers are sequential circuits that store multiple bits of data. They are used for temporary data storage and transfer. Registers can operate in serial mode (one bit at a time) or parallel mode (all bits simultaneously).

**Counters:**
Counters are sequential circuits that generate a sequence of outputs, often in synchronization with a clock signal. They are used for counting events, measuring time intervals, and generating timing signals.

- **Types of Counters:**
    - **Synchronous Counters:** All flip-flops are triggered by the same clock signal, ensuring precise timing.
    - **Asynchronous Counters:** Flip-flops are triggered sequentially, leading to potential timing delays.
    - **Upward Counters:** Increment the count value with each clock pulse.
    - **Downward Counters:** Decrement the count value with each clock pulse.
    - **Reversible Counters:** Can increment or decrement based on a control input, offering greater flexibility.

Sequential circuits are essential for designing complex digital systems that require memory and time-dependent behavior, such as processors, communication systems, and control units.