from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='alex',
    author_email='munikl869d@gmail.com',
    description='FastApi app',
    install_requires=[
        'fastapi==0.111.0',
        'uvicorn==0.30.0',
        'SQLAlchemy==2.0.30',
        'pytest==8.2.1',
        'requests==2.32.2',
        'celery==5.3',
        'pytesseract',
        'psycopg2-binary',
        'alembic'
    ],
    scripts=[
        'app/main.py',
        'scripts/create_db.py'
    ]
)
