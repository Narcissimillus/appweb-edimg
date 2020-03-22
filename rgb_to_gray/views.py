from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from delete_processed_images.views import delete_images
from PIL import Image

rgb_to_gray = Blueprint('rgb_to_gray', __name__, template_folder='templates')

@rgb_to_gray.route('/rgb_to_gray', methods=['GET', 'POST'])
def rgb2gray():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im_gray = Image.open(image_src).convert(mode='L') # Transformam imaginea din RGB in monocrom
            im_gray.save('static/uploads/img_rgb2gray.jpg')
            image_url_gray = url_for('static',filename="uploads/img_rgb2gray.jpg")
            return jsonify({'image_url_gray' : image_url_gray})
        except Exception as e:
            print(e)
