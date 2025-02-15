import forms
# modal format for 
# PROJECTS PAGE
def project_modals(request):
    return  [{'id':'create_UI_Project', 'action':'/create/UIProject', 
              'title':'Create Project', 'form':forms.UIProject()},
             {'id':'delete_UI_Project', 'action':'/delete/UIProject', 
              'title':'Delete Project', 'form':forms.UIProject()},
#             {'id':'Create_Cluster_Account', 'action':'/Create/Cluster_Account', 
#              'title':'Add Cluster Account', 'form':forms.Create_Cluster_Account()},
#             {'id':'Delete_Cluster_Account', 'action':'/Delete/Cluster_Account', 
#              'title':'Delete Cluster Account', 'form':forms.Delete_Cluster_Account()},
             {'id':'add_Cluster_Project', 'action':'/create/ClusterProject', 
              'title':'Add Cluster Project', 'form':forms.ClusterProject()},
             {'id':'delete_Cluster_Project', 'action':'/delete/ClusterProject', 
              'title':'Delete Cluster Project', 'form':forms.ClusterProject()}
            
            ]
def vm_modals(request):
   return   [{'id':'createVM', 'action' : '/createVM/ui',
              'title':'Create VM', 'form':forms.Create_VM()},
             {'id':'deleteVM', 'action':'/deleteVM', 
              'title':'Delete VM', 'form':forms.Delete_VM()}
            ]