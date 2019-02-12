from sys import stdin
import math
import sys
import random
########一次性版本

TILES_USED = 0 # records how many tiles have been returned to user
CELL_WIDTH = 3 # cell width of the scrabble board
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7 and TILES_USED < len(Tiles):
        myTiles.append(Tiles[TILES_USED])
        TILES_USED += 1


# prints tiles and their scores
def printTiles(myTiles):
    tiles = ""
    scores = ""
    for letter in myTiles:
        tiles += letter + "  "
        thisScore = getScore(letter)
        if thisScore > 9:
            scores += str(thisScore) + " "
        else:
            scores += str(thisScore) + "  "

    print("\nTiles : " + tiles)
    print("Scores: " + scores)


# gets the score of a letter
def getScore(letter):
    for item in Scores:
        if item[0] == letter:
            return item[1]

# initialize n x n Board with empty strings
def initializeBoard(n):
    Board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("")
        Board.append(row)

    return Board

# put character t before and after the string s such that the total length
# of the string s is CELL_WIDTH.
def getString(s,t):
    global CELL_WIDTH
    s = str(s)
    rem = CELL_WIDTH - len(s)
    rem = rem//2
    s = t*rem + s
    rem = CELL_WIDTH - len(s)
    s = s + t*rem
    return s

# print the Board on screen
def printBoard(Board):
    global CELL_WIDTH
    print("\nBoard:")
    spaces = CELL_WIDTH*" "
    board_str =  "  |" + "|".join(getString(item," ") for item in range(len(Board)))  +"|"
    line1 = "--|" + "|".join(getString("","-") for item in range(len(Board)))  +"|"

 
    print(board_str)
    print(line1)
    
    for i in range(len(Board)):
        row = str(i) + " "*(2-len(str(i))) +"|"
        for j in range(len(Board)):
            row += getString(Board[i][j]," ") + "|"
        print(row)
        print(line1)
        
    print()
#！！！！！！！！！！！！！！！！！！ass1代码
scoresFile = open('scores.txt')
tilesFile = open('tiles.txt')

# read scores from scores.txt and insert in the list Scores
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line= line.strip()
    Tiles.append(line)
tilesFile.close()

# decide whether to return random tiles
rand = input("Do you want to use random tiles (enter Y or N): ")
if rand == "Y":
    SHUFFLE = True
else:
    if rand != "N":
        print("You did not enter Y or N. Therefore, I am taking it as a Yes :P.")
        SHUFFLE = True
if SHUFFLE:
    random.shuffle(Tiles)


validBoardSize = False
while not validBoardSize:
    BOARD_SIZE = input("Enter board size (a number between 5 to 15): ")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE >= 5 and BOARD_SIZE <= 15:
            validBoardSize = True
        else:
            print("Your number is not within the range.\n")
    else:
        print("Are you a little tipsy? I asked you to enter a number.\n")


Board = initializeBoard(BOARD_SIZE)
printBoard(Board)

myTiles = []
getTiles(myTiles)
printTiles(myTiles)
myTiles1=myTiles[:]
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
########################################################################
# Write your code below this
#**************

#+++++++++++++++++++++++++++++++++++++ass1作业+++++++++++++++++++
def getSumSCore(world):
    sumScore=0                  #score is zero at the start     
    for data in world:          #each charactor of the word
        for dataScore in Scores:    #each score of the charactors of the word
            if dataScore[0]==data:   #find the corresponding charactor and add
                sumScore+=dataScore[1]
    return sumScore
##################################
#To judge if the word is compromised of the charactors in titles, if yes return 1, else return 0.
def judgeInTiles(World,myTile):

    
    InOrOFF=0   
    signFor=0   
    for data in World:
        for dataT in myTile:
            if data == dataT:
                myTile.remove(dataT)#If they matches,delete the charactor from myTile
                signFor+=1#and plus one
                break#go for next search


    if signFor==len(World):#if the score of signFor is equal to the lenth of the word, it represents that all charactors are found. Return 1 at the stage.
        InOrOFF=1 
    return InOrOFF
###################################
#get the maxmun scores.

def getMaxScore(Tiles,dicWorl,strH,strV,size):
    validList={}
    signMax=1#判断titles里是否有组成在字典里的值\
    rORc=int(strH[0])
    for dataD in dicWorl:
        Title=Tiles[:]#creat a copy in order to get it back
        judgeG=judgeInTiles(dataD, Title)#Judge if the word is comprimised with the charactors in tiles, 1 with yes, 0 with no.
        

        if judgeG==1:#If yes with 1, dictionary has this word, then calculate the score.
            if rORc+len(dataD)<=size :                                #if c+leng>lengC or r>lengR :
                validList[dataD]=getSumSCore(dataD)
                signMax=0

    if signMax==0:#the charactors in titles can comprimise the words in dictionary.
        

        #MaxKey=max(validList, key=validList.get)#得到validList字典里value值最大的key,validList为{key:value,key:value....}形式
        MaxValue=0
        for i in validList:#i表示单词，validList[i]表示单词i的分数
            if validList[i]>MaxValue:
                MaxValue=validList[i]
                MaxKey=i



        #MaxValue=validList[MaxKey]#find the value according to the key
        #print ("The word "+MaxKey+" is the word with highest score. Its score is "+str(MaxValue))
        print("Maximum possible score in this move was "+str(MaxValue)+" with word "+MaxKey+" at "+strH)
    else:
        print ("No word can be made using these tiles")       


##################################得到规格化字典

dic=open("dictionary.txt")
dicWorld=dic.readlines()
#delete every enter symble 
def removeN(x):
        y=x.replace('\n','')
        return y
dicWorld1=[]
for i in dicWorld:
    dicWorld1.append(removeN(i))

########################################################################
def judgeWorldLe(myTiles,dicWorld1):
    sign=1
    signOn=1#输入"***"退出标志
    while sign:

        myTiles1=myTiles[:]
        GetWorld=input("Enter a word:")
        UpperWorld=GetWorld.upper()
        if GetWorld=="***":
            print ("Better luck next time!!!")
            #getMaxScore(myTiles1,dicWorld1)
            sign=0
            signOn=0#，signOn=0时表示使用了"***"退出标志
            continue

        

        k=0#得分判断
        for j in UpperWorld:#循环每个字母
            x=0#p判断标志
            for i in Scores:
                if j==i[0]:#如果这个字符在字母表里则判断标志改为1
                    x=1
                    break
            if x==1:#当判断标志为1时得分标志加1分
                k+=1
        if k!=len(UpperWorld):#当分数与单词长度不相等，就报错
            print ("Only use English letters!!!")
            continue        
        #the word exist in ditionary?
        OnOff=0
        for dataD in dicWorld1:
            if UpperWorld==dataD:#Search if the word exist in dictionary. If yes, change OnOff to 1,the break.
                OnOff=1
                break
        if OnOff==0:#no such word
            print ("I have never heard of this word.")
            continue
        judge=judgeInTiles(UpperWorld,myTiles1)#If in tiles
        if judge==0:
            print ("This word cannot be made using your tiles.")
            continue
        
        sign=0#exiting the loop
    return UpperWorld,signOn
#UpperWorld,signOn=judgeWorldLe(myTiles,dicWorld1)
#if signOn==0:
#    sys.exit()
#if signOn==1:
#    WorldScore=getSumSCore(UpperWorld)
#    print ("Cool, this is a valid word.\nScore for the word SENT is: "+str(WorldScore))

#    getMaxScore(myTiles,dicWorld1)
#+++++++++++++++++++++++++++++++++++++signOn==1得改+++++++++++++++++++++++++
#GetWorld=input("Enter your word:")

def locationRight(myTiles,Board,UpperWorld,firstSign=0):  #判断输入位置形式是否有效
    myTilesY=myTiles[:]
    location=input("Enter the location in row:col:direction format:")#"6,6,H"
    location=location.split(":")#"6:6:H"==>['6','6','H']
    r=location[0]#row 6    "123" "abc" "1a2"
    c=location[1]#6
    d=location[2]#H

    signJ=1
    canModification=False#能不能修改Broad的标志
    for i in r:    #判断行为数字
        if i < '0' or i>'9':
            print("Invalid Move!!!")
            return signJ,myTilesY,Board,r,c,d,canModification,0,0
    for i in c:   #判断列为数字
        if i < '0' or i>'9':
            print("Invalid Move!!!")
            return signJ,myTilesY,Board,r,c,d,canModification,0,0
    if len(location)!=3: #判断格式是否正确
        print("Invalid Move!!!")#跳出当前循环
        return signJ,myTilesY,Board,r,c,d,canModification,0,0

    '''
    if r >= '0' and r<='9' and c>='0' and c<='9' and len(location)==3:#输入位置是数字且只有三个值
        pass
    else:
        print("Invalid Move!!!")#跳出当前循环
        return signJ,myTilesY,Board,r,c,d,canModification
    '''
    

    r=int(r)
    c=int(c)
    centerNum=len(Board)//2
    strH=str(centerNum)+":"+str(centerNum)+":H"
    strV=str(centerNum)+":"+str(centerNum)+":V"
    if firstSign:
        centerNum=len(Board)//2
        if r!=centerNum or c!=centerNum:
            strH=str(centerNum)+":"+str(centerNum)+":H"
            strV=str(centerNum)+":"+str(centerNum)+":V"
            print("The location in the first move must be "+strH+" or "+strV)
            print("Invalid Move!!!")
            return signJ,myTilesY,Board,r,c,d,canModification,0,0
    leng=len(UpperWorld)
    lengC=len(Board[0])
    lengR=len(Board)
    #判断格式是否正确
    
    
    if d=="H":
        #此处为画板大小容错处理
        if c+leng>lengC or r>lengR :
            print("the size is too big ")
        else:
            canModification=True
            signJ=0
    elif d=="V":
        if r+leng>lengR or c>lengC:
            print("the size is too big ")
            #return 1,myTiles,Board
        else:
            canModification=True
            #for i in range(leng):
            #    Board[r+i][c]=UpperWorld[i]
            #    myTiles.remove(UpperWorld[i])
            signJ=0
    else:
        print("please enter 'H' or 'V' for direction")#跳出当前循环
        #return 1,myTiles,Board
    return signJ,myTilesY,Board,r,c,d,canModification,strH,strV
#修改Broad
def modification(r,c,d,UpperWorld,Board,myTiles,moveCharFromTitles):
    myTilesX=myTiles[:]
    leng=len(UpperWorld)

    if d=="H":
        for i in range(leng):
            Board[r][c+i]=UpperWorld[i]
            #if UpperWorld[i]
            #myTilesX.remove(UpperWorld[i])        
    else:
        for i in range(leng):
            Board[r+i][c]=UpperWorld[i]
            #myTilesX.remove(UpperWorld[i])
    for j in  moveCharFromTitles:
        myTilesX.remove(j)
    return Board,myTilesX


#每次使用title里的东西后重载title
def maintianTitle(myTiles):
    myTilesQ=myTiles[:]
    stri='['
    for i in range(len(myTilesQ)):
        if i==len(myTilesQ)-1:
            stri=stri+myTilesQ[i]+']'
        else:
            stri=stri+myTilesQ[i]+','
    print("Tiles remaining after the move: "+stri)
    print("Calling getTiles(myTiles) function...\n\n"+"Printing the tiles.\n")
    getTiles(myTilesQ)
    printTiles(myTilesQ)
    return myTilesQ

####判断单词是否与board里字符冲突，并且得到剔除board字符的字符串
def InvalidMove(Board,r,c,d,UpperWorld,myTiles):
    myTilesW=myTiles[:]
    leng=len(UpperWorld)
    exceptBoard=list(UpperWorld)
    signM=1#判断是否有效位置，1表示有效位置
    signJ=0#对匹配空字符的个数进行统计
    for i in range(leng):
        if d=="H":
            compareChar=Board[r][c+i]
            if compareChar=='':
                signJ+=1
            else:
                if compareChar!=UpperWorld[i]:
                    #print("Invalid Move!")
                    signM=0
                else:
                    exceptBoard.remove(compareChar)
        else:

            compareChar=Board[r+i][c]
            if compareChar=='':
                signJ+=1
            else:
                if compareChar!=UpperWorld[i]:
                    #print("Invalid Move!")
                    signM=0
                else:
                    exceptBoard.remove(compareChar)
    #########################判断exceptBoard是否在titles里2222222222222222222222222222222222222222
    exceptBoardStr=''.join(exceptBoard)#列表字符串化
    #myTiles2=myTiles[:]
    judge=judgeInTiles(exceptBoardStr,myTilesW)
    if judge==0:
        print ("This word cannot be made using your tiles and board's tiles.")
        signM=0  
    if signJ==leng:#无匹配的字符
        signM=0
    #if signM==0:#####################################有问题改回这里
        #print("Invalid Move!")##################################
    return signM,exceptBoardStr
def getMaximum(myTiles,Board,dicWorld1):
    size=len(Board)
    ScoreList=[]
    dataList=[]
    for i in range(size):
        for j in range(size):
            if Board[i][j]!='':  #Board[i][j]找到的字母T
                #print(Board[i][j])
                myTilesG=myTiles[:]
                myTilesG.append(Board[i][j]) #新的tiles
                #print(myTilesG)
                #print(len(dicWorld1))
                for data in dicWorld1:
                    #data=dicWorld1[k]
                    #print(data)
                    Titles= myTilesG[:]                   
                    judgeG=judgeInTiles(data, Titles)#如果返回是1就正确
                    if judgeG==1:
                        myTilesA=myTiles[:]
                        #print(data)
                        if Board[i][j] not in data:

                            continue
                        #print(Board[i][j])
                        #print(data)
                        indexInData=data.index(Board[i][j])
                        #print(indexInData)
                        lenData=len(data)
                        ##横放所做判断
                        R=i
                        C=j-indexInData
                        D="H"
                        
                        if C+lenData>size or R>size or C<0:
                            pass

                        else:
                            signM,exceptBoardStr=InvalidMove(Board,R,C,D,data,myTilesA)
                            if signM:
                                maxScore=getSumSCore(exceptBoardStr)
                                ScoreList.append(maxScore)
                                dataList.append([R,C,D,data])
                            else:
                                pass

                        ###竖放所做判断
                        R=i-indexInData
                        C=j
                        D="V"
                        if R+lenData>size or C>size or R<0:
                            pass
                        else:
                            signM,exceptBoardStr=InvalidMove(Board,R,C,D,data,myTilesA)
                            '''
                            if R+lenData>size or C>size:
                                continue
                            '''
                            if signM:
                                maxScore=getSumSCore(exceptBoardStr)
                                dataList.append([R,C,D,data])
                                ScoreList.append(maxScore)
                            else:
                                pass
                
    #print(ScoreList)
    maxIndex=ScoreList.index(max(ScoreList))
    return dataList[maxIndex],ScoreList[maxIndex]

#第一次输入单词所进行的程序

sign=1
while sign:
    UpperWorld,signOn=judgeWorldLe(myTiles,dicWorld1)
    if signOn==0:#如果输入的***，就退出
        sys.exit()
    firstSign=1
    sign,myTiles,Board,r,c,d,canModification,strH,strV=locationRight(myTiles,Board,UpperWorld,firstSign)
    if canModification:
        Board,myTiles=modification(r,c,d,UpperWorld,Board,myTiles,UpperWorld)#修改board

WorldScore=getSumSCore(UpperWorld)
totalSocre=WorldScore###统计总分，此处为第一个单词的分数
print("Your score in this move:"+str(WorldScore))
print("Your total score is:"+str(totalSocre))
getMaxScore(myTiles1,dicWorld1,strH,strV,len(Board))
printBoard(Board)
myTiles=maintianTitle(myTiles)
#第二次输入单词及第二次之后输入的程序
while True:
    sign=1#判断是否正确输入，如果输入有错误的地方sign就等于1，继续循环
    maxData,maxSocre=getMaximum(myTiles, Board, dicWorld1)
    while sign:
        newTiles=myTiles[:]
        for i in Board:
            for j in i:
                if j!='':
                    newTiles.append(j)

        UpperWorld,signOn=judgeWorldLe(newTiles,dicWorld1)
        if signOn==0:
            sys.exit()
        sign,myTiles,Board,r,c,d,canModification,strH,strV=locationRight(myTiles,Board,UpperWorld)
        if canModification:
            signM,exceptBoardStr=InvalidMove(Board,r,c,d,UpperWorld,myTiles)#exceptBoardStr为除去Board里字符剩下的字符，使用它计算分数
            if signM:
                Board,myTiles=modification(r,c,d,UpperWorld,Board,myTiles,exceptBoardStr)
                sign=0
            else:
                print("Invalid Move!")
                sign=1
    #print(UpperWorld+"#######################")
    WorldScore1=getSumSCore(exceptBoardStr)#
    totalSocre+=WorldScore1###统计总分，此处为第一个单词的分数
    print("Your score in this move:"+str(WorldScore1)) 
    print("Your total score is:"+str(totalSocre))
    print("Maximum possible score in this move was "+str(maxSocre)+" with word "+maxData[3]+" at "+str(maxData[0])+":"+str(maxData[1])+":"+maxData[2])
    printBoard(Board)
    myTiles=maintianTitle(myTiles)


#************


########################################################################