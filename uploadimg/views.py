from flask import Blueprint, render_template, Flask, request, jsonify, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from PIL import Image
import os

uploadimg = Blueprint('uploadimg', __name__, template_folder='templates')

apk = Flask(__name__)

# Permite incarcarea de fisiere doar de tip imagine (extensie .png, .PNG etc.)
photos = UploadSet('photos', IMAGES)

apk.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(apk, photos)
# Accepta fisiere <= 16MB
patch_request_class(apk, size=16777216)

# Verifica daca fisierul este o imagine, are o extensie regasita in IMAGES 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGES

@uploadimg.route('/uploadimg', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        try:
            if 'imgfile' in request.files:
                # Se sterge daca exista un fisier anterior img.png in directorul imaginilor incarcate
                if os.path.exists("static/uploads/img.png"):
                    os.remove("static/uploads/img.png")
                    os.remove("static/uploads/imgoriginal.png")
                imageFile = request.files['imgfile']
                # Daca fisierul este o imagine, eroare => 0, altfel eroare => 1
                if allowed_file(imageFile.filename):
                    filename = photos.save(imageFile,name='img.png') # Salveaza imaginea cu numele img.png
                    im = Image.open('static/uploads/img.png')
                    im.save('static/uploads/imgoriginal.png') # Salveaza o copie a originalului
                    image_url = "static/uploads/"+filename
                    return jsonify({'image_url': image_url,
                                    'rendered_left': render_template('panel_left.html'),
                                    'rendered_right': render_template('panel_right.html'),
                                    'error': 0})
                else:
                    return jsonify({'error': 1})
        except Exception as e:
            print(e)
    return render_template('upload.html')



