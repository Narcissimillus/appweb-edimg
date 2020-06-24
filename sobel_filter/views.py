from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images

sobel_filter = Blueprint('sobel_filter', __name__, template_folder='templates')

# Filtrul mastii Sobel Nord
@sobel_filter.route('/sobel_filter_N', methods=['GET', 'POST'])
def sobel_filt_N():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L") # convertire in imagine monocroma
            # Masca Sobel nord pentru detectarea conturului fara coeficientul 1/4            
            sobel_mask = (
                1, 2, 1,
                0, 0, 0,
                -1, -2, -1,
            )
            im_sobel = im.filter(ImageFilter.Kernel((3,3),sobel_mask,scale=4)) # scale => coeficientul 1/4 al sobel_mask (se aduna toate elemente pozitive din masca => 4)
            im_sobel.save('static/uploads/img_sobel_N.png')
            image_url_sobel = url_for('static',filename="uploads/img_sobel_N.png")
            return jsonify({'image_url_sobel_N' : image_url_sobel})
        except Exception as e:
            print(e)

# Filtrul mastii Sobel Est
@sobel_filter.route('/sobel_filter_E', methods=['GET', 'POST'])
def sobel_filt_E():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L")            
            sobel_mask = (
                -1, 0, 1,
                -2, 0, 2,
                -1, 0, 1,
            )
            im_sobel = im.filter(ImageFilter.Kernel((3,3),sobel_mask,scale=4))
            im_sobel.save('static/uploads/img_sobel_E.png')
            image_url_sobel = url_for('static',filename="uploads/img_sobel_E.png")
            return jsonify({'image_url_sobel_E' : image_url_sobel})
        except Exception as e:
            print(e)

# Filtrul mastii Sobel Sud
@sobel_filter.route('/sobel_filter_S', methods=['GET', 'POST'])
def sobel_filt_S():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L")            
            sobel_mask = (
                -1, -2, -1,
                0, 0, 0,
                1, 2, 1,
            )
            im_sobel = im.filter(ImageFilter.Kernel((3,3),sobel_mask,scale=4))
            im_sobel.save('static/uploads/img_sobel_S.png')
            image_url_sobel = url_for('static',filename="uploads/img_sobel_S.png")
            return jsonify({'image_url_sobel_S' : image_url_sobel})
        except Exception as e:
            print(e)

# Filtrul mastii Sobel Vest
@sobel_filter.route('/sobel_filter_V', methods=['GET', 'POST'])
def sobel_filt_V():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src).convert(mode="L")            
            sobel_mask = (
                1, 0, -1,
                2, 0, -2,
                1, 0, -1,
            )
            im_sobel = im.filter(ImageFilter.Kernel((3,3),sobel_mask,scale=4))
            im_sobel.save('static/uploads/img_sobel_V.png')
            image_url_sobel = url_for('static',filename="uploads/img_sobel_V.png")
            return jsonify({'image_url_sobel_V' : image_url_sobel})
        except Exception as e:
            print(e)