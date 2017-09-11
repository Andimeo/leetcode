def ip_2_num(ip):
    parts = ip.split('.')
    num = 0
    for part in parts:
        num = (num << 8) + int(part)
    return num


def num_2_ip(num):
    parts = []
    for i in range(4):
        parts.append(num % 256)
        num //= 256
    return '.'.join([str(x) for x in reversed(parts)])


def find(start, end, prefix, cur_bit, cidrs):
    range_start, range_end = prefix, prefix + (1 << cur_bit) - 1
    if start == range_start and end == range_end:
        cidrs.append(num_2_ip(start) + '/' + str(32 - cur_bit))
        return
    prefix += (1 << (cur_bit - 1))
    if end < prefix:
        find(start, end, range_start, cur_bit - 1, cidrs)
    elif start >= prefix:
        find(start, end, prefix, cur_bit - 1, cidrs)
    else:
        find(start, prefix - 1, range_start, cur_bit - 1, cidrs)
        find(prefix, end, prefix, cur_bit - 1, cidrs)


def ip_2_cidr(start_ip, end_ip):
    cidrs = []
    start, end = ip_2_num(start_ip), ip_2_num(end_ip)
    find(start, end, 0, 32, cidrs)
    return cidrs


print(ip_2_cidr('0.0.0.0', '0.0.0.0'))
print(ip_2_cidr('0.0.0.0', '255.255.255.255'))
print(ip_2_cidr('0.0.0.2', '0.0.1.3'))
print(ip_2_cidr('192.168.1.127', '192.168.2.129'))
