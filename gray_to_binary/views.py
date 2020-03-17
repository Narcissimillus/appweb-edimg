from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
#from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image, ImageOps
import numpy as np
import os

gray_to_binary = Blueprint('gray_to_binary', __name__, template_folder='templates')

@gray_to_binary.route('/gray_to_binary', methods=['GET', 'POST'])
def im2bw():
    if request.method == "POST":
        try:
            if os.path.exists("static/uploads/img_processed.jpg"):
                os.remove("static/uploads/img_processed.jpg")
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")
            # im.save('static/uploads/img_processed.jpg')
            pixels = np.array(im)
            prag = request.prompt['prag']
            [x, y] = pixels.shape
            for i in range(x):
                for j in range(y):
                    if pixels[i][j] >= prag:
                        pixels[i][j] = 255
                    else:
                        pixels[i][j] = 0
            im_bw = Image.fromarray(pixels)
            im_bw.save('static/uploads/img_bw.jpg')
            image_url_bw= url_for('static',filename="uploads/img_bw.jpg")
            return jsonify({'image_url_bw' : image_url_bw})
        except Exception as e:
            print(e)
