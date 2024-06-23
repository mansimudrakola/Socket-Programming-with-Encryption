Socket Programming with Encryption

The application concerns remote evaluation of simple arithmetical expressions using only one of the operators +, -, * and / (no parenthesis or other operators). Examples: 3 + 5, 5 * 8, etc. After an initial greeting message used by the client to start the connection to the server, the 
server asks the client to evaluate a (server-chosen, unspecified) number of expressions one after the other. Each of these expressions will be sent as a separate message. For each expression message, the server expects a response message containing the result of the evaluation of the 
expression. If the client is able to correctly evaluate all the expressions, then the server will return a secret flag to the client. This flag is unique. The message containing the flag will signify the end of the communication session. At this point, the client can close the connection 
to the server, and the application terminates. 

Protocol Actions and Messages:
Upon starting, the client must setup a TCP connection with the server. Then, the client must send the introductory message to the server. The server will respond with an expression message. The client must evaluate the expression and send back a result message. If the result is incorrect, 
the server will send back a failure message and close the connection to the client. Otherwise, the server will either send another expression message or, if enough expressions have been evaluated,a success message. The success carries the secret flag. The following types of messages are
expected: 

        • The introductory message is sent from the client to the server to signal the start of communications. It is also used authenticate the sender. This message uses the following format: 
                    EECE7374 INTR nuid 
          Where nuid is Northeastern University identification number. Make sure to enter NU ID number as a string that includes all leading zeroes. 
        • The expression message is sent from the server to the client, carrying the expression to be evaluated. This message uses the following format: 
                    EECE7374 EXPR expression 
          Where expression is the expression to be evaluated. 
        • The result message is sent from the client to the server, carrying the result of the last expression to be evaluated. This message uses the following format: 
                    EECE7374 RSLT result 
          Where result is the value of the evaluated expression. 
        • The failure message is sent from the server to the client to indicate that the last expression was evaluated incorrectly. After the server sends this message it closes the connection to the client. This message has the following format: 
                    EECE7374 FAIL 
        • The success message is sent from the server to the client, indicating that the application has completed successfully. It carries the secret flag for submission. This message uses the following format: 
                    EECE7374 SUCC flag 
          Where flag is the secret flag.
All of these messages must be case-sensitive strings that have been encoded using UTF-8. 

Servers:
The server is running on a remote machine with the host name kopi.ece.neu.edu. The server uses the port numbers in the range [5203, 5212]. Therefore, ensure that the client uses TCP sockets. Testing A sample server sample server_code.py is available.

