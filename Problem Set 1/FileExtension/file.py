file = input("Filename: ")
file = file.lower()
if ".gif" in file:
    print("image/gif")
elif ".txt" in file:
    print("image/txt")
elif ".zip" in file:
    print("image/zip")
elif ".pdf" in file:
    print("image/pdf")
elif ".png" in file:
    print("image/png")
elif ".jpg" in file:
    print("image/jpeg")
elif "jpeg" in file:
    print("image/jpeg")
else:
    print("application/octet-steam")