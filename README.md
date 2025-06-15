# Project Setup

To run this Django project:

```bash
1. Clone the project

  git clone git@github.com:your-org/your-repo.git
  cd your-repo

2. Create virtual environment

  python -m venv venv

3. Activate it (use the appropriate one for your OS)

  # Windows:
    venv\Scripts\activate

  # macOS/Linux:
    source venv/bin/activate

4. Install requirements

  pip install -r requirements.txt

5. Apply migrations

  python manage.py migrate

6. Run the development server

  python manage.py runserver
