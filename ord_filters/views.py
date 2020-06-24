from flask import Blueprint, request, url_for, jsonify
from PIL import Image, ImageFilter
from delete_processed_images.views import delete_images
import numpy as np

ord_filters = Blueprint('ord_filters', __name__, template_folder='templates')

@ord_filters.route('/min_filter', methods=['GET', 'POST'])
def min_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            im_min = im.filter(ImageFilter.MinFilter(size=3)) # Se alege pixelul minim dintr-un bloc de pixeli 3x3
            im_min.save('static/uploads/img_min.png')
            image_url_min = url_for('static',filename="uploads/img_min.png")
            return jsonify({'image_url_min' : image_url_min})
        except Exception as e:
            print(e)

@ord_filters.route('/max_filter', methods=['GET', 'POST'])
def max_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            im_max = im.filter(ImageFilter.MaxFilter(size=3)) # Se alege pixelul maxim dintr-un bloc de pixeli 3x3
            im_max.save('static/uploads/img_max.png')
            image_url_max = url_for('static',filename="uploads/img_max.png")
            return jsonify({'image_url_max' : image_url_max})
        except Exception as e:
            print(e)

@ord_filters.route('/median_filter', methods=['GET', 'POST'])
def median_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            im_median = im.filter(ImageFilter.MedianFilter(size=3)) # Se alege pixelul median (cel din mijlocul listei ordonate) dintr-un bloc de pixeli 3x3
            im_median.save('static/uploads/img_median.png')
            image_url_median = url_for('static',filename="uploads/img_median.png")
            return jsonify({'image_url_median' : image_url_median})
        except Exception as e:
            print(e)

@ord_filters.route('/medext_filter', methods=['GET', 'POST'])
# Filtrul media extremelor
def medext_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Se face media aritmetica dintre pixelul maxim si pixelul minim dintr-un bloc de pixeli 3x3
            im_medext = Image.fromarray(np.uint8(1/2*np.array(im.filter(ImageFilter.MaxFilter(size=3)),dtype='float32')+1/2*np.array(im.filter(ImageFilter.MinFilter(size=3)),dtype='float32')))
            im_medext.save('static/uploads/img_medext.png')
            image_url_medext = url_for('static',filename="uploads/img_medext.png")
            return jsonify({'image_url_medext' : image_url_medext})
        except Exception as e:
            print(e)

@ord_filters.route('/range_filter', methods=['GET', 'POST'])
def range_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Se calculeaza "distanta" dintre pixelul maxim si pixelul minim dintr-un bloc de pixeli 3x3
            im_range = Image.fromarray(np.uint8(np.array(im.filter(ImageFilter.MaxFilter(size=3)))-np.array(im.filter(ImageFilter.MinFilter(size=3)))))
            im_range.save('static/uploads/img_range.png')
            image_url_range = url_for('static',filename="uploads/img_range.png")
            return jsonify({'image_url_range' : image_url_range})
        except Exception as e:
            print(e)
        
# Blocul de pixeli 3x3 trebuie sa fie ordonat crescator!
@ord_filters.route('/disprange_filter', methods=['GET', 'POST'])
# Filtrul dispersion-range
def disprange_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            # Se calculeaza "distanta" dintre pixelelii mai mari ca pixelul median si pixelii mai mici ca pixelul median dintr-un bloc de pixeli 3x3
            im_disprange = Image.fromarray(np.uint8(
            1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')+1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')+1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')+1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')
            -1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')-1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')-1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')-1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')))
            im_disprange.save('static/uploads/img_disprange.png')
            image_url_disprange = url_for('static',filename="uploads/img_disprange.png")
            return jsonify({'image_url_disprange' : image_url_disprange})
        except Exception as e:
            print(e)

@ord_filters.route('/alphamed_filter', methods=['GET', 'POST'])
# Filtrul alpha-median
def alphamed_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            alpha = int(request.get_data())
            imgname = 'img_alphamed_' + str(alpha) + '.png'
            if alpha == 1:
                # Se calculeaza media aritmetica a pixelilor alpha egal departat la stanga si la dreapta fata de pixelul median dintr-un bloc de pixeli 3x3
                im_alphamed = Image.fromarray(np.uint8(
                1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')+1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')+
                1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')+1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float32')+
                1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')+1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')+
                1/7*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')))
                im_alphamed.save('static/uploads/' + imgname)
                image_url_alphamed = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphamed' : image_url_alphamed})
            elif alpha == 2:
                im_alphamed = Image.fromarray(np.uint8(
                1/5*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')+1/5*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')+
                1/5*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float32')+1/5*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')+
                1/5*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')))
                im_alphamed.save('static/uploads/' + imgname)
                image_url_alphamed = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphamed' : image_url_alphamed})
            elif alpha == 3:
                im_alphamed = Image.fromarray(np.uint8(
                1/3*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')+1/3*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)),dtype='float32')+
                1/3*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')))
                im_alphamed.save('static/uploads/' + imgname)
                image_url_alphamed = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphamed' : image_url_alphamed})
            elif alpha == 4:
                im_alphamed = Image.fromarray(np.uint8(
                np.array(im.filter(ImageFilter.RankFilter(size=3,rank=4)))))
                im_alphamed.save('static/uploads/' + imgname)
                image_url_alphamed = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphamed' : image_url_alphamed})
        except Exception as e:
            print(e)

@ord_filters.route('/alphacom_filter', methods=['GET', 'POST'])
# Filtrul alpha-complementar
def alphacom_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            alpha = int(request.get_data())
            imgname = 'img_alphacom_' + str(alpha) + '.png'
            if alpha == 1:
                # Se calculeaza media aritmetica a alpha pixeli din margini (alpha din stanga, alpha din dreapta) dintr-un bloc de pixeli 3x3
                im_alphacom = Image.fromarray(np.uint8(
                1/2*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')+1/2*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')))
                im_alphacom.save('static/uploads/' + imgname)
                image_url_alphacom = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphacom' : image_url_alphacom})
            elif alpha == 2:
                im_alphacom = Image.fromarray(np.uint8(
                1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')+1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')+
                1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')+1/4*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')))
                im_alphacom.save('static/uploads/' + imgname)
                image_url_alphacom = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphacom' : image_url_alphacom})
            elif alpha == 3:
                im_alphacom = Image.fromarray(np.uint8(
                1/6*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')+1/6*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')+
                1/6*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')+1/6*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')+
                1/6*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')+1/6*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')))
                im_alphacom.save('static/uploads/' + imgname)
                image_url_alphacom = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphacom' : image_url_alphacom})
            elif alpha == 4:
                im_alphacom = Image.fromarray(np.uint8(
                1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=0)),dtype='float32')+1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)),dtype='float32')+
                1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)),dtype='float32')+1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)),dtype='float32')+
                1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)),dtype='float32')+1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)),dtype='float32')+
                1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)),dtype='float32')+1/8*np.array(im.filter(ImageFilter.RankFilter(size=3,rank=8)),dtype='float32')))
                im_alphacom.save('static/uploads/' + imgname)
                image_url_alphacom = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphacom' : image_url_alphacom})
        except Exception as e:
            print(e)

@ord_filters.route('/alphaqsr_filter', methods=['GET', 'POST'])
# Filtrul alpha-quasi-range
def alphaqsr_filter():
    if request.method == "POST":
        try:
            delete_images()
            image_src = 'static/uploads/img.png'
            im = Image.open(image_src)
            alpha = int(request.get_data())
            imgname = 'img_alphaqsr_' + str(alpha) + '.png'
            if alpha == 1:
                # Se calculeaza "distanta" 2 pixeli din capatul vectorului minus alpha dintr-un bloc de pixeli 3x3
                im_alphaqsr = Image.fromarray(np.uint8(
                np.array(im.filter(ImageFilter.RankFilter(size=3,rank=7)))-np.array(im.filter(ImageFilter.RankFilter(size=3,rank=1)))))
                im_alphaqsr.save('static/uploads/' + imgname)
                image_url_alphaqsr = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphaqsr' : image_url_alphaqsr})
            elif alpha == 2:
                im_alphaqsr = Image.fromarray(np.uint8(
                np.array(im.filter(ImageFilter.RankFilter(size=3,rank=6)))-np.array(im.filter(ImageFilter.RankFilter(size=3,rank=2)))))
                im_alphaqsr.save('static/uploads/' + imgname)
                image_url_alphaqsr = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphaqsr' : image_url_alphaqsr})
            elif alpha == 3:
                im_alphaqsr = Image.fromarray(np.uint8(
                np.array(im.filter(ImageFilter.RankFilter(size=3,rank=5)))-np.array(im.filter(ImageFilter.RankFilter(size=3,rank=3)))))
                im_alphaqsr.save('static/uploads/' + imgname)
                image_url_alphaqsr = url_for('static',filename="uploads/" + imgname)
                return jsonify({'image_url_alphaqsr' : image_url_alphaqsr})
        except Exception as e:
            print(e)