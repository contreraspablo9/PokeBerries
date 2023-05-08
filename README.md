# PokeBerries System v1.10.1

 ## What is PokeBerries? 

This django and djangorestframework system is a brief demonstration of the basic structure of 
a scalable django proyect. 

as it is conventional in the project you can add different apps, each of them is designed to contain
its normal modules that are responsible for handling the functionality for a web browser and 
additionally within the app a folder api/ in which the API functionality is handled.

 ## How to get started? 

For this simple example you dont need to setup any database engine since it is not handling any models yet.
however, the pokeberries.pokeberries.base_configuration module already has the predefined structure to take
environment variables for the database credentials and configuration and in the PokeBerries repo is included
an env-example.sh to setup these variables

to do the setup of the env varibales simply run:
 
        cp env-example.sh env.sh
        . env.sh

when running the project for the first time make sure you already have all the dependencies installed,
just run :

        pip install -r requirements.txt

Once you have done all these steps you can go to manage.py file location in the console and run
the command

python manage.py runserver

which will start the django developments server.. 

if you see the mesage: 'starting development server at http://xxx.x.x.x:xxxx/'
then congratulations! It means you succesfully ran the API!!!

(note that you should replace the X for the ip of your django development server and port)

 ## USAGE

if you go to the main url of the django web server, you are going to be redirected to the api/ url 
which will display the djangorestframework browsable api

to change this behaviour and add your custom web browser views of the system modify the pokeberries.urls module


to see the pokeberries stats just follow the browsable api links or go directly to:
 
        api/berries/allBerryStats

## FEATURES

The allBerryStats endpoint instantiate the berries.api.berries_api.BerriesData class
on each request, which queries all the berries data from all the  pokemon API, check the documentation here:

        https://pokeapi.co/docs/v2


since around 65 queries needs to be done, the BerriesData object uses a paralel requests approach 
to significatively reduce the execution time.

Have fun!
