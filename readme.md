Curriculum Generator
====================

### This is a graduate school project that takes in input from a user and generates a custom curriculum based on a number of specifications.

### The system has a number of interconnected components, most notably it utilizes the following languages and/or frameworks

* Python -> Server side language used for controlling the flow of the application
* SWI-Prolog -> Declarative logic based language used for generating the curriculum
* Django -> Web framework utilized to handle routing, database connection, etc.
* JavaScript -> Front end scripting language to render a number of UI elements
* HTML/CSS -> Markup languages for UI styling

### To run the program locally you need to:
* [Download python](https://www.python.org/download/)
* Install pip using <code>sudo apt-get install python-pip</code>
* Install Django using <code>pip install -r requirements.txt</code>
* [Download SWI-Prolog](http://www.swi-prolog.org/build/Debian.html)

then run the following commands:

<code>python manage.py syncdb</code>

<code>python manage.py runserver --nothreading</code>
