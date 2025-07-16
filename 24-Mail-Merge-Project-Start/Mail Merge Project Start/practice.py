# READ FILE
with open("../../../Desktop/my_life.txt") as file:

    contents = file.read()
    print(contents)

    file.close()


# WRITE FILE
# with open("my_life.txt", mode="w") as file:
#     file.write("i am 20 years old")


# APPEND FILE
# with open("my_life.txt", mode="a") as file:
#     file.write("\ni am 20 years old")


# CREATE A NEW FILE IF IT DOESN'T EXIST
# with open("new_file.txt", mode="a") as file:
#     file.write("\ni am 20 years old")