import matplotlib.pyplot as plt

initial_followers = int(input("Current followers ")) #attributing the number of followers to the variable 'initial_followers'
initial_following = int(input("Current following ")) #attributing the number of accounts followed to the variable 'inital_following'
    

if initial_followers ==0 and initial_following == 0: #deals with /0 error. If only one variable is 0 no /0 error can occur (look below)
    print ("No rating can be generated")
    exit()
else:
    pass
    
total_people = int(input
                   ("For how many people do you want to simulate for? ")) #attributing the number of 'follow them and they follow back' scenarios to the 'total_people' variable

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
plt.xlabel("Additional followers who you follow back")
plt.ylabel("Instagram rating (higher is better)")
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
if reciprocal == True:
    plt.title("""(A + n)/(B + n)    
A = """+str(initial_following)+"  |  B = "+str(initial_followers)+ "  |  0≤n≤" +str(total_people))
elif reciprocal == False:
    plt.title("""(A + n)/(B + n)    
A = """+str(initial_followers)+"  |  B = "+str(initial_following)+ "  |  0≤n≤" +str(total_people))
else:
    pass

print("Current instagram rating = "+str(ratios[0]))
plt.show()
