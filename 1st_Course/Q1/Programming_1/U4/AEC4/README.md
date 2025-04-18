# AEC4 - Magic Number

This C program prompts the user for a **valid birth date** and calculates their **magic number**, a single-digit number obtained by summing all the digits of the date until it is reduced to one digit.

---

### 📂 Project Contents

- Interactive date validation (day, month, year)
- Calculation of the magic number associated with the date
- Use of prototyped functions
- Input buffer cleaning to avoid errors

---

### 🛠️ How does it work?

### `main()`

1. Prompts the user to enter their birth date.
2. Validates that the day, month, and year are correct.
3. Displays the entered date in the format `dd/mm/yyyy`.
4. Calculates and displays the corresponding **magic number**.

### `void leeFechaCorrecta(int *dia, int *mes, int *year)`

- Ensures that:
    - The **year** is greater than 0.
    - The **month** is between 1 and 12.
    - The **day** is valid for that month (leap years are not considered in this example).
- Cleans the input buffer (`while (getchar() != '\n')`) if the user enters a non-numeric value.

### `int calculaNumeroMagico(int dia, int mes, int year)`

- Sums the numeric values of `day`, `month`, and `year`.
- Repeats the digit-summing process until a **single digit** (between 1 and 9) is obtained.

---

### 🧪 Execution Example

```
yaml

Enter your Birth Date.
year: 2000
month: 12
day: 15
Your Birth Date is: 15/12/2000
The magic number associated with your birth date is: 2
```

---

### 📌 Author Notes

- A separate function for buffer cleaning was omitted as it was concisely handled with `while (getchar() != '\n');` directly in the validation.
- Leap years are not included for simplicity (February always has 28 days).
- Code is divided into functions to maintain clarity and facilitate maintenance.
