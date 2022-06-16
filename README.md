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
![Edit Existing Birthday](docs/images/)


## Retrieve all Birthdays

![Menu example of 4 options](docs/images/)


# Future Features

## Days until data

## Bot created to automate texts to Birthday Boys and Girls 

## Automated email Birthday Cards to recipients

## Automated birthday reminders 

[Back to top](<#contents>)

# Technologies Used

* [HTML5]
* [CSS3]
* [Python]
* [Google Chrome DevTools]
* [Lucidchart]
* [Google sheets]
* [Gitpod]
* [Heroku]

## Python Libraries

* [gspread]
* [Google Auth]
* [colorama]
* [pyfiglet]
* [PyInputPlus]

[Back to top](<#contents>)

# Data Model

![Google sheets](docs/images/)

[Back to top](<#contents>)

# Testing

## PEP8 Validation

[PEP8](http://pep8online.com/) 

### run.py

![run.py PEP8 test result](docs/images/)

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

[Back to top](<#contents>)

## Bugs Fixed

<details><summary>Bugs Fixed info</summary>

### Bug 1

![bug 1](docs/images/)


### Bug 2

![bug 2](docs/images/)

### Bug 3

![bug 3](docs/images/)


</details>

[Back to top](<#contents>)

## Exsiting Bugs 

## Terminal Compatibility

![Heroku Terminal](docs/images/heroku-terminal.png)

![Local Terminal](docs/images/local-terminal.png)

[Back to top](<#contents>)

# Deployment

## Deployment to Heroku

## To fork the repository on GitHub

## To clone the repository on GitHub

</details>

[Back to top](<#contents>)

# Credits

[Back to top](<#contents>)

# Acknowledgements

[Back to top](<#contents>)
