from flask import Flask

ALLOWED_EXTENSIONS = set(['txt'])
app = Flask(__name__,static_folder='TempStorage')
app.config['PATH_FOR_DOWNLOADS'] = 'TempStorage'


