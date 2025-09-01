# 🔧 ChipIgnite Counter Test Guide


This guide provides step-by-step instructions for testing your Caravel ChipIgnite chip using a simple counter module. The images and procedures are based on official documentation from Efabless and the RISC-V Collaboration.
The firmware used in this repository was slightly adapted from caravel_user_project/verilog/dv/io_ports/io_ports.c to test the chip.


## 📦 1. Clone the RISC-V GNU Toolchain Repository

Start by cloning the official RISC-V GNU Toolchain repository:

👉 [riscv-gnu-toolchain on GitHub](https://github.com/riscv-collab/riscv-gnu-toolchain/tree/master)

![Repository Screenshot](https://github.com/user-attachments/assets/597a7a8c-e34d-490a-879f-33604566112c)

---

## ⚙️ 2. Install Prerequisites

Install the required packages based on your operating system. Refer to the image below for guidance:

![Install Dependencies](https://github.com/user-attachments/assets/fad8ec0d-8645-4949-a0a7-10e923cedaba)

---

## 🛠️ 3. Set Up the RISC-V Toolchain Path

Before building the toolchain, make sure to add the following path to your environment:

```
/opt/riscv/bin
```

### On Linux

1. Open your `.bashrc` file:

    ```bash
    nano ~/.bashrc
    ```

2. Add the following line to the end of the file:

    ```bash
    export PATH="$PATH:/opt/riscv/bin"
    ```

3. Save and apply the changes:

    ```bash
    source ~/.bashrc
    ```

---

## 🧱 4. Build the RISC-V Compiler

Navigate into the cloned `riscv-gnu-toolchain` directory and run:

```bash
./configure --prefix=/opt/riscv
sudo make
```

> 💡 You might need to prefix the command with `sudo` depending on your system permissions.

![Build Compiler](https://github.com/user-attachments/assets/0648ebd2-b563-4dd8-9d4f-d32e3be35101)

---

## 🧪 5. Set Up the Counter Test Project

Clone the test project repository:

```bash
git clone https://github.com/Iranildot/chipignite-counter-test.git
cd chipignite-counter-test/counter
```

---

## 🐍 6. Set Up Python Environment

Open a terminal and run the following:

### Create a Virtual Environment

```bash
python3 -m venv venv
```

### Activate the Environment

```bash
source ./venv/bin/activate
```

### Install Required Python Package

```bash
pip3 install pyftdi
```

---

## 🚀 7. Compile and Flash the Project

To build and flash your code onto the chip:

```bash
make clean flash
```

> ⚠️ **Important:** You may need to press and hold the **reset button** on your board **before connecting it to your computer**, and continue holding it until the `make clean flash` command starts.

---

✅ You're now ready to run your counter test with ChipIgnite!

