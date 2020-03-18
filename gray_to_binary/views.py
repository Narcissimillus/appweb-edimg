from flask import Blueprint, render_template, Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from PIL import Image
from delete_processed_images.views import delete_images
import numpy as np
import datetime
import os

gray_to_binary = Blueprint('gray_to_binary', __name__, template_folder='templates')

@gray_to_binary.route('/gray_to_binary', methods=['GET', 'POST'])
def im2bw():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")
            pixels = np.array(im)
            text = request.get_data().decode('UTF-8')
            textsplit = text.split('.')
            prag = int(textsplit[0])
            count = textsplit[1]+".jpg"
            del_img = str(int(textsplit[1])-1)+".jpg"
            if os.path.exists("static/uploads/" + del_img):
                os.remove("static/uploads/" + del_img)
            print(prag, count)
            [x, y] = pixels.shape
            for i in range(x):
                for j in range(y):
                    if pixels[i][j] >= prag:
                        pixels[i][j] = 255
                    else:
                        pixels[i][j] = 0
            im_bw = Image.fromarray(pixels)
            # time = datetime.datetime.now().strftime("%H-%M-%S-%f")+".jpg"
            im_bw.save('static/uploads/' + count)
            image_url_bw= url_for('static',filename="uploads/" + count)
            return jsonify({'image_url_bw' : image_url_bw})
        except Exception as e:
            print(e)
