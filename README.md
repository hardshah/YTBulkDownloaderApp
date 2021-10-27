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
However if the Query function recieves an input with a non-alphanumeric character, it will not be able to search Youtube and thus returns an error. We catch the exc

The project utilizes a temporary storage folder, so that all files can be easily added to a zip file via the shutil library.
The mp4 files downloaded by Pytube are stored here until converted to mp3 files, and are then deleted. 
Then the download method is invoked which creates a zip file containing the contents of the TempStorage folder
This zip file is returned to the user

And then the remove method is called. The remove method
