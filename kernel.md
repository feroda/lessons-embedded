
# Partiamo da una connessione seriale
  * Il connettore FTDI
  * Avviare il raspberry e vedere la console su seriale tramite gtkterm
  * Vedere i moduli del kernel che consentono la connessione
  * modprobe e creazione del device

  ![il sistema operativo](./UserSpaceSyscallKernel.png "User space e syscall del kernel")

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
  - La mappa: http://www.makelinux.net/kernel_map/

## La via comoda
  * Le distribuzioni forniscono immagini del kernel precompilate, ma ... generiche
  * Gli sviluppatori pubblicano i propri pacchetti kernel da installare
  * Le distribuzioni hanno il proprio sistema di build per creare il kernel della loro distribuzione

## La via dell'illuminazione: http://www.kernel.org

### Configurazione del kernel
  * .config -> quante opzioni di configurazione ci sono nel kernel?
  * make defconfig
  * make menuconfig o make nconfig o make gconfig o make xconfig

### [Compilazione del kernel](https://wiki.archlinux.org/index.php/Kernels/Compilation/Traditional#Compile)
  * make -j2 bzImage modules
  * make modules_install
  * cp -v arch/x86/boot/bzImage /boot/vmlinuz-YourKernelName
  * mkinitcpio -k FullKernelName -c /etc/mkinitcpio.conf -g /boot/initramfs-YourKernelName.img
  * consentire al bootloader di caricare il kernel

### Integrare un proprio modulo nel kernel
  * Creare una directory (i.e: drivers/char/examples)
  * Creare il modulo `hello.c`
  * Estendere `Makefile` e `Kconfig` della parent directory (i.e: drivers/char/)
  * Creare i propri `Makefile` e `Kconfig`
  * Compilare con `make M=drivers/char/examples`
  * Inserire il modulo con `insmod` e toglierlo con `rmmod`
  * Copiarlo nella directory di default di tutti i moduli
  * Usare `modprobe` e `modprobe -r`
  * Per allocare MAJOR number leggere `Documentation/devices.txt`

## [Crosscompilazione del kernel raspberry](https://www.raspberrypi.org/documentation/linux/kernel/building.md)
  - [Ottieni la toolchain: compiler, linker, libraries, debugger](https://github.com/raspberrypi/tools)
    - Con questa puoi crosscompilare un sorgente per ARM:
        * da: gcc -o hello hello.c -> a: arm-linux-gnueabihf-gcc -o hello hello.c
        * qemu-arm -L /opt/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/arm-linux-gnueabihf/libc/ hello
  - [Ottieni il kernel](https://github.com/raspberrypi/linux)
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

### Linaro: un buon riferimento per ARM
  - Linux su ARM: https://wiki.linaro.org/FrontPage
