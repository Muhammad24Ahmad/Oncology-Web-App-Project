from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']

        # Render a template with success/failure message and download link
        return render_template('result.html', success=True, download_link="/download_report")
        # Handle file upload here
        # flash('File uploaded successfully!', 'success')
        # return redirect(url_for('index'))

@app.route('/extract', methods=['POST'])
def extract():
    if request.method == 'POST':
        # Handle drug extraction logic here
        flash('Drugs extracted successfully!', 'success')
        return redirect(url_for('index'))

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        # Handle report download here
        flash('Report downloaded successfully!', 'success')
        return redirect(url_for('index'))

@app.route('/nih_check', methods=['POST'])
def nih_check():
    if request.method == 'POST':
        # Handle NIH approval check here
        flash('NIH approval check complete!', 'success')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
