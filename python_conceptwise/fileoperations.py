# with open("temp_file.txt", "a") as f:
#     f.write("Grape is a fruit")


# with open("temp_file.txt", "r") as f:
#     content = f.read()

# print(content)


# with open("dummy_text.txt", "r") as f:
#     content_read = f.read()

# print(content_read)
# with open("dummy_text.txt", "r") as f:
#     content_read_1 = f.readline()
#     print(content_read_1)
#     content_read_2 = f.readline()

# print(content_read_2)


# Create a file with content of 4 lines
# read the whole content
with open("file1.txt", "r") as file1:
    content = file1.read()
print(content)
print("...........===========================================================================")
# now read only first line
with open("file1.txt", "r") as file1:
    first_line = file1.readline()
print(first_line)
print("...........===========================================================================")
# # create  a file with the content from first line
# # call it file 2
with open("file2.txt", "w") as file2:
    file2.write(first_line)

# # now read content from file 2
with open("file2.txt", "r") as file2:
    content_file2 = file2.read()
print(content_file2)
print("...........===========================================================================")
# # reverse that content and create another file f3
reversed_content = content_file2[::-1]

with open("file3.txt", "w") as file3:
    file3.write(reversed_content)
with open("file3.txt", "r") as file3:
    content_file3 = file3.read()
print(content_file3)
