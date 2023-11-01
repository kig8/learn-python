file_name = input("File name: ")
"application/octet-stream"


match file_name:  # cat.jpg
    case file_name if file_name.endswith(".gif"):
        print("image/gif")
    case file_name if file_name.endswith(".jpg"):
        print("image/jpg")
    case _:
        print("valami")
