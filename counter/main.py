import subprocess
from pathlib import Path

TOOLCHAIN_PATH = "/opt/riscv/bin/"
TOOLCHAIN_PREFIX = "riscv64-unknown-elf"
ARCH = "rv32i_zicsr"
PATTERN = "la_test1"

def compile_elf():
    cmd = [
        f"{TOOLCHAIN_PATH}{TOOLCHAIN_PREFIX}-gcc",
        "-I../", "-I../generated/", "-O0",
        "-mabi=ilp32", f"-march={ARCH}", "-D__vexriscv__",
        "-Wl,-Bstatic,-T,../sections.lds,--strip-debug",
        "-ffreestanding", "-nostdlib",
        "-o", f"{PATTERN}.elf",
        "../crt0_vex.S", "../isr.c", "../stub.c", f"{PATTERN}.c"
    ]
    subprocess.run(cmd, check=True)
    subprocess.run([
        f"{TOOLCHAIN_PATH}{TOOLCHAIN_PREFIX}-objdump", "-D", f"{PATTERN}.elf"
    ], stdout=open(f"{PATTERN}.lst", "w"), check=True)
    print("[OK] ELF gerado")

def generate_hex():
    subprocess.run([
        f"{TOOLCHAIN_PATH}{TOOLCHAIN_PREFIX}-objcopy", "-O", "verilog",
        f"{PATTERN}.elf", f"{PATTERN}.hex"
    ], check=True)

    # Corrige endereço base
    with open(f"{PATTERN}.hex", "r") as f:
        content = f.read().replace("@1000", "@0000")
    with open(f"{PATTERN}.hex", "w") as f:
        f.write(content)
    print("[OK] HEX gerado")

def flash():
    subprocess.run(["venv/bin/python3", "../util/caravel_hkflash.py", f"{PATTERN}.hex"], check=True)

def clean():
    for ext in [".elf", ".hex", ".bin", ".vvp", ".vcd", ".lst", ".hexe"]:
        Path(f"{PATTERN}{ext}").unlink(missing_ok=True)
    print("[OK] Limpeza feita")

# Você pode então criar um menu como no exemplo anterior
compile_elf()
generate_hex()
flash()
clean()