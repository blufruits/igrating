import matplotlib.pyplot as plt
import math

initial_followersnotrunc = float(input("Current followers ")) #attributing the number of followers to the variable 'initial_followers'
initial_followingnotrunc = float(input("Current following ")) #attributing the number of accounts followed to the variable 'inital_following'

initial_followers = math.trunc(initial_followersnotrunc) #removing fractional part if need be. 
initial_following = math.trunc(initial_followingnotrunc)

if initial_followers ==0 and initial_following == 0: #deals with /0 error. If only one variable is 0 no /0 error can occur (look below)
    print ("No rating can be generated")
    exit()
elif initial_followers < 0 or initial_following < 0:
    print ("No rating can be generated")
    exit()
else:
    pass
    
total_peoplenotrunc = int(input
                   ("How many 'mutal' people should the graph simulate? ")) #attributing the number of 'follow them and they follow back' scenarios to the 'total_people' variable
total_people = math.trunc(total_peoplenotrunc)
if total_people < 0:
    print ("No rating can be generated")
    exit()
else:
    pass
#############################################################################################################################################    

n = [] #defining the x axis list
for i in range(total_people + 1):
    n.append(i) #generates a list from '0' to 'total_people'

ratios = [] #defining y axis list

if initial_followers > initial_following:
    reciprocal = True
else:
    reciprocal = False

if reciprocal == True: #if followers>following the reciprocal fraction is plotted instead. This limits the range from [0:1]. It also makes the rating more consistent with the following>followers scenario
    for i in range(total_people + 1):
        ratios.append((initial_following+i)/(initial_followers+i)) #generates a list of (following + n)/(followers + n) up to 'total_people'
elif reciprocal == False:
    for i in range(total_people + 1):
        ratios.append((initial_followers+i)/(initial_following+i)) #generates a list of (followers + n)/(following + n) up to 'total_people'
else:
    pass

############################################################################################################################################# 

plt.plot(n,ratios) #plotting graph
plt.xlabel("Number of 'mutal' accounts followed")
plt.ylabel("Instagram rating (higher is better)")
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
if reciprocal == True:
    plt.title("""(A + n)/(B + n)    
A = """+str(initial_following)+"  |  B = "+str(initial_followers)+ "  |  0≤n≤" +str(total_people)+ "  |  A,B,n ∈ Z*")
elif reciprocal == False:
    plt.title("""(A + n)/(B + n)    
A = """+str(initial_followers)+"  |  B = "+str(initial_following)+ "  |  0≤n≤" +str(total_people)+ "  |  A,B,n ∈ Z*")
else:
    pass

print("Current instagram rating = "+str(ratios[0]))
plt.show()
