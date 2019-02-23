import sys
for i in range(2,3):
    f_result = open('F:/importantfilecopy/tandomrepeat/2019.121test/v'+str(i)+'.txt', 'w')
    sys.stdout = f_result
    class info:

        def __init__(self, line_str):
            self.row_num = int(line_str.split()[0])
            self.start = int(line_str.split()[1])
            self.length = int(line_str.split()[2])
            self.letter = line_str.split()[6]
            self.end = int(self.start + self.length)
            if int(line_str.split()[4])==2:
                if int(line_str.split()[5])==0:
                    self.type = 4
                else:
                    self.type = 3
            else:
                if int(line_str.split()[3])==3:
                    self.type = 2
                else:
                    self.type = 1
    fin = open("F:/importantfilecopy/tandomrepeat/2019.121test/s"+str(i)+".txt","r")

    file_info_set = []
    for line in fin:
        file_info_set.append(info(line))

    comp_num = -1
    a = 1

    while (True):

        comp_num += 1
        start = file_info_set[comp_num].start
        end = file_info_set[comp_num].end
        type = file_info_set[comp_num].type
        letter = file_info_set[comp_num].letter
        if comp_num + 1 < len(file_info_set):
            if file_info_set[comp_num + 1].row_num % 2 == 0:
                # if(file_info_set[comp_num+1].row_num == file_info_set[comp_num].row_num+1):
                end = end + file_info_set[comp_num + 1].length

                comp_num += 1

        # print("*"*20)
        print "19"+"\t"+str(start)+"\t"+str(start)+"_cdi"+"\t"+str(letter)+"\t"+str(letter)+"\t"+"."+"\t"+"."+"\t"+"SVTYPE=CDI;END="+str(end)+";TYPE="+str(type)
        a += 1
        if (comp_num > len(file_info_set) - 2):
            break

        i += 1







