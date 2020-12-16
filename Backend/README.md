# Fragen-Antwort-App

Um das Backend starten zu können müssen ein paar Vorbereitungen auf der lokalen Maschine getroffen werden.

- Ein PostgreSQL-Server muss laufen --> https://www.postgresql.org/download/
- Python (3.9.1) muss vorhanden sein --> https://www.python.org/downloads/

How to setup:
-
- Den Backend Folder im Terminal öffnen (Open With --> Terminal) und folgenden Befehle eingeben:
    - pipenv install django
    - python manage.py migrate quizzes
    - pip install django-cors-headers
    - python manage.py createsuperuser (um Zugriff auf die Adminpage der API zu erhalten)
    
- Danach muss das Dumb-file (QuizDB) in der Datenbank eingespielt werden.
- Nun sollte die API mit: "python manage.py runserver" gestartet werden können
    
