from flask import Flask, Blueprint, render_template, request, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from uploadimg.views import uploadimg
from rgb_to_gray.views import rgb_to_gray

app = Flask(__name__)

app.register_blueprint(uploadimg)
app.register_blueprint(rgb_to_gray)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)