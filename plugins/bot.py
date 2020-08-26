#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


import os
from pyrogram import Client,Filters
from hurry.filesize import size
import requests
import shutil 

# Image Formats
ex_array = ['tiff', 'jpeg', 'jpg', 'gif', 'png']

# Keep track of the progress while uploading
async def progress(current, total):
    print("{:.1f}%".format(current * 100 / total))

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        
        chat_id=message.chat.id,
        text=f"<b>Hey {message.from_user.first_name},\nThis is an image download bot. Created using the available open-source code.\nSource Code: https://github.com/Abhijith-cloud/Telegram_URL_Image_UploadBot/ \n© @thankappan369</b>",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )

#Help cmd
@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    await client.send_message( 
        chat_id=message.chat.id,
        text=f"<b>Hey {message.from_user.first_name},\nBot to upload the image to Telegram from direct links.\ne.g: https://website.com/img.png \nContact Admin © @thankappan369</b>",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )



# This only pass http values   
@Client.on_message(Filters.regex(pattern=".*http.*"))
async def echo(bot , update):
    status = await bot.send_message(
        chat_id=update.chat.id,
        text=f"Processing your request...",
        reply_to_message_id=update.message_id  
    )
    
    #Get the Image Url
    image_url = str(update.text)

    #Real File Name
    img_name = image_url.split('/')[-1]

    #Get the Image extension
    image_url_ex = image_url.split('.')[-1]

    #Checking the extension
    if image_url_ex in ex_array:
        ex_av = image_url_ex
        # Set File Name
        filename = str(update.chat.id) + '.' + ex_av

        # Open the url image, set stream to True, this will return the stream content.
        req = requests.get(image_url, stream = True)

        # Check if the image was retrieved successfully
        if req.status_code == 200:

            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            req.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(req.raw, f)

            await status.edit_text(
                text=f'Downloading....'
            )
        else:
            await status.edit_text(
            text=f'The url is not valid'
        )

        await status.edit_text(
            text='Uploading....'
        )

        #File_Size
        img_size = os.path.getsize(filename)
        cnv_size = size(img_size)


        await status.edit_text(
            text=f'<b>File Name: {img_name}</b>\n<b>Size: {cnv_size}</b>',
            parse_mode = 'html'
        )

        try:
            # Send The Image to User
            await update.reply_photo(
                photo=filename,
                caption='@thankappan369',
                progress=progress

            )
            
            #delete old Messages
            # await status.delete()
        except Exception as error:
            await bot.send_message(
                chat_id=update.chat.id,
                text=f'Sorry Somting is\n{error}\nContact Admin @thankappan369'
            )
        try:
            os.remove(filename)
        except Exception as error:
            print(f'File not Removed {error}')



    else:
       await status.edit_text(
           text=f"This is not a image url"
       )
       
