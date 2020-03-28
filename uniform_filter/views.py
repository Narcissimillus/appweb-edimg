from flask import Blueprint, Flask, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images

uniform_filter = Blueprint('uniform_filter', __name__, template_folder='templates')

@uniform_filter.route('/uniform_filter_3x3', methods=['GET', 'POST'])
def unif_filt_3x3():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            # Masca uniforma 3x3 fara coeficientul 1/9
            uniform_mask = (
                1, 1, 1,
                1, 1, 1,
                1, 1, 1,
            )
            im_unif = im.filter(ImageFilter.Kernel((3,3),uniform_mask,scale=9))# scale reprezinta la cat se imparte uniform_mask (suma elementelor din ea)
            im_unif.save('static/uploads/img_unif_3x3.jpg')
            image_url_unif = url_for('static',filename="uploads/img_unif_3x3.jpg")
            return jsonify({'image_url_unif_3x3' : image_url_unif})
        except Exception as e:
            print(e)

@uniform_filter.route('/uniform_filter_5x5', methods=['GET', 'POST'])
def unif_filt_5x5():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            # Masca uniforma 5x5 fara coeficientul 1/25
            uniform_mask = (
                1, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
            )
            im_unif = im.filter(ImageFilter.Kernel((5,5),uniform_mask,scale=25))# scale reprezinta la cat se imparte uniform_mask (suma elementelor din ea)
            im_unif.save('static/uploads/img_unif_5x5.jpg')
            image_url_unif = url_for('static',filename="uploads/img_unif_5x5.jpg")
            return jsonify({'image_url_unif_5x5' : image_url_unif})
        except Exception as e:
            print(e)