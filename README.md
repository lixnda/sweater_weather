# sweater_weather


## Project Description
Everyone has those days where they do not know what to wear. This is the problem that my project
attempts to solve, giving users weather suitable outfit inspiration. User would be able to enter the
specific city that they are in, and the program will be able to extract weather data using an API.
Next, according to the type of clothing suitable for that weather, an image processing algorithm will
then generate a top and a bottom piece that most suits each other. The user will then be able to
click on a certain piece of clothing if they are interested and it will link them to a Depop page where
they could purchase the piece. Overall, this program attempts to inspire different outfits and give
users the opportunity to buy new clothing.

## Install Guide

**Prerequisites**

Ensure that **Git** is installed on your machine. For help, refer to the following documentation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### How to clone/install
1. In terminal, clone the repository to your local machine:

SSH METHOD (requires the SSH key):

```
git clone git@github.com:lixnda/sweater_weather.git
```
2. Install dependencies

```
pip install -r requirements.txt
```

## Launch Codes

**Prerequisites**

Ensure that **Git** and **Python** are installed on your machine. It is recommended that you use a virtual machine when running this project to avoid any possible conflicts. For help, refer to the following documentation:
   1. Installing Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
   2. Installing Python: https://www.python.org/downloads/

### How to run

1. Create Python virtual environment:

```
python3 -m PATH/TO/venv_name
```

2. Activate virtual environment

   - Linux: `. PATH/TO/venv_name/bin/activate`
   - Windows (PowerShell): `. .\PATH\TO\venv_name\Scripts\activate`
   - Windows (Command Prompt): `>PATH\TO\venv_name\Scripts\activate`
   - macOS: `source PATH/TO/venv_name/bin/activate`

   *Notes*

   - If successful, command line will display name of virtual environment: `(venv_name) `

   - Type `deactivate` in the terminal to close a virtual environment

3. Navigate to project app directory

```
 cd sweater_weather/
```

4. Run App

```
 python3 app.py
```

5. Open the link that appears in the terminal to be brought to the website
    - You can visit the link via several methods:
        - Control + Clicking on the link
        - Typing/Pasting http://127.0.0.1:5000 in any browser
    - To close the app, press control + C when in the terminal

```    
* Running on http://127.0.0.1:5000
```
