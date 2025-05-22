TOOLCHAIN_PATH=/opt/riscv/bin/
TOOLCHAIN_PREFIX=riscv64-unknown-elf
ARCH=rv32i_zicsr

# ---- Test pattern for la_test1 (contador) ----

.SUFFIXES:

PATTERN = counter

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../crt0_vex.S
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=$(ARCH) -D__vexriscv__ \
		-Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib \
		-o $@ ../crt0_vex.S ../isr.c ../stub.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-objdump -D $@ > ${PATTERN}.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-objcopy -O verilog $< $@
	sed -ie 's/@1000/@0000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-objcopy -O binary $< $@

client: client.c
	python3 ./client.py

flash: ${PATTERN}.hex
	venv/bin/python3 ../util/caravel_hkflash.py ${PATTERN}.hex

flash2: ${PATTERN}.hex
	python3 ../util/caravel_flash.py ${PATTERN}.hex

show_projectid:
	python3 ../util/caravel_projectid.py

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd *.lst *.hexe

.PHONY: clean hex all flash

