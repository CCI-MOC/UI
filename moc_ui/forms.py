from django import forms
import models

class Login(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegister(forms.ModelForm):
    user_name = forms.CharField(help_text="Please enter username.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter password.")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), )
    
    class Meta:
        model = models.User
        fields = ['user_name',]

    def save(self, force_insert=False, force_update=False, commit=True):
        new_user = super(UserRegister, self).save(commit=False)
        # Create new_user with 
        new_user = models.User(user_name=self.user_name)
        new_user.set_password(password=self.password)
        request.session['user_name'] = user_name

        if commit:
            new_user.save()
        return new_user 

# project actions
class CreateUIProject(forms.ModelForm):
    def __init__(self,request,*args,**kwargs):
        super (CreateUIProject, self).__init__(*args,**kwargs)

    class Meta:
        model = models.UIProject
        fields = ['name', ]
        # widgets = {'users': forms.HiddenInput()}

    def save(self, request, force_insert=False, force_update=False, commit=True):
        # Create new UIProject with user from request
        new_ui_project = models.UIProject(name=self.cleaned_data['name'])
        if commit:
            new_ui_project.save()
            # Add user as foreign key to UIProject
            new_ui_project.users.add(request.session['user_name'])

        return new_ui_project

class DeleteUIProject(forms.ModelForm):
    # Custom init function to initialize the correct projects 
    def __init__(self,request,*args,**kwargs):
        # populates function from the parent class with request.POST 
        super (DeleteUIProject, self).__init__(*args,**kwargs)
        # Grab current user object from request.session info
        current_user = models.User.objects. \
                                        get(user_name=request.session["user_name"])
        # populate name field with projects owned by user 
        project_names = models.UIProject.objects.filter(users=current_user)
        self.fields['name'] = forms.ModelChoiceField(queryset=project_names)

    class Meta:
        model = models.UIProject
        fields = ['name', ]

    def save(self, force_insert=False, force_update=False, commit=True):
        # Create new_user with 
        new_ui_project = models.UIProject.objects.get(name=self.cleaned_data['name'])

        print new_ui_project.name
        print new_ui_project.id

        if commit is True:
            new_ui_project.delete()
            return

        return new_ui_project

# Cluster_Project actions
class CreateClusterProject(forms.ModelForm):
    def __init__(self,request,*args,**kwargs):
        super (CreateClusterProject, self).__init__(*args,**kwargs)
        # Grab current user object from request.session info
        current_user = models.User.objects.get(user_name=request.session["user_name"])
        # Populate ui_project field with projects owned by user 
        ui_project_names = models.UIProject.objects.filter(users=current_user)
        self.fields['ui_project'] = forms.ModelChoiceField(queryset=ui_project_names)
        # Populate cluster field with clusters from db
        clusters = models.Cluster.objects.all()
        self.fields['cluster'] = forms.ModelChoiceField(queryset=clusters)

    class Meta:
        model = models.ClusterProject
        fields = ['name', 'cluster', 'ui_project']

    def save(self, request, force_insert=False, force_update=False, commit=True):
        # Create new_user with 
        new_cluster_project = models.ClusterProject(name=self.cleaned_data['name'],
                                                    cluster=self.cleaned_data['cluster'],
                                                    ui_project=self.cleaned_data['ui_project']
                                                   )

        if commit is True:
            new_cluster_project.save()
            return

        return new_cluster_project

class DeleteClusterProject(forms.ModelForm):
    def __init__(self,request,*args,**kwargs):
        # populates function from the parent class with request.POST 
        super (DeleteClusterProject, self).__init__(*args,**kwargs)
        # Grab current user object from request.session info
        current_user = models.User.objects. \
                                        get(user_name=request.session["user_name"])
        # populate name field with Cluster projects owned by user 
        cluster_project_list = models.ClusterProject.objects.filter(ui_project__users=current_user)
        print cluster_project_list
        print type(cluster_project_list)
        self.fields['name'] = forms.ModelChoiceField(queryset=cluster_project_list)

    class Meta:
        model = models.ClusterProject
        fields = ['name', ]

    def save(self, force_insert=False, force_update=False, commit=True):
        # Create new_user with 
        new_cluster_project = models.ClusterProject.objects.get(name=self.cleaned_data['name'])

        print new_cluster_project.name
        print new_cluster_project.id

        if commit is True:
            new_cluster_project.delete()
            return

        return new_cluster_project

# vm actions
class CreateVM(forms.Form):
    name = forms.CharField()

    #def create(self):

    

class DeleteVM(forms.Form):
    name = forms.CharField()

class ControlVM(forms.Form):
    name = forms.CharField()
    action = forms.CharField()


