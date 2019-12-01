# AOS Service

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Ubuntu Server LTS (16.04) (used on developement)
- or a alternative debian based distro

1. Install python3 - virtualenv
```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
```

### Installing

1. Clone github repository
```
$ git clone 
```

2. Create a new virtual enviroment
```
$ virtualenv -p python3 myenv
$ source myenv/bin/activate
```

3. Install requirements
```
(myenv) $ pip3 install -r requirements.txt
```

4. Migrate project
```
(myenv) $ python3 manage.py makemigrations
(myenv) $ python3 manage.py migrate
```

5. Run local server
```
(myenv) $ python3 manage.py runserver 0.0.0.0:8000
```
