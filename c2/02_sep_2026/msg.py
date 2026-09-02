# msg.txt file ko write mode me open karo
with open("msg.txt", "w") as f:
    f.write("Hello Vikash!\n")
    f.write("This is my first file handling program.")

# Ab file ko read karo
with open("msg.txt", "r") as f:
    print("the file content:")
    print(f.read())



