from flask import Flask, Blueprint, render_template, request, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from uploadimg.views import uploadimg
from rgb_to_gray.views import rgb_to_gray
from gray_to_binary.views import gray_to_binary
from delete_processed_images.views import delete_processed_images
from uniform_filter.views import uniform_filter
from gauss_filter.views import gauss_filter
from roberts_filter.views import roberts_filter
from prewitt_filter.views import prewitt_filter
from sobel_filter.views import sobel_filter
from kirsch_filter.views import kirsch_filter

app = Flask(__name__)

app.register_blueprint(uploadimg)
app.register_blueprint(rgb_to_gray)
app.register_blueprint(gray_to_binary)
app.register_blueprint(delete_processed_images)
app.register_blueprint(uniform_filter)
app.register_blueprint(gauss_filter)
app.register_blueprint(roberts_filter)
app.register_blueprint(prewitt_filter)
app.register_blueprint(sobel_filter)
app.register_blueprint(kirsch_filter)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)