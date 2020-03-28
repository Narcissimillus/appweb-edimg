from flask import Blueprint, Flask, request, url_for, jsonify
from PIL import Image, ImageFilter, ImageMath
from delete_processed_images.views import delete_images

kirsch_filter = Blueprint('kirsch_filter', __name__, template_folder='templates')

@kirsch_filter.route('/kirsch_filter_N', methods=['GET', 'POST'])
def kirsch_filt_N():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L") # convertire in imagine monocroma
            # Masca Kirsch nord pentru detectarea conturului fara coeficientul 1/15           
            kirsch_mask = (
                3, 3, 3,
                3, 0, 3,
                -5, -5, -5,
            )
            im_kirsch = im.filter(ImageFilter.Kernel((3,3),kirsch_mask,scale=15)) # scale => coeficientul 1/15 al kirsch_mask (se aduna toate elemente pozitive din masca => 15)
            im_kirsch.save('static/uploads/img_kirsch_N.jpg')
            image_url_kirsch = url_for('static',filename="uploads/img_kirsch_N.jpg")
            return jsonify({'image_url_kirsch_N' : image_url_kirsch})
        except Exception as e:
            print(e)

# Est
@kirsch_filter.route('/kirsch_filter_E', methods=['GET', 'POST'])
def kirsch_filt_E():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")            
            kirsch_mask = (
                -5, 3, 3,
                -5, 0, 3,
                -5, 3, 3,
            )
            im_kirsch = im.filter(ImageFilter.Kernel((3,3),kirsch_mask,scale=15))
            im_kirsch.save('static/uploads/img_kirsch_E.jpg')
            image_url_kirsch = url_for('static',filename="uploads/img_kirsch_E.jpg")
            return jsonify({'image_url_kirsch_E' : image_url_kirsch})
        except Exception as e:
            print(e)

# Sud
@kirsch_filter.route('/kirsch_filter_S', methods=['GET', 'POST'])
def kirsch_filt_S():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")            
            kirsch_mask = (
                -5, -5, -5,
                3, 0, 3,
                3, 3, 3,
            )
            im_kirsch = im.filter(ImageFilter.Kernel((3,3),kirsch_mask,scale=15))
            im_kirsch.save('static/uploads/img_kirsch_S.jpg')
            image_url_kirsch = url_for('static',filename="uploads/img_kirsch_S.jpg")
            return jsonify({'image_url_kirsch_S' : image_url_kirsch})
        except Exception as e:
            print(e)

# Vest
@kirsch_filter.route('/kirsch_filter_V', methods=['GET', 'POST'])
def kirsch_filt_V():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")            
            kirsch_mask = (
                3, 3, -5,
                3, 0, -5,
                3, 3, -5,
            )
            im_kirsch = im.filter(ImageFilter.Kernel((3,3),kirsch_mask,scale=15))
            im_kirsch.save('static/uploads/img_kirsch_V.jpg')
            image_url_kirsch = url_for('static',filename="uploads/img_kirsch_V.jpg")
            return jsonify({'image_url_kirsch_V' : image_url_kirsch})
        except Exception as e:
            print(e)