# ChipIgnite Counter Test

This repository will give you the step by step to test your caravel chipignite chip with a counter.

The following images will guide you through process and come from main source (Efabless repositories).

First of all, you need to download the following repository:

Click this link to get there: https://github.com/riscv-collab/riscv-gnu-toolchain/tree/master

![image](https://github.com/user-attachments/assets/597a7a8c-e34d-490a-879f-33604566112c)

Then install prerequisits based on your Operating System:

![image](https://github.com/user-attachments/assets/fad8ec0d-8645-4949-a0a7-10e923cedaba)

Before installing compiler you need to put this into your path: ```/opt/riscv/bin```. If you are a linux like you can do the following step.

Open .bashrc file using your prefered text editor (nano, vim, stc.):

```
nano ~/.bashrc
```

At the end of .bashrc file put:

```
export PATH="$PATH:/opt/riscv/bin"
```

then save the file.

And to get the compiler run the following (you must be inside riscv-gnu-toolchain folder):

![get_compiler](https://github.com/user-attachments/assets/0648ebd2-b563-4dd8-9d4f-d32e3be35101)
