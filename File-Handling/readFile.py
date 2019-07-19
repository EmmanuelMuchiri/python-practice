# handle = open("test.txt", "r")

# data = handle.read()
# print(data)

# handle.close()

# handle = open("test.txt", "r")

# data = handle.readlines()
# print(data)

# handle.close()

# handle = open("test.txt", "r")
# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "Python":
#        counter += 1

# print(counter)

# handle = open("text-write.txt", "w")

# handle.write("Emmanuel Muchiri")
# handle.close()

with open("test.txt","r") as handle:
    data = handle.read()
    print(data)
