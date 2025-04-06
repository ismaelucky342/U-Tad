# Chapter 1 - Computer Architecture and Hardware Components

## Computer Concepts and Computer Architecture

A computer, in simplified terms, is a programmable device or machine composed of electronic circuits capable of processing information or data in digital format. This definition leads us to two main issues:

- **First:** There is a wide variety of systems that can be called computers, each with distinct characteristics.
- **Second:** The rapid advancement of computer technologies means that more advanced versions with new and improved functionalities are constantly emerging.

Computers originated from the need to automate calculation tasks and data management, with population censuses being one of the first tasks, initially using punched cards and the term "digital computer" (computador digital) in Spanish. Computer architecture is a field of knowledge that integrates the study of a system's hardware and ensures its integration with software, scalability, and abstraction to make it usable for everyday users.

# History of Computers

### The Abacus

The abacus is considered the first mechanical calculating tool, invented around 5000 B.C. It allows the execution of arithmetic operations based on a series of beads placed on wires, each representing a specific value (ones, tens, hundreds, etc.) according to their position. This is a clear implementation of a positional number system, which will be discussed in later chapters.

### The Pascaline

Created by mathematician Blaise Pascal in 1642, the Pascaline was essentially a set of gears that allowed the execution of basic arithmetic operations, working with 8 digits in decimal.

### Leibniz's Universal Calculator

Unlike the Pascaline, Leibniz's device allowed for multiplication and division by simulating the leftward movement typically done when multiplying by hand. This device was used in all calculating machines until the 1960s when electronic calculation emerged.

### Jacquard Loom

French inventor Joseph-Marie Jacquard invented an automatic loom that used punched cards. These cards were used to indicate the design pattern for fabric production, making this the first machine that could be "programmed."

### Babbage's Machine

Charles Babbage's machine was capable of constructing logarithm and trigonometric function tables. Unfortunately, it failed due to the lack of technology needed to build durable gears. However, in 1834, while working on improvements to this machine, Babbage conceived the idea for another machine: the Analytical Engine. This was essentially a general-purpose computer. Ada Lovelace, known as the "mother of programming," was one of the first to realize that the Analytical Engine could go beyond executing operations. She introduced the concept of algorithms, which could be executed by a machine. In her honor, the programming language Ada was named.

### Tabulating Machine

Herman Hollerith designed a punched card system to assist in calculating the 1890 United States census. The machine saved the government several years of calculations and about 5 million dollars, according to Columbia University.

# Historical Computers

### Turing Machine

Alan Turing was a British mathematician often regarded as one of the fathers of computer science, laying the foundations for modern computing. He worked on deciphering Nazi codes and participated in the creation of the Bombe machine. After the war, he worked on the design of the first electronic computers. The Turing Machine is a device that can simulate the logic of any computer algorithm. Turing's design involved a device capable of reading a tape with a series of symbols, which it would process according to a set of rules.

### Von Neumann Architecture

John Von Neumann, a Hungarian-American mathematician and physicist, participated as an advisor in the creation of ENIAC. He introduced a design that would improve the slow programming of ENIAC with the "stored-program concept." He developed an architecture that we will discuss below, first implemented in a machine called EDVAC. Unlike ENIAC, which operated in base 10, EDVAC used base 2. This design became the standard architecture for most modern computers. The basic components of Von Neumann's architecture are: the Arithmetic Logic Unit (ALU), the Control Unit (CU), Memory, and the Input/Output unit.

# Generations of Computers

### First Generation (1940-1952)

- **Main Characteristics:** They used vacuum tubes, consumed a lot of energy, were large in size, and used punched cards and magnetic tapes. They were programmable only in specific machine language.
- **Representative Computers:** Univac I and II, IBM 701 and 702.

### Second Generation (1952-1964)

- **Main Characteristics:** Vacuum tubes were replaced by transistors, which were smaller, cheaper, more energy-efficient, and more reliable. High-level programming languages and system software were introduced.
- **Representative Computer:** IBM 7094 (1964).

### Third Generation (1964-1971)

- **Main Characteristics:** The use of microelectronics and integrated circuits led to lower costs and greater energy efficiency. Components such as logic gates, memory cells, and interconnection circuits appeared.
- **Representative Computers:** IBM 360, DEC PDP-8.

### Fourth Generation (1971-1981)

- **Main Characteristics:** Advances in microelectronics with varying levels of integration (SSI, MSI, LSI, VLSI, ULSI, GLSI) paved the way for personal computers.
- **Representative Computers:** MITS Altair, Apple I (1976), Apple II (1977), IBM PC (1981).

### Fifth Generation (1981-present)

- **Main Characteristics:** Development of 16 and 32-bit processors. Advancements in microcomputing. More advanced fifth-generation devices, aimed at artificial intelligence, are still under development. There is mention of a potential sixth generation involving quantum computing and molecular nanotechnology.
- **Representative Computers:** Any current computers.

# Levels of Abstraction

### PHYSICAL LEVEL

This is the most basic level, which is primarily concerned with physics, particularly the study of electron behavior. At this level, the input element is the semiconductor called silicon. In the future, other materials such as graphene are being considered for replacement. As a semiconductor, it allows electricity to pass through, but unlike metals, it enables easy control of electron flow. By modifying its electron conduction properties, we obtain components like resistors, transistors, and diodes (output elements of this level).

### ELECTRONIC LEVEL

At this level, we use elements from the previous level, such as resistors and transistors, and the output elements are bistable devices and logic gates. Further details of these elements will be discussed in subsequent units.

## Logical Level

The input elements at this level are bistable devices and logic gates, while the output elements are combinational and sequential modules such as multiplexers, encoders, adders, registers, counters, etc. Similar to the previous level, we will explore these components in more detail in later chapters. Examples of logical circuits include:

### Register Transfer Level (RTL)

The input elements at the RTL level are:

- **Registers**: These maintain the system's state.
- **Combinational Modules**: These define the elementary transformations of the state.
- **Interconnection Elements** (buses and/or multiplexers): These enable the exchange of information between the previous two elements.

The output elements are the set of elementary transfers possible within the data path constructed with these three types of input elements.

### Architecture Level (LM)

This level defines the boundary between software and hardware. The input elements are the transformations and transfers of information, which are mapped with machine instructions and their sequencing method, forming the machine language.

The machine language level is typically the first level that the user directly interacts with a computer. Normally, users do not use machine language directly, but instead, they use an assembler representation, which provides more functionality than raw machine language. We will practice with this language in later chapters.

This level is defined by the repertoire of instructions, with their formats, addressing modes, sequencing methods, and data representation. Additionally, memory management and the set of registers visible to the programmer are critical elements.

In modern computers, these resources are utilized by the user program via the operating system. Two distinct approaches define the machine language level:

1. **CISC (Complex Instruction Set Computers)**: This approach defines a complex and extensive instruction set, with many addressing modes and control mechanisms. Its goal is to reduce the semantic gap between machine language and high-level languages, thus simplifying the compiler design.
2. **RISC (Reduced Instruction Set Computers)**: This approach simplifies the machine instruction set, reducing it to a small, fast set of instructions that cover most computational needs. In RISC systems, compilers are responsible for using efficient instructions with less semantic content but high execution speed.

In modern architectures, memory management and I/O are managed by the operating system, and the architecture, such as Intel's x86, is defined by a set of instructions and registers for programmers. Microarchitecture combines logical elements to execute these instructions, with different microarchitectures implementing the same architecture with variations in price, performance, and energy consumption, as seen in processors like Intel Core i7 and AMD Athlon.

### Basic Software Level (SO)

The Operating System (OS) is not a level like machine language or high-level language; it is more of a manager for certain machine-level resources that are more efficiently used as a "unit" providing these services. In early computers, the OS's functions were limited to loading programs and managing input/output. However, with the increasing complexity of modern machines, the OS's role has expanded to managing multi-user and multitasking environments, handling all of the machine's resources.

### High-Level Programming Languages

At this level, we deal with imperative languages like Pascal, Fortran, etc., which present an operational semantics reflecting the Von Neumann machine model. These languages require the programmer to specify the sequence of operations that will solve the problem.

Other paradigms, such as declarative programming languages like Prolog or Lisp (pure), provide a different but equivalent computational model to the Von Neumann machine. In these languages, the programmer only needs to declare the logical or functional relationships of the elements involved in the problem.

This level requires translation into machine language, typically done by a program called a compiler. This process involves turning the high-level code into instructions that the machine can execute.

### Algorithms Level

This level deals with problem-solving using a set of rules applied systematically and in order—i.e., an algorithm. The procedures defined by an algorithm are independent of any programming language or specific machine.

### Applications Level

This is the highest level, corresponding to various activities, needs, or problems that can be automated. From the analysis of functional specifications, technical designs are created based on algorithms that represent the output of the previous level.

---

**7. Operation of Modern Computers**
When a computer starts up, actions occur at the hardware level, accessing ROM or flash memories via wired circuits. The startup program, like BIOS/UEFI in PCs, detects devices and performs basic checks. Then, it loads the operating system's programs into the RAM from an external medium (like a hard drive).

At the system level, the operating system controls operations and presents the user with an interface (e.g., prompt in Linux or desktop in other systems). The user gives commands through the prompt, starting the processing of instructions at high speed, with pauses for interactivity if needed, and finally, the computer presents the results on the screen or other peripherals.

Each instruction in a program has a unique binary code interpreted by the computer's CPU. The CPU processes instructions automatically, performing data transfers, arithmetic, and logical operations. The computer interprets 1's and 0's as voltage levels in its circuits, where 0 represents a low voltage (near 0 volts) and 1 represents a high voltage (near 5 volts). By applying high or low voltages to logic gates in the digital circuits, the behavior is determined, either opening or closing circuits. The program executes by rapidly switching circuits on and off in sync, transferring information between the computer's units.

**Basic Operation of a Computer:**

1. The Control Unit accesses the memory address where the next instruction to execute is stored, using the program counter (PC).
2. The Control Unit fetches the instruction and decodes it. If the instruction involves operands, it requests them from memory.
3. The Control Unit sends the operands (if any) and the instruction to the Arithmetic Logic Unit (ALU). The instruction is executed, and the result is stored in memory or a register if necessary.
4. Once the instruction is executed, the program counter increments, and the process starts again from step 1.

### Essential Components

### The Motherboard

The motherboard is the central integrator of the PC. It is a large printed circuit board that connects the various components of the computer. Its elements include:

- **BIOS (Basic Input-Output System)**: This is a software of specific purpose that is executed first when the computer starts. It is stored in an EEPROM (Electrically Erasable Programmable Read-Only Memory). This type of memory is read-only but can be reprogrammed to make changes to the BIOS. The correct BIOS software is provided by the motherboard manufacturer. Functions include:
    1. When the PC starts, the CPU points to the BIOS memory address.
    2. Stores the entire system boot configuration.
    3. Configures the input/output devices connected to the motherboard.
    4. Configures the system clock.
- **CMOS Battery**: The CMOS battery provides electrical power to the motherboard's clock.
- **Microprocessor Sockets**: The socket is where the microprocessor is inserted. Each socket supports a range of processors, so choosing the correct socket for the desired processor is essential.
- **RAM Slots**: These are specific slots where the RAM modules are connected, differing based on the type of RAM supported.
- **Expansion Bays**: Slots for adding additional functionality to the motherboard by connecting input/output devices. These are typically used for installing graphics, sound, network cards, etc.
- **IDE/ADA/SATA Connectors**: These connectors are for cables connecting hard drives and optical drives (Blu-ray, DVD, CD, card readers). Some motherboards still include these for backward compatibility, though newer motherboards use faster connectors.

### The Chipset

The chipset is a set of chips integrated into the motherboard to control the microprocessor and other motherboard elements. It used to consist of two chips: Northbridge and Southbridge (Intel's series 4).

- **Northbridge**: It controls the microprocessor, RAM, and expansion bays.
- **Southbridge**: It controls lighter operations like USB, audio, serial ports, BIOS, ATA ports, and the system clock.

This setup had a limitation in the **Front-Side Bus (FSB)**, where a bottleneck would occur as the CPU's speed increased while the FSB remained the same. To solve this problem, Intel designed the **Platform Controller Hub (PCH)** architecture:

- The Northbridge and Southbridge are eliminated.
- The control of memory and PCI is reassigned to the CPU.
- Other functions are concentrated in the PCH.
- The PCH and CPU are connected via the **Direct Media Interface (DMI)**.
- This architecture has been present in Intel chipsets since the **5 series (2008)**.

Currently, Intel’s microprocessor connections use DMI, and additional functionalities have been included:

- **Turbo Boost**: This feature controls the microprocessor’s temperature, allowing temporary performance increases by boosting the clock speed while managing heat dissipation.
- **Cache Memory**: L1 and L2 caches are specific to each core, while L3 is shared among all cores.
- **Integrated Graphics**: Typically the 630, with 620 found in low-power laptop processors.

### RAM (Random Access Memory)

RAM plays a crucial role in computers by temporarily storing instructions and data required to run programs. Key features include:

- **Temporary Storage**: It stores data and instructions temporarily and is volatile, meaning its contents are erased when the computer is powered off.
- **Connected to the Northbridge** via the Memory Bus or directly to the CPU in PCH-based systems. The capacity of RAM is limited by:
    - The microprocessor's addressing capabilities (32-bit: 4 GB, 64-bit: 16 exabytes).
    - The chipset's limitations.
    - The number of slots and the maximum size of RAM modules supported by the motherboard.

### Types of RAM:

- **SRAM (Static RAM)**: Does not need refreshing, faster and more expensive. It is used in cache memory.
- **DRAM (Dynamic RAM)**: Slower but cheaper and higher capacity, used as primary memory.
- **DDR (Double Data Rate)**: A technology that allows simultaneous data transfer on both the rising and falling edges of a clock cycle. DDR has evolved from DDR1 to DDR6, improving speed and capacity.

### ROM (Read-Only Memory)

ROM is fundamental in computing systems because of its characteristics:

- **Non-Volatile**: Can retain information without power.
- **Slower than RAM**: Access times are higher.

**Types of ROM**:

- **ROM**: Read-only memory, immutable content, designed for specific-purpose equipment.
- **PROM (Programmable ROM)**: Programmable once.
- **EPROM (Erasable Programmable ROM)**: Can be erased via ultraviolet light and reprogrammed.
- **EEPROM (Electrically Erasable Programmable ROM)**: More flexible ROM that can be erased and modified electrically via software. This is used to store the BIOS.

### Hard Disk

Every computer needs non-volatile storage for data and programs. Early storage devices included magnetic tapes, and later, spinning disk drives became the standard for secondary storage for over half a century. In the 1980s, magnetic disks began to enter homes, and devices like the ZX Spectrum used cassettes. Today, solid-state drives (SSDs) have largely replaced magnetic disks in personal computers, though magnetic disks are still used in data centers and for massive, cost-effective secondary storage.

**Magnetic Hard Drives**:

- **Composition**: Consist of several stacked magnetic disks connected by a central axis.
- **Structure**: Two high-precision read/write heads are used between the disks.
- **Fragmentation Problem**: Non-contiguous storage creates gaps between written zones, solved by defragmentation.
- **Rotation**: The central axis rotates to allow the heads to float above the disk surface.
- **Recording Density**: Measures the number of bits per inch (BPI), tracks per inch (TPI), and bits per sector inch (BPSI), which determines the amount of data on a surface.

**Solid-State Drives (SSD)**:

- **Definition**: Storage devices that use non-volatile memory (flash) rather than magnetic disks.
- **Advantages**:
    - No mechanical parts, leading to faster boot times, higher read/write speeds, lower latency, less energy consumption, no noise, and reduced weight and size.
    - More resistant to shocks.
    - Constant performance without degradation (no fragmentation).
- **Disadvantages**:
    - Higher cost (though prices are becoming comparable).
    - Lower data recovery capacity and shorter lifespan.

### Microprocessor

The microprocessor is both the brain and heart of the PC. It has undergone significant evolution in terms of power dissipation and technical characteristics. Early microprocessors did not require heat dissipation systems, but now, powerful models demand cooling solutions, including fans and liquid cooling systems, with power requirements ranging from 100W to 300W.

The **clock frequency**, limited by the time it takes to charge and discharge the transistors' gate capacitance, currently peaks at 4 GHz. The power supply voltage has decreased to reduce heat dissipation, from 5V to 2.5V and even 1V. Static power, related to leakage currents, can account for up to 40% of total power consumption in modern processors. Additionally, the manufacturing process reached 5 nanometers by 2022, with expectations to reach 2 nm by 2023.

### Processor Limits

To increase performance, multiple techniques are used, including parallel processing, embedding multiple cores in one chip, and even cloning internal blocks (ALUs, control units, etc.). This is part of more complex architectures, such as multiple cores, multithreading, parallel execution, speculative execution, multi-level caches, data paths, etc.

### Moore's Law

Gordon Moore, co-founder of Fairchild (the first monolithic integrated circuits) and Intel, observed in 1975 that the number of transistors in an integrated circuit doubles every two years. This became known as **Moore's Law**. However, Moore himself and others predicted around 2007 that this law would stop being true around 2025 due to power dissipation limitations in chips. By 2010, Intel's former CEO stated that the rate of growth would slow to two and a half years.

### Graphics Cards

The **GPU** is hardware responsible for generating the signals needed to control and properly display an image on the screen, just as important as the monitor itself. Many microprocessors include integrated GPUs (e.g., Intel 620, 630), but for more powerful graphics (e.g., for video games, graphic design, 3D modeling), an external GPU (e.g., NVIDIA) is necessary. GPUs are now used in supercomputers and data mining (Bitcoin, Ethereum, etc.).

### Other Components:

- **Power Supply**: Responsible for supplying power to the motherboard and connected devices.
- **Fan**: Primarily cools the microprocessor. More efficient cooling mechanisms like liquid cooling can be used as well.
- **Heat Sinks**: These conduct and dissipate the heat generated by processors to prevent overheating.

# **Boolean Algebra**

A Boolean Algebra (B) is a finite set with two binary operations: Sum (+) and multiplication (.) that satisfy the following rules:

- For every Boolean variable x (which can take two values), the following is true:
    - x = 1 or x = 0
    - There exists a complement or negation operation (NOT):
        - NOT(0) = 1
        - NOT(1) = 0
- There exists a logical AND operation (product):
    - 0 . 0 = 0
    - 0 . 1 = 0
    - 1 . 0 = 0
    - 1 . 1 = 1
        
        *(Note: You can replace the `.` operator with the logical AND function for better understanding.)*
        
- There exists a logical OR operation (sum):
    - 0 + 0 = 0
    - 0 + 1 = 1
    - 1 + 0 = 1
    - 1 + 1 = 1
        
        *(Note: You can replace the `+` operator with the logical OR function for better understanding.)*
        

By convention, the AND operation has higher precedence than the OR function.

### Postulate 1: Internal Composition Laws

This means that for all a and b belonging to the set B, the result of a + b or a . b also belongs to the set B. Mathematically, this is expressed as:

### Postulate 2: Identity Element

All operations have an identity element.

### Postulate 3: Inverse Element

For every element in B, there exists an inverse or opposite element.

### Postulate 4: Commutative Property

The operations satisfy the commutative property.

- For the AND operation: a . b = b . a
- For the OR operation: a + b = b + a

### Postulate 5: Distributive Property

The operations satisfy the distributive property.

- The AND operation distributes over the OR operation: a . (b + c) = (a . b) + (a . c)
- The OR operation distributes over the AND operation: a + (b . c) = (a + b) . (a + c)

### General Properties

Any digital system can be represented in various forms:

- **Formulas** as we have seen earlier. For example: f(x) = x . y.
- **Truth tables**: These show what happens at the output of the digital system based on the input variable values.
    
    For example, the truth table of the function f(x) = x . y:
    

Any Boolean function can be explicitly defined using a truth table, and any truth table has its corresponding Boolean function. These functions can be implemented using logic circuits made from logic gates. Remember that a logic gate is the fundamental building block of digital circuits. Logical operations can be implemented through logic gates, which have input and output signals corresponding to the variables and outputs of the logical operations they perform.