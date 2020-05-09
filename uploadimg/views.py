from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from PIL import Image, ImageOps
import os

uploadimg = Blueprint('uploadimg', __name__, template_folder='templates')

apk = Flask(__name__)

# Permite incarcarea de fisiere doar de tip imagine (extensie .JPG, .PNG etc.)
photos = UploadSet('photos', IMAGES)

apk.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(apk, photos)
# Accepta fisiere <= 16MB
patch_request_class(apk, size=16777216)

@uploadimg.route('/uploadimg', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        try:
            if 'imgfile' in request.files:
                if os.path.exists("static/uploads/img.jpg"):
                    os.remove("static/uploads/img.jpg")
                imageFile = request.files['imgfile']
                filename = photos.save(imageFile,name='img.jpg')
        except Exception as e:
            print(e)
        image_url = "static/uploads/"+filename
        return jsonify({'image_url': image_url,
                        'rendered_left': render_template('panel_left.html'),
                        'rendered': render_template('panel.html')})
    else:
        return render_template('upload.html')



