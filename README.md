UI
==
Setup
1. Devstack(OpenStack env)
2. Configuration Files
3. Run Django project

Recommended Environment:
Use a VM with atleast 4GB RAM and 10GB Storage

Dependencies:
OpenStack install will download all nevessary depndencies 
DJango?? 

1. Devstack
http://docs.openstack.org/developer/devstack/

Install devstack
git clone https://git.openstack.org/openstack-dev/devstack
cd devstack; ./stack.sh

2. Configuration 
...

3. Run Django project
python manage.py runserver 
hosted on localhost:8000 


Stretch Goals:
Add State DB 
Add calls to OCx Library 


FAQ
Why does the UI not work anymore? 
Run ./rejoin-stack.sh

Why does OpenStack send connection errors? 
You might need to rejoin or restack 

