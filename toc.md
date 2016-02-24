
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




## Lezione 4 - Sviluppo di un software di rete per recupero e visualizzazione dati (7 ore)

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

## Lezione 4 - Il kernel e i moduli, struttura e compilazione (7 ore)

* I ruoli del kernel, driver (moduli) e firmware
* L'albero dei sorgenti del kernel: inizializzazione, architetture e moduli
* Ricompilazione del kernel
* Caricamento dinamico dei moduli
* Realizzazione del modulo HelloWorld
* Compilazione e caricamento

## Lezione 5 - Buildroot: la creazione di un filesystem da 0 (7 ore)

* La mia architettura e la crosscompilazione
* Il mio kernel
* BusyBox e le mie applicazioni di base
* Init BusyBox o SystemV
* I miei script di init
* Preparazione dell'immagine e scrittura su SD

## Lezione 6 - debug, sviluppo in team e consigli pratici (6 ore)

[NOTA: è probabile che dovremo recuperare altre lezioni]

* Tool di debug: gdb, strace, mtrace, ...
* Git e workflow di programmazione
* GITHub, Bitbucket, Gitlab, Gogs per gestire lo sviluppo in un team

* Questionario di verifica
