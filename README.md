# django-practice-tutorials-and-refreshers
A repository where I can keep different django apps that I create for practice, to follow along with tutorials, play with new practices, work on improving my django skills, etc. This way I can keep it on github, and look back at these later as refreshers. The initial purpose isn't for this repository to be one giant Django project, each project is meant to be standalone, the repository is just a place to hold them. If some projects practice linking to other projects in this repository, it will be specified.

## Getting Started
Each folder is it's own Django project and works independenlty of the others, they may use different virtualenvs. Each project will have a README file that specifies it's purpose, virtualenv, version of python/django used, etc. The different projects are lsited below along with what they show or can be looked at for a refresher

## Note
Due to most of these using Django version 2.0.4, the syntax of some things (such as using url vs path in the urls.py files) may be different than what you normally use

## List of Projects In Directory
Note: The below projects are followed by what they show or what you can get a refresher from by looking at them. They are listed in the order they were created.

* django-directory-example-project
  * demonstrates more sophisticated setup of project directory
  * includes a settings file for each environment (dev, prod, etc.) inheriting from a base settings file.

* populating_database_example
  * demonstrates how to populate the db with dummy/seed data through the use of a file

* template_and_static_example
  * shows different ways of organizing and using templates and static files
  * shows default way and how to setup a global folders in the main project directory for each
  * also demonstrates a simple use of using namespaces and named routes

* forms_and_form_validation
  * shows use of the built in forms
  * also shows different methods of validating django forms, with custom validations, and built in 'clean' methods

* model_forms
  * shows use of built in model forms
  * shows examples of how to specify, include, and exclude certain fields from the model and save directly to the model
  * Also shows the difference between user.save(commit = True) and user.save(commit = False)

* template_inheritance
  * demonstrates the use of template inheritance
  * Shows how to extend a base template

* basic_authentication
  * demonstrates basic user Authentication and registration/login
  * shows how to use multiple hashing Algorithms
  * shows how to use multiple forms
  * shows how to extend the default User model with a one to one relationship
  * shows how to save user uploaded images
  * demonstrate the use of built in django methods such as login_required, authenticate, login, and logout
  * demonstrates using the built in is_authenticated method in the templates to check if the user is logged in.

* my_blog_clone_project
	* clone project
