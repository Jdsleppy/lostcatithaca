ssh lostcatithaca.com
cd lostcat
nvm install
npm install
npm run build:css
poetry install
poetry shell
cd src
python manage.py check --deploy --fail-level=WARNING
python manage.py migrate
python manage.py collectstatic --clear --no-input
sudo systemctl reload lostcat.service
