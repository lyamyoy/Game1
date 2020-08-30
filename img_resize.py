from PIL import Image

img=Image.open('./images/ships3.png')
img_resize=img.resize((60, 60))
img_rotate=img.transpose(Image.ROTATE_180)
img_rotate.save('./images/shooter.png')
