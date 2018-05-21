# Overview/Purpose of this Django Project
To demonstrate basic authentication with django using different algorithms and built in utility.

## Other Useful Info/Directions
See the settings.py file for comments related to password validation, starting on the "Password validation" section, around line 85.

The model UserProfile extends the default User model via a OneToOne relationship. You see how to have formModels for each model, save both, hash passwords, and save user uploaded images.

We also demonstrate the use of built in django methods such as login_required, authenticate, login, logout, and is_authenticated. You can see this in views.py and the templates.

Algorithms used: PBKDF2 (built in), bcrypt, and Argon2. If necessary, install the two latter ones with "pip install bcrypt" and "pip install django[argon2]".

Something new in this project is working with user uploaded images. We have separate directories, 'static' for the usual static files, and 'media' for user uploaded images. Also, in order to work with images in python, I used the python image library 'pillow', install if necessary with "pip install pillow"

## Linked To Any Other Django projects
N/A


## Environment Information
* Python version: 3.6.5
* Django version: 2.0.4
* Relevant url:
* Other relevant info:
