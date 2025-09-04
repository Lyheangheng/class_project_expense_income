echo "Building the project..."
pip install -r requirements.txt

echo "Collect static files..."
python manage.py collectstatic --noinput --clear