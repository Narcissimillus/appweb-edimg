from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images
import numpy as np

mean_filters = Blueprint('mean_filters', __name__, template_folder='templates')

@mean_filters.route('/artm_filter', methods=['GET', 'POST'])
# Filtrul medie aritmetica
def artm_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Se calculeaza media aritmetica a pixelilor dintr-un bloc de pixeli 3x3
            im_artm = Image.fromarray(np.uint8(
            1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')+1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')+1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')+
            1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')+1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float32')+1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')+
            1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')+1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')+1/9*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')))
            im_artm.save('static/uploads/img_artm.png')
            image_url_artm = url_for('static',filename="uploads/img_artm.png")
            return jsonify({'image_url_artm' : image_url_artm})
        except Exception as e:
            print(e)
            
@mean_filters.route('/geom_filter', methods=['GET', 'POST'])
# Filtrul medie geometrica
def geom_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Se calculeaza media geometrica a pixelilor dintr-un bloc de pixeli 3x3
            im_geom = Image.fromarray(np.uint8(np.multiply(np.multiply(
            np.multiply(np.multiply(
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32'),np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')),np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32'))**(1/9),
            np.multiply(np.multiply(
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32'),np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float32')),np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32'))**(1/9)),
            np.multiply(np.multiply(
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32'),np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')),np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32'))**(1/9))))
            im_geom.save('static/uploads/img_geom.png')
            image_url_geom = url_for('static',filename="uploads/img_geom.png")
            return jsonify({'image_url_geom' : image_url_geom})
        except Exception as e:
            print(e)

@mean_filters.route('/harm_filter', methods=['GET', 'POST'])
# Filtrul medie armonica
def harm_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Se calculeaza media armonica pixelilor dintr-un bloc de pixeli 3x3
            im_harm = Image.fromarray(np.uint8(9*(
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')**-1+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')**-1+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')**-1+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')**-1+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float32')**-1+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')**-1+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')**-1+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')**-1+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')**-1)**-1))
            im_harm.save('static/uploads/img_harm.png')
            image_url_harm = url_for('static',filename="uploads/img_harm.png")
            return jsonify({'image_url_harm' : image_url_harm})
        except Exception as e:
            print(e)

@mean_filters.route('/alphach_filter', methods=['GET', 'POST'])
# Filtrul medie contra-armonica-alpha
def alphach_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            alpha = int(request.get_data())
            imgname = 'img_alphach_' + str(alpha) + '.png'
            # Se calculeaza media contraarmonica cu alpha (pentru alpha = 0 => media aritmetica // pentru alpha = -1 => media armonica) dintr-un bloc de pixeli 3x3
            im_alphach = Image.fromarray(np.uint8(np.divide(
            (np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float64')**(alpha+1)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float64')**(alpha+1)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float64')**(alpha+1)+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float64')**(alpha+1)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float64')**(alpha+1)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float64')**(alpha+1)+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float64')**(alpha+1)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float64')**(alpha+1)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float64')**(alpha+1)),
            (np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float64')**(alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float64')**(alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float64')**(alpha)+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float64')**(alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float64')**(alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float64')**(alpha)+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float64')**(alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float64')**(alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float64')**(alpha))
            )))
            im_alphach.save('static/uploads/' + imgname)
            image_url_alphach = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_alphach' : image_url_alphach})
        except Exception as e:
            print(e)

@mean_filters.route('/alphapow_filter', methods=['GET', 'POST'])
# Filtrul medie putere-alpha
def alphapow_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            alpha = int(request.get_data())
            imgname = 'img_alphapow_' + str(alpha) + '.png'
            # Se calculeaza media putere cu alpha dintr-un bloc de pixeli 3x3
            im_alphapow = Image.fromarray(np.uint8(
            ((np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float64')**alpha+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float64')**alpha+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float64')**alpha+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float64')**alpha+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float64')**alpha+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float64')**alpha+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float64')**alpha+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float64')**alpha+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float64')**alpha)/9)**(1/alpha)))
            im_alphapow.save('static/uploads/' + imgname)
            image_url_alphapow = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_alphapow' : image_url_alphapow})
        except Exception as e:
            print(e)

@mean_filters.route('/alphapow2_filter', methods=['GET', 'POST'])
# Filtrul medie putere 1/alpha
def alphapow2_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            alpha = int(request.get_data())
            imgname = 'img_alphapow2_' + str(alpha) + '.png'
            # Se calculeaza media putere cu 1/alpha dintr-un bloc de pixeli 3x3
            im_alphapow2 = Image.fromarray(np.uint8(
            ((np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float64')**(1/alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float64')**(1/alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float64')**(1/alpha)+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float64')**(1/alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float64')**(1/alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float64')**(1/alpha)+
            np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float64')**(1/alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float64')**(1/alpha)+np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float64')**(1/alpha))/9)**alpha))
            im_alphapow2.save('static/uploads/' + imgname)
            image_url_alphapow2 = url_for('static',filename="uploads/" + imgname)
            return jsonify({'image_url_alphapow2' : image_url_alphapow2})
        except Exception as e:
            print(e)