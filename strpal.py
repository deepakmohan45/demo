str = input("enter the string")

str = str.casefold ()

rev_str = reversed (str)

if list(str)==list(rev_str):

              print ("The string is a palindrome.")

else:

              print ("the string is not a palindrome.")   
