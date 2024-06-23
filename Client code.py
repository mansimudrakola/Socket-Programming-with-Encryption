###################################################################################################
#                                                                                                 #
# This python program represents the client side of the network. It connects to the server,       #
# sends an initial greeting message, receives simple mathematical expressions as strings          #
# via TCP from server and then sends back the correct answer for each of the operations.After the #
# server receives correct results to all the expressions from the client, it sends a unique       #
# secret flag to the client. The message containing the flag will signify the end of the          #
# communication session. Or maybe, a failure message could also be sent from the server to        #
# indicate that the expression was evaluated incorrectly and closes the connection.               #
# All the steps in the program are followed by comments that explain the reason and logic behind  # 
# the program lines.                                                                              #      
#                                                                                                 # 
# NUID number : 002702946                                                                         #  
#                                                                                                 #      
# The program is running successfully and the obtained secret flag is :                           #
# 37e62a09b1a9c3f33460f194f84401c5f7635d71294ef571947eb3b82ee858f6                                #    
#                                                                                                 #
###################################################################################################

import socket #importing socket module from Python standard library
servername = 'kopi.ece.neu.edu'#host name of server 
serverport = 5208 #port no. of server, can be any between [5203, 5212]
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a TCP socket for server
# AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP
clientSocket.connect((servername, serverport)) 
#establishing a connection between client and server by forwarding servername and port no. to server
message = "EECE7374 INTR 002702946" #initial greeting message containg my NUID number
print(message)
clientSocket.send(message.encode('UTF-8')) #greet message encoding using 'UTF-8' and sending it to server from client
while True: #while loop is being used to receive all of the expressions the server will send for evaluation
    recmsg=clientSocket.recv(1024) #recmsg stores the server sent expression message 
    print(str(recmsg, 'UTF-8')) #printing the received and decoded string message using 'UTF-8'
    lst=(str(recmsg, 'UTF-8')).split( ) #split function is used to create a list of the elements of decoded string message 
    #expression message example : EECE7374 EXPR 4+8
    #succes message example : EECE7374 SUCC FLAG
    #failure message example : EECE7374 FAIL
    breakpt=lst[1] #the differentiator between expression and (success or failure) message is the second word
    if breakpt=='SUCC' or breakpt=='FAIL':
        break
    ''' logic: for client to differentiate between an expression message and (success or failure) message,'if' 
    block is being used, if the condition of the 'if' block is met, compiler gets out of 'while' loop and the client terminates'''
    op=(lst[3]) #storing the operator from list to 'op' variable(the operator is the fourth element)
    if op == '+':
        sol = int(lst[2])+int(lst[4])
    elif op == '-':
        sol = int(lst[2])-int(lst[4])
    elif op == '*':
        sol = int(lst[2])*int(lst[4])
    elif op == '/':
        sol = int(lst[2])/int(lst[4])
    '''if-elif blocks to check for the type of operator and calculate sol accordingly'''
    solution = "EECE7374 RSLT " + str(sol) #creating a string 'solution' and concatenating the result of evaluated expressions to it
    print(solution)
    clientSocket.send(solution.encode('utf-8')) #sending solution message to server using 'UTF-8' encoding

