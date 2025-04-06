## Chapter 3: Arithmetic and Computer Functioning

### 1. Number Systems

Number systems are essential for representing and processing numbers in computers. The decimal system, which we commonly use, is a positional number system that employs the symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. In this system, the value of a quantity depends on the position of its symbols and the decimal point, which is conventionally placed implicitly at the far right.

For example, in the decimal system:

- 1325 = 1×10³ + 3×10² + 2×10¹ + 5×10⁰
- 1.235 = 1×10⁰ + 2×10⁻¹ + 3×10⁻² + 5×10⁻³

The binary system is the number system used internally by computers, with a base of 2. To make it easier to work with, we sometimes use octal (base 8), which represents 3 binary digits, or hexadecimal (base 16), which represents 4 binary digits.

The binary system represents quantities using the symbols 0 and 1, known as bits. Higher units above the bit are also important to understand, with 1 byte (B) being equal to 8 bits.

The octal system uses the symbols 0, 1, 2, 3, 4, 5, 6, 7, and the hexadecimal system uses 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F. As mentioned, these are often used for more convenient handling of binary data.

The Fundamental Theorem of Numeration relates a quantity expressed in any positional number system to its decimal equivalent. In summary, the theorem states that the decimal value of a quantity expressed in any positional number system can be determined by the following formula:

For example, let's consider the number 543.3 in base 6. This uses the digits 0, 1, 2, 3, 4, 5, and its decimal equivalent is:

543.3 in base 6 = 5×6² + 4×6¹ + 3×6⁰ + 3×6⁻¹ = 180 + 24 + 3 + 0.5 = 207.5 in decimal.

### 2. Conversions

To convert decimal integers to binary, the process involves dividing the decimal number by 2 repeatedly and recording the remainders. The binary number is obtained by reading the remainders in reverse order.

To convert from binary to decimal, simply sum the powers of 2 corresponding to the positions (digits) that have a 1 in the binary number. For example:

- 1101 in binary is equivalent to 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13 in decimal.

To convert from decimal to octal or hexadecimal, the method of successive division by 8 or 16 is used.

### 3. Basic Arithmetic Operations in Binary

Binary addition is similar to decimal addition, except that it only involves the digits 0 and 1. A "carry" occurs when the sum exceeds 1. The following table illustrates the basic binary addition rules:

| 0 + 0 = 0 | 0 + 1 = 1 | 1 + 0 = 1 | 1 + 1 = 10 (carry 1) |

Binary subtraction is also similar to decimal subtraction, with the key difference being that it only involves the digits 0 and 1. When subtracting, if the minuend is smaller than the subtrahend, a 1 must be borrowed from the next leftmost bit. The following table illustrates the basic binary subtraction rules:

| 0 - 0 = 0 | 1 - 0 = 1 | 1 - 1 = 0 | 0 - 1 = borrow from the left |

### 4. Other Representations

In the binary system, any number can be represented using 0s and 1s, a decimal point (or comma) for fractional numbers, and a minus sign (-) for negative numbers. However, a processor can only handle 0s and 1s. To represent other symbols like commas or signs, different encoding systems are used to store the sign and decimal point.

### Limitations of Binary Representation:

- The sign is stored separately from the magnitude, making calculations more difficult for the computer.
- There are two representations for the number 0. For example, in an 8-bit system:
    - +0 = 00000000
    - 0 = 10000000

### Advantages of This System:

- A major advantage of this binary system is its symmetric representation range.
- For example, with 8 bits, the range goes from -127 to +127, and with 16 bits, it ranges from -32767 to +32767.

Since arithmetic in computers is based on modular arithmetic, there are limitations, but it also has advantages. In modular arithmetic, subtraction and addition are the same operation if the negative numbers are represented properly. In modular arithmetic with modulus N, two numbers A and B are equivalent if: A mod N = B mod N, and this is written as (A = B) mod N. If this condition holds, there exists an integer such that A = B + KN.

### 5. Two's Complement Representation

In the Two’s Complement system, to represent signed integers, the first bit is used to encode the sign. The way the magnitude is encoded differs, and this allows for only one encoding for the number 0.

In Two’s Complement, the negative of a number is obtained by inverting all its bits (changing 0s to 1s and vice versa) and adding 1 to the result.

For example:

- Number 10 in binary (8-bit representation): 00001010
- Number -10 in Two’s Complement: 11110101

This representation has the advantage of being symmetric like Signed Magnitude (S-M) but suffers from the disadvantage of having two representations for 0 (positive 0 and negative 0).

### 6. Arithmetic in Integers and Representation Systems

### Negation:

Negating a number is essentially the process of finding its negative counterpart. In Signed Magnitude (S-M), it’s done by flipping the sign bit:

- Number 10: 00001010
- Number -10: 10001010

In One's Complement, the negation is done by flipping all the bits, including the sign bit:

- Number 10: 00001010
- Number -10: 11110101

In Two’s Complement, negation is done by first inverting all the bits and then adding 1 to the result:

- Number 10: 00001010
- Number -10 in Two’s Complement: 11110101 + 1 = 11110110

### Addition and Subtraction:

We can demonstrate that addition and subtraction can be the same operation in modular arithmetic if negative numbers are represented appropriately.

For example, consider the operation 6 - 3 using modular arithmetic (mod 16). First, find the modular 16 representation of -3:

- p = 16 - 3 = 13

Then, perform the addition modularly:

- (6 + 13) mod 16 = 19 mod 16 = 3

Thus, 13 and -3 are congruent modulo 16.

### Carry and Overflow:

In multiplication, the algorithm typically used is the sum-shift method, which involves the following steps:

1. Initialize two registers Q and M with the multiplier and multiplicand.
2. Initialize an accumulator register A to 0 and a carry bit C to 0.
3. If the least significant bit of Q (Q0) is 1:
    - Add A and M, storing the result in A. If there’s a carry, store it in C.
    - Shift all bits of C, A, and Q one position to the right.
        - C → An-1
        - A0 → Qn-1
        - Q0 is discarded.
4. If Q0 is 0, only shift the bits of C, A, and Q.
5. Repeat the process until all bits of the multiplier are processed.
The result of the product is the concatenation of registers A and Q.

### 7. Floating-Point Representation

Floating-point representation is used to handle real numbers that cannot be represented as integers. It is based on scientific notation, where a number is expressed as a mantissa and an exponent. In binary floating-point representation, the general format is:

```
(-1)^S × M × 2^E
```

Where:
- `S` is the sign bit (0 for positive, 1 for negative).
- `M` is the mantissa, representing the significant digits.
- `E` is the exponent, which determines the scale or magnitude.

#### IEEE 754 Standard

The IEEE 754 standard is widely used for floating-point arithmetic. It defines two common formats:
1. **Single Precision (32 bits):**
    - 1 bit for the sign.
    - 8 bits for the exponent (biased by 127).
    - 23 bits for the mantissa (with an implicit leading 1).

2. **Double Precision (64 bits):**
    - 1 bit for the sign.
    - 11 bits for the exponent (biased by 1023).
    - 52 bits for the mantissa (with an implicit leading 1).

#### Example of Single Precision Representation

Consider the decimal number -5.75:
1. Convert to binary: -5.75 = -101.11 in binary.
2. Normalize: -101.11 = -1.0111 × 2^2.
3. Encode:
    - Sign bit: 1 (negative).
    - Exponent: 2 + 127 = 129 = 10000001 in binary.
    - Mantissa: 01110000000000000000000 (23 bits).

The final representation is:
```
1 10000001 01110000000000000000000
```

#### Advantages of Floating-Point Representation
- Allows representation of very large and very small numbers.
- Supports a wide range of values with reasonable precision.

#### Limitations
- Precision is limited by the number of bits in the mantissa.
- Rounding errors can occur in arithmetic operations.

### 8. Error Detection and Correction

Error detection and correction are crucial in computer systems to ensure data integrity. Common methods include:

#### Parity Bits
A parity bit is added to a binary number to make the total number of 1s either even (even parity) or odd (odd parity). This helps detect single-bit errors.

#### Hamming Code
Hamming codes are used for error correction. They add redundant bits to data to detect and correct single-bit errors. For example, a 7-bit Hamming code can represent 4 data bits and 3 parity bits.

#### Checksum
A checksum is a value calculated from a data set to detect errors. It is commonly used in network communication and file storage.

#### Cyclic Redundancy Check (CRC)
CRC is a more robust error-detection method that uses polynomial division to generate a checksum. It is widely used in digital networks and storage devices.

By incorporating these techniques, computer systems can detect and correct errors, ensuring reliable data transmission and storage.
