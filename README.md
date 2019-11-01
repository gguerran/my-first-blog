# my-first-blog
Um simples blog baseado no tutorial Django Girls (deployed in http://gguerran.pythonanywhere.com/)
## How to set up the local environment?

1. Clone this repository.
2. Create a virtualenv with Python 3.6.
3. Activate the virtualenv.
4. Install the requirements.
5. Setup the instance with .env
6. Perform the migrations.
7. Add a superuser to access the admin area.

```console
git clone https://github.com/gguerran/my-first-blog.git
cd my-first-blog
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py createsuperuser
```
