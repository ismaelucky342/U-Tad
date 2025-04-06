# CHAPTER 4 - ARITHMETIC AND COMPUTER FUNCTIONING II

### 1. Representation Systems II and Arithmetic with Integers

The Booth multiplication algorithm for signed numbers was created by Andrew Booth in 1950. He made this observation on how human calculators worked to speed up multiplication with their mechanical devices. They used the 10's complement of the digits of the multiplier.

The algorithm uses two steps: addition and shifting, guided by four possible conditions. Let’s first look at the algorithm and then work through an example.

The algorithm works with numbers in two's complement.

1. Initialize three registers M, S, and Q with the multiplier, its two's complement, and the multiplicand.
2. Initialize register A to 0 and a one-bit register Q-1 to 0.
3. If Q0 and Q-1 are not equal (0-1, 1-0):
    - If 0,1: Add A + M and store it in A. The carry is discarded.
    - If 1,0: Add A + S and store it in A. The carry is discarded.
4. Shift A, Q, and Q-1 right by one bit (extend the sign in A).
5. If Q0 and Q-1 are equal (1-1, 0-0): Only shift A, Q, and Q-1. Return to step 3 until all bits of the original multiplier are processed. The result of the product is the concatenation of A and Q.

To summarize, the rules are:

1. Q0Q1 = 10 => Add S to A and shift.
2. Q0Q1 = 00 or 11 => Just shift.
3. Q0Q1 = 01 => Add M to A and shift.

The Booth algorithm reduces the number of additions required by eliminating the ones where the result is zero.

At this point, it is advisable for the student to practice this algorithm with an exercise where one of the operands is negative to verify that the correct sign is obtained.

On the other hand, there is the restoration division algorithm for signed integers that works with two's complement numbers.

Its algorithm is as follows:

1. Initialize two registers M and S with the divisor and its two's complement. Then initialize two registers A and Q with the dividend in two’s complement, extended to size 2n.
2. Shift A and Q one bit to the left.
3. If M and A have the same sign: Add A + S and store in A. The carry is discarded.
4. If M and A have different signs: Add A + M and store in A. The carry is discarded.
5. The operation is successful if the sign of A does not change.
    - If successful or (A = 0 and Q = 0), set Q0 = 1.
    - If not successful and (A ≠ 0 or Q ≠ 0), set Q0 = 0 and restore the previous value of A.
6. Return to step 3 until all bits of the original dividend are processed.
7. The remainder is in A.
    - If the signs of the divisor and dividend were the same, the quotient is in Q.
    - If not, the quotient is the two's complement of Q.

Before seeing an example, it is important to understand the concept of “success” used in the algorithm. A partial division is said to be successful if the sign of the accumulator register does not change.

The rules can be summarized as follows:

- Shift A and Q one bit to the left.
- If M and A have the same sign, A = A + S and ignore the carry.
- If sign(M) is not the same as sign(A), A = A + M and ignore the carry.
- The operation is successful if the sign of A does not change (act accordingly).
- If the sign of the dividend = sign of the divisor at the end => quotient = Q, otherwise quotient = two's complement of Q.

### 2. Floating Point Representation

Signed floating point numbers are represented with a sign bit, where 1 is negative and 0 is positive. The magnitudes must be presented in normalized form. The decimal point can be placed between any two bits or at one of the ends.

In normalized form, the decimal point is assumed to be to the left of the most significant bit (the leftmost one). In S-M, a magnitude is normalized if the bit accompanying the sign bit is 1.

Since the most significant bit of the magnitude must always be 1, it is never represented; it is implied. In other words, the first bit of the mantissa is suppressed, which is said to be “implicit,” gaining an extra bit of precision.

For example:
0.28125 in decimal is represented as 0 001 0010. The first 0 indicates that it is positive, the 001 is the exponent, and the 0010 corresponds to 1001 where the first 1 is considered implicit (thus not stored), and we gain more precision with an additional zero at the end.

The exponent is encoded in biased representation, also known as excess M:

- The exponent can be negative, but the sign is not encoded in any bit.
- The encoded value of the exponent is equal to the binary value plus a fixed value called the bias. A typical bias value is 2q−1−12^{q-1} - 12q−1−1. In the example, the bias for 4 is:
    - The bias allows negative exponents to be encoded. With q = 4, we can encode from 0000 to 1111 in pure binary.

The biased representation is also called excess M. For a generic value of q bits, the exponent range in biased representation is [−(2q−1−1),2q−1][- (2^{q-1} - 1), 2^{q-1}][−(2q−1−1),2q−1].

IEEE 754 is a standard for single precision floating-point representation using 32 bits. It uses 1 bit for the sign, 8 bits for the exponent, and 23 for the magnitude. The bias is 27−1=1272^{7} - 1 = 12727−1=127.

Special values are summarized as follows:

- Exponent 0 and Mantissa 0 = Number 0 (now we can represent +0 and -0).
- Exponent 255 and Mantissa 0 = + or - infinity.
- Exponent 255 and Mantissa not 0 = NaN (Not a Number).

### 3. Functions of the Computer

The structure of a software-programmable computer includes several interconnected components. The CPU (Central Processing Unit) is the core of the system and communicates with memory and input/output (I/O) devices through registers. For example, the MAR (Memory Address Register) specifies the next address to read/write in memory, while the MBR (Memory Buffer Register) stores the data to be read or written. Additionally, the CPU exchanges data with I/O devices through registers like the IOAR (I/O Address Register) and the IOBR (I/O Buffer Register).

The PC (Program Counter) is another vital component that holds the address of the next instruction to be executed. The IR (Instruction Register) stores the current instruction being executed. The system's memory is made up of a series of positions identified by addresses, where each position stores a binary value that can be interpreted as an instruction or data.

Data transfers between components are done through the system bus, which serves as a communication channel for data within the system. This bus facilitates communication between the CPU, memory, and I/O devices.

### Program Execution

A software program is executed through a process called the instruction cycle, which has two essential phases: the fetch cycle and the execute cycle. During the fetch cycle, the CPU retrieves the instruction indicated by the Program Counter (PC) from memory and stores it in the Instruction Register (IR), while the PC increments to point to the next instruction.

In the execute cycle, the CPU interprets the instruction to determine the action to take, such as transferring data between the CPU and memory or between the CPU and I/O devices, applying logical or arithmetic operations, or altering the value of the PC for the next instruction.

For example, consider a computer that handles 16-bit data and whose instruction and data format is shown in the attached image.

The following diagram summarizes the instruction cycle, showing schematically the different states that an instruction goes through, which have been discussed in the video without naming them.

Within the instruction cycle, there is an additional cycle called the interrupt cycle.

- An interrupt is a mechanism that temporarily halts the normal functioning of the CPU to handle an incident, such as an I/O operation, timing issue, hardware failure, or program error.
- I/O interrupts are the most common because I/O devices tend to operate slower than the CPU.
- It is important to avoid having the CPU wait for the I/O operation to finish before continuing with other work, as this would be inefficient.
- Interrupts allow the CPU to continue executing instructions while I/O completes its work, improving system efficiency.
- The topic of interrupts will be explored in greater detail in the Operating Systems course.

### 4. Memory Hierarchy and Cache

Modern computer systems use a memory hierarchy to balance speed, cost, and capacity. The hierarchy consists of multiple levels of memory, each with different characteristics:

1. **Registers**: The fastest and smallest memory located inside the CPU. They store data that the CPU is currently processing.
2. **Cache Memory**: A small, high-speed memory located close to the CPU. It stores frequently accessed data to reduce the time needed to access main memory.
3. **Main Memory (RAM)**: The primary memory used to store data and instructions that the CPU needs during execution. It is slower than cache but has a larger capacity.
4. **Secondary Storage**: Non-volatile storage like hard drives or SSDs, used for long-term data storage. It is much slower than RAM but offers significantly higher capacity.
5. **Tertiary Storage**: External storage devices like tapes or optical disks, used for backup and archival purposes. These are the slowest and least frequently accessed.

#### Cache Memory

Cache memory plays a critical role in improving system performance by reducing the time it takes for the CPU to access data. It operates based on the principle of locality:

- **Temporal Locality**: Recently accessed data is likely to be accessed again soon.
- **Spatial Locality**: Data located near recently accessed data is likely to be accessed soon.

Caches are organized into levels (L1, L2, L3), with L1 being the smallest and fastest, and L3 being larger but slower. Data is transferred between these levels and main memory in blocks called cache lines.

#### Cache Mapping Techniques

To determine where data is stored in the cache, different mapping techniques are used:

1. **Direct Mapping**: Each block of main memory maps to exactly one cache line. It is simple but can lead to conflicts if multiple blocks map to the same line.
2. **Associative Mapping**: A block can be placed in any cache line. This reduces conflicts but requires more complex hardware.
3. **Set-Associative Mapping**: A compromise between direct and associative mapping. The cache is divided into sets, and each block maps to a specific set but can occupy any line within that set.

#### Cache Replacement Policies

When the cache is full, a replacement policy determines which cache line to evict to make room for new data. Common policies include:

- **Least Recently Used (LRU)**: Replaces the line that has not been used for the longest time.
- **First-In-First-Out (FIFO)**: Replaces the oldest line in the cache.
- **Random Replacement**: Replaces a randomly selected line.

Understanding the memory hierarchy and cache mechanisms is essential for optimizing program performance and designing efficient computer systems.

### 5. Input/Output Systems

Input/Output (I/O) systems enable communication between the computer and external devices like keyboards, monitors, printers, and storage devices. The CPU interacts with these devices through I/O controllers, which manage data transfer and device-specific operations.

#### I/O Techniques

There are three primary techniques for performing I/O operations:

1. **Programmed I/O**: The CPU directly controls the I/O device by executing instructions. This method is simple but inefficient, as the CPU must wait for the device to complete its operation.
2. **Interrupt-Driven I/O**: The CPU initiates the I/O operation and continues executing other instructions. The device sends an interrupt signal to the CPU when it is ready, allowing the CPU to handle the I/O operation without waiting.
3. **Direct Memory Access (DMA)**: A DMA controller transfers data directly between the I/O device and memory, bypassing the CPU. This method is efficient and reduces CPU overhead.

#### I/O Addressing

I/O devices are accessed using unique addresses, similar to memory addresses. There are two main addressing methods:

- **Memory-Mapped I/O**: I/O devices share the same address space as memory. The CPU uses standard memory instructions to access devices.
- **Isolated I/O**: I/O devices have a separate address space. Special instructions are used to access devices.

Efficient I/O systems are crucial for achieving high performance in modern computers, as they minimize bottlenecks and ensure smooth data flow between the CPU, memory, and external devices.
