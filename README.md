  Locker

Locker
======

Locker is a simple application designed to lock your mouse and keyboard, providing additional protection when you don’t want input from these devices. With Locker, you can maintain your privacy and prevent unauthorized access to your device.

Main Features
-------------

*   **Mouse and Keyboard Locking**: Prevents others from accessing your device without permission.
*   **Easy to Use**: A simple interface for locking and unlocking.
*   **Flexible Settings**: Customizable to meet user needs.

Project Structure
-----------------

Locker/
│
├── .gitignore            # File to ignore certain files in Git
├── .vscode               # Folder for Visual Studio Code configuration
├── build                 # Folder for build files
│   ├── build.bat        # Script to build the application
│   ├── locker.spec      # Specification for the Locker application
│   ├── unlocker.spec    # Specification for the Unlocker application
│
├── images                # Folder to store images
│   ├── lock.jpg         # Image related to the application
│
├── LICENSE.txt           # License file for the project
├── locker.py             # Main script for the Locker application
├── unlocker.py           # Script to unlock
├── pnputil.py            # Module to manage devices
├── pnp\_controller.py     # Controller for plug and play devices
├── \_\_pycache\_\_           # Folder that stores Python cache files
└── README.md             # Project documentation
    

Installation
------------

1.  **Clone Repository**:
    
    git clone https://github.com/username/Locker.git
    cd Locker
                
    
2.  **Install Dependencies**: Ensure you have Python installed, then run:
    
    pip install -r requirements.txt
                
    
3.  **Run the Application**:
    *   To lock:
        
        python locker.py
                            
        
    *   To unlock:
        
        python unlocker.py
                            
        
4.  **Build the Application**:
    
    To build the application, you can use PyInstaller. Run the `build.bat` script to build the application automatically. You can check the output in build folder, and make sure to turn off ur antivirus
    

License
-------

This project is licensed under the [MIT License](LICENSE.txt).

Contributing
------------

feel free to update this project

Contact
-------

If you have any questions, please contact:  
[Haku / SK 19-2](mailto:sandyka.bala@binus.edu)

Thank you for using Locker!