Jesse = open("Jesse.txt","r")

print(Jesse.read())
Jesse.close()


Jesse = open("Jesse.txt","w")
Jesse.write("i like file handling so far")
Jesse.close()


Jesse = open("Jesse.txt","a")
Jesse.write("i dislike exams")
Jesse.close