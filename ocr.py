import easyocr

reader = easyocr.Reader(["en"])
result = reader.readtext("./Bill.png")
for detection in result:
    print(detection[1])
