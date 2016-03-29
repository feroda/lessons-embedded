# Linux Command:

  - ref: http://linuxcommand.org
  - ref: guida istituto majorana
  - ref: linux facile di Daniele Medri

## Comandi emersi:

  - man: FONDAMENTALE per capire come funziona il mondo ;)
    - man -k <parola chiave>: ricerca per parola chiave
    - man man: spiega come funziona il man
  - cat
  - less e more
  - grep (con e senza |)
  - ln: hard e symlink
  - mount e umount: collegare una partizione ad una directory
  - vi e vim
  - dmesg (con il | tail)
  - tail e tail -f
  - top e htop e ps e pstree: processi attivi. I primi 2 interattivi, ps no. pstree ad albero
  - netstat: visualizza lo stato delle connessioni di rete. L'abbiamo usato per i servizi in ascolto (porta 80 http con apache e porta 22 ssh)
  - init: il primo processo utente ad essere lanciato nel root filesystem dal kernel (SystemV, Systemd, Busybox)
  - dd: copia a basso livello (a blocchi) dei file
  - mv: sposta/rinomina un file
  - cp: copiare un file
  - chown, chgrp, chmod: cambiare utenti, gruppi e permessi ai file
  - sudo: eseguire un comando da superutente
  - su: diventare superutente (consigliato "su -") oppure qualunque altro utente (ad es: "su www-data")
  - kill <PID>, killall <nome>: uccide un processo (o meglio, manda un segnale al processo di default il 15 = SIGTERM, oppure ad es: "kill -9 <PID>" = "kill -SIGKILL <PID>" o altro segnale "kill -HUP")
  - cut: prende specifici campi di un file (usalo solo su file di testo ;))
  - file: mostra il tipo di file
  - lscpu: mostra le info sul processore
  - lspci: mostra le info sul bus pci e periferiche connesse
  - lsusb: mostra le info sul bus usb e periferiche connesse
  - lsmod: mostra i moduli caricati attualmente dal kernel
  - modprobe (-r), insmod, rmmod: caricamento e scaricamento moduli con nome o con path completo
  - chroot: cambia la directory root (/) e vi esegue un comando. Di default il comando eseguito è la shell
  - editor: esegue l'editor di sistema predefinito
  - export (di bash): esporta una variabile d'ambiente nella shell corrente e shell figlie
  - set (di bash): setta un'opzione della shell corrente
  - whoami: mostra chi sono io
  - who, w: mostra gli utenti collegati ora nel sistema
  - which: mostra il path completo di un comando cercandolo nel $PATH
  - whereis: ricerca esatta del nome file senza estensione in tutto /
  - locate: ricerca una parte del nome file usando le informazioni nel database generato con updatedb
  - updatedb: aggiorna il database dei file per locate
  - find /usr/ -name "w*": cerca i file che iniziano per w a partire da  /usr . Il comando find ha tante possibilità utili. Da studiare quando servono ;)
  - head e tail: mostra intestazione e coda di file
  -

## FHS: appunti

  - /proc/<pid> info su processi
  - /proc/cpuinfo: info su cpu
  - ...
