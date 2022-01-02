import random
import matplotlib.pyplot as plt

#Switch door function for other unopened doors
def switch_door(non_prize_door,no_of_doors,choice):
    num=0
    while(num==non_prize_door or num == choice and num < no_of_doors):
       num = num+1
 
    return num

def switch_door2(non_prize_door1,non_prize_door2,no_of_doors,choice):
    num=0
    while(num==non_prize_door1 or num == choice or num == non_prize_door2 and num < no_of_doors ):
        num = num+1
        
    
    return num

#Function for host to open the door which doesn't contain prize
def get_nonprizedoor(host,no_of_doors,choice):
    num=0
    while(num==host or num == choice and num < no_of_doors):
        num = num+1
        
  
    return num

# function to get the second non prize door 
def get_nonprizedoor2(host,non_prize_door1,no_of_doors,choice):
    num=0
    while(num==host or num == choice or num == non_prize_door1 and num < no_of_doors):
        num = num+1
        
  
    return num

# SIMULATION FOR THREE DOOR 
def simulate_game(switch_cond,no_of_tests):
    winbyswitch_count = 0
    winwithoutswitch_count = 0
    losewithswitch_count = 0
    losewithoutswitch_count = 0

    doors=[]
    no_of_doors = 3
    for i in range(0,no_of_doors):
        doors.append(i)
      

    for i in range(0, no_of_tests):
        door_with_prize = random.randint(0,no_of_doors-1)
        host = door_with_prize # letting host know where the prize is
        # print("door with prize :",host)
        player_choice = random.randint(0, no_of_doors-1)
        # print("player choice :",player_choice)
        non_prize_door=get_nonprizedoor(host,no_of_doors,player_choice)

        #if player always switch
        if switch_cond == True:
            player_choice = switch_door(non_prize_door,no_of_doors,player_choice)
            # print("player choice after switch :",player_choice)
        
        if player_choice == door_with_prize and switch_cond == False:
            
            winwithoutswitch_count = winwithoutswitch_count+1
        elif player_choice == door_with_prize and switch_cond == True:
             
             winbyswitch_count = winbyswitch_count+1
        elif player_choice != door_with_prize and switch_cond == True:
             
             losewithswitch_count = losewithswitch_count+1
        elif player_choice != door_with_prize and switch_cond == False:
             
             losewithoutswitch_count = losewithoutswitch_count + 1
        else:
            print("!!! Something wrong occured!!!")

    return winbyswitch_count,winwithoutswitch_count,losewithswitch_count,losewithoutswitch_count,no_of_tests


# SIMULATION FOR FOUR DOOR 
def simulate_game2(switch_cond1,switch_cond2,no_of_tests):
    winbytwoswitch_count = 0
    winwithoutswitch_count = 0
    winwithfirstswitch_count = 0
    winwithsecondswitch_count = 0
    losewithtwoswitch_count = 0
    losewithouttwoswitch_count = 0
    losewithoutfirstswitch_count = 0
    losewithoutsecondswitch_count = 0

    doors=[]
    no_of_doors = 4
    for i in range(0,no_of_doors):
        doors.append(i)
      

    for i in range(0, no_of_tests):
        door_with_prize = random.randint(0,no_of_doors-1)
        host = door_with_prize # letting host know where the prize is
        player_choice = random.randint(0, no_of_doors-1)
      
        #opening first non prize door 
        non_prize_door1=get_nonprizedoor(host,no_of_doors,player_choice)

       
        if switch_cond1 == True and switch_cond2 == False:
            player_choice = switch_door(non_prize_door1,no_of_doors,player_choice)

           
        elif switch_cond1 == False and switch_cond2 == True:

            #opening second non prize door
            non_prize_door2 = get_nonprizedoor2(host,non_prize_door1,no_of_doors,player_choice)
            player_choice = switch_door2(non_prize_door1,non_prize_door2,no_of_doors,player_choice)
        elif switch_cond1 == True and switch_cond2 == True:
            player_choice = switch_door(non_prize_door1,no_of_doors,player_choice)
            #Opening second non prize door 
            non_prize_door2 = get_nonprizedoor2(host,non_prize_door1,no_of_doors,player_choice)
            player_choice = switch_door2(non_prize_door1,non_prize_door2,no_of_doors,player_choice)
        
        if player_choice == door_with_prize and switch_cond1 == False and switch_cond2 == False:
            
            winwithoutswitch_count = winwithoutswitch_count+1
        elif player_choice == door_with_prize and switch_cond1 == True and switch_cond2 == True :
             
             winbytwoswitch_count = winbytwoswitch_count+1
        elif player_choice == door_with_prize and switch_cond1 == True and switch_cond2 == False :
             
             winwithfirstswitch_count = winwithfirstswitch_count+1
        elif player_choice == door_with_prize and switch_cond1 == False and switch_cond2 == True :
             
             winwithsecondswitch_count = winwithsecondswitch_count+1
        elif player_choice != door_with_prize and switch_cond1 == True and switch_cond2 == True:
             
             losewithtwoswitch_count = losewithtwoswitch_count+1
        elif player_choice != door_with_prize and switch_cond1 == False and switch_cond2 == False:
             
             losewithouttwoswitch_count = losewithouttwoswitch_count + 1
        elif player_choice != door_with_prize and switch_cond1 == False and switch_cond2 == True:
             
             losewithoutfirstswitch_count = losewithoutfirstswitch_count + 1
        elif player_choice != door_with_prize and switch_cond1 == True and switch_cond2 == False:
             
             losewithoutsecondswitch_count = losewithoutsecondswitch_count + 1
        else:
            print("!!! Something wrong occured!!!")

    return winbytwoswitch_count,winwithoutswitch_count,winwithfirstswitch_count, winwithsecondswitch_count,losewithtwoswitch_count, losewithouttwoswitch_count, losewithoutfirstswitch_count, losewithoutsecondswitch_count,no_of_tests


#               !!!! GRAPHICAL VISUALISATION !!!!

# FOR THREE DOOR 
def threedoor_graph(no_of_tests):
    num_tests = []
    win_percentage = []
    if no_of_tests <= 1500:
        no_of_tests_run = no_of_tests
    else:
        no_of_tests_run = 1500
    for i in range(1,no_of_tests_run+1):
        num_tests.append(i) 
        y = simulate_game(True, i) 
        win_percentage.append(y[0]/ y[4])

   

    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot( num_tests, win_percentage  )
  
    plt.title('MONTY HALL SIMULATION - WITH SWITCH')
   
    plt.xlabel('NUMBER OF SIMULATIONS',fontsize=18)
    plt.ylabel('WIN PERCENTAGE',fontsize=18)
    plt.show()

def threedoor_graph2(no_of_tests):
    num_tests = []
    win_percentage = []
    if no_of_tests <= 1500:
        no_of_tests_run = no_of_tests
    else:
        no_of_tests_run = 1500
    for i in range(1,no_of_tests_run+1):
        num_tests.append(i) 
        y = simulate_game(False, i) 
        win_percentage.append(y[1]/ y[4])

    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot( num_tests, win_percentage  )
  
    plt.title('MONTY HALL SIMULATION - NO SWITCH')
   
    plt.xlabel('NUMBER OF SIMULATIONS',fontsize=18)
    plt.ylabel('WIN PERCENTAGE',fontsize=18)
    plt.show()



# FOR FOUR DOOR
def fourdoor_graph1(no_of_tests):
    num_tests = []
    win_percentage = []
    if no_of_tests <= 1500:
        no_of_tests_run = no_of_tests
    else:
        no_of_tests_run = 1500
    for i in range(1,no_of_tests_run+1):
        num_tests.append(i) 
        y = simulate_game2(True,True,i) 
        win_percentage.append(y[0]/ y[8])

    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot( num_tests, win_percentage  )
    plt.title('MONTY HALL SIMULATION - TWO SWITCH')
   
      
    plt.xlabel('NUMBER OF SIMULATIONS',fontsize=18)
    plt.ylabel('WIN PERCENTAGE',fontsize=18)
    plt.show()

def fourdoor_graph2(no_of_tests):
    num_tests = []
    win_percentage = []
    if no_of_tests <= 1500:
        no_of_tests_run = no_of_tests
    else:
        no_of_tests_run = 1500
    for i in range(1,no_of_tests_run):
        num_tests.append(i) 
        y = simulate_game2(True,False,i) 
        win_percentage.append(y[2]/ y[8])

    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot( num_tests, win_percentage  )
    plt.title('MONTY HALL SIMULATION - FIRST SWITCH')
   
      
    plt.xlabel('NUMBER OF SIMULATIONS',fontsize=18)
    plt.ylabel('WIN PERCENTAGE',fontsize=18)
    plt.show()

def fourdoor_graph3(no_of_tests):
    num_tests = []
    win_percentage = []
    if no_of_tests <= 1500:
        no_of_tests_run = no_of_tests
    else:
        no_of_tests_run = 1500
    for i in range(1,no_of_tests_run):
        num_tests.append(i) 
        y = simulate_game2(False,True,i) 
        win_percentage.append(y[3]/ y[8])

    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot( num_tests, win_percentage  )
    plt.title('MONTY HALL SIMULATION - SECOND SWITCH')
   
      
    plt.xlabel('NUMBER OF SIMULATIONS',fontsize=18)
    plt.ylabel('WIN PERCENTAGE',fontsize=18)
    plt.show()

def fourdoor_graph4(no_of_tests):
    num_tests = []
    win_percentage = []
    if no_of_tests <= 1500:
        no_of_tests_run = no_of_tests
    else:
        no_of_tests_run = 1500
    for i in range(1,no_of_tests_run):
        num_tests.append(i) 
        y = simulate_game2(False,False,i) 
        win_percentage.append(y[1]/ y[8])

    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot( num_tests, win_percentage  )
    plt.title('MONTY HALL SIMULATION - NO SWITCH')
   
      
    plt.xlabel('NUMBER OF SIMULATIONS',fontsize=18)
    plt.ylabel('WIN PERCENTAGE',fontsize=18)
    plt.show()

# fourdoor_graph4()
# a= simulate_game(True,1)
# b= simulate_game(False,1)
# percentage_of_win_by_switch = round((a[0]/a[4])*100,2)
# percentage_of_loss_by_switch = round((a[2]/a[4])*100,2)
# percentage_of_win_without_switch = round((b[1]/b[4])*100,2)
# percentage_of_loss_without_switch = round((b[3]/b[4])*100,2)