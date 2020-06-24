from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images

prewitt_filter = Blueprint('prewitt_filter', __name__, template_folder='templates')

# Masca Prewitt Nord
@prewitt_filter.route('/prewitt_filter_N', methods=['GET', 'POST'])
def prewitt_filt_N():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L") # convertire in imagine monocroma
            # Masca Prewitt nord pentru detectarea conturului fara coeficientul 1/3            
            prewitt_mask = (
                1, 1, 1,
                0, 0, 0,
                -1, -1, -1,
            )
            im_prewitt = im.filter(ImageFilter.Kernel((3,3),prewitt_mask,scale=3)) # scale => coeficientul 1/3 al prewitt_mask (se aduna toate elemente pozitive din masca => 3)
            im_prewitt.save('static/uploads/img_prewitt_N.png')
            image_url_prewitt = url_for('static',filename="uploads/img_prewitt_N.png")
            return jsonify({'image_url_prewitt_N' : image_url_prewitt})
        except Exception as e:
            print(e)

# Masca Prewitt Est
@prewitt_filter.route('/prewitt_filter_E', methods=['GET', 'POST'])
def prewitt_filt_E():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L")            
            prewitt_mask = (
                -1, 0, 1,
                -1, 0, 1,
                -1, 0, 1,
            )
            im_prewitt = im.filter(ImageFilter.Kernel((3,3),prewitt_mask,scale=3))
            im_prewitt.save('static/uploads/img_prewitt_E.png')
            image_url_prewitt = url_for('static',filename="uploads/img_prewitt_E.png")
            return jsonify({'image_url_prewitt_E' : image_url_prewitt})
        except Exception as e:
            print(e)

# Masca Prewitt Sud
@prewitt_filter.route('/prewitt_filter_S', methods=['GET', 'POST'])
def prewitt_filt_S():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L")            
            prewitt_mask = (
                -1, -1, -1,
                0, 0, 0,
                1, 1, 1,
            )
            im_prewitt = im.filter(ImageFilter.Kernel((3,3),prewitt_mask,scale=3))
            im_prewitt.save('static/uploads/img_prewitt_S.png')
            image_url_prewitt = url_for('static',filename="uploads/img_prewitt_S.png")
            return jsonify({'image_url_prewitt_S' : image_url_prewitt})
        except Exception as e:
            print(e)

# Masca Prewitt Vest
@prewitt_filter.route('/prewitt_filter_V', methods=['GET', 'POST'])
def prewitt_filt_V():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L")            
            prewitt_mask = (
                1, 0, -1,
                1, 0, -1,
                1, 0, -1,
            )
            im_prewitt = im.filter(ImageFilter.Kernel((3,3),prewitt_mask,scale=3))
            im_prewitt.save('static/uploads/img_prewitt_V.png')
            image_url_prewitt = url_for('static',filename="uploads/img_prewitt_V.png")
            return jsonify({'image_url_prewitt_V' : image_url_prewitt})
        except Exception as e:
            print(e)