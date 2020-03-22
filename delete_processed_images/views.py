from flask import Blueprint, Flask, render_template
import os

delete_processed_images = Blueprint('delete_processed_images', __name__, template_folder='templates')

@delete_processed_images.route('/delete_processed_images')
# Sterge imaginile create in functii precedente
def delete_images():
    if os.path.exists("static/uploads/img_rgb2gray.jpg"):
            os.remove("static/uploads/img_rgb2gray.jpg")
    if os.path.exists("static/uploads/img_unif.jpg"):
            os.remove("static/uploads/img_unif.jpg")
    if os.path.exists("static/uploads/img_gauss.jpg"):
            os.remove("static/uploads/img_gauss.jpg")
    return 1