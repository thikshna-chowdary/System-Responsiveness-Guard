#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

static int __init guard_init(void) {
    printk(KERN_INFO "System Guard Kernel Module Loaded\n");
    return 0;
}

static void __exit guard_exit(void) {
    printk(KERN_INFO "System Guard Kernel Module Unloaded\n");
}

module_init(guard_init);
module_exit(guard_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Thiksh");
MODULE_DESCRIPTION("Minimal Kernel Module for System Responsiveness Guard");
