from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image, ImageOps
import base64

uploadimg = Blueprint('uploadimg', __name__, template_folder='templates')

apk = Flask(__name__)

photos = UploadSet('photos', IMAGES)

apk.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(apk, photos)

@uploadimg.route('/uploadimg', methods=['GET', 'POST'])
def upload():
    # if request.method == 'POST':
    #     filename = photos.save(request.files['image'])
    #     opened = Image.open(filename)
    #     opened.show()
    #     #im_gray = rgb2gray(filename)
    #     rendered = render_template('process.html', image_url = "uploads/"+filename)
    #     return jsonify({'rendered':rendered})
    if request.method == "POST":
        try:
            if 'file' in request.files:
                imageFile = request.files['file']
                filename = save_image(imageFile)
                # opened = Image.open(imageFile)
                # opened.show()
        except Exception as e:
            print(e)
        image_url = "uploads/"+filename
        return jsonify({'image_url' : image_url})
    else:
        return render_template('upload.html')

@uploadimg.route('/uploaded', methods=['GET', 'POST'])
def uploaded():
    pass

def save_image(file):
    return photos.save(file)

def rgb2gray(filename):
    image_src = 'static/uploads/'+filename
    #new_filename = 'gray_'+filename
    im = Image.open(image_src)
    imm = ImageOps.grayscale(im)
    #imm.save('static/uploads/'+new_filename)
    return imm

