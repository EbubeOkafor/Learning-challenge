file = input()
file = file.lower()
print(f"Filename: {file}")
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
elif ".jpg" or "jpeg" in file:
    print("image/jpeg")
else:
    print("application/octet-steam")