from flask import Blueprint
import os

delete_processed_images = Blueprint('delete_processed_images', __name__, template_folder='templates')

@delete_processed_images.route('/delete_processed_images')
# Sterge imaginile create in functii precedente
def delete_images():
        updir = 'static/uploads/'
        imglist = [ im for im in os.listdir(updir) if im.startswith("img_") ]
        for im in imglist:
                os.remove(os.path.join(updir, im))
        return 1