# AEC5 - Z80 Spectrum Array Comparison Template

This project is a **basic 48K Spectrum program written in Z80 assembly**, using the **Zeus assembler** with support for ULA+ graphics and profiling/debugging options.

## 📄 File Overview

- **Filename**: `NewFile`
- **Start Address**: `$8000` (Uncontended RAM)
- **Platform**: Sinclair ZX Spectrum 48K with ULA+ enabled

## 🔍 Program Purpose

This program compares two arrays of integers (`num1` and `num2`), element by element, and stores the result of each comparison in a third array `res2`.

The comparison logic:

- `1` if `num1[i] < num2[i]`
- `0` if `num1[i] == num2[i]`
- `1` if `num1[i] > num2[i]`

## 🔧 Program Flow

1. **Setup:**
    - Register `B` is initialized to 5 (number of comparisons).
    - Register `IX` is set to point to the start of `num1`.
2. **Main Loop (`bucle`):**
    - Loads current value from `num1` into `C`.
    - Loads corresponding value from `num2` into `D` (by offsetting IX by +5).
    - Calls `compara` to compare `C` and `D`.
    - Stores the result in `res2` (by offsetting IX by +10).
    - Increments `IX` to point to the next element.
    - Uses `DJNZ` to repeat 5 times.
3. **Subroutine (`compara`):**
    - Compares `D` with `C`.
    - Returns:
        - `1` if D < C
        - `0` if D == C
        - `1` if D > C
4. **End of Program (`fin`):**
    - The program halts with an infinite loop.

## 🧠 Data Section

| Label | Description | Values |
| --- | --- | --- |
| `num1` | First array to compare | `1, 1, 2, 2, 3` |
| `num2` | Second array to compare | `3, 3, 2, 2, 1` |
| `res2` | Stores comparison results | (reserved 5 bytes) |

## 💻 Emulation & Output

- Emulator is set up for **48K with ULA+**
- Profiling is enabled from `AppFirst` to `AppLast`
- Emulator registers:
    - `PC = AppEntry` (program entry point)
    - `SP = $FF40` (stack pointer)
- Output files generated:
    - `.szx` snapshot file
    - `.tzx` tape file with optional screen loading support (commented)

## 📦 File Outputs

| File | Purpose |
| --- | --- |
| `NewFile.szx` | For snapshot debugging |
| `NewFile.tzx` | Tape file for loading |
| `NewFile.scr` *(opt)* | Optional loading screen |

## 🚀 Build & Run

To assemble and run the project using Zeus:

1. Assemble the source in Zeus.
2. Load the generated `.szx` or `.tzx` in a Spectrum emulator.
3. Observe the comparison logic in action.