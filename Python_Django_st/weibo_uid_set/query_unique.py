

def main():
    file = open("query_result_comment_url.txt",'r')
    dict = {}
    for line in file:
        url = line[1:line.find(']')]
        num_str = line[line.find('[',1)+1:-2]
        dict.update({url:num_str})
    
    file_unique = open("query_result_comment_url_unique.txt",'a')
    for key in dict:
        line = "["+key+"]"+"["+dict[key]+"]"
        print line
        file_unique.write(line+'\n')
        
    file.close()
    file_unique.close()
    pass


if __name__ == '__main__':
    main()
    pass