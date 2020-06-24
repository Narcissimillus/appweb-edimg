from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageOps
from delete_processed_images.views import delete_images

iOps = Blueprint('iOps', __name__, template_folder='templates')

@iOps.route('/autocont', methods=['GET', 'POST'])
# Autocontrast
def autocont():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = ImageOps.autocontrast(im) # Selecteaza cel mai luminos pixel si il face alb, si cel mai intunecat pixel si il face negru, restul se normalizeaza
        im.save('static/uploads/img.png')
        image_url_autocont = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_autocont' : image_url_autocont})

@iOps.route('/scalare', methods=['GET', 'POST'])
# Scale
def scalare():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        # Convertim datele primite care apartin [0,100] in date care apartin [0,2]
        # Pentru factor = 1 imaginea este cea originala, valori din ce in ce mai mici (<1) imaginea se micsoreaza
        # si pentru valori din ce in ce mai mari (>1) imaginea se mareste
        factor = int(request.get_data())*2/100
        im_scale = ImageOps.scale(im, factor)
        imgname = 'img_scale_' + str(factor) + '.png'
        im_scale.save('static/uploads/' + imgname)
        image_url_scale = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_scale' : image_url_scale})

# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
@iOps.route('/save_scale', methods=['GET', 'POST'])
def save_scale():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        factor = int(request.get_data())*2/100
        im = ImageOps.scale(im, factor)
        im.save('static/uploads/img.png')

@iOps.route('/flip_image', methods=['GET', 'POST'])
def flip_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = ImageOps.flip(im) # Intoarce imaginea vertical (de sus in jos)
        im.save('static/uploads/img.png')
        image_url_flip = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_flip' : image_url_flip})

@iOps.route('/mirror_image', methods=['GET', 'POST'])
def mirror_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im= ImageOps.mirror(im) # Intoarce imaginea orizontal (in oglinda, de la stanga la dreapta)
        im.save('static/uploads/img.png')
        image_url_mirror = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_mirror' : image_url_mirror})

@iOps.route('/invert_image', methods=['GET', 'POST'])
def invert_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = ImageOps.invert(im) # Inverseaza culorile imaginii => negativul imaginii
        im.save('static/uploads/img.png')
        image_url_invert = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_invert' : image_url_invert})

@iOps.route('/cropper', methods=['GET', 'POST'])
# Crop
def cropper():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        width, height = im.size # Latimea si inaltimea imaginii
        box = request.get_data(as_text=True)
        # Datele primite sunt separate in left, upper, right, lower si stocate toate intr-un tuple
        box = box.split('&')
        box_left = box.pop(0)
        print(box_left)
        box_left =  box_left.split('=')
        box_left = int(box_left.pop())*width/100 # Datele primite de la client sunt transformate din procente in dimensiuni in pixeli ale imaginii
        box_upper = box.pop(0)
        box_upper =  box_upper.split('=')
        box_upper = int(box_upper.pop())*height/100
        box_right = box.pop(0)
        box_right =  box_right.split('=')
        box_right = int(box_right.pop())*width/100
        box_lower = box.pop(0)
        box_lower =  box_lower.split('=')
        box_lower = int(box_lower.pop())*height/100
        box_tuple = box_left, box_upper, box_right, box_lower # Tuple-ul unde sunt memorate datele modificate
        im_crop = im.crop(box_tuple) # Se taie imaginea dupa coordonatele imaginii stanga,sus,dreapta,jos
        imgname = 'img_crop_' + str(box_tuple[0]) + str(box_tuple[1]) + str(box_tuple[2]) + str(box_tuple[3]) + '.png'
        im_crop.save('static/uploads/' + imgname)
        image_url_crop = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_crop' : image_url_crop})

# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
@iOps.route('/save_crop', methods=['GET', 'POST'])
def save_crop():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        width, height = im.size
        box = request.get_data(as_text=True)
        box = box.split('&')
        box_left = box.pop(0)
        box_left =  box_left.split('=')
        box_left = int(box_left.pop())*width/100
        box_upper = box.pop(0)
        box_upper =  box_upper.split('=')
        box_upper = int(box_upper.pop())*height/100
        box_right = box.pop(0)
        box_right =  box_right.split('=')
        box_right = int(box_right.pop())*width/100
        box_lower = box.pop(0)
        box_lower =  box_lower.split('=')
        box_lower = int(box_lower.pop())*height/100
        box_tuple = box_left, box_upper, box_right, box_lower
        im = im.crop(box_tuple)
        im.save('static/uploads/img.png')

@iOps.route('/rotate_image', methods=['GET', 'POST'])
def rotate_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        factor = int(request.get_data()) # reprezinta unghiul de rotatie
        im_rotate = im.rotate(angle=factor, expand=True, fillcolor='#FFFFFF') # fundalul de umplere va fi alb, iar imaginea initiala isi va pastra dimensiunile
        imgname = 'img_rotate_' + str(factor) + '.png'
        im_rotate.save('static/uploads/' + imgname)
        image_url_rotate = url_for('static',filename="uploads/" + imgname)
        return jsonify({'image_url_rotate' : image_url_rotate})

# Salveaza imaginea cu ultima valoare selectata de utilizator astfel incat sa se poata modifica in continuare si pentru alte procese (contrast, saturatie etc.)
@iOps.route('/save_rotate', methods=['GET', 'POST'])
def save_rotate():
    if request.method == "POST":
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        factor = int(request.get_data())
        im = im.rotate(angle=factor, expand=True, fillcolor='#FFFFFF')
        im.save('static/uploads/img.png')

@iOps.route('/rotate_90_image', methods=['GET', 'POST'])
def rotate_90_image():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = im.transpose(method=Image.ROTATE_90) # Roteste imaginea cu 90 grade
        im.save('static/uploads/img.png')
        image_url_rotate_90 = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_rotate_90' : image_url_rotate_90})

@iOps.route('/equalizer', methods=['GET', 'POST'])
# Equalize Histogram
def equalizer():
    if request.method == "POST":
        delete_images()
        image_src = 'static/uploads/img.png'
        im = Image.open(image_src)
        im = ImageOps.equalize(im) # Egalizeaza histograma imaginei
        im.save('static/uploads/img.png')
        image_url_equalize = url_for('static',filename="uploads/img.png")
        return jsonify({'image_url_equalize' : image_url_equalize})