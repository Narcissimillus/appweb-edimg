from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image, ImageOps
from numpy import asarray

uploadimg = Blueprint('uploadimg', __name__, template_folder='templates')

apk = Flask(__name__)

photos = UploadSet('photos', IMAGES)

apk.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(apk, photos)

@uploadimg.route('/uploadimg', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'image' in request.files:
        filename = photos.save(request.files['image'])
        im_gray = rgb2gray(filename)
        return render_template('uploaded.html', image_url = "uploads/"+filename, image_url_gray = "uploads/"+im_gray)
    return render_template('upload.html')

def rgb2gray(filename):
    image_src = 'static/uploads/'+filename
    new_filename = 'gray_'+filename
    im = Image.open(image_src)
    imm = ImageOps.grayscale(im)
    imm.save('static/uploads/'+new_filename)
    return new_filename

