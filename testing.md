## Manual Testing of Application 

<details>
<summary>Register and Login</summary>
<br>

<b>Register and Login</b>

Testing was performed by registering a new user. The application warns that there is already an existing user when it was tried to input information already in the database. Once unique information was registered, a new user was created, with which you can log in. 

The registration and autherization of users is handled by the Django authentication system. 

- Register - registration_form.html
- Login - login.html

![Register and Login](assets/images/register_and_login.gif)

</details>

<details>
<summary>Create Cruise</summary>
<br>

<b>Create Cruise</b>

Once you have created a user, you can create a cruise. The autherization system is put in place to track who has created the cruise in question. When clicking the "Create Cruise"-button, you will either get directed to the create_cruise.html to create a cruise, or you will be asked to login, in case you haven't done this already. 

![Create Cruise](assets/images/create_cruise.gif)

</details>

<details>
<summary>Add Item</summary>
<br>

<b>Add Item</b>

Once the cruise is created, you can start adding items to the packing items. You insert the name of the item, the quantity which you wish to bring, and an optional description. Any user that is logged in can add items to any cruise. But only the creator of a cruise can edit the items. This to keep traceability for changes in the planning stages of the cruise. 

![Add and Edit Item](assets/images/add_item.gif)

</details>

