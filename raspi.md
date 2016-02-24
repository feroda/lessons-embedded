# Raspberry è "embedded"?

- Specifiche base determinate (CPU/RAM/Video non espandibili) http://elinux.org/RPi_Hardware:
  - Raspberry Pi Model A: ARM1176JZF-S 700MHz single core, 256MB RAM, Broadcom Videocore IV, 1.5W
  - Raspberry Pi Model B: ARM1176JZF-S 700MHz single core, 512MB RAM, Broadcom Videocore IV, 3.5W
  - Raspberry Pi 2: ARM Cortex-A7 900MHz quad core, 1GB RAM, Broadcom Videocore IV, 4.0W
  - Raspberry Pi 0: ARM1176JZF-S 1GHz single core, 512MB RAM, Broadcom Videocore IV, 0.8W - no usb

- Bootloader specializzato:
  * da: http://raspberrypi.stackexchange.com/questions/10489/how-does-raspberry-pi-boot
    - when the Raspberry Pi is first turned on, the ARM core is off, and the GPU core is on. At this point the SDRAM is disabled.
    - The GPU starts executing the first stage bootloader, which is stored in ROM on the SoC. The first stage bootloader reads the SD card, and loads the second stage bootloader (bootcode.bin) into the L2 cache, and runs it.
    - bootcode.bin enables SDRAM, and reads the third stage bootloader (loader.bin) from the SD card into RAM, and runs it.
    - loader.bin reads the GPU firmware (start.elf).
    - start.elf reads config.txt, cmdline.txt and kernel.img
  - guardare i file config.txt e cmdline.txt
  - ...

- General Purpose Input/Output:
  - Estensibilità e comodità http://pinout.xyz/pinout/spi
  - https://www.raspberrypi.org/documentation/usage/gpio/

# Script di avvio

  - raspi-config: eseguito al primo avvio
    * https://www.raspberrypi.org/documentation/configuration/raspi-config.md


