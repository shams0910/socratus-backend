# Socratus
Socratus - CMS software platform designed to help elementary/high schools to automate daily routines, better manage school contents and many other things.
[Learn more](https://www.facebook.com/socratus.platform/)

[Project presentation](https://docs.google.com/document/d/1U2YtZv3Bno64o4bpiU4C5AVlg7wZtXmyPHZtPh_eymg/edit?usp=sharing)

### Setup instuctions
main working branch is <strong>develop</strong> 

1. create environment
```
virtualenv env_name -p python3.8.5
```

2. Activate it
Linux
```
source env_name/bin/activate
```

Windows
```
env_name\Scripts\activate
```

3. install packages for the project


```
pip install -r requirements.txt

```

4. Setup env file to use for db and django settings.py configuration

5. And finally
```
py manage.py migrate
py manage.py runserver
```
