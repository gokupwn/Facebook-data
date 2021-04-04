#!/bin/python3


import json 
from  color import light_red, dark_gray, light_blue, light_green

print(light_red("""
####################################################################################
""")
+dark_gray("""
# coded by: Hassan Al Achek                                                        # 
# instagram: @hassanalachek                                                        #
# twitter: @HassanAlachek                                                          #
""")
+light_red("""
#################################################################################### """))


# enter your file name here
fileName = input(light_blue("[*]Enter The Txt Leaked File[*] "))
outFile = input(light_blue("[*]Enter The Json Output File Name [*] "))

print (light_green("[!]Due To The Lanrge Number Of Data, And The Data Not Organized,  Delete The First Line[!]"))
print (light_green("[!]id,phone,first_name,last_name,email,birthday,gender,locale,hometown,location,link[!]"))
print (light_green("[!]This Is The First Line[!]"))
print(light_green("[!]Replace Every Occurence Of This Pattern (,,,,,), I Use Sumblime To Replace Them[!]"))


# data identifier list
form = ['id','phone','first_name','last_name','email','birthday','gender','locale','hometown','location','link']

# formator function
def formator(data):
    counter = 0
    output = {}
    if len(data) > 11:
        for add  in range(1, len(data) - 11):
            form.append('more')

    for test in data.split(','):
        output[form[counter]]=test
        counter +=1
    return output

def writer(fileName, outFile):
    with open(fileName) as f_obj:
        lines = f_obj.readlines()
        for line in lines:
            with open(outFile, 'a') as of_obj:
                of_obj.write(json.dumps(formator(line),separators=(',', ': '), indent=4))

writer(fileName, outFile)
