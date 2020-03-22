from flask import Blueprint, Flask, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images

gauss_filter = Blueprint('gauss_filter', __name__, template_folder='templates')

@gauss_filter.route('/gauss_filter', methods=['GET', 'POST'])
def gauss_filt():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            # Masca Gauss 3x3 fara coeficientul 1/16
            gauss_mask = (
                1, 2, 1,
                2, 4, 2,
                1, 2, 1,
            )
            im_gauss = im.filter(ImageFilter.Kernel((3,3),gauss_mask,scale=16))  # scale reprezinta la cat se imparte gauss_mask (suma elementelor din ea)
            im_gauss.save('static/uploads/img_gauss.jpg')
            image_url_gauss = url_for('static',filename="uploads/img_gauss.jpg")
            return jsonify({'image_url_gauss' : image_url_gauss})
        except Exception as e:
            print(e)