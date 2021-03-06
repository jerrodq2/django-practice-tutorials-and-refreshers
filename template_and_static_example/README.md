# Overview/Purpose of this Django Project
This project is meant to demonstrate two ways of organizing and using templates and static files, simple project for a refreshers if I need it

## Other Useful Info/Directions
There are two main/commonly accepted methods I've found to organize and use both the static and template files/directories. Both methods are detailed below

### Method One - Default
This is Django's default method (at least for this version). By default, Django looks in each app for a 'templates' and 'static' directory. For example, if in the basic_app in this project, I render the view "index.html", django will search through each app's templates directory for the first 'index.html' file and server that up. This can lead to files being ignored, a simple fix is by putting static files and templates in sub folders. For example, in basic_app, I have the directory 'basic_app/templates/basic_app/index.html' and i'll return render 'basic_app/index.html'. This is more specific and won't have the problem detailed above. Same principle for static files. Following this method allows each app to function completely independently when it comes to their templates and static files.

### Method Two - Global directories
The second commonly used method is to create a 'templates' and 'static' in the main project directory (same directory as manage.py). You then make slight changes to the settings.py file so that Django knows to look there for static/template files, and you can store all static files in one static folder, and same for templates. You can see examples in the settings.py file, you need to use 'os.path.join(BASE_DIR, 'FOLDER_NAME')' in order to tell django to look for either template or static files, you then add them to either the TEMPLATES array in DIRS, or in a new STATICFILES_DIRS array. 

## Linked To Any Other Django projects
N/A


## Environment Information
* Python version: 3.6.5
* Django version: 2.0.4
* Relevant url: N/A
* Other relevant info: N/A
