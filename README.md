# Instagram Follower Bot

This project is a Python script that utilizes Selenium, a web automation tool, to automate the process of logging into Instagram, finding followers of a specified account, and automatically following them.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or above)
- Selenium library (`pip install selenium`)
- ChromeDriver executable (compatible with your Chrome browser version)

## Setup

1. Clone or download the project files to your local machine.
2. Download the ChromeDriver executable and specify its path by setting the `CHROME_DRIVER_PATH` variable in the script to the correct path on your system.
3. Open the script file in a text editor and set the following variables:
   - `SIMILAR_ACCOUNT`: The Instagram account for which you want to find and follow the followers.
   - `EMAIL`: Your Instagram username or email address.
   - `PASSWORD`: Your Instagram password.

## Usage

To use the Instagram Follower Bot, follow these steps:

1. Run the script by executing the command `python main.py`.
2. The script will open a Chrome browser window and navigate to the Instagram login page.
3. After a few seconds, the script will automatically fill in the login form with the provided credentials and submit it.
4. Once logged in, the script will close any popups that appear (such as the "Save Login Info" and "Turn on Notifications" prompts).
5. Next, the script will navigate to the profile page of the specified `SIMILAR_ACCOUNT`.
6. It will click on the "followers" link to open the followers popup.
7. The script will then scroll through the followers list, allowing it to load more followers dynamically. By default, it scrolls 10 times, but you can adjust this value as needed.
8. After scrolling, the script will start following the found followers. It will click the "Follow" button for each user in the list.
9. If the "Follow" button is not clickable due to an intercepted element exception, the script will handle it by clicking the "Cancel" button and move on to the next user.
10. Once all followers have been processed, the script will exit.

**Note:** It's important to use this script responsibly and in accordance with Instagram's terms of service. Automated actions on Instagram may be against their policies, and your account could be restricted or banned as a result. Use this script at your own risk.

## Limitations and Future Improvements

- The script assumes that the ChromeDriver executable is placed in the specified `CHROME_DRIVER_PATH`. Ensure that the ChromeDriver version matches your Chrome browser version.
- The script currently follows all the found followers automatically. To enhance it, you can add logic to check if a user is already being followed or implement filters to select specific followers based on criteria.
- The script uses hardcoded delays (`time.sleep()`) to allow time for page loads and interactions. Depending on your system and internet speed, you may need to adjust these delays to ensure proper execution.
- The script interacts with the web elements based on their locators. If Instagram's web interface changes, the locators may need to be updated accordingly.

## Disclaimer

This project is for educational purposes only. The use of automated tools on social media platforms may violate the terms of service of those platforms. Use this script responsibly and at your own risk. The developer is not responsible for any misuse or consequences caused by the usage of this script.
