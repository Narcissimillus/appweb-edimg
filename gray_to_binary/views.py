from flask import Blueprint, render_template, Flask, request, url_for, jsonify
from PIL import Image
from delete_processed_images.views import delete_images
import numpy as np
import os

gray_to_binary = Blueprint('gray_to_binary', __name__, template_folder='templates')

@gray_to_binary.route('/gray_to_binary', methods=['GET', 'POST'])
def im2bw():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L") # imaginea devine monocroma
            pixels = np.array(im, dtype=np.uint8) # matricea pixelilor imaginii
            text = request.get_data().decode('UTF-8') # preluam sub forma de string, data din front-end: prag si count (nr. click-uri buton)
            textsplit = text.split('.') # separam prag si count
            prag = int(textsplit[0])
            count = "img_bw_" + textsplit[1] + ".jpg" # count va deveni numele imaginii curente
            [x, y] = pixels.shape # dimensiunile imaginii
            for i in range(x):
                for j in range(y):
                    # ce este peste prag devine alb, ce este sub prag, devine negru
                    if pixels[i][j] >= prag:
                        pixels[i][j] = 255
                    else:
                        pixels[i][j] = 0
            im_bw = Image.fromarray(pixels) # transformare din matricea de pixeli (numere) in imagine binara
            im_bw.save('static/uploads/' + count)
            image_url_bw= url_for('static',filename="uploads/" + count)
            return jsonify({'image_url_bw' : image_url_bw})
        except Exception as e:
            print(e)
