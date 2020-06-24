from flask import Blueprint, request, url_for, jsonify
from delete_processed_images.views import delete_images
from PIL import Image

rgb_to_gray = Blueprint('rgb_to_gray', __name__, template_folder='templates')

@rgb_to_gray.route('/rgb_to_gray', methods=['GET', 'POST'])
def rgb2gray():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im_gray = Image.open(image_src).convert(mode='L') # Transformam imaginea din RGB in monocrom
        im_gray.save('static/uploads/img_rgb2gray.png')
        image_url_gray = url_for('static',filename="uploads/img_rgb2gray.png")
        return jsonify({'image_url_gray' : image_url_gray})
