
Simple demo for testing Django applications
===========================================

This is an attempt to port the SpringFramework petclinic app
to the Django framework.  This is partly a learning exercise
and partly a candidate testing application since it is known
that PetClinc exhibits characteristics that make it a good
demo or testing application.
The demo uses MySQL as it's database.  You may need to make changes to use
another datasource.

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


Instructions for deploying in Apache WebServer
-----------------------------------------------

 * Ensure apache in installed with url rewrite enabled (compile from source if necessary.
 * Download and install mod_wsgi - see [WSGI install](http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide)
 * You should use the virtualenv python in compiling mod_wsgi
 * The applicaiton is preconfigured to use wsgi.  Follow the instructions on
[Wsgi Django](http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango) to integrate into apache.

The changes should look a little like this:

    WSGIPythonHome $$checkout-dir$$
    WSGIScriptAlias / $$checkout-dir$$/nrpetclinic/apache/django.wsgi

    Alias /static $$checkout-dir$$/nrpetclinic/petclinic/static

    <Directory $$checkout-dir$$/nrpetclinic/petclinic/static>
        Order deny,allow
        Allow from all
    </Directory>

    <Directory $$checkout-dir$$/nrpetclinic/apache >
        Order deny,allow
        Allow from all
    </Directory>

Where $$checkout-dir$$ is replaced with teh directory you checked the code out to and ran virtualenv