from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image, ImageOps

process_image= Blueprint('process_image', __name__, template_folder='templates')

@process_image.route('/process_image/', methods=['GET', 'POST'])
def process_image():
    # filename = request.files['']
    processed_image = "Da am primit"
    return jsonify({'data':processed_image})
