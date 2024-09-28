from instagrapi import Client
import os

class ReadInstaEnvs:
    def __init__(self) -> None:
        self.insta_user = os.getenv('INSTA_USERNAME')
        self.insta_pass = os.getenv('INSTA_PASSWORD')
        self.image_path = os.getenv('INSTA_PATH')


class Instaops:
    def __init__(self) -> None:
        self.client = None

    def login(self, login_name, login_pass):
        """ login into account """
        self.client = Client()
        self.client.login(username=login_name, password=login_pass)
        user_info = self.client.user_info(self.client.user_id)  # Example action to verify login

    def upload_image(self, img_path, img_caption):
        """ Upload image """
        self.client.photo_upload(img_path, caption=img_caption)
        print("Image Uploaded!")


if __name__ == "__main__":
    """ main method """

    # Read Env Variables
    instavars = ReadInstaEnvs()
    
    # Instatiate Instragram Operations Class and login
    instaobj = Instaops()
    instaobj.login(instavars.insta_user, instavars.insta_pass)

    # Post a photo to Insta account
    image_file = f"{instavars.image_path}/sf-bridge-01.jpg"
    print (f"{image_file}")
    instaobj.upload_image(
        image_file,
        "Update 06"
    )
