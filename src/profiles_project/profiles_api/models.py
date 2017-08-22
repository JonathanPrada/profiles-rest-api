from django.db import models
# The standard base model of the django users
from django.contrib.auth.models import AbstractBaseUser
# The standard permissions
from django.contrib.auth.models import PermissionsMixin
# Import django base user manager class
from django.contrib.auth.models import BaseUserManager

# The user profile class manager, needs to match the object manager inside
# The UserProfile class
class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""
    def create_user(self, email, name, password=None):
        """Creates a new user profile object"""
        # Check that they provided an email address
        if not email: # If blank or false
            raise ValueError("Users must have an email address")

        # Sets all emails to lowercase email
        email = self.normalize_email(email)

        # Create a new user profile
        user = self.model(email=email, name=name)

        # Set the password for this user that they provided
        # We do it here because the set password function will encrypt it here
        user.set_password(password)
        # Save this user to the model in the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user with given details"""
        # Use the create user function
        user = self.create_user(email, name, password)
        # Assigns the user as super user and Staff
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

# The user profile class
class UserProfile(AbstractBaseUser, PermissionsMixin): # Inherit from imports
    """Represent an user profile inside our system"""

    # Have an email field, each email must be unique
    email = models.EmailField(max_length=255, unique=True)
    # Name field per user
    name = models.CharField(max_length=255)
    # Used to determine if this user is currently active in the system
    is_active = models.BooleanField(default=True)
    # Used to determine if this user is staff, new members are not Staff
    # This field is required when you substitute the django user model for our own
    is_staff = models.BooleanField(default=False)

    # Object manager used to manage user profiles, required when using our own model
    objects = UserProfileManager()

    # The standard model uses this field for logging in users, we are saying
    # Instead of a username lets use the email field, as its unique anyway.
    USERNAME_FIELD = 'email'
    # List of fields that are required for all user profile objects
    REQUIRED_FIELDS = ['name']

    # Helper functions for our model, self because its a class function
    def get_full_name(self):
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    # This function is required in Django so its know how to return our
    # object as a string.
    def __str__(self):
        """Django uses when it needs to convert the object to a string"""
        return self.email
