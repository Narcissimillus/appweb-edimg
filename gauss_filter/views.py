from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images

gauss_filter = Blueprint('gauss_filter', __name__, template_folder='templates')

@gauss_filter.route('/gauss_filter_3x3', methods=['GET', 'POST'])
# Filtrare cu masca Gauss 3x3
def gauss_filt_3x3():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Masca Gauss 3x3 fara coeficientul 1/16
            gauss_mask = (
                1, 2, 1,
                2, 4, 2,
                1, 2, 1,
            )
            im_gauss = im.filter(ImageFilter.Kernel((3,3),gauss_mask,scale=16))  # scale reprezinta la cat se imparte gauss_mask (suma elementelor din ea)
            im_gauss.save('static/uploads/img_gauss_3x3.png')
            image_url_gauss = url_for('static',filename="uploads/img_gauss_3x3.png")
            return jsonify({'image_url_gauss_3x3' : image_url_gauss})
        except Exception as e:
            print(e)

# Filtrare cu masca Gauss 5x5
@gauss_filter.route('/gauss_filter_5x5', methods=['GET', 'POST'])
def gauss_filt_5x5():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Masca Gauss 5x5 fara coeficientul 1/256
            gauss_mask = (
                1, 4, 6, 4, 1,
                4, 16, 24, 16, 4,
                6, 24, 36, 24, 6,
                4, 16, 24, 16, 4,
                1, 4, 6, 4, 1,
            )
            im_gauss = im.filter(ImageFilter.Kernel((5,5),gauss_mask,scale=256))  # scale reprezinta la cat se imparte gauss_mask (suma elementelor din ea)
            im_gauss.save('static/uploads/img_gauss_5x5.png')
            image_url_gauss = url_for('static',filename="uploads/img_gauss_5x5.png")
            return jsonify({'image_url_gauss_5x5' : image_url_gauss})
        except Exception as e:
            print(e)