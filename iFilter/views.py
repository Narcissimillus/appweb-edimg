from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images

iFilter = Blueprint('iFilter', __name__, template_folder='templates')

@iFilter.route('/blur_image', methods=['GET', 'POST'])
# Estompeaza imaginea
def blur_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.BLUR) # Micsoreaza claritatea imaginii
        im.save('static/uploads/img.png')
        image_url_blur = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_blur' : image_url_blur})

@iFilter.route('/bblur', methods=['GET', 'POST'])
# Estompeaza imaginea folosind BoxBlur
def bblur():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        radius = int(request.get_data()) # reprezinta raza blur-ului
        im_bblur = im.filter(ImageFilter.BoxBlur(radius)) # filtrul de Box Blur
        imgname = 'img_bblur_' + str(radius) + '.png'
        im_bblur.save('static/uploads/' + imgname)
        image_url_bblur = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_bblur' : image_url_bblur})

# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
@iFilter.route('/save_bblur', methods=['GET', 'POST'])
def save_bblur():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        radius = int(request.get_data())
        im = im.filter(ImageFilter.BoxBlur(radius))
        im.save('static/uploads/img.png')

@iFilter.route('/gblur', methods=['GET', 'POST'])
# Estompeaza imaginea folosind netezirea gaussiana
def gblur():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        radius = int(request.get_data()) # reprezinta raza blur-ului
        im_gblur = im.filter(ImageFilter.GaussianBlur(radius)) # filtrul de Gaussian Blur
        imgname = 'img_gblur_' + str(radius) + '.png'
        im_gblur.save('static/uploads/' + imgname)
        image_url_gblur = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_gblur' : image_url_gblur})

# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
@iFilter.route('/save_gblur', methods=['GET', 'POST'])
def save_gblur():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        radius = int(request.get_data())
        im = im.filter(ImageFilter.GaussianBlur(radius))
        im.save('static/uploads/img.png')

@iFilter.route('/sharpen_image', methods=['GET', 'POST'])
def sharpen_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.SHARPEN) # Mareste claritatea imaginii
        im.save('static/uploads/img.png')
        image_url_sharpen = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_sharpen' : image_url_sharpen})

@iFilter.route('/unsharp', methods=['GET', 'POST'])
# Mascarea Unsharp
def unsharp():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        trio = request.get_data(as_text=True)
        # Datele primite sunt separate in radius, strength, threshold si stocate toate intr-un tuple
        trio = trio.split('&')
        trio_radius = trio.pop(0)
        trio_radius =  trio_radius.split('=')
        trio_radius = int(trio_radius.pop())
        trio_strength = trio.pop(0)
        trio_strength =  trio_strength.split('=')
        trio_strength = int(trio_strength.pop())
        trio_threshold = trio.pop(0)
        trio_threshold =  trio_threshold.split('=')
        trio_threshold = int(trio_threshold.pop())
        im_unsharp = im.filter(ImageFilter.UnsharpMask(trio_radius, trio_strength, trio_threshold))
        imgname = 'img_unsharp_' + str(trio_radius) + str(trio_strength) + str(trio_threshold) + '.png'
        im_unsharp.save('static/uploads/' + imgname)
        image_url_unsharp = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_unsharp' : image_url_unsharp})

# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
@iFilter.route('/save_unsharp', methods=['GET', 'POST'])
def save_unsharp():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        trio = request.get_data(as_text=True)
        trio = trio.split('&')
        trio_radius = trio.pop(0)
        trio_radius =  trio_radius.split('=')
        trio_radius = int(trio_radius.pop())
        trio_strength = trio.pop(0)
        trio_strength =  trio_strength.split('=')
        trio_strength = int(trio_strength.pop())
        trio_threshold = trio.pop(0)
        trio_threshold =  trio_threshold.split('=')
        trio_threshold = int(trio_threshold.pop())
        im = im.filter(ImageFilter.UnsharpMask(trio_radius, trio_strength, trio_threshold))
        im.save('static/uploads/img.png')

@iFilter.route('/contour_image', methods=['GET', 'POST'])
def contour_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.CONTOUR) # Accentueaza conturul elementelor din imagine
        im.save('static/uploads/img.png')
        image_url_contour = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_contour' : image_url_contour})

@iFilter.route('/detail_image', methods=['GET', 'POST'])
def detail_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.DETAIL) # Indetaliaza imaginea
        im.save('static/uploads/img.png')
        image_url_detail = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_detail' : image_url_detail})

@iFilter.route('/edge_enhance_image', methods=['GET', 'POST'])
def edge_enhance_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.EDGE_ENHANCE) # Accentueaza marginile din imagine
        im.save('static/uploads/img.png')
        image_url_edge_enhance = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_edge_enhance' : image_url_edge_enhance})

@iFilter.route('/emboss_image', methods=['GET', 'POST'])
def emboss_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.EMBOSS) # Imprima in relief imaginea
        im.save('static/uploads/img.png')
        image_url_emboss = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_emboss' : image_url_emboss})

@iFilter.route('/smooth_image', methods=['GET', 'POST'])
def smooth_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.filter(ImageFilter.SMOOTH) # Netezeste imaginea
        im.save('static/uploads/img.png')
        image_url_smooth = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_smooth' : image_url_smooth})