from flask import Flask, render_template, request, redirect, Response, session
from werkzeug.utils import secure_filename
import librosa, madmom
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io, random, base64, os

ALLOWED_EXTENSIONS = {'wav'}
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'audiolist')
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 #16MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route("/metro")
# def metro():
#     return render_template("metro.html")

@app.route("/", methods=["GET", "POST"])
def index():
    beat_times = []
    tempo = ""
    pngImageB64String = ""
    
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        

        if file.filename == "":
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(UPLOAD_PATH, file.filename))

            y, sr = librosa.load(file)

            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            beat_times = librosa.frames_to_time(beat_frames, sr=sr)

            duration = len(y) / sr
            t = np.linspace(0, duration, len(y))

            fig = Figure(figsize=(15,5), facecolor="#fff3e7")
            axis = fig.add_subplot(1, 1, 1)
            axis.set_title("Sound wave with estimated beat")
            axis.set_xlabel("Time(second)")
            axis.set_ylabel("Magnitude")
            axis.grid()
            axis.plot(t,y,color='#a28b77',label='Audio Wave')
            axis.vlines(x=beat_times, ymin= - max(y), ymax=max(y), alpha=0.5, color='r',
            linestyle='--', label='Estimated Beats')
            axis.legend()

            pngImage = io.BytesIO()
            FigureCanvas(fig).print_png(pngImage)

            pngImageB64String = "data:image/png;base64,"
            pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template('index.html', tempo=tempo, beat_times=beat_times, image=pngImageB64String)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)