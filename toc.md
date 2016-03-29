
# Corso Linux Embedded

## Lezione 1 - Introduzione ai sistemi GNU/Linux su Embedded (ore 8)

* Parte I - impatto con il mondo GNU/Linux ed Embedded
  - Cosa vuol dire embedded oggi?
  - Toccare con mano l'embedded: RaspberryPi, Arduino, Beaglebone
  - Avvio di diversi sistemi GNU/Linux installati su memoria flash: OpenELEC, Raspbian
  - Il terminale: un sistema può funzionare anche senza interfaccia grafica
  - I tipi di file, i permessi, i proprietari e i gruppi
  - L'utente root e gli utenti non privilegiati
  - Creazione utenti dei corsisti su Raspbian
  - Ogni corsista:
    - Configurare una rete locale
    - Accede a Raspbian tramite accesso sicuro (ssh)
    - Si ritrova sperduto con il terminale aperto

* Parte II - Cos'è il Software libero, la storia di GNU/Linux e le distribuzioni

* Parte III - FHS, la gerarchia delle directory
 - esame del Filesystem Hierarchy Standard (FHS) e delle directory più significative
 - esempi pratici
 - navigazione della directory /dev con l'accesso ai device
 - navigazione della directory /proc con la configurazione del sistema operativo

## Lezione 2 - Installazione e configurazione di Debian GNU/Linux su PC ed embedded (ore 6)

* Installazione di una distribuzione Linux su macchina virtuale
  - Localizzazione
  - Utenti
  - Partizionamento del disco
    - RAID Software
    - Logical Volume Manager
    - filesystem: ext2, ext3, ext4, brtfs, ZFS, XFS, JFS
  - Il gestore pacchetti: mirror, selezione
* Il primo avvio
  - bootloader -> kernel -> initramfs -> rootfs -> init -> getty
  - la shell bash
  - i processi e il task manager
  - i servizi (processi demoni): ssh
* Struttura File System e comandi di base
* Comandi di base:
  - lshw, lsb_release, lspci, lscpu
  - cat /proc/cpuinfo
  - cat /proc/swaps
  - cat /proc/meminfo
  - cd, ls, echo, man
  - cat, less, head, tail, grep, find
  - nano, vim
  - chown, chmod
  - cat /etc/fstab
* Gestore Pacchetti
  - dpkg, apt-get, apt-cache
  - installare lxde, xfce4, screen, lynx
  - aptitude, synaptic
* Installazione e configurazione del server web Apache
* Installazione Raspbian Linux su HW Embedded (RaspberryPi)
* Analisi comparativa tra PC ed embedded
* Scrittura di un semplice script da shell per scrivere il carico della macchina ogni secondo su un file
* NOTA: per capire meglio i passaggi base di installazione di una distribuzione Linux installare ArchLinux

### Esercizi

- Installare Debian su PC

## Lezione 3 - Dal bootloader Raspberry a init SystemV

* La sequenza di boot del raspberry
* Init SystemV:
  - /etc/inittab
  - /etc/init.d/
  - /etc/rcS.d/
  - /etc/rc2.d/
  - /etc/rc.local
* Configurazione della rete al boot:
  - /etc/network/interfaces
  - /etc/rc.local
* man: init , runlevel, interfaces, bootparam
* Connessione di un giroscopio tramite I2C
  - caricamento dei moduli al boot
  - avvio della lettura dati e visualizzazione su console (e.g: /dev/tty8)

## Lezione 4 - Il kernel e i moduli, struttura e compilazione (7 ore)

* I ruoli del kernel, driver (moduli) e firmware
* L'albero dei sorgenti del kernel: inizializzazione, architetture e moduli
* Ricompilazione del kernel
  - .config
* Caricamento dinamico dei moduli
* Realizzazione del modulo HelloWorld
* Compilazione e caricamento

Risposte alle domande precedenti:
* Il parametro 'bs' del comando 'dd' legge al più bs BYTES
* initrd vs initramfs -> https://wiki.ubuntu.com/Initramfs

## Lezione 5 - Creare un filesystem root da 0 (7 ore)


* Alcune possibilità:
  - [Buildroot](https://buildroot.org)
  - [Deboostrap/Multistrap](https://wiki.debian.org/EmDebian/CrossDebootstrap)
  - [Ubuntu-core](https://wiki.ubuntu.com/Core)
* Guide:
  - [Linux From Scratch](http://linuxfromscratch.org) - dal silicio in su
  - [Mini guida TLDP](http://www.tldp.org/HOWTO/Bootdisk-HOWTO/buildroot.html)

* rootfs debootstrap --foreign
* rootfs buildroot crosscompilato
* Mount del root filesystem via nfs
  * il kernel deve essere abilitato con l'opzione NFSroot
  * Usare questo cmdline.txt: `dwc_otg.lpm_enable=0 console=ttyAMA0,115200 console=tty1 root=/dev/nfs rootfstype=nfs elevator=deadline fsck.repair=no rootwait ip=10.0.0.10:10.0.0.1:10.0.0.1:255.255.255.0:raspy:eth0:off nfsroot=10.0.0.1:/usr/local/buildroot/output/target`

* Personalizzazioni di base:
  - /etc/fstab
  - /etc/hosts

### Eseguire il nostro root filesystem con qemu-system-arm

* Scaricare kernel,initrd e iso da https://people.debian.org/~aurel32/qemu/armel/ e poi
  * qemu-system-arm -M versatilepb -kernel vmlinuz-3.2.0-4-versatile -initrd initrd.img-3.2.0-4-versatile -hda debian_wheezy_armel_standard.qcow2 -append "root=/dev/sda1" -m 512
* Per eseguire il nostro root filesystem creato con `debootstrap --arch=armel --foreign`:
    * qemu-system-arm -M versatilepb -kernel vmlinuz-3.2.0-4-versatile -initrd initrd.img-3.2.0-4-versatile -hda myforeignrootfs-wheezy.img -append "root=/dev/sda init=/bin/sh rw" -m 512
    * *attenzione che in questo caso root=/dev/sda senza numero di partizione perché il valore di "-hda" è in realtà una partizione e non un intero disco*
    * al prompt eseguire `debootstrap/debootstrap --second-stage`
    * una volta concluso si può eseguire il nostro sistema ARM con
    qemu-system-arm -M versatilepb -kernel vmlinuz-3.2.0-4-versatile -initrd initrd.img-3.2.0-4-versatile -hda myforeignrootfs-wheezy.img -append "root=/dev/sda" -m 512

### Creare un rootfs per Raspberry

* Seguire le informazioni qui: http://elinux.org/Raspbian
* Viene usato debootstrap con --arch=armhf --foreign e repository custom raspbian

## Lezione 6 - Sviluppo di un software di rete per recupero e visualizzazione dati (7 ore)

* Questionario di verifica

* Come possiamo esporre funzionalità all'esterno?
* Struttura di un'applicazione web
  - `web console`: un'applicazione web di esempio
  - `web gyroscope`:
* Monitorare

### Diversi web servers, differenti caratteristiche
  * apache2: il colosso, supporto estensivo e configurabilità a tutto, moltissimi moduli
  * nginx: veloce, soprattutto file statici + proxy, molto di moda
  * lighttpd: il nano, estendibile semplicemente
  * cherokee: veloce, scritto in python, ottima (ed educativa) interfaccia web di configurazione
  * Benchmark semplice: http://wiki.dreamhost.com/Web_Server_Performance_Comparison
  * Benchmark articolato (complicato): https://www.techempower.com/benchmarks/
  * Consiglio estensione Firefox Wappalyzer

### Diversi database, differenti caratteristiche
  * RDBMS:
    * sqlite3: minimale, file-based, attenzione ai lock
    * mysql/mariadb: veloce, diffusissimo, di base non un RDBMS
    * postgresql: il colosso, un framework per RDBMS, il più "pulito"
  * Database per serie temporali
    * Round Robin Database (RRD): storico molto usato http://oss.oetiker.ch/rrdtool/gallery/index.en.html
    * Whisper: evoluzione di RRD, poco usato, ma interessante la possibilità di modificare la storia
    * Influxdb: moderno, potente, linguaggio simile a SQL


* Client di rete:
  - telnet, netcat
  - curl, wget
* Python: un linguaggio semplice e flessibile
  - interrogazione di una API
  - scrittura di un file CSV
  - invio mail: con problematiche del Far West SMTP
* RDBMS SQLite: semplici e veloci archivi relazionali
  - strutturazione dei dati ricevuti
* Application server in python per visualizzare via web i risultati
