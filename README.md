# ChipIgnite Counter Test Guide

This guide provides step-by-step instructions for testing your **Caravel ChipIgnite** chip using a counter module. The process includes visuals sourced from the official Efabless repositories to make each step easier to follow.

---

## 1. Clone the RISC-V GNU Toolchain Repository

To begin, you'll need to download the RISC-V toolchain:

➡️ [riscv-gnu-toolchain GitHub Repository](https://github.com/riscv-collab/riscv-gnu-toolchain/tree/master)

![Repository Screenshot](https://github.com/user-attachments/assets/597a7a8c-e34d-490a-879f-33604566112c)

---

## 2. Install Prerequisites

Install the required dependencies based on your operating system. Refer to the image below for guidance:

![Install Dependencies](https://github.com/user-attachments/assets/fad8ec0d-8645-4949-a0a7-10e923cedaba)

---

## 3. Set Up the RISC-V Toolchain Path

Before installing the compiler, ensure the following directory is included in your system `PATH`:

```
/opt/riscv/bin
```

For Linux users:

1. Open your `.bashrc` file using your preferred text editor (e.g., `nano`, `vim`):

    ```bash
    nano ~/.bashrc
    ```

2. Add the following line at the end of the file:

    ```bash
    export PATH="$PATH:/opt/riscv/bin"
    ```

3. Save and close the file. Then, apply the changes:

    ```bash
    source ~/.bashrc
    ```

---

## 4. Build the Compiler

Once you're inside the cloned `riscv-gnu-toolchain` folder, run the following command to build the compiler (maybe you will need to use sudo before make):

![Build Compiler](https://github.com/user-attachments/assets/0648ebd2-b563-4dd8-9d4f-d32e3be35101)

---

Clone this repository by runing:

```
git clone https://github.com/Iranildot/chipignite-counter-test.git
```

Go inside counter folder.

open a terminal

Create a virtual environment

```
python3 -m venv venv
```

activate virtual environment

```
source ./venv/bin/activate
```

install pyftdi

```
pip3 install pyftdi
```

Now you can run the following to compile your code:

```
make clean flash
```

OBS.: Maybe you need to push the reset button down before conecting your testing board to the computer then keep holding it down until you run ```make clean flash```
