from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageEnhance
from delete_processed_images.views import delete_images

iEnhance = Blueprint('iEnhance', __name__, template_folder='templates')

# Se foloseste aceeasi interfata in modulul ImageEnhance

@iEnhance.route('/bright', methods=['GET', 'POST'])
# Previzualizare pentru butonul Brightness
def bright():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        # enhancer reprezinta o imagine pregatita pentru a i se modifica luminozitatea, acesteia i se va aplica o metoda comuna enhace(factor), adica interfata
        enhancer = ImageEnhance.Brightness(im)
        # Convertim datele primite care apartin [0,100] in date care apartin [0,2]
        # Pentru factor = 1 imaginea este cea originala, valori din ce in ce mai mici (<1) imaginea devine din ce in ce mai intunecata 
        # si pentru valori din ce in ce mai mari (>1) imaginea devine din ce in ce mai luminata
        factor = int(request.get_data())*2/100
        imgname = 'img_bright_' + str(factor) + '.png' # o noua imagine este salvata la fiecare valoare selectata
        im_bright = enhancer.enhance(factor)
        im_bright.save('static/uploads/' + imgname)
        image_url_bright = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_bright' : image_url_bright})

@iEnhance.route('/save_bright', methods=['GET', 'POST'])
# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
def save_bright():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Brightness(im)
        factor = int(request.get_data())*2/100
        im = enhancer.enhance(factor)
        im.save('static/uploads/img.png')

# Idem ca la Brightness
@iEnhance.route('/contrast', methods=['GET', 'POST'])
# Previzualizare pentru butonul Contrast
def contrast():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Contrast(im)
        factor = int(request.get_data())*2/100
        imgname = 'img_contrast_' + str(factor) + '.png'
        im_contrast = enhancer.enhance(factor)
        im_contrast.save('static/uploads/' + imgname)
        image_url_contrast = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_contrast' : image_url_contrast})

# Idem ca la Brightness
@iEnhance.route('/save_contrast', methods=['GET', 'POST'])
def save_contrast():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Contrast(im)
        factor = int(request.get_data())*2/100
        im = enhancer.enhance(factor)
        im.save('static/uploads/img.png')

# Idem ca la Brightness
@iEnhance.route('/sharp', methods=['GET', 'POST'])
# Previzualizare pentru butonul Sharpness
def sharp():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Sharpness(im)
        factor = int(request.get_data())*2/100
        imgname = 'img_sharp_' + str(factor) + '.png'
        im_sharp = enhancer.enhance(factor)
        im_sharp.save('static/uploads/' + imgname)
        image_url_sharp = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_sharp' : image_url_sharp})

# Idem ca la Brightness
@iEnhance.route('/save_sharp', methods=['GET', 'POST'])
def save_sharp():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Sharpness(im)
        factor = int(request.get_data())*2/100
        im = enhancer.enhance(factor)
        im.save('static/uploads/img.png')

# Idem ca la Brightness
@iEnhance.route('/sat', methods=['GET', 'POST'])
# Previzualizare pentru butonul Saturation
def sat():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Color(im)
        factor = int(request.get_data())*2/100
        imgname = 'img_sat_' + str(factor) + '.png'
        im_sat = enhancer.enhance(factor)
        im_sat.save('static/uploads/' + imgname)
        image_url_sat = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_sat' : image_url_sat})

# Idem ca la Brightness
@iEnhance.route('/save_sat', methods=['GET', 'POST'])
def save_sat():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        enhancer = ImageEnhance.Color(im)
        factor = int(request.get_data())*2/100
        im = enhancer.enhance(factor)
        im.save('static/uploads/img.png')