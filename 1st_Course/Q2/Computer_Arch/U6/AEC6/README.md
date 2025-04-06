# AEC6 - ArrayParityCheck in ZX Spectrum 48K Assembly

This is a basic Z80 assembly program for the ZX Spectrum 48K, written using the **Zeus Assembler**. It copies two arrays (`NUM1` and `NUM2`) into memory and then checks the **parity (odd/even)** of the sum of each pair of elements.

---

## 📄 Program Overview

The program does the following:

1. **Copies** two arrays (`NUM1` and `NUM2`) into memory starting from address `$8100`.
2. **Adds** corresponding elements from both arrays.
3. **Stores** the **parity** (0 = even, 1 = odd) of each sum into a result array starting at `$8110`.

The program then halts, making it easy to inspect memory contents via an emulator or debugger.

---

## 🧠 Logic Breakdown

- `NUM1` and `NUM2` each contain **7 elements**.
- The data is copied into memory using a loop in `COPIAR_NUMEROS`.
- The `CALCULAIMPAR` routine:
    - Adds corresponding elements from `NUM1` and `NUM2`.
    - Masks the least significant bit to determine parity (`AND 01H`).
    - Stores the result (0 or 1) into the result array.

---

## 🛠️ Technical Details

- **Start address:** `$8000` (defined by `AppFirst`)
- **Execution entry point:** `AppEntry`
- **Emulation model:** `48K` with `ULA+` enabled
- **Stack pointer:** `$FF40`
- **Code ends at:** `AppLast`

---

## 📦 Output Files

- `NewFile.szx`: Snapshot file for debugging with an emulator.
- `NewFile.tzx`: Tape file for loading the program on real or emulated hardware.

Optional:

- A `.scr` screen can be loaded for a visual loader (commented out in this version).

---

## 🧪 Example Arrays

```
asm
CopyEdit
NUM1: DB 7, 4, 2, 10, 4, 1, 7
NUM2: DB 5, 6, 9, 10, 1, 0, 4

```

**Sum results** (before parity):

```
CopyEdit
12, 10, 11, 20, 5, 1, 11

```

**Parity values** (stored in memory starting at `$8110`):

```
CopyEdit
0, 0, 1, 0, 1, 1, 1

```

---

## 🧰 Development Notes

- The code is **fully profiled**, allowing you to measure execution time using `Zeus`.
- The project is ready for testing with breakpoints or visual inspection in emulators like **Fuse** or **Spectaculator**.