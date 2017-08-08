# coding: utf-8

import sys
from io import BytesIO
from PIL import Image


def compress(image, rate):
    buffer = BytesIO()
    image.save(buffer, "JPEG", quality=(95-rate))

    if len(buffer.getvalue()) < file_size:
        with open(new_img_name,"wb") as f:
            f.write(buffer.getvalue())
        return True
    else:
        return False

    buffer.close()


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

    # It can be compressed to specified size or less
    if compress(img, 94):

        # compression ratio: 0 -> 47
        if compress(img, 47):
            for i in range(48):
                if compress(img, i):
                    print("Succeed!, compression rate: {}".format(95-i))
                    break

        # compression ratio: 48 -> 95
        else:
            for i in range(47):
                if compress(img, i+48):
                    print("Succeed!, compression rate: {}".format(95-48-i))
                    break

    # impossible
    else:
        print("Error: can not compress to the specified size")

else:
    print("Error: input error")
    print("python3 compress_image.py IMAGE_PATH DESIRED_SIZE(KB)")
