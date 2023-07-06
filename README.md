# Automated Testing with Selenium

This program demonstrates automated testing using Python and Selenium to test fields on a web page. The goal is to ensure the fields still work even if their positions or properties change.

## Prerequisites

To run this program, you need to have the following dependencies installed:

- Python (version 3 or above)
- Selenium library
- Web driver (specific to the browser you are using)

## Installation

1. Clone this repository to your local machine or download the files as a ZIP archive.

2. Install the necessary dependencies. You can install Selenium using pip:

```
shell
pip install selenium
```

3. Download and install the appropriate web driver for the browser you plan to use. This program uses ChromeDriver by default. Make sure the web driver version matches your browser version. You can download ChromeDriver from the official website: ChromeDriver - WebDriver for Chrome

4. Extract the web driver executable to a location on your system and add that location to your system's PATH variable.

# Usage

1. Open the command line or terminal and navigate to the project directory.

2. Run the Python script:

```
python automated_testing.py
```
3. The Chrome browser window will open and navigate to the specified web page. You can observe the automated testing in action.

4. Once the testing is complete, the program will print the result in the console. If the form submission was successful, it will display "Form submitted successfully." Otherwise, it will show "Form submission failed."

# Customization

1. To test different fields on the web page, you can modify the code in the automated_testing.py file. Locate the relevant elements by using different locator strategies provided by Selenium.

2. If you are using a different web browser, you need to download the appropriate web driver and update the code to use the corresponding web driver.

3. If your web driver executable is located in a different path, update the code in automated_testing.py to include the correct path to the web driver.

# Notes

This program assumes a stable internet connection. Make sure you have a reliable internet connection to ensure the web page loads correctly.

If the web page URL or the HTML structure changes, you may need to update the code accordingly to locate the elements correctly.

For more advanced scenarios, you can add additional assertions and error handling to enhance the robustness of the automated testing.
