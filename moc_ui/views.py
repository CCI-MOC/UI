    # Django helpers for rendering html and redirecting
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Dictionaries to pass to template context
import dicts
# Forms to use in pages
import forms
# Models to access our database's tables
import models 
# Helper functions to make form processing easier 
import query_helpers as helpers
# HTML descriptions mixed with modal calls, 
# passed to template context in order to
# render modal / button / table templates
import html_helpers as html


####################
## TEMPLATE VIEWS ##
####################

def front_page(request): 
    """ Front page; 
    
    Enter credentials to be processed by the login view 
    """ 
    
    return render(request, 'front_page.html', 
                 {'login_data': dicts.login_data, 'login_form': forms.Login(), 
                  'reg_modal': dicts.reg_modal, 'reg_form': forms.UserRegister()}) 

def clouds(request): 
    """List projects and vms in user's clouds""" 
    

    user = helpers.retrieve_object("User", "user_name", request.session['user_name'])
    if user is not None:
        try:
            projects = models.UIProject.objects.filter(users=user)
            #print projects
        except Exception as e:
            print e 
            projects = []
    else:
        return HttpResponseRedirect('/')


    project_list = []
    for project in projects:
        vm_list = []
#        for vm in models.VM.objects.filter(ui_project=project):
#            vm_list.append(vm)
        project_list.append({'name':project.name, 'vm_list': vm_list})

    for project in dicts.test_project_list:
        project_list.append(project)


    return render(request, 'clouds.html', 
                  {'project_list': project_list, 
                   'cloud_modals': html.cloud_modals(request), 
                  }
                 )

def market(request, project):
    market_list = []
    # for market in markets:
    #     market_choice_list = []
    #     for choice in dicts.test_

    for market in dicts.test_market_list:
        market_list.append(market)

    return HttpResponseRedirect('/')

################
## FORM VIEWS ##
################

### User Actions ###
def login(request):
    """View to Login a user
    
    Checks post credentials, redirects
    to clouds or back to front page with error 
    """
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            print "form is valid"
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = helpers.retrieve_object("User", "user_name", user_name)
            if user is not None:
                print "verifying password"
                if user.verify_password(password=password):
                    request.session['user_name'] = user_name
                    return HttpResponseRedirect('/clouds')

    # temporary workaround to auto-login
    print "using workaround"
    request.session['user_name'] = "jbell" 
    return HttpResponseRedirect('/clouds')

def logout(request):
    """View to Logout of session 

    remove session variables and return to login page 
    """
    for state, sessionInfo in request.session.items():
        sessionInfo = None

    return HttpResponseRedirect('/')
## STILL EXISTS BECAUSE OWEN IS WORKING ON LOGIN PAGE 
## I DON'T WANT TO RESTRUCTURE REG FORMS, WILL BE Create_Object
def register(request):
    """Register new user with keystone;

    called from login page Needs error checking 
    """

    if request.method == "POST":
        form = forms.UserRegister(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = helpers.retrieve_object("User", "user_name", user_name)
            if user is None:
                new_user = models.User.create_user(user_name=user_name,
                                                   password=password)
                new_user.save()
                request.session['user_name'] = user_name
                return HttpResponseRedirect('/clouds')
            else:
                print "user %s exists" % user
        else:
            print form.errors 
        

    return HttpResponseRedirect('/')

# Generic dust views
# Earth to earth, ashes to ashes, dust to dust
def create_object(request, object_class):
    """Process POST form to create generic database object"""
    if request.method == "POST":
        # get the current user for auth and fk creation
        current_user = request.session['user_name']
        # Grab form class for object creation and initialize with request info
        form_name = "Create%s" % object_class
        # Passing request.POST for django auto-pop, request to pull session info out
        post_form = getattr(forms, form_name)(request, request.POST)
        # Debug code to print form html to console
        #for field in post_form:
           #print "%s: %s" % (field.label_tag(), field.value())
        if post_form.is_valid():
            # Debug code to print form info in better format
            #for key, value in post_form.cleaned_data.iteritems():
                #print "%s: %s" % (key, value)
            try:
                # Call the save function on the form 
                new_object = post_form.save(request)
            except Exception as e:
                print "Hit exception:"
                print e 
        else:
            print post_form.errors
    return HttpResponseRedirect('/clouds')

def delete_object(request, object_class):
    """Process POST form to delete generic database object"""
    if request.method == "POST":
        form_name = "Delete%s" % object_class
        # Grab form class and initialize with request and POST info
        post_form = getattr(forms, form_name)(request, request.POST)
        # Debug code to print form html to console
#        for field in post_form:
#            print "%s: %s" % (field.label_tag(), field.value())
        if post_form.is_valid():
            # Debug code to print form info in better format
#            for key, value in post_form.cleaned_data.iteritems():
#                print "%s: %s" % (key, value)
#            print "end of form data"
            try:
                # Call the save function on the form 
                form_object = post_form.save()
                #print "name: %s" % form_object
                #print "id: %d" % form_object.id
            except Exception as e:
                print "Hit exception:"
                print e 
        else:
            print post_form.errors
    return HttpResponseRedirect('/clouds')

def control_vm(request, action, vm_name):
    if request.method == "PUT":
    # check that the user has privalidge on vm
    # actually do the action
        pass


#Haas Plugin page
def haas(request):
    return render(request, 'haas.html')
