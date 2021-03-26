from flask import Flask, render_template, request, url_for, redirect, send_file, session
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "DemoString"

def download(url):
    video = url.streams.first()
    return video.download()

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        url = YouTube(session['link'])
        return render_template('youtube_video.html', url=url)
    return render_template("index.html")

@app.route("/youtube_video", methods=['GET', 'POST'])
def youtube_video():
    if request.method == 'POST':
        url = YouTube(session['link'])
        itag = request.form.get('itag')
        video = url.streams.get_by_itag(itag)
        filname = video.download()
        return send_file(filname, as_attachment=True)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
