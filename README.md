# :)



# Creating a Python Package

This guide outlines the steps to create a simple python package with basic functionality.

### Steps for Creating a Python Package:

1. **Create Package Code**:
   - Create a directory for your package (e.g., `my_package`).
   - Inside that directoy, write your python code. For example:
     - `app.py`: Contains your main logic or functionality.
     - `__init__.py`: Marks the directory as a python package. It can be empty or contain initialization code.

2. **Create `setup.py`**:
   - The `setup.py` file is used by setuptools to define the package's metadata and installation requirements.
   - Example of `setup.py`:
     ```python
     from setuptools import setup, find_packages

     setup(
         name='name_of_package', 
         version='0.1',
         packages=find_packages(),
         install_requires=[
             'numpy',  # dependencies 
         ],
     )
     ```
     - **`name`**: The name of your package. This should match the name of the folder where the package is contained.
     - **`version`**: Version number of the package.
     - **`packages`**: Automatically discovers all sub-packages in your project.
     - **`install_requires`**: Lists any external dependencies your package requires (e.g., `numpy`).

3. **Create `README.md`**: 
   - A `README.md` file provides a description of the package, how to install it, and any additional information such as usage examples.

4. **Install the Package Locally**:
   - From the root of your project, run the following command to install the package locally:
     ```bash
     pip install ./examplepackage
     ```
   - This makes your package available for use in other python scripts.

5. **Use the Package**:
   - In any script, you can now import and use your package:
     ```python
     from examplepackage import app
     ```

---

### Summary of Key Files:

- **`my_package/__init__.py`**: Contains initialization code.
- **`my_package/app.py`**: Contains the actual python code for your package functionality.
- **`setup.py`**: Used by setuptools to install your package. It includes metadata (name, version) and dependencies (`install_requires`).
- **`README.md`**: A documentation file that describes your package and how to use it.

--- 

