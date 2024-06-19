# Science Cruise Planner 

The application Science Cruise Planner is developed to facilitate the preperations for scientific cruises conduct with research vessels, in the terms of packing. When planning for a scientific cruise, the packing itinerary is crucial to ensure that sampling can go ahead as planned. 

[Live Site](https://cruise-preparation-92c5a099dd05.herokuapp.com/)

![Device Mockup](assets/images/still/all-devices-black.png)

# Content 
- [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [Admin Goals](#admin-goals)
  - [User Stories](#user-stories)
- [Features](#features)
  - [Navigation Bar](#navigation-bar)
  - [Register Page](#register-page)
  - [Login Page](#login-page)
  - [Create Cruise](#create-cruise)
  - [Cruise Details](#cruise-details)
  - [Add Item](#add-item)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validation](#validation)
- [Deployment](#deployment)
- [Planning](#planning)
  - [Database schema and flowchart](#database-schema-and-flowchart)
- [Security](#security)
- [Further Development](#further-development)
- [Credits](#credits)

# Project Goals 

### User Goals 
- Create a new cruise
- View cruise details
- Manage packing list 
- User authentication
- Mark item as packed

### Admin Goals 
- Admin Permissions 

## User Stories

### User Stories implemented 

- There is a form of interface to enter cruise name/number, start date and end date
- When data is entered, a new cruise is created
- It is possible to start adding packing itinerary
- There is a page view that displays cruise name, start date and end date
- The cruise is accessible through a unique URL or identifier
- There is an interface where items can be added to a specific cruise
- I can add new items to the packing list, specifying item name and quantity
- I can edit items from the packing list
- There is a user registration and login system
- Only users can create and modify cruises and packing lists
- I can access all cruises and items created
- I can delete a cruise from the system along with associated data
- I can access, create, manage and delete users from the system

### User Stories for further develoment 

- There is a checkbox next to the item which can be checked to mark it as packed
- Marking an item as packed updates its status in the database
- When viewing the cruise details, the items status is reflected in the pack list

[Link to user stories](https://github.com/users/hebjornberg/projects/2/views/1)

![Agile planning](assets/images/still/agile.png)

# Features

## Navigation Bar 

### The navigation bar of the website is responsive and contain the following links: 

- Home page
- Login page
- Register page
- View Cruises page
- Create Cruise page

The navigation bar will contain different buttons depending on if the site user is logged in or not. 

<b>Before logging in:</b>

![Navigation bar before logging in](assets/images/still/navbar-login.png)

<b>When logged in as a user:</b>

![Navigation bar when logged in as a user](assets/images/still/navbar-user.png)

The Science Cruise Planner logo also directs back to the Home page of the website. 

## Register Page 

### For a user to be able to create and plan a cruise, they will have to register as a user to the site. 

![Register Page](assets/images/still/register.png)

## Login Page 

### Before being able to create and plan a cruise, the user needs to login to the website. This in order to keep traceability of who created which cruise. 

![Login Page](assets/images/still/login.png)

## Create Cruise 

### The user is able to create cruises with: 

- Cruise Name
- Start date
- End date

![Create Cruise](assets/images/still/create-cruise.png)


![Create New Cruise](assets/images/still/create-new-cruise.png)


## Cruise Details 

### Once a cruise is created, it will be directed to the Cruise Details section of the page. This will display: 

- Name of cruise
- Start date
- End date 
- Created by
- Packing Items 

In this view, it is also possible to start adding items to the packing list. 

![Cruise Details](assets/images/still/cruise-details.png)

## Add Item 

### Once a cruise is created, it is possible to start adding items to the packing list. The user that created the cruise additionally can edit the items added to the cruise. 

In the Add Items view, it is possible to state: 

- Name of item
- Quantity 
- Description 

![Add Item](assets/images/still/add-item.png)

# Testing

## Manual Testing 

The website has undergone manual testing. This has been documented in a separate testing file. 

Testing and validation: [Testing and validation](testing.md)

## Validation

Validation of code can be found in the testing-documentation. 

Testing and validation: [Testing and validation](testing.md)

# Deployment 

### The website has been deployed to Heroku. 

# Planning 

## Database schema and Flowchart 

# Security 

# Further Development

# Credits



