waiting_time=[]
Table=[]
completion_time=[]
t=int(input("\t\tenter the number of Teachers in line : "))
o=int(input("\t\tenter the number of Students in line : "))
process=[]
Teacher=[]
Burst_t=[]
Student=[]
cpu_time=[]
gunt=[]
chat=[]
edging=int(input("\n\tENTER THE EDGING TIME "))
for b in range(t):
    print("\n\tTEACHRE :",b+1)
    process.append(input("\n\tprocess name "))
    Burst_t.append(int(input("\n\tenter arrival time: ")))
    Burst_t.append(int(input("\n\tenter Burst time: ")))
    process.append(Burst_t)
    Teacher.append(process)
    cpu_time.append(Burst_t[1])
    Burst_t=[]
    process=[]
    
for c in range(o):
    print("\n\tSTUDENT :",c+1)
    process.append(input("\n\tprocess name "))
    Burst_t.append(int(input("\n\tenter arrival time: ")))
    Burst_t.append(int(input("\n\tenter Burst time: ")))
    process.append(Burst_t)
    Student.append(process)
    cpu_time.append(Burst_t[1])
    Burst_t=[]
    process=[]


running=0;
i=0;
j=0;
k=0;
l=0;
m=0;
n=0;
p=0;
q=0;
time=0;
processing_time=0;
sec=0;
count=0;
complete=0;
turn_around=[]
for i in range(t):
    turn_around.append(Teacher[i][1][1])
    
for j in range(o):
    turn_around.append(Student[j][1][1])
TTT=sum(turn_around)

for m in range(len(Teacher)):
    for p in range(len(Teacher)):
        if(Teacher[p][1][0]>Teacher[m][1][0]):
            temp=Teacher[m];
            Teacher[m]=Teacher[p];
            Teacher[p]=temp;
            
for n in range(len(Student)):
    for q in range(len(Student)):
        if(Student[q][1][0]>Student[n][1][0]):
            temp1=Student[n];
            Student[n]=Student[q];
            Student[q]=temp1;
if(len(Student)==0):
    print("\n\tYOU HAVE NOT ENTERED ANY STUDENT IN LINE ")
    
elif(len(Teacher)==0):
    print("\n\tYOU HAVE NOT ENTERED ANY TEACHER IN LINE ")
   
else:
    while(time<(TTT)):
        if (running == 0):
            if((processing_time>=Teacher[l][1][0])and(count<=edging)and(complete!=1)):
                if(Teacher[l][1][0]>sec):
                    waiting_time.append(0)
                else:
                    waiting_time.append(sec-Teacher[l][1][0])
                running=1;
        
                for j in range (0,Teacher[l][1][1]) :
                    print("\n\tTeacher processing is  : ",Teacher[l][0],"\tat Second   :  ",sec);
                    sec=sec+1;
                gunt.append(sec)
                completion_time.append(sec)
                time=time+Teacher[l][1][1]
                processing_time=processing_time+Teacher[l][1][1];##2
                print("")
                print("\tCPU_T : ",sec);
                print("")
                running=0;
                count=count+1;
                chat.append(Teacher[l])
                Table.append(Teacher[l])
                l=l+1;
                if(l>=len(Teacher)):
                    complete=1;
                    l=0;
            
            
            elif((processing_time>=Student[k][1][0])and((processing_time<Teacher[l][1][0])or(count>edging)or(complete==1))):
                if(Student[k][1][0]>sec):
                    waiting_time.append(0)
                else:
                    waiting_time.append(sec-Student[k][1][0])
                running=2;
    
                for j in range (0,Student[k][1][1]) :           
                    print("\n\tStudent running is  :  ",Student[k][0],"\tat Second   :  ",sec);
                    sec=sec+1;
                gunt.append(sec)
                completion_time.append(sec)
                print("")
                print("\tCPU_T : ",sec);
                print("")
                processing_time+=Student[k][1][1];##3
                time=time+Student[k][1][1]
                running=0;
                count=0;
                chat.append(Student[k])
                Table.append(Student[k])
                k=k+1;
                if(k>=len(Student)):
                    complete=2;
                    k=0
            
            else:
                print("\n\tCPU is IDEL at Second :  ",sec)
                print("")
                processing_time=processing_time+1##2
                sec=sec+1
                gunt.append(sec)
                chat.append("0")
    print("")
    print("")
    print("\t===================================================================================")
    print("\t|| PROCESS NAME || ARRIVAL TIME ||  CPU TIME  || WAITING TIME || COMPLETION TIME ||")
    print("\t===================================================================================")
    for tb in range(len(Table)):
   
        print("\t||\t",Table[tb][0],end=" \t||")
        print("\t",Table[tb][1][0],end=" \t||")
        print("\t",Table[tb][1][1],end=" \t||")
        print("\t",waiting_time[tb],end="\t ||")
        print("\t",completion_time[tb],"\t||")
    print("\t===================================================================================")
    print("")
    print("")
    print("\n\n\n\tTOTAL TURN ARROUND TIME IS :",TTT)
    print("\tAVRAGE TURN ARROUND TIME IS :",TTT/len(Table))
    print("\n\t\t##GANTT CHART##")
    print("\t\t+++++++++++++++++\n")
    print("\t",end="")
    for J in range(len(chat)):
        print(" _______",end="")
    print("")
    print("\t",end="")
    for P in range(len(chat)):
        print("| ",chat[P][0],end="\t")
    print(" |")
    print("\t",end="")
    for N in range(len(chat)):
        print("|_______",end="")
    
    print("_|")
    print("\t",end="")
    print("0\t",end="")
    for T in range(len(gunt)):
        print(gunt[T],end="\t")

    
