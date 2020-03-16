from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image, ImageOps
import os

rgb_to_gray = Blueprint('rgb_to_gray', __name__, template_folder='templates')

@rgb_to_gray.route('/rgb_to_gray', methods=['GET', 'POST'])
def rgb2gray():
    if request.method == "POST":
        try:
            if os.path.exists("static/uploads/img_processed.jpg"):
                    os.remove("static/uploads/img_processed.jpg")
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            im_gray = ImageOps.grayscale(im)
            im_gray.save('static/uploads/img_processed.jpg')
            image_url_gray = url_for('static',filename="uploads/img_processed.jpg")
            return jsonify({'image_url_gray' : image_url_gray})
        except Exception as e:
            print(e)
