# LinkedIn-Scrapper
A simple tool to extract basic profile information from a LinkedIn profile URL (name, location, description, experience, and "about" section) using Selenium and BeautifulSoup. The extracted data is displayed through a Streamlit interface.
### Features
- Fetches LinkedIn user profile information (Name, Location, Description, Experience, About)
- Uses Selenium to load and navigate the LinkedIn page.
- Parses the HTML with BeautifulSoup.
- Provides a user-friendly interface built with Streamlit.
## Requirements
- Python (of course)
- A compatible WebDriver for your browser (e.g., EdgeDriver, ChromeDriver). The WebDriver executable should be available in your system PATH or specified in your code. In my case I'm using Edge.
- Python libraries:
  - streamlit
  - selenium
  - beautifulsoup4
