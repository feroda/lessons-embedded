#include <linux/module.h>
#include <linux/fs.h>

#define HELLO_MAJOR 234

static int debug_enable = 0;
module_param(debug_enable, int, 0);
MODULE_PARM_DESC(debug_enable, "Enable module debug mode.");
struct file_operations hello_fops;

static int hello_open(struct inode *inode, struct file *file) {
      printk("hello_open: successful\n");
    return 0;
}
static int hello_release(struct inode *inode, struct file *file)
{
    printk("hello_release: successful\n");
    return 0;
}
static ssize_t hello_read(struct file *file, char *buf, size_t count,
                loff_t *ptr)
{
    printk("hello_read: returning zero bytes\n");
    return 0;
}
static ssize_t hello_write(struct file *file, const char *buf,
                size_t count, loff_t * ppos)
{
    printk("hello_read: accepting zero bytes\n");
    return 0;
}
static int hello_ioctl(struct inode *inode, struct file *file,
                unsigned int cmd, unsigned long arg)
{
    printk("hello_ioctl: cmd=%ld, arg=%ld\n", cmd, arg);
    return 0;
}

static int __init hello_init(void)
{
    /* Now print value of new module parameter */
    printk("Hello Example Init - debug mode is %s\n",
                        debug_enable ? "enabled" : "disabled");
    return 0;
}

static void __exit hello_exit(void)
{
        printk("Hello Example Exit\n");
}

module_init(hello_init);
module_exit(hello_exit);
MODULE_AUTHOR("Chris Hallinan");
MODULE_DESCRIPTION("Hello World Example");
MODULE_LICENSE("GPL");
