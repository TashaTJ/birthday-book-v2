# **Birthday Book - Project Portfolio 3 - Python**

Birthday Book is a Command Line Interface styled application, designed for a user to access their contacts birthday's, retrieve specific age & date information, edit & delete existing birthday contacts, and add new birthday entries data. This project has been designed for educational purposes and uses the Code Institutes mock terminal to run.

You can view the live program here: <a href ='' target="_blank"> Birthday Book Application</a>

![Birthday Book Image](docs/images/)

# Contents

* [Objective](<#objective>)
* [User Experience](<#user-experience-ux>)
  * [Site Aims](<#site-aims>)
  * [User Stories](<#user-stories>)
  * [Flow Chart](<#flowchart>)
* [Features](<#features>)
* [Future Features](<#future-features>)
* [Technologies Used](<#technologies-used>)
* [Data Model](<#data-model>)
* [Testing](<#testing>)
  * [PEP8 Valdation](<#pep8-validation>)
  * [Manual Testing](<#manual-testing>)
  * [Validation](<#validation>)
  * [Bugs Fixed](<#bugs-fixed>)
  * [Existing Bugs](<#existing>)
  * [Terminal Compatibility](<#terminal-compatibility>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# Objective

The aim of this project is to deliver an easy and satisfiying command line interface directory that simplifies life for the user.

[Back to top](<#contents>)

# User Experience (UX)

## Site Aims

* To provide the user with a simple app that allows them to find contact's birthdays quickly 
* To create an app the user is more than happy to return to based on ease of use and functionality
* To provide an interactive experience that's easy to navigate and understand
* To provide a clear and appropriate response to any user inputs

[Back to top](<#contents>)

## User Stories

The **user** is any person who likes productivity and organisation apps, partocularly ones that run via the command line.

| ID  | ROLE |                                   ACTION                                   |                    GOAL                     |
| --- | :--- | :------------------------------------------------------------------------: | :-----------------------------------------: |
| 1   | USER |    As a user, I want to access all of my contact's birthdays at once       |        So I can browse at leisure           |
| 2   | USER |    I want to be able to navigate around the interface easily               |          so I feel like returning           |
| 3   | USER |          I want to know what app does from the opening message             |        So as to avoid any confusion         |
| 4   | USER |       I want to retrieve a contact's information based upon their name     |       So I can execute action quickly       |
| 5   | USER |               I want to add new contact information                        |          to keep information current        |
| 6   | USER |     I want to update an existing entry if there's been a change            |           So I can stay organised           |
| 7   | USER |   I want to be able to retrieve entries by category (family/friends)       |         to streamline my searching          |   

**user**  

[Back to top](<#contents>)

## Flowchart

![Birthday Book Flowchart](docs/flowchart/)

[Back to top](<#contents>)

# Features

There are 4 main features in the Birthday Book, which are numbered in the main menu:

![Main Menu](assets/images/)
 
## Search Birthdays

Once selected, Search Birthdays allows the user to search the connected google worksheet by either

  * First name
  * Last name
  * Category

![Search Birthdays](docs/images/)

## Add New Birthday

  * The 3rd feature accessible from the main menu, is the Add New Birthday feature
  * Once selected, the user is asked to input a value for either First Name, Last Name, Age Turning, birthday, or Category. 
  * Both names, phone number and category are required entries, the user can input NA for those not required.
  * Once all fields have been entered the entry is saved to the google sheet
  * The details are printed to the terminal and the user is asked if they want to edit the information.
  * If they do, they'll be taken to edit the contact, otherwise they can go back to the main menu.

![Add New Birthday](docs/images/)


## Edit Existing Birthday

* third option in the main menu is Edit Existing Birthday. On selection they'll first be taken to search for the entry they wish to edit.
* after locating the required entry, the app will ask the user if they'd like to edit this entry by typing Y/N
* If Y, they'll then be able to select which field of the entry they'd like to alter. 
* The user makes the relevant changes and saves, with a reasuring message from the app that prints the updated entry.
* The worksheet is updated with the new birthday information.


![Edit Existing Birthday](docs/images/)


## Retrieve all Birthdays

* lastly from the main menu, When selected, Retrieve all Birthday's prints all birthday entries to the terminal  

![Menu example of 4 options](docs/images/)


# Future Features

## Days until data

A function could be added to calculate the days until the contact's birthdays. This would be based on the date the entry was made (using datetime) and the birthday date entered manually. A fuction could then calculate the days until, and upate the form.

## Text Bot 

A Bot could be built using Twilio, to generate and send a birthday text on each individuals birthday, based on a phone number being entered along with the other data fields provided here.  

## Automated Email Birthday Cards

Zapier could be used here to set up an automated email card on each individuals birthday.

## Automated birthday reminders 

User's could set up a text reminder so they'd never have to forget giving mum a call on her birthday! 

[Back to top](<#contents>)

# Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) - to provide some structure to the program
* [CSS3](https://en.wikipedia.org/wiki/CSS) - to provide the styling for the program
* [Python](https://www.python.org/) - To provide the functionality to the program
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug
* [Lucidchart](https://www.lucidchart.com/pages/tour) - Used to create the flow chart
* [Google sheets](https://www.google.co.uk/sheets/about/) - used to host the programs data
* [Gitpod](https://www.gitpod.io/) - Used to create, edit and compile the code for the program
* [Heroku](https://dashboard.heroku.com/apps) Used to deploy application.

## Python Libraries

* [gspread](https://google-auth.readthedocs.io/en/master/) allows communication with Google Sheets
* [Google Auth](https://google-auth.readthedocs.io/en/master/) Used to provide access for the app to interact with google sheet.
* [colorama](https://pypi.org/project/colorama/) allows terminal text to be printed in different colors
* [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - used to access figlet fonts
* [PyInputPlus](https://pypi.org/project/PyInputPlus/) - used to validate user inputs

[Back to top](<#contents>)

# Data Model

Google Sheets was used to store all the data for the Birthday Book. Data was sent to and retrieved from it. The google sheet had a singular worksheet which stored all the data. The columns of the worksheet provided the different entry fields for the birthday data. 

![Google sheets](docs/images/)

[Back to top](<#contents>)

# Testing

## PEP8 Validation

[PEP8](http://pep8online.com/) Online validation was used to check that the code is up to standard. All pages cleared the PEP8 validation with no errors.

[PEP8](http://pep8online.com/) 

## Manual Testing

<details><summary> Manual Testing Info</summary>

### Welcome screen

### Search birthdays

### Add New Birthday

### Edit Existing Birthday

### Retrieve all Birthdays
  
### Exit

### Other


</details>

[Back to top](<#contents>)  

## Validation 

Birthday Book relies heavily on information input, so validation of this data is paramount to the correct functionality of the app.
I used the `pyinputplus` module which offers in built validation.

* the users are presented with a numbered menu, 
* they then must input their choice 

The following function runs: 

`def user_response(message, min_value, max_value):    
    input = pyip.inputInt(prompt=message, min=min_value, max=max_value)  
    return input`    

The minimum and maximum value parameters ensure the user is only able to enter the numbers present in the menu, if they do not then the following error message is displayed:  

![](assets/images/invalid_entry1.png)

pyinputplus also has methods for email & string inputs, which you can see being used below:

![](assets/images/input_validation_code.png)

I added an additional validate_next_birthday function for date entries whihc allows inputs of only 10 characters and no alphabetical characters. If the date entered does not pass the validation an error message is thrown:

![](assets/images/)

[Back to top](<#contents>)

## Bugs Fixed

### Bug 1

Initially the category coloumn of the google sheet was not being updated when editing that field from the App. This was due to a logic error and fixed by creating a new variable category_input, line 434, ass opposed to user_input as it was before. 
 
<details><summary>Bugs Fixed info</summary>

![bug 1](docs/images/)

</details>

[Back to top](<#contents>)

## Existing Bugs 

When there are 2 Birthday contacts with the same first name, and 1 of those entries is selected to be deleted, the programme will delete the first returned entry. This is due to the contact id not being specific enough and intefering with the age_turning coloumn integer. This could be fixed by creating more complex id names for each Birthday entry. 

![Existing Bug](docs/images/)

## Terminal Compatibility

![Heroku Terminal](docs/images/heroku-terminal.png)

![Local Terminal](docs/images/local-terminal.png)

[Back to top](<#contents>)

# Deployment

## Deployment to Heroku

* Create a Heroku account and login
* Click 'New' from the dashboard, underneath the header in the top right corner
* Click 'Create new app' option
* Enter your unique application name, select your region and then click 'Create App'
* Now on the project page, click the 'Settings' tab and scroll down to Config Vars.
* In the KEY input field, enter 'CREDS' and in the VALUE input field, enter the content of you creds.json file in your repository
* Click the 'Add' button to the right to add the Convig Vars
* On the same page scroll down to the buildpacks section and click 'Add Buildpack'
* Add both the Python and node.js buildpacks, making sure Python is above node.js
* Go back to the 'Deploy' tab
* Select Github deployment method
* Search for your repository and click the 'Connect' to link Heroku to your repository
* select your preferred deplyment type; Automatic Deployment or Manual Deployment

## To fork the repository on GitHub

## To clone the repository on GitHub

</details>

[Back to top](<#contents>)

# Credits

[Back to top](<#contents>)

# Acknowledgements

[Back to top](<#contents>)
