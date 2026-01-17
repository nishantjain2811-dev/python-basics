#String is Data type Stores a sequence of characters.
# String can be implement by 1)'--' 2)"--" 3)"""--""".
#ex. str1='five' (escape sequence character) 1) \n= for next line
# 2) \t= space b/w two line .
# concatenation = str1+ str2 = "hello" + "world" = "helloworld"
#Length of string =len(str1)

#Slicing=Accessing parts of a string 
# {syntax= str[starting idx: ending idx]} 
# ending idx is not included
#In python Negative index can be use like
#  A  P  P  L  E    } str='apple' -> str[-4:-1]= ppl
# -5 -4 -3 -2 -1  


# String Functions-
# str= "i am coder"
# print(str.endswith('er'))         #Return true if string ends with substr    #output=  true
# print(str.capitalize() )            #capitalizes 1st char                    #output= I am coder
# print(str.replace('a',"e"))         #replaces all occurrences of old         #output= i em coder
# print(str.find("coder") )            #returns 1st index of 1st occurrer      #output= 5
# print(str.count("am"))               #counts the occurrence of substr        #output=  1
# print(str)                                                                   #output=  i am coder



# str1= 'Nishant'
# str2='Jain'
# print(str1+" "+str2)                  #output= Nishant Jain
# print(str1[3])                  #It is indexing (idx), output= h
# print(len(str1+str2))              #output= 11 (lenght is {last_idx + 1})
# print(str1[1:4])                     #slice __ output= ish
# print(str1[:])                #space means - left_space=0 and right_space=last idx(or len(str))
                                   #output=Nishant
             
#WAP to input user's first name & print its length
# Name = input("Enter your Name:")
# print(Name,len(Name))
# print( 'ur name contain' ,len(Name), 'letter' )

#WAP to find the occurrence of '$' in a string
# str=input('write ur string:')
# print("No. of '$'occurrence is",str.count('$'))
