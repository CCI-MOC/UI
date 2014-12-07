## Installation

1. Install devstack, visit http://docs.openstack.org/developer/devstack/ 
2. Clone CCI-MOC/UI project into devstack folder
3. Run python manage.py runserver 
4. Open localhost:8000

## Known Issues

VM Edit Box - Error on start machine after pause, must unpause machine 
Modal View - Occasioanlly adjusts the HTML on click

## TODO 

Add error checking (ie. valid library calls) 
Add State DB for checking users and endpoints
Add OCX Library  

## Recommended Environment

Use Linux VM with atleast 4GB RAM and 10GB Storage

## FAQ
Why does the UI not work anymore? 
Run ./rejoin-stack.sh

Why does OpenStack send connection errors? 
You might need to rejoin or restack 

Why does Django say port already in use when running server?
OpenStack may be using the port, either runserver first, or specify port (ie. python manage.py runserver 9999) 

