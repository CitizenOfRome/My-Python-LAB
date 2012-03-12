from PIL import Image
img = Image.open("C:\\Users\\User\\Dummy.png")
data = img.getdata()
newdata = list()
for item in data:
    if item==(0,0,0,0):
        newdata.append(item)
    else:
        newdata.append((150,0,0,0))
img.putdata(newdata)
img.save("d2.png", "PNG")
