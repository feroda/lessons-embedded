# Il kernel

  - sito di riferimento: www.kernel.org -> git.kernel.org
  - sorgente del kernel ufficiale: https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/
  - Il tree dei sorgenti (con hyperlinks su http://lxr.free-electrons.com/)
    - **Documentation/**: don't miss this! Può salvarti la vita ;)
        * Documentation/kbuild/makefiles.txt: come scrivere i Makefile del kernel
        * Documentation/kbuild/kconfig-language.txt
    - **drivers/** : i driver
    - **arch/**: le architetture
    - **init/main.c**: `try_to_run_init_process` per l'esecuzione del processo init (PID 1)

# Compilazione del kernel
    * make defconfig
    * .config

# Crosscompilazione del kernel
  - Toolchain: compiler, linker, libraries, debugger
    - crosscompilare un sorgente per ARM:
        * da: gcc -o hello hello.c
        * a: gcc-arm-linux-gnueabi-gcc -o hello hello.c
    - Toolchain arm: arm-linux-gnueabi-gcc
  - Build del kernel raspberry
    * https://www.raspberrypi.org/documentation/linux/kernel/building.md
        * make -j2 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcmrpi_defconfig
        * make -j2 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
        * sudo mount /dev/sdc2 /mnt/
        * sudo mount /dev/sdc1 /mnt/boot/
        * sudo make -j2 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=/mnt/ modules_install
        * sudo cp /mnt/boot/kernel.img /mnt/boot/kernel-backup.img
        * sudo scripts/mkknlimg arch/arm/boot/zImage /mnt/boot/kernel.img
        * sudo cp arch/arm/boot/dts/*.dtb /mnt/boot/
        * sudo cp arch/arm/boot/dts/overlays/*.dtb* /mnt/boot/overlays/
        * sudo umount /mnt/boot
        * sudo umount /mnt

# ARM
  - Linux su ARM: https://wiki.linaro.org/FrontPage


