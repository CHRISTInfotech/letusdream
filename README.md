# letusdream

LET US DREAM is a locally rooted and globally established not-for-profit organization. Since its inception, LET US DREAM has envisioned globally interconnected communities where no one and nothing stands alone. Grounded in volunteerism, collaboration, and networking principles, LET US DREAM promotes the idea of holistically developed, sustainable communities worldwide.

### Contributors guide
To contribute to the LUD project:
1. Fork the project repository [https://github.com/CHRISTInfotech/letusdream.git].
2. clone the project to your system.
3. create an issue in the main project repository [https://github.com/CHRISTInfotech/letusdream.git] and describe on what you are working on it.
4. create a branch for your contribution in your system.
5. finish the chnages and push the repo to your repository.
6. raise a PR to [https://github.com/CHRISTInfotech/letusdream.git] main branch.

### Developers guide
Steps to run the development version of the project:

1. Create a Virtual Environment [https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/]
2. Activating the Virtual Environment
3. Instaling the required packages for the project [pip install -r requirements.txt]
4. Running the Django Server [python manage.py runserver] [https://docs.djangoproject.com/en/5.0/intro/tutorial01/]
5. Go to the local webserver at: http://127.0.0.1:8000/

    ---
To setup the project, either follow the documents as mentioned in the above or below

1. To create virtualenv
    
    ```
    python -m venv venv                       # windows

    python3 -m venv venv                      # linux
    ```

2. Activate the virtual environment
    ```
    ./venv/Scripts/activate                   # windows

    source venv/bin/actvate                   # linux
    ```

3. To install the project requirements

    ```
    pip install -r requirements.txt
    ```

4. To run the server
    ```
    python manage.py runserver
    ```
    If you are seeing the screen "Bad Request (400)", make sure that you are turning on the development mode on in settings.py file located inside the letusdream/settings.py file line no 26 [DEBUG = True]
5. Go to the local webserver at: http://127.0.0.1:8000/