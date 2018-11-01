# Basic Django Web Creation:
# 	To run server > python manage.py runserver

#//////////////////////Setup//////////////////////
# conda create --name myenv
# Create directory
# > activate virtualenvironment
# > django-admin startproject projectname
# >python manage.py startapp appname
# If using passwords install:
	# pip install bcrypt
	# pip install django[argon2]
# To install python imaging library for user media
	# pip isntall pillow (try first if fails try below)
	# pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"

#************************************************
# Code for base
#************************************************
# Add templates, templatetags, media (if having user media), and static folder to the directory
# If using user media create a profile_pic or what ever folder is needed inside the media folder
# Each app should have  directory within the folders
# Use migrate when adding applications, models, or big changes
#///////////////settings.py////////////////////
# Add app to settings.py
# Go to INSTALLED_APPS and add app name to the list

		INSTALLED_APPS = [
			...,
			appname
		]

# Add templates, static, and media directory

		TEMPLATE_DIR = os.path.join(BASE_DIR,'templates') # HTML directory
		STATIC_DIR = os.path.join(BASE_DIR,'static') # Website media directory
		MEDIA_DIR = os.path.join(BASE_DIR,'media') # A directory for user media
		# Scroll down
		TEMPLATES = [
			...
			'DIRS': [TEMPLATE_DIR,],
			...
		]
		#Scroll to bottom for static files section
		STATICFILES_DIRS = [
			STATIC_DIR,
		]
		#MEDIA
		MEDIA_ROOT = MEDIA_DIR
		MEDIA_URL = '/media/'
		LOGIN_URL = '/appname/user_login' # use if website has users

# When website has passwords below are different types of password hashers
#Optional password validators check if password is too short, simple, etc...
#Password validation
		PASSWORD_HASHERS = [
		    'django.contrib.auth.hashers.Argon2PasswordHasher',
		    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
		    'django.contrib.auth.hashers.BCryptPasswordHasher',
		    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
		    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
		]
		AUTH_PASSWORD_VALIDATORS = [
		    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
		    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS':{'min_length':9} },
		    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
		    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
		]

#////////////project urls.py///////////////////
# In project folder edit url.py
# Add line
		from appname import views
		from django.urls import path,include
# Add new line on top of urlpatterns ex.
		path('',views.index,name='index'), # for importing FBV
		path('appname/',include('appname.urls')),
		path('',views.classname.as_view()) #for importing CBV
# First lines defines the homepage
# In second line first part allow for new url with extension /appname calls on apps url.py file
#************************************************
# Code for base
#************************************************

#************************************************
# Code for applications
#************************************************
#////////////appname urls.py/////////////
# Add urls.py to appname folder
# Add the lines
		from django.urls import path
		from appname import views
		#template tagging
		app_name = 'appname'
		urlpatterns = [
		    path('',views.functioname,name='functioname'),
			#allows more urls this would be /appname/other or what ever it is calledi the global urls.py
		    path('other/',views.otherfunction,name='otherfunction'),
		]

#///////////////////appname views.py//////////////////////
# Go to /appname/view.py (call function index to create homepage
# Add the following lines
		from django.http import HttpResponse

# Create function ex.
		def functionname(request):
		       return HttpResonse('Hello World')

# referancing html ex.
		def index(request):
		       return render(request,'index.html')

# For inserting into template html use context to give ability to insert value from function ex.
		def functionname(request):
		       dictreferance = {'dictreferance':'Hello I am from views.py'}
		       return render(request,'appname/index.html',context='dictreferance')

# Adding models ex.
		from appname.models import Topic,Webpage, AccessRecord
		def index(request):
		    webpages_list = AccessRecord.objects.order_by('date')
		    date_dict = {"access_records":webpages_list}
		    return render(request,'appname/index.html',date_dict)

# Add forms ex.
		from . import forms
		def form_name_view(request):
        #creating variable of form
		form = forms.FormName()
		#how to use submitted data
		if request.method == 'POST':
			form = forms.FormName(request.POST)
			if form.is_valid():
				print('VALIDATION SUCCESS!')
				#use to grab form value print, create var, etc'
				print(form.cleaned_data['name'])
				#to save to the model
				form.save()
		#to render in html user key
		return render(request,'appname/form_page.html',{'form':form})

# For adding log in/register view Django_level_Five views.py file

# Class based view (CBV) basic example view Advanced_Django_CBV for more examples
		from django.shortcuts import render
		from django.core.urlresolvers import reverse_lazy
		from django.http import HttpResponse
		from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
		from . import models
		class IndexView(TemplateView):
		    # Just set this Class Object Attribute to the template page.
		    # template_name = 'app_name/site.html'
		    template_name = 'index.html'
		    def get_context_data(self,**kwargs):
		        context  = super().get_context_data(**kwargs)
		        context['injectme'] = "Basic Injection!"
		        return context

		# Mixin example use similarily to decorators
		class CreatePostView(LoginRequiredMixin,CreateView):
		    login_url = '/login/'
		    redirect_field_name = 'blog/post_detail.html'
		    form_class = PostForm
		    model = Post

#//////////////////////appname model.py////////////////////////
# Adding model to appname
# To add model in terminal do after adding to models.py
# migrate for any changes
# >python manage.py migrate
# >python manage.py makemigrations appname
# >python manage.py migrate
# Go to models.py create class for each table ex.
		from django.contrib.auth.models import User # for adding user profiles

		class Topic(models.Model):
		    top_name = models.CharField(max_length=264,unique=True)
		    #string representation of model
		    def __str__(self):
		        return self.top_name

		class Webpage(models.Model):
		    topic = models.ForeignKey(Topic)
		    name = models.CharField(max_length=264,unique=True)
		    url = models.URLField(unique=True)
		    def __str__(self):
		        return self.name

		# User profile examples model
		class UserProfileInfo(models.Model):
		    # Create relationship (don't inherit from User!)
		    user = models.OneToOneField(User)
		    # Add any additional attributes you want
		    portfolio_site = models.URLField(blank=True)
		    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
		    def __str__(self):
		        # Built-in attribute of django.contrib.auth.models.User !
		        return self.user.username

#////////////////appname admin.py//////////////////
# In /appname admin.py
# Import statement:
		from appname.models import Topic,Webpage,AccessRecord
		admin.site.register(AccessRecord)
		admin.site.register(Topic)
		admin.site.register(Webpage)
# Create super user in terminal (follow prompts):
# >python manage.py createsuperuser
# With server running and in browser go to /admin to access admin page

#/////////////////////appname forms.py///////////////////
# To add forms create forms.py in appname folder
		from django import forms
		#add form data to models
		from appname.models import mymodel
		from django.core import validators
		#create custom validator
		def check_for_z(value):
			if value[0].lower() != 'z':
				raise forms.ValidationError('Name needs to start with z')
		#create form
		class FormName(forms.Form):
			#names has custom validator
			name=forms.CharField(validators=[check_for_z()])
			email=forms.EmailField()
			verify_email = forms.EmailField(label='Enter your email again:')
			#hidden field use validator to catch bots auto-filling form
			botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
			#function within form to verify inputs
			def clean(self):
				all_clean_data = super().clean()
				email = all_clean_data['email']
				vmail = all_clean_data['verify_email']
				if email != vmail:
					raise forms.ValidationsError('Make sure emails match')
			#create form to add to model
			class MyNewForm(forms.ModelForm):
			#you can remove field values from above if already in model unless you want custom validators
				class Meta:
					model = MyModel
					#options
					field = '__all__'
					exclude = ('field1','field2')
					include = ('field1','field2')

		# form for creating users profiles
		from django import forms
		from django.contrib.auth.models import User
		from basic_app.models import UserProfileInfo

		class UserForm(forms.ModelForm):
		    password = forms.CharField(widget=forms.PasswordInput())
		    class Meta():
		        model = User
		        fields = ('username','email','password')
		class UserProfileInfoForm(forms.ModelForm):
		    class Meta():
		        model = UserProfileInfo
		        fields = ('portfolio_site','profile_pic')
#************************************************
# Code for applications
#************************************************

#************************************************
# Code for templatetags
#************************************************
# create __init__.py and my_templates.py (can be any name)
#creating custom filters
		from django import template
		register = template.library
		@register.filter(name='cut')
		def cut(value,arg):
			#replaces all values of arg
			return value.replace(arg,'')
#************************************************
# Code for templatetags
#************************************************

#************************************************
# Code for templates
#************************************************
#////////////templates//////////////////////////
# In templates/appname folder create appname.html (or any name you choose)
# Must have index.html for the homepage
# Create regular html code
# Below <!DOCTYPE html>  ---->  {% load staticfiles %}
# css link <link rel='stylesheet' href='{% static 'css/mystyle.css' %}'/>
# Insert into body to refereance view.py (reference dict key) {{ dictreferance }}
# To insert static files <img src={% static 'images/djangoguitar.jpg' %} alt='No Image' >
# Adding model to template html
	# {% if access_records %} close with {% endif %}
	# checks if access record is there from view.py
	# {% for acc in access_records %} close with {% endfor %} #loops through table
	# {% else %}
# Adding Django form {{form}} same structure use dict key
	# Use form tag from boostrap
	# {{form.as_p}} puts the forms in paragraph tag
	# Must have {% csrf_token %} security check next to {{form}}
	# use html input tag class button
# Adding a registration or login page
	# {% if registered %} check is user is registered
	# {% else %} present registery form
	# <form method='post' enctype='multipart/form-data'> encytype allows for pic upload
	# if creating login page just need input tags
	# <form method='post' action="{% url 'appname:user_login' %}"> action needed for login page
	# {% csrf_token %}
	# {{ user_form.as_p }}
	# {{ profile_form.as_p }}
	# <input type="submit" class="btn btn-primary" value="Submit"> </form>
# for template tagging allows for relative urls
	#<a href="{% url 'appname:otherfunction' %}">link to new page</a>
	#<a href="{% url 'admin:index' %}">link to admin</a>
	#<a href="{% url 'index' %}">link to index</a>
# creating base.html file allows for inhertance to other html staticfiles
	#in base.html set up like a normal html can have any name
		# <links to JS, CSS, boostrap>
		# <body>
		# <bunch of html like navbars> this code will automatically appear on any extended html
		# {% block body_block %}
		# anything inbetween will be unique to that html file
		# {% endblock %}
		# ex. can use container for block code
		# </body>
		# </More footer html>
	#in other.html
		# <!DOCTYPE html> this is the only required html code
		# {% extends "appname/base.html" %}
		# {% load my_templates %} name of .py file in templatetags folder used to load filters etc...
		# {% block body_block %}
		# <HTML specific for other.html>
		# {% endblock %}
# html filters
	# <h1>{{ dictref:upper }}</h1> upper is could be any function/filter
#************************************************
# Code for templates
#************************************************

#************************************************
# Code for hosting and deployment
#************************************************
# Create repository on github
# Follow instructions for loading files into repository
# Go to pythonanywhere
# Open $Bash console
# Create virtualenvironment >mkvirtualenv --python=python3.5 evnname
# Find version of django installed on desktop use desktop terminal
	# Open >python
	# >import django >django.__version__
# Install Django >pip install django==version#
# Confirm installation >which django-admin.py
# Go to github repository copy clone/download link
# >git clone repositoryURL
# CD into appropriate folder
# Migrate models
	# >python manage.py migrate
	# >python makemigrations appname
	# >python manage.py migrate
# >python manage.py createsuperuser
# Go to Web App page in pythonanywhere and add a new web app
# Select framework (manual configuration of Django is already loaded) and versions
# Open web app, click web app setup, and click Enter path to a virtualenv, if desired
# Enter virtualenv path ex. /home/user/.virtualenvs/envname
# Under Code: enter the path to your web app source Code ex. /home/user/appname
	# Enter virtualenv console if you need to look it up
	# open the configuration file
		# Delete pages 13-47 and under ++++++ Django ++++++
		# some lines may already be present just uncomment
		import os
		import sys
		path = '/home/user/appname'
		if path not in sys.path:
			sys.path.append(path)
		os.chdir(path)
		os.envrion.setdefault("DJANGO_SETTINGS_MODULE","appname.settings")
		import django
		django.setup()
		from django.core.wsgi import get_wsgi_application
		application = get_wsgi_application()
# In web app go to Static files:
	# For Django
	# URL = /static/admin directory = /home/user/.virtualenvs/envname/lib/python#ver/site-packages/django/contrib/admin/static/admin
	# Also load appname static files
# Scroll to top click Reload:
# Go to files section on pythonanywhere open path to settings.py
		ALLOWED_HOSTS = ['pythonanywhere.url']
# change Debug to false when in production mode
#************************************************
# Code for hosting
#************************************************

# Misc:
# Creating fake data
# >pip install faker
# View Django_level_two/populate_first_app.py
