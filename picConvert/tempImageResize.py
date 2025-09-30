import os
from PIL import Image

pic=[]
picd = os.listdir('oldpic')
for i in picd:
    pic.append(str(i))

imgf = Image.open('fon.jpeg')
    width, height = imgf.size
    imgf.load()
    #type(img)
    isinstance(imgf, Image.Image)

for filename in pic:
    #print(filename)
    img=Image.open('oldpic//'+filename)
    width, height = img.size
    img.load()
    #type(img)
    isinstance(img, Image.Image)
    
    temp_pic = img.crop((0,0,800,800))
    temp_pic = temp_pic.resize((600,800))
    img.paste(imgf, (0, 0, 800, 800))
    img.paste(temp_pic, (100, 0, 700, 800))

    #сжатие
    #new_img = img.resize((800,800))
            #low_res_img.show()
    #сохранение
    img.save("pic//"+filename)
print('Ok')




# а можно, например, повернуть и вставить обратно
#rotated_face = one_face.transpose(Image.ROTATE_180)
#family_image.paste(rotated_face, (240, 42, 450, 312))

#family_image.save("family_with_rotated_face.png"
