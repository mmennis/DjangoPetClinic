Simple demo for testing Django applications
===========================================

This is an attempt to port teh SpringFramework petclinic app
to the Django framework.  This is partly a learning exercise
and partly a candidate testing application since it is known
that PetClinc exhibits characteristics that make it a good
demo or testing application.

Instructions for setup and initialization
-----------------------------------------
 * Set up python virtual_env.
 * Add dependencies using pip (installed by virtual_env.)
 'pip install -r requirements.txt`
 * Change to the nrpetclinic directory.
 * Update the settings.py file in the nrpetclinic directory with suitable values.
 * Create database per the settings.py information
 * Create the database tables using django tools
 `cd nrpetclinic; python manage.py syncdb`
 * Edit teh populate_db.py script to change the number of owners and vets.
 * Run the database population script
 `python populate_db.py`
 * 