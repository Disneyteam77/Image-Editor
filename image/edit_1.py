# By @TroJanzHEX

import pyrogram
import cv2
from PIL import Image,ImageEnhance,ImageFilter



async def bright(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    image = Image.open(a)
    brightness=ImageEnhance.Brightness(image)
    brightness.enhance(1.5).save('brightness.jpg')
    await message.reply_chat_action("upload_photo")
    await message.reply_to_message.reply_photo("brightness.jpg", quote=True)
    await msg.delete()    

      
async def mix(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    image = Image.open(a)
    red, green, blue = image.split()
    new_image = Image.merge("RGB", (green, red, blue))
    new_image.save('mix.jpg')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_to_message.reply_photo("mix.jpg", quote=True)

async def black_white(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    image_file =  cv2.imread(a)
    grayImage = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("black_white.jpg",grayImage)
    await msg.delete()
    await message.reply_chat_action("upload_photo")
   
    await message.reply_to_message.reply_photo("black_white.jpg", quote=True)
    
async def normal_blur(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    OriImage = Image.open(a)
    blurImage = OriImage.filter(ImageFilter.BLUR)
    blurImage.save('BlurImage.jpg')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
   
    await message.reply_to_message.reply_photo("BlurImage.jpg", quote=True)

async def g_blur(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    im1 = Image.open(a)
    im2 = im1.filter(ImageFilter.GaussianBlur(radius = 5)) 
    im2.save("gaussian_blur.jpg")
    await msg.delete()
    await message.reply_chat_action("upload_photo")
   
    await message.reply_to_message.reply_photo("gaussian_blur.jpg", quote=True)

async def box_blur(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    im1 = Image.open(a)
    im2 = im1.filter(ImageFilter.BoxBlur(0))
    im2.save("box_blur.jpg")
    await msg.delete()
    
    await message.reply_chat_action("upload_photo")
   
    await message.reply_to_message.reply_photo("box_blur.jpg", quote=True)
