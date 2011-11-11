
Simple demo for testing Django applications
===========================================

This is an attempt to port the SpringFramework petclinic app
to the Django framework.  This is partly a learning exercise
and partly a candidate testing application since it is known
that PetClinc exhibits characteristics that make it a good
demo or testing application.

Instructions for setup and initialization
-----------------------------------------
 * Set up python virtual_env in the checked out directory.
     `virtualenv --no-site-packages .`
 * Source the virtualenv setup.
     `source bin/activate`
 * Add dependencies using pip (installed by virtual_env.)
     `pip install -r requirements.txt`
 * Change to the nrpetclinic directory.
 * Update the license key and application name in the newrelic.ini file.
 * Update the settings.py file in the nrpetclinic directory with suitable values.
 * Create database per the settings.py information.
 * Create the database tables using django tools.
     `cd nrpetclinic; python manage.py syncdb`
 * Edit the populate_db.py script to change the number of owners and vets.
 * Run the database population script.
     `python populate_db.py`
 * Verify that the server runs in development mode.
     `python manage.py runserver`
 * http://localhost:8000/petclinic/ You should see typical petclinic home page.
