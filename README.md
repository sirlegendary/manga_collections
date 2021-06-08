# Manga Collections

## Why?
This allows you to have a place to store all your favourite mangas in one place and also see when the latest chapters were released.
This way you can only focus on the mangas you really want.

## Language & Framework 
- Python 3.7
- Django 3.0.5

## Manga Source
- [TAADD](https://www.taadd.com/)

## Instructions 
- Migrate DB
	`docker-compose run web python manage.py makemigrations`
	`docker-compose run web python manage.py migrate`

- Create Super user
	`docker-compose run web python manage.py createsuperuser`

- Start
	`docker-compose up`

- Add Manga to shelf
    1. Visit: `0.0.0.0:8000/admin` and login with the user you created above
    2. Click on the `+Add` inside the `Manga collections`
    3. Enter the title of your desired Manga in the `Name` field
    4. Paste the exact URL of your dessired Managa from [TAADD](https://www.taadd.com/) inside the `URL` field i.e. [ONE PIECE](http://www.mangareader.net/one-piece)
    5. Click `SAVE`
    6. Now Visit: `0.0.0.0:8000` and your manga and its latest releases should be in the shelf
    7. Repeat step 1-5 to add more mangas

- If you wish to stop your server
	`docker-compose down`
