vm_names = ["vm{0}".format(i+1) for i in xrange(45)]


def poweron(vm_list):
        # vm_list should be of len <=20 only
    if len(vm_list) > 20:
        return
    print("Turning On the VMs: {}".format(vm_list))


def divide_the_list(vm_list, number=20):
    for i in range(0, len(vm_list), number):
        # print("i:{0},i+number:{1}".format(i, i+number))
        yield vm_list[i:i+number]


if __name__ == '__main__':
    vms_tobe_turned_on = divide_the_list(vm_names)
    # poweron(vm_names)
    for vms in vms_tobe_turned_on:
        poweron(vms)
