#write a program to append the text using "a"

# File ko append mode ("a") me open karo
with open("msg.txt", "a") as f:
    f.write("\nThis text is appended to the file.")

# File ko read karke content dekho
with open("msg.txt", "r") as f:
    print("The file content:")
    print(f.read())
