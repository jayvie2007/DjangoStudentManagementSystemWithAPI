# DjangoStudentManagementSystemWithAPI

<h2> To run the system first install Python 3.10 </h2>
<p> Open your VS Code then open this folder <p>

do not clone the .env folder instead create a new virtual environment

<h3>Installing new virtual environment</h3>

```bash
  python -m venv .env
```

Then install the prequisite data

<h3>Installing the necessary files</h3>

```bash
  pip3 install -r .\requirements.txt
```

<h3>Activate the virtual environment</h3>

```bash
  .env\scripts\activate
```

<p> Make sure you are in the AuthDjango Folder </p>

<h3>change folder directory</h3>

```bash
  cd base
```

<p>After entering the base folder you may now run the server</p>

<p> in order to run the system first you must the data </p>

```bash
  python manage.py makemigrations
  python manage.py migrate
```

<p>After migrating you may now run the server</p>

<h3>Running Localhost server</h3>

```
  python manage.py runserver
```

--------------------------------------------------------------------------------------------------------------------------
<h2> System Overview </center>

<h3> Homepage </h3>

![Homepage](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/b0c5a58a-727f-4047-8fa2-5176d36646bb)

<h3> Register </h3>

![register](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/17d6fc1b-9b89-45c3-8fc9-c29873fa9a34)

<h3> Register Fail </h3>

![emailexist](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/0d6f0010-94a4-4936-88bb-0eb7cc057f63)

![password](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/36b2ff64-b7dc-49ba-b5ee-4f7b822ec969)


<h3> Login </h3>

![login](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/fe880af5-fdb3-4240-85fd-e6500bd58820)

<h3> Login Fail </h3>

![failedlogin](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/f13eca8d-71dd-46ce-94b1-fde4ce21c1e7)

<h3> Login Success </h3>

![loginsuccess](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/79b8c81f-76e3-4fa3-aa69-d27bf0ae1b01)

<h3> Add Student </h3>

![add](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/da682111-6d92-4398-b0ab-f0a41195f663)

![added](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/45045d43-586a-4ca5-a600-4fed0d57a6d9)

<h3> Edit Student </h3>

<h3> Delete Student </h3>

![delete](https://github.com/jayvie2007/DjangoStudentManagementSystemWithAPI/assets/123736031/3415d9f4-01c3-4f2b-b4c7-93f562bdde56)




