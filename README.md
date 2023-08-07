# Automate Website with Selenium and Django (Zanwar Industry)

This repository contains a Django web application that automates website interactions using Selenium. The application was developed for Zanwar Industry to streamline repetitive tasks and increase efficiency in website operations.


## Skills i have learned : 
Project Planning most IMP ,selenium , djnago with selenium , Automation ,   


## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Overview

As part of the automation initiative for Zanwar Industry, this Django web application leverages the power of Selenium to automate interactions on a specific website. The primary goal is to eliminate manual effort and save time by automating repetitive tasks.

The main features of this application, developed exclusively for Zanwar Industry, include:
- Auto login: Automatic login to the target website using provided credentials.
- Manual login with Captcha: Supports manual login with Captcha input, where required by the website.
- Bulk Upload: Enables users to upload multiple files for automated processing.
- Headless Mode: Provides an option to run the automation in headless mode, without displaying the browser window.

## Prerequisites

Before using this application, ensure that the following prerequisites are met:

- Python 3.10 or higher
- Django 4.1.7 or higher
- ChromeDriver (for Selenium)

## Installation

To get started with the application, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/chinmay404/Automate_website-Zanver_group
   cd automate-website
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Download ChromeDriver and add its location to the system PATH.

4. Run the Django development server:

   ```
   python manage.py runserver
   ```

5. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

Using the application is straightforward:

1. Navigate to the homepage of the application.

2. Click on the "Auto Login" button to perform an automated login using predefined credentials.

3. Click on the "Manual Login" button to perform a manual login where Captcha input might be required.

4. To change the login credentials, click on the "Change Username and Password" link and update the values.

5. Upload files on the "Home" page to perform automated tasks on them.

6. To run the automation in headless mode, click on the "Headless Mode" button.

## Features

- Automated login using predefined credentials
- Manual login with Captcha support
- Bulk upload for automated tasks on multiple files
- Headless mode option for running automation in the background

This project was developed exclusively for Zanwar Industry to enhance website automation and optimize daily tasks. The application is tailored to meet the specific needs of Zanwar Industry's website operations. For any inquiries or assistance, feel free to contact the project contributors.

Happy automating and thank you for using this application!
