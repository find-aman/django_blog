## django_blog
**PyBlog** - Blog application built using Django

**Try Out The App :** [https://py-blogg.herokuapp.com/](https://py-blogg.herokuapp.com/)

*Note:* After opening the application using the above link, some profile images may not be visible, since it is deployed on Heroku and static files storage is not provided there. *But will work if a new user is registered and a new profile image is uploaded.*

**Features of the application:-**
- Able to view the post from every user on the home page. 
- User registration
- User login
- User logout
- User profile 
- User profile update
- User password reset using email 
- New post creation 
- Update and Delete posts
- Posts list Pagination
- Routes restrictions using decorators and mixins
- Check specific user's posts and its count
- About section
- Admin panel

**Steps to run the application:-**
*Assumption python 3  is installed properly*
1. Clone this repository.
2. Open the folder created and open cmd in it.
3. Install virtual environment by `pip install virtualenv`
4. Create a virtual environment by `virtualenv venv` 
5. Activate the virtual environment by `venv\Scripts\activate`
6. Install all the packages from requirments.txt file by `pip install -r requirements.txt`
7. Now create some User Environment Variables with names like.
	- **EMAIL_USER** (set value to an gmail email address from which password reset mail will be sent).
	- **EMAIL_PASS** (set value to the password of above email id)
	- **DEBUG_VALUE**(set value True for testing)
	- **SECRET_KEY**(set value to a newly generated secret key using *secrets* module in python using `token_hex(24)`)
	- Make sure that email address should be of *Gmail* only for sending passsword reset email and "Login using less secure apps" function is enabled in the email id.
8. Make migrations by `python manage.py migrate`
9. Create a superuser to admin testing by `python manage.py createsuperuser` and enter the details asked.
10. Then run the server by `python manage.py runserver` 

**Testing of Features:-**
- Click on **Register** on the home page to create a new account.
-  Enter valid **Username**, **Email**, **Password** *(Enter correct email to check password reset functionality)*
- Click **Sign Up**, will be redirected to **Log In** page.
- Login using the **Username** and **Password** created.
- Click on **Profile** to view and edit user profile and can update profile image also.
- User Profile URL can be accessed only when a user is Logged In otherwise redirected to the Login page.
- Click on **New** to create new posts.
- Fill in the **Title** and **Content** and click **Post**.
- Will be redirected to the post edit page having **Update** and **Delete** buttons.
- Click on **Home** to view the created post.
- Click on the post again and click on **Update** to update the and click **Post** post the changes made.
- Click on **Home**, click the **Post** created and click **Delete**, posts will be deleted.
- User can only **Update** and **Delete** post when logged in and that too only posts, posted by him.
- Add more posts *(more than 5)* to see the implementation of **Pagination**. In the bottom of home page **Previous**, **Next** and **Numbered** buttons will appear.
- Click on the **Username** of any post, it will show the post from that user only and its count.
- Click on **Logout** to logout from the application.
- Click on **Login Again** and click **Forgot Password**.
- Enter the email id of the registered user and click **Request Password Reset**. An email will be sent to the entered email id with the password reset link, click on the link and enter a new password and test the new password.
