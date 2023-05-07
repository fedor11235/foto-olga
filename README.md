# telegram game bot
## Project setup
creating a virtual environment
```
python -m venv venv
```
launch virtual environment in cmd (windows)
```
venv\Scripts\activate
```
install all the necessary dependencies from requirements
```
pip install -r requirements.txt
```
bot launch
```
python app.py
```
server start
open another terminal and in it we write the command
```
python server.py
```
## for development
information about the bot is in the file "info_information.txt"

exit the virtual environment (windows)
```
venv\Scripts\deactivate.bat
```
save all project dependencies to a file
```
pip freeze > requirements.txt
```
## for development
comments on the project

For some reason, when describing the model, when I set the index in this way, the index is always written Null
```
id = db.Column(db.Integer, primary_key=True)
```
command to stop git from tracking a file
```
git rm --cached .you_name_file 
```
useful links
```
create a migration repository
```
flask db init
```

