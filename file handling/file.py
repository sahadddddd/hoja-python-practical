file=open('notes.txt',"w")
file.write("hello this is my fisrt note.")
file.close()

file=open("c:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\file handling\\notes.text","w")
file.write("hello this is my second note.")
file.close()

#pinne ee code 2 aamath adikande avshyalla mele kodtha codil changes verthya mathi w a aaka pinne \a addeyya
file=open("c:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\file handling\\notes.text","a")
file.write("\nhello this is my third note.")
file.close()

#FOR READING ENTIRE FILE
file=open("c:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\file handling\\notes.text","r")
print(file.read())
file.close()

#FOR LINE BY LINE READING

file=open("c:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\file handling\\notes.text","r")
for f in file:
    print(f.strip())
file.close()

#READ ONLY SPECIFIC NUMBER OF CHARECTERS
file=open("c:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\file handling\\notes.text","r")
print(file.read(11))
file.close()

#USING WITH STATEMENT
#You don't need to manually close the file - Python does it for you automatically!
with open("c:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\file handling\\notes.text","r") as file:
    print(file.read())