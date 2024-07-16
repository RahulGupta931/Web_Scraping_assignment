# Web Scraping Registered Projects from HPRERA

This project is a Python script to scrape the first 6 projects under the "Registered Projects" heading from the [HPRERA Public Dashboard](https://hprera.nic.in/PublicDashboard). The script extracts the following fields from the project detail pages: GSTIN No, PAN No, Name, and Permanent Address. The extracted data is then saved to a CSV file.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone this repository or download the script file.

2. Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have Google Chrome installed.


2. Run the script:

    ```bash
    python scrape_projects.py
    ```

3. The script will navigate to the HPRERA Public Dashboard, scrape the required project details, and save them to `project_details.csv`.

## Project Structure

- `scrape_projects.py`: The main script that performs web scraping.
- `requirements.txt`: List of dependencies required to run the script.
- `project_details.csv`: The CSV file where the scraped data will be stored (generated after running the script).

## Script Details

The script performs the following steps:

1. Sets up the Chrome WebDriver using `webdriver_manager`.
2. Navigates to the HPRERA Public Dashboard and clicks on the 'Registered Projects' section.
3. Iterates through the first 6 projects, clicks on each to view details, and extracts the required fields.
4. Saves the extracted details to a CSV file named `project_details.csv`.

## Example Output

The `project_details.csv` file will have the following structure:

```csv
GSTIN No,PAN No,Name,Permanent Address
XX1234XXXX,ABCDE1234F,Project Name,1234 Permanent Address
...
