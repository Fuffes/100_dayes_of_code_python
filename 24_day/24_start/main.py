# r = read only
# w = write only (rewrite file).
# if file with this name doesn't exist. system will create new one
# a = append. add text at the end



with open("my_file.txt") as file:
    content = file.read()
    print(content)


with open("new_file.txt", mode="a") as file:
    file.write("\nNew text")




