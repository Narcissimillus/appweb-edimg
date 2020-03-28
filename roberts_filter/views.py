from flask import Blueprint, Flask, request, url_for, jsonify
from PIL import Image, ImageFilter, ImageMath
from delete_processed_images.views import delete_images

roberts_filter = Blueprint('roberts_filter', __name__, template_folder='templates')

@roberts_filter.route('/roberts_filter_N', methods=['GET', 'POST'])
def roberts_filt_N():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L") # convertire in imagine monocroma
            # Masca Roberts nord pentru detectarea conturului            
            roberts_mask = (
                0, 1, 0,
                0, -1, 0,
                0, 0, 0,
            )
            im_roberts = im.filter(ImageFilter.Kernel((3,3),roberts_mask,scale=1))
            im_roberts.save('static/uploads/img_roberts_N.jpg')
            image_url_roberts = url_for('static',filename="uploads/img_roberts_N.jpg")
            return jsonify({'image_url_roberts_N' : image_url_roberts})
        except Exception as e:
            print(e)

@roberts_filter.route('/roberts_filter_E', methods=['GET', 'POST'])
def roberts_filt_E():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")    
            # Masca Roberts est pentru detectarea conturului         
            roberts_mask = (
                0, 0, 0,
                0, -1, 1,
                0, 0, 0,
            )
            im_roberts = im.filter(ImageFilter.Kernel((3,3),roberts_mask,scale=1))
            im_roberts.save('static/uploads/img_roberts_E.jpg')
            image_url_roberts = url_for('static',filename="uploads/img_roberts_E.jpg")
            return jsonify({'image_url_roberts_E' : image_url_roberts})
        except Exception as e:
            print(e)

@roberts_filter.route('/roberts_filter_S', methods=['GET', 'POST'])
def roberts_filt_S():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")      
            # Masca Roberts sud pentru detectarea conturului       
            roberts_mask = (
                0, 0, 0,
                0, -1, 0,
                0, 1, 0,
            )
            im_roberts = im.filter(ImageFilter.Kernel((3,3),roberts_mask,scale=1))
            im_roberts.save('static/uploads/img_roberts_S.jpg')
            image_url_roberts = url_for('static',filename="uploads/img_roberts_S.jpg")
            return jsonify({'image_url_roberts_S' : image_url_roberts})
        except Exception as e:
            print(e)

@roberts_filter.route('/roberts_filter_V', methods=['GET', 'POST'])
def roberts_filt_V():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src).convert(mode="L")
            # Masca Roberts vest pentru detectarea conturului             
            roberts_mask = (
                0, 0, 0,
                1, -1, 0,
                0, 0, 0,
            )
            im_roberts = im.filter(ImageFilter.Kernel((3,3),roberts_mask,scale=1))
            im_roberts.save('static/uploads/img_roberts_V.jpg')
            image_url_roberts = url_for('static',filename="uploads/img_roberts_V.jpg")
            return jsonify({'image_url_roberts_V' : image_url_roberts})
        except Exception as e:
            print(e)