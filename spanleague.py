titles ={
    "TITLE_HEAD":"SPAN Digital ::Score League::",
    "TITLE_MENU":"Capture the score {Team1 Score1, Team2 Score2}. Instructions: 0.- Exit | 1.- Show results | 2.- Load file ::",
    "TITLE_EXIT":"Exit",
    "TITLE_HEAD_RESULTS":"SPAN Digital ::Results::",
    "TITLE_INPUT_FILENAME":"Input the file name {e.g. test.txt}:: ",
    "TITLE_VALIDATION_RIGHT_CAPTURE":"Capture the right option",
    "TITLE_VALIDATION_RIGHT_INPUT":"Input the right information",
    "TITLE_VALIDATION_TEAMS_EQUAL":"Teams equals arent valid",
    "TITLE_VALIDATION_WHOLE_NUMBER":"The scores arent whole number",
    "TITLE_VALIDATION_REVIEW_FILE":"Review the file",
    "TITLE_PTS":"pts",
    "TITLE_PT":"pt",
    "TITLE_RESULT_FILENAME":"->See the result in the file:",
    "TITLE_RESULT_LOG":"->See the log in the file:",
    "TITLE_EXTENSION_RESULT":".results",
    "TITLE_EXTENSION_LOG":".log",
    "TITLE_Validation":"Validation:: ",
}
teams={}

def results(teams):
    results = ""
    teams_sort =  sorted(teams.items(), key=lambda x:(-x[1],x[0]))
    print(titles["TITLE_HEAD_RESULTS"])
    for indice, item in enumerate(teams_sort, 1):
        results += "{}. {}, {} {}\n".format(indice,item[0],item[1],titles["TITLE_PT"] if item[1]==1 else titles["TITLE_PTS"])
    return results

def update(teams,team,points):
    if team[0].lstrip() in teams:
        teams[team[0].lstrip()] = int(teams[team[0].lstrip()]) + points
    else:
        teams[team[0].lstrip()] = points
        
def calculate(teams,data,fileFlag):
    team1 = data.split(",")[0].rpartition(" ")
    team2 =data.split(",")[1].rpartition(" ")
    flag,logstmp = validation(data,team1,team2)
    if(flag):
        if int(team1[2])>int(team2[2]):
            update(teams,team1,3)
            update(teams,team2,0)
        elif int(team1[2])==int(team2[2]):
            update(teams,team1,1)
            update(teams,team2,1)
        else:
            update(teams,team2,3)
            update(teams,team1,0)
        return ""
    else:
        if(fileFlag):
            return logstmp
        else:
            print(logstmp)
            return ""
    
def validation(data,team1,team2): 
    if(team1[0].lstrip()==team2[0].lstrip()):
        return False, "{} {} :: {} \n".format(titles["TITLE_Validation"],data, titles["TITLE_VALIDATION_TEAMS_EQUAL"])
    if(not team1[2].isnumeric() or not team2[2].isnumeric()):
        return False,"{} {} :: {} \n".format(titles["TITLE_Validation"],data, titles["TITLE_VALIDATION_WHOLE_NUMBER"])
    return True,""

def writefile(results,filename,label,extension):
    newfilename = filename +extension
    print(label + newfilename)
    with open(newfilename, 'w') as f:
        print(results,file=f)
        f.close()
    
def readfile(teams,filecontent,filename):
    logs= ""
    for x in filecontent:
        logs = logs + calculate(teams,x.rstrip(),True) 
    writefile(results(teams),filename,titles["TITLE_RESULT_FILENAME"],titles["TITLE_EXTENSION_RESULT"])
    writefile(logs,filename,titles["TITLE_RESULT_LOG"],titles["TITLE_EXTENSION_LOG"])
    teams.clear()

def loadfile(teams):
    filename = str(input(titles["TITLE_INPUT_FILENAME"]))
    try:
        with open(filename,"r") as f:
            teams={}
            filecontent = [ line for line in f.readlines()]            
            f.close()
        readfile(teams,filecontent,filename)    
    except:
        print(titles["TITLE_VALIDATION_REVIEW_FILE"])

print(titles["TITLE_HEAD"])
while(True):
    try:
        data = str(input(titles["TITLE_MENU"]))
        if len(data) == 1:
            if int(data) == 0:
                print(titles["TITLE_EXIT"])
                break
            elif int(data) == 1:
                print(results(teams))
            elif int(data) == 2:
                loadfile(teams)
            else:
                print(titles["TITLE_VALIDATION_RIGHT_CAPTURE"])
        else:
            calculate(teams,data,False)
    except:
        print(titles["TITLE_VALIDATION_RIGHT_INPUT"])