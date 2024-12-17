# a project for the restaurant LittLemon, created with Django and a MySQL database.

## Features
- List all menu items
- Add new menu items
- Update existing menu items
- Delete menu items

## Installation
To run the project locally, clone the repository and set up the environment:

```bash
git clone https://github.com/yourusername/LittleLemon.git
cd LittleLemon
python -m venv myenv
source myenv/bin/activate  # For Windows use myenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
