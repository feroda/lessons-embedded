cmd_drivers/char/examples/hello1.ko := arm-linux-gnueabihf-ld -EL -r  -T ./scripts/module-common.lds --build-id  -o drivers/char/examples/hello1.ko drivers/char/examples/hello1.o drivers/char/examples/hello1.mod.o
