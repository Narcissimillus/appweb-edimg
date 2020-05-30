from flask import Blueprint, Flask, request, url_for, jsonify
from PIL import Image, ImageEnhance
from delete_processed_images.views import delete_images
import numpy as np

BCSS = Blueprint('BCSS', __name__, template_folder='templates')

@BCSS.route('/bright', methods=['GET', 'POST'])
def bright():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Brightness(im)
            factor = int(request.get_data())*2/100
            imgname = 'img_bright_' + str(factor) + '.jpg'
            im_bright = enhancer.enhance(factor)
            im_bright.save('static/uploads/' + imgname)
            image_url_bright = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_bright' : image_url_bright})
        except Exception as e:
            print(e)

@BCSS.route('/save_bright', methods=['GET', 'POST'])
def save_bright():
    if request.method == "POST":
        try:
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Brightness(im)
            factor = int(request.get_data())*2/100
            im = enhancer.enhance(factor)
            im.save('static/uploads/img.jpg')
        except Exception as e:
            print(e)

@BCSS.route('/contrast', methods=['GET', 'POST'])
def contrast():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Contrast(im)
            factor = int(request.get_data())*2/100
            imgname = 'img_contrast_' + str(factor) + '.jpg'
            im_contrast = enhancer.enhance(factor)
            im_contrast.save('static/uploads/' + imgname)
            image_url_contrast = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_contrast' : image_url_contrast})
        except Exception as e:
            print(e)

@BCSS.route('/save_contrast', methods=['GET', 'POST'])
def save_contrast():
    if request.method == "POST":
        try:
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Contrast(im)
            factor = int(request.get_data())*2/100
            im = enhancer.enhance(factor)
            im.save('static/uploads/img.jpg')
        except Exception as e:
            print(e)

@BCSS.route('/sharp', methods=['GET', 'POST'])
def sharp():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Sharpness(im)
            factor = int(request.get_data())*2/100
            imgname = 'img_sharp_' + str(factor) + '.jpg'
            im_sharp = enhancer.enhance(factor)
            im_sharp.save('static/uploads/' + imgname)
            image_url_sharp = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_sharp' : image_url_sharp})
        except Exception as e:
            print(e)

@BCSS.route('/save_sharp', methods=['GET', 'POST'])
def save_sharp():
    if request.method == "POST":
        try:
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Sharpness(im)
            factor = int(request.get_data())*2/100
            im = enhancer.enhance(factor)
            im.save('static/uploads/img.jpg')
        except Exception as e:
            print(e)

@BCSS.route('/sat', methods=['GET', 'POST'])
def sat():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Color(im)
            factor = int(request.get_data())*2/100
            imgname = 'img_sat_' + str(factor) + '.jpg'
            im_sat = enhancer.enhance(factor)
            im_sat.save('static/uploads/' + imgname)
            image_url_sat = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_sat' : image_url_sat})
        except Exception as e:
            print(e)

@BCSS.route('/save_sat', methods=['GET', 'POST'])
def save_sat():
    if request.method == "POST":
        try:
            image_src = 'static/uploads/img.jpg'
            im = Image.open(image_src)
            enhancer = ImageEnhance.Color(im)
            factor = int(request.get_data())*2/100
            im = enhancer.enhance(factor)
            im.save('static/uploads/img.jpg')
        except Exception as e:
            print(e)