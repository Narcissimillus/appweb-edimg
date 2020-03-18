from flask import Blueprint, Flask, render_template
import os

delete_processed_images = Blueprint('delete_processed_images', __name__, template_folder='templates')

@delete_processed_images.route('/delete_processed_images')
def delete_images():
    if os.path.exists("static/uploads/img_rgb2gray.jpg"):
            os.remove("static/uploads/img_rgb2gray.jpg")
    return 1