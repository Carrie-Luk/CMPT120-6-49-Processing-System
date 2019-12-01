#Def Function

#-------------------------START---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Start_Program():
    print(" Welcome to CMPT 120 6-49 Processing System!")
    print(" ===========================================\n")
    print("you first need to provide the input file name")
    print("You will be asked to provide the output file later\n")
    print("The input file should be in this folder")
    print("The output file will be created in this folder\n")
    print("you will be able to provide new names for the files or accept the default names. Both files should have the extension '.csv'\n")

#-------------------Obtain List---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def read_csv_into_list_of_lists(IN_file):
    import csv
    lall = []
    ### print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)
    return lall

#--------------------INPUT FILE---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Input_file_name():
    list = input("type x for INPUT file name 'IN_data_draws3.csv', or a new file name: ")
    if list == "x":
        list = "IN_data_draws3.csv"
    lall=read_csv_into_list_of_lists(list)
    return lall

''' # validate file input
def Input_file_name():
    error = "Y"
    while error == "Y":
        try:
            list = input("type x for INPUT file name 'IN_data_draws3.csv', or a new file name: ")
            if list == "x":
                list = "IN_data_draws3.csv"
            lall=read_csv_into_list_of_lists(list)
            error = "N"
        except:
            print("An error occured trying to read file")
    return lall
'''

#---------- function for confirming OUTPUT ---------------------------------------------------------------------------------------------------------------------------------------------------------#
def Confirm_Ouput_F_Name():
    print("Please confirm the output file name for your selected data\n (if there is a file with this name in the folder this new file will substitute the previous one)\n")
    OUTPUT =input("type x for OUTPUT file name 'OUT_results3.csv', or a new file name: ")
    if OUTPUT == "x":
        OUTPUT = "OUT_results3.csv"
    return OUTPUT

#----------------SEL, ALL, or END ------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Sel_All_End(list):
    start = "-1"
    while start != "END":
        start ="-1"
        print("Please choose on of three options: \n")
        print("type ALL to process all data")
        print("type SEL to process selected draws")
        print("type END to end this program\n")
        start = input("Type All, SEL, or END (not case sensitive): ").upper()
        if start == "SEL":
            
            ### run Sel program ###
            print("=========SELECTED data will be processed==========")
            info = Sel_Start(list)
            #print("sel trace",info)
            if info == -2:
                print("Nothing will be processed, you can try another option")
                start=info
            #print(info,"\n")

            ### Confirm OutPut FIle ##
            if info != -2:
                global output_f_name
                output_f_name = Confirm_Ouput_F_Name()
                print(output_f_name)
                for i in range(len(info)):
                    print("JUST TO TRACE, the draw being processed is:\n")
                    print("index#",i)
                    print()
                    print("date",info[i][0])
                    print()
                    print("numbers drawn",info[i][1:8])
                    print()
                    print("jackpot",info[i][8])
                    print()
                    print("num winners",info[i][9])
                print("TRACE", info,"\n")
                return info
            
        if start == "ALL":
            output_f_name = Confirm_Ouput_F_Name()
            print(output_f_name)
            ### run ALL program ###
            print("TRACE --- Running ALL program")
            info = list
           
            return info
    else:
        return -12

#---------- Function for converting list -----------------------------------------------------------------------------------------------------------------------------------------------------------#
def convert_lall_to_seperate_lists(lall):
    ldates=[]
    lwnum=[]                                        
    ljack=[]
    lwin=[]
    laveja=[]
    for i in range(len(lall)):
            ldates=ldates+[lall[i][0]]
            linner=[]
            linner=[[lall[i][1],lall[i][2],lall[i][3],lall[i][4],lall[i][5],lall[i][6],lall[i][7]]]
            lwnum=lwnum+linner
            ljack=ljack+[lall[i][8]]
            lwin=lwin+[lall[i][9]]
            if (int(lall[i][9])>0):
                laveja=laveja+[int(lall[i][8])/int(lall[i][9])]
            else:
                laveja=laveja+[0]                                   #To get each invividual list slice the string, for ldates, do returned[0] etc
    return ldates,lwnum,ljack,lwin,laveja


#-- ------- Ask for selected data ------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#use lall to gather all data listed
def Sel_Start(lall):
##    
##    x = input("Want to select by month (M) or day of week (D)?: ")
##    while x != "D" and x != "M" and x != "d" and x != "m":
##        print("Invalid Response, please type 'M' or 'D'\n")
##        x = input("Want to select by month (M) or day of week (D)?: ")
##        
##    #MONTHS    
##    if x =="M" or x == "m":
        months = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
        sel_data = []
        
        print("Please select a month")
        print("Only the draws associated to this month will be processed\n")
        month_num= input("Please type a month number (1 to 12):")

        #Validation of month number
        while not(month_num.isdigit()) or not(month_num in ["1","2","3","4","5","6","7","8","9","10","11","12"]):
            print("invalid response")
            month_num= input("Please type a month number (1 to 12): ")  

        #is month in data set?
        num_of_data = 0
        for i in lall:
            if months[int(month_num)-1] in i[0]:
                #print("the month",(months[int(month_num)-1]), "is in data")
                sel_data.append(i)
                #print(sel_data)
                num_of_data += 1
        ##print(num_of_data, "draws were found in the data for", str(months[int(month_num)-1]))
        if num_of_data == 0:
            print("The file does not have any draws in",str(months[int(month_num)-1]))
            return(-2)
        else:
            print("TRACE of ",sel_data)
            return(sel_data)

    #DAYS
##    if (x =="d" or x == "D"):
##        return "unfinished"
#=========================OUTPUT LIST CREATOR===========================#
def Outlist(seplist):
    
    anslt=[]
    for k in range(len(seplist[0])):
        list1=["'" + str(seplist[0][k])+"'"+",",0,0,0,0,0,str(seplist[4][k])+"\n"]
        for i in range(7):
            if int(seplist[1][k][i])<=10:
                list1[1]=list1[1]+1
            if int(seplist[1][k][i])>10 and int(seplist[1][k][i])<=20:
                list1[2]=list1[2]+1
            if int(seplist[1][k][i])>20 and int(seplist[1][k][i])<=30:
                list1[3]=list1[3]+1
            if int(seplist[1][k][i])>30 and int(seplist[1][k][i])<=40:
                list1[4]=list1[4]+1
            if int(seplist[1][k][i])>40 and int(seplist[1][k][i])<50:
                list1[5]=list1[5]+1
        list1[1]=str(list1[1])+","
        list1[2]=str(list1[2])+","
        list1[3]=str(list1[3])+","
        list1[4]=str(list1[4])+","
        list1[5]=str(list1[5])+","
        anslt.append((list1))
    #print("Trace print of anslist",anslt)
    
    return
#=========================Provided OUTPUT LIST CREATOR===========================#
def append_1_draw_to_output_list(lout,date,lfreq_ran,avg_paid):
    '''
    PROVIDED. CMPT 120
    this function would append one line (the result associated to one draw)
    to a list. (this list will later be used to create the output file)
    
    
    The input parameters to this function are:
        - the list used to incorporate all the results
        - a string representing the date of this one draw to be appended
  ye      - the list with the range frequency distribution for this draw
        - the average paid to each winner for this draw
    '''
    
    lout.append("'" + date + "'" + ",")
    for freq in lfreq_ran:
        lout.append(str(freq) + ",")
    lout.append(str(avg_paid) + "\n")
    return


#=========================OUTPUT FILE CREATOR===========================#
def write_list_of_output_lines_to_file(lout,file_name):
    '''
    PROVIDED. CMPT 120
    Assumptions:
    1) lout is the list containing all the lines to be saved in the output file
    2) file_name is the parameter receiving a string with the exact name of the output file
       (with the csv extension, e.g "OUT_results.csv")
    3) after executing this function the output file will be in the same
       directory (folder) as this program 
    4) the output file contains just text representing one draw data per line 
    5) after each line in the file  there is the character "\n"
       so that the next draw is in the next line, and also
       there is (one single) "\n" character after the last line
    6) after the output file was created you should be able to open it
       with Excell as well
    '''
    
    fileRef = open(file_name,"w") # opening file to be written
    for line in lout:
        fileRef.write(line)
                                    
    fileRef.close()  
    return
#--------------------------STATS CALCULATIONS NOW------------------------#

#---------------------Draws Processed----------------------#
def draws_processed(seperated_list):
    ans=len(seperated_list[1])
    return ans
#----------------------Max Jackpot-------------------------#
def max_jack_and_date(seperated_lists):
    maxjack=0
    datejack=""
    for i in range(len(seperated_lists[2])):
        if int(seperated_lists[2][i])>maxjack:
            maxjack=int(seperated_lists[2][i])
            datejack=seperated_lists[0][i]
    return maxjack,datejack
#----------------------Max Average Jackpot-----------------#
def max_avejack_and_date(seperated_lists):
    maxavejack=0
    dateavejack=""
    for i in range(len(seperated_lists[4])):
        if int(seperated_lists[4][i])>maxavejack:
            maxavejack=int(seperated_lists[4][i])
            dateavejack=seperated_lists[0][i]
    return maxavejack,dateavejack
#----------------------number of times each number was drawn-#
def numtimedraw(seplist):
    flist=[0]*50
    num=0
    #print("TRACE PRINT of flist",flist)
    for i in range(len(seplist[1])):
        for k in range(7):
            num=int(seplist[1][i][k])
            flist[num]=flist[num]+1
    return flist
#----------------------Ranges of drawn numbers------------#
def rangesnumdrawn(numtimedrawn):
    #print(numtimedrawn)
    lranges=[0]*5
    for i in range(50):
        if i>0 and i<=10:
            lranges[0]=lranges[0]+numtimedrawn[i]
        if i>10 and i<=20:
            lranges[1]=lranges[1]+numtimedrawn[i]
        if i>20 and i<=30:
            lranges[2]=lranges[2]+numtimedrawn[i]
        if i>30 and i<=40:
            lranges[3]=lranges[3]+numtimedrawn[i]
        if i>40 and i<50:
            lranges[4]=lranges[4]+numtimedrawn[i]
    return lranges
#---------------------Six most frequently drawn numbers---#
def sixmost(numtimedrawn):
    lstans=[0]*6
    indexans=[0]*6
    for i in range(50):
        if numtimedrawn[i]>lstans[0]:
            lstans[0]=numtimedrawn[i]
            indexans[0]=i
    numtimedrawn[indexans[0]]=-1
    for i in range(50):
        if numtimedrawn[i]>lstans[1]:
            lstans[1]=numtimedrawn[i]
            indexans[1]=i
    numtimedrawn[indexans[1]]=-1
    for i in range(50):
        if numtimedrawn[i]>lstans[2]:
            lstans[2]=numtimedrawn[i]
            indexans[2]=i
    numtimedrawn[indexans[2]]=-1
    for i in range(50):
        if numtimedrawn[i]>lstans[3]:
            lstans[3]=numtimedrawn[i]
            indexans[3]=i
    numtimedrawn[indexans[3]]=-1
    for i in range(50):
        if numtimedrawn[i]>lstans[4]:
            lstans[4]=numtimedrawn[i]
            indexans[4]=i
    numtimedrawn[indexans[4]]=-1
    for i in range(50):
        if numtimedrawn[i]>lstans[5]:
            lstans[5]=numtimedrawn[i]
            indexans[5]=i
    numtimedrawn[indexans[5]]=-1
    
    return lstans,indexans
#--------------------------------Turtle graphical representation---------#
def ranges_distribution(rglist):
    import turtle as t
    t.fillcolor("blue")
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(10*rglist[0])
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10*rglist[0])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10*rglist[1])
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10*rglist[1])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10*rglist[2])
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10*rglist[2])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10*rglist[3])
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10*rglist[3])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10*rglist[4])
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10*rglist[4])
    t.left(90)
    t.forward(30)
    t.end_fill()
    return ""
################################# TOP LEVEL ########################
Start_Program()
ltall=Input_file_name()
#print("TRACE PRINT LTALL",ltall)
sellist=Sel_All_End(ltall)
while sellist!=-12:
    #print("TRACE PRINT SELLIST",sellist)
    seplist=convert_lall_to_seperate_lists(sellist)
    #print("TRACE PRINT OF SEPERATE LISTS", seplist)
    lout=[]
    for k in range(len(seplist[0])):
        date=seplist[0][k]
        list1=[0]*5
        for i in range(7):
            if int(seplist[1][k][i])<=10:
                list1[0]=list1[0]+1
            if int(seplist[1][k][i])>10 and int(seplist[1][k][i])<=20:
                list1[1]=list1[1]+1
            if int(seplist[1][k][i])>20 and int(seplist[1][k][i])<=30:
                list1[2]=list1[2]+1
            if int(seplist[1][k][i])>30 and int(seplist[1][k][i])<=40:
                list1[3]=list1[3]+1
            if int(seplist[1][k][i])>40 and int(seplist[1][k][i])<50:
                list1[4]=list1[4]+1
        lfreq_ran=list1
        ave_paid=seplist[4][k]
        append_1_draw_to_output_list(lout,date,lfreq_ran, ave_paid)
    print("Output to be saved to file:")
    print(lout)
    print("\n============STATS:================\n")
    numdraw=draws_processed(seplist)
    print("draws processed",numdraw,"\n")
    maxjack=max_jack_and_date(seplist)
    print("max jackpot",maxjack[0],"\n")
    print("date max jackpot", maxjack[1],"\n")
    maxavejack=max_avejack_and_date(seplist)
    print("max average won",maxavejack[0],"\n")
    print("date max average won",maxavejack[1],"\n")
    numtimedrawn=numtimedraw(seplist)
    print("number of times each number was drawn \n", numtimedrawn,"\n")
    lranges=rangesnumdrawn(numtimedrawn)
    print("number of number in each range - all selected draws \n considered \n ranges: (0,10],(10,20],(20,30],(30,40],(40,50) \n",lranges,"\n")
    sixmosts=sixmost(numtimedrawn)
    print("Six most frequently drawn numbers")
    print("number",sixmosts[1][0],"was drawn",sixmosts[0][0],"times")
    print("number",sixmosts[1][1],"was drawn",sixmosts[0][1],"times")
    print("number",sixmosts[1][2],"was drawn",sixmosts[0][2],"times")
    print("number",sixmosts[1][3],"was drawn",sixmosts[0][3],"times")
    print("number",sixmosts[1][4],"was drawn",sixmosts[0][4],"times")
    print("number",sixmosts[1][5],"was drawn",sixmosts[0][5],"times")
    distribution=input("Would you like to graph the ranges distribution? (Y/N):")
    if distribution=="y" or distribution=="Y":
        print(ranges_distribution(lranges))
    elif distribution=="n" or distribution=="N":
        print()
    write_list_of_output_lines_to_file(lout,output_f_name)
    sellist=Sel_All_End(ltall)
print("BYE.... No more stats for you!!!!")
