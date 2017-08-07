# coding: utf-8

import sys
from io import BytesIO
from PIL import Image


argvs = sys.argv

if len(argvs) == 3:
    try:
        img_name = argvs[1]
        img = Image.open(img_name)
    except:
        print("Error: can not open image")

    file_size = int(argvs[2]) * 1000
    splited_name =img_name.split(".")
    new_img_name = splited_name[0]+"_compressed."+".".join(splited_name[1:])

    for i in range(100):
        buffer = BytesIO()
        img.save(buffer, "JPEG", quality=(100-i))

        if len(buffer.getvalue()) < file_size:
            with open(new_img_name,"wb") as f:
                f.write(buffer.getvalue())
            break
        elif i >= 99:
            print("Error: can not compress to the specified size")

else:
    print("Error: input error")
    print("python3 compress_image.py IMAGE_PATH DESIRED_SIZE(KB)")
