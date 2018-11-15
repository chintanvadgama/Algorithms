# aaabbb a3b3

def compress_string(data):
    if not data or len(data) ==1:
        return data
    if len(set(data)) == len(data):
        return data
    output = ''
    count = 1

    for i in range(len(data)-1):
        # print 'data[%s] = %s, data[%s] = %s' % (i,data[i],i+1,data[i+1])
        if data[i] == data[i+1]:
            count += 1
        else:
            output = output + data[i] + str(count)
            count = 1
    output = output + data[len(data)-1] + str(count)
    return output






if __name__ == '__main__':
    data = b'aaabbb'
    data2 = b'aaabbbccccccc'
    data3 = b'abbbcdefgh'

    print compress_string(data2)
    print compress_string(data)
    print compress_string(data3)