


def main():
    file = open("out_uid.txt",'r')
    
    all_uid = []
    for line in file:
        list_line = line.split(' ')
        if str(list_line[-1]).endswith('\n'):
            list_line[-1] = list_line[-1][:-1]
        if list_line[-1]=='':
            list_line = list_line[:-1]
        all_uid = all_uid+list_line
    file.close()
    print len(all_uid)
#     print len(set(all_uid))
#     print all_uid[-10:]
    
    out_file = open("out_uid_unique.txt",'a')
    i = 1
    for uid in set(all_uid):
        if i%10==0:
            out_file.write(uid+'\n')
        else:
            out_file.write(uid+' ')
        i = i+1
    out_file.flush()
    out_file.close()
    print "num:  "+str(i)


if __name__ == '__main__':
    main()
    pass