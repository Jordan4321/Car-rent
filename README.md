# Car-rent
Work in Progress

For start project:
1. Download code and open in python.
2. Create new virtual environment. ( Files -> settings -> Python:Car Rent -> Python interpreter -> setting(icon) -> add -> ok -> apply
3. Enter to Car-rent/main catalog (cd car-rent/main)
4. In terminal use command: pip install -r requirements.txt 
5. In the "main" folder, create a text file named .env and copy the contents of the keyenv file to it.
6. in terminal use commands: 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   (write name, email, password, and set y)
python manage.py runserver
7. Now you can check website.