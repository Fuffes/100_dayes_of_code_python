# 1 task.
# try:
#     with open("a_file.txt", "r") as f:
#         f.read()
#     a_dict = {"key": "value"}
#     val = a_dict["kk"]
# except FileNotFoundError:
#     with open("a_file.txt", "w") as ff:
#         ff.write("Some")
# except KeyError as e:
#     print(e)
# else:
#     content = f.read()
#     print(content)
# finally:
#     raise KeyError("FFFFF")


# 2 task
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Height shouldn't be over 3 meters. ")
# bmi=weight/height**2
# print(bmi)


# 3 task. Catch the exception and make sure the code runs without crashing.
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")
# make_pie(4)


# 4 task
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
# def count_likes(posts):
#     total_likes = 0
#
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             pass
#     return total_likes
# count_likes(facebook_posts)







