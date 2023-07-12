import base64
import os
from flask import Flask, redirect, render_template, request, url_for
from config import Config
from color_roads import main
from filepath import process_shapefiles

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_PATH


@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def get_user_data_files():
    """
    Handles file upload and processes the shapefile to generate the resulting image.

    Returns:
        str: The rendered HTML page with the processed image displayed.
    """
    if request.method == 'POST':
        files = request.files.getlist('file')
        for f in files:
            if f.filename != '':
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        shp_path = process_shapefiles(app.config['UPLOAD_FOLDER'])
        processed_image = main(shp_path)
        if processed_image:
            image_ready = True
            with open(processed_image, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            return redirect(url_for("display_image"), code=302)
    return render_template('index.html', image_ready=image_ready, processed_image_path=processed_image)


@app.route('/image', methods=['GET'])
def display_image():
    """
    Displays the processed image.

    Returns:
        str: The HTML code to display the processed image.
    """
    processed_image_path = 'static/images/result.png'
    if processed_image_path:
        with open(processed_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f'<img src="data:image/png;base64,{encoded_string}"  alt="Color Streets">'
    return "Invalid image path"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
