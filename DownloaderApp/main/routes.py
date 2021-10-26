from typing import Type
from flask import Blueprint,render_template,request,redirect,send_file
from werkzeug.utils import secure_filename
import os
from .download import Query
from .__init__ import app
import shutil
import re 

main = Blueprint('main',__name__)



@main.route("/", methods=["GET", "POST"])
def upload_file():
        if request.method == "POST":
            if request.files:
                file = request.files["text"]
                filename = secure_filename(file.filename)
                print(filename)

                for line in file:
                    query=line.rstrip().decode()
                    if re.search(r'[^a-zA-Z\d\s:]',query)== None :
                        return redirect('/error')
                    else:
                        Query(query)

                return redirect('/download')
     
        return render_template("index.html")

@main.route('/download', methods=['GET'])
def download():
    zipfolder = shutil.make_archive('YTmp3','zip','./DownloaderApp/TempStorage') 
    try:
         return send_file(zipfolder,as_attachment = True)
    finally: 
         for root,dirs, files in os.walk('DownloaderApp\TempStorage'):
             for file in files:
                 print('DownloaderApp/TempStorage'+file)
                 os.remove('DownloaderApp/TempStorage/'+file)
             return redirect('/remove')

@main.route('/remove',methods=['GET'])
def remove():
    os.remove('YTmp3.zip')
    return render_template('success.html')

@main.route('/error',methods=['GET'])
def error():
    return render_template('Error.html')
         

    
 
    
    



