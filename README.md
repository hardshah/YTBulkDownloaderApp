# YTBulkDownloaderApp
This conversion tool allows you to download mp3 files from Youtube in bulk. 
Simply make a text file with names of songs you want to download, each seperated by line. 
It will perform a search on Youtube to find the top search result, and download it using PyTube
It will return a zip file that contains all mp3 files that were requested

#Project Design

All html templates are located in the templates folder. All CSS is located in the static folder. Inside the main folder lies the routes.py file.
The routes.py contains the endpoint logic.

In routes.py, I create an API. One for uploading which detects a POST method and automatically calls the one for downloading via redirecting it to the '/download' endpoint.
The download method also does the same and redirects to the '/remove' endpoint. 

When a user uploads a file and clicks the submit button, a POST method is recieved by the upload method, which then iterates the Query function over every line in a text file.
However if the Query function recieves an input with a non-alphanumeric character, it will not be able to search Youtube and thus returns an error. Therefore where it is called in routes.py, we check if the input to the Query function is valid with a regular expression searching for all non-alphanumeric characters. If it isn't then the user is directed to the '/error' endpoint which renders the Error template in templates.
If it is valid, then the Query function is called with the line from the text file as input. 

The Query function first turns each whitespace in the input to a '+', because this is how youtube searches search queries. Youtube performs a search for the most relevant youtube video. Youtube gives each video a unique 11 digit string. Using a regular expression we return a list of these 11 digit strings.  Assuming the first video is likely the song we were searching for we use the first string and concatenate it to the youtube video default url. I am looking for IndexOutOfRangeError here so that I can stop reading the text file at that point. This gives us the url for the top video when the query is searched. Once here, we use PyTube to download the video as an mp4 file with no frames and is stored in the TempStorage folder. This allows the video to converted to an AudioFileClip via MoviePy and change the extension to mp3 and downloading to TempStorage. Finally deleting the mp4 file.

The user is then redirected to '/download' due to the upload method.

The download method allows me to serve a zip file.Then the download method is invoked, due to a redirect at the end of the upload method, which creates a zip file containing the contents of the TempStorage folder. This zip file is returned to the user. A simple 'finally' block in python allows me to extend my code after the return statement and delete every file in the TempStorage folder and then redirect to the remove method to further extend my code delete the zip file from my main directory, as it should have already been served to the user.
