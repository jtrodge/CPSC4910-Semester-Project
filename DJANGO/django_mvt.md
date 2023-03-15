***DJANGO***
*MVT (Model-View-Template)*

- MODEL and TEMPLATE never talk directly
- VIEW connects MODEL and TEMPLATE

- **TEMPLATE** sends user input to *VIEW*
- *VIEW* sends updates/requests to **MODEL**
- **MODEL** sends data to *VIEW*
- *VIEW* edits the display in **TEMPLATE**

**Model**
*data interface*
*Python/MySQL*
- maintains/tracks data
- logical data structure for the entire application

**View**
*user interface*
*Python/HTML/CSS/Javascript*
- what is seen in the browser when on the web
- renders the HTML/CSS/Javascript from Template
- view functions are python functions that take a web request and return a web response

**Template**
*static components/data*
*HTML/CSS/Javascript*
- describes how dynamic content will be handled


***DJANGO FILES***

**manage.py**
- used to interact with project using the command line
- starting the server etc.
- 'manage.py help' -> returns a full list of commands

**settings.py**
- contains all website settings
- register all applications, location of files, databse configurations, etc.

**urls.py**
- stores all project links and callable functions