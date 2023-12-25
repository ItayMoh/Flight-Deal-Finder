# Flight Deal Finder
Small project for finding flight deals.

Flight Deal Finder is a Python project that helps users find the best flight deals by comparing prices, sending notifications through SMS, and updating information in a Google Sheet.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

### Services Used

Flight Deal Finder relies on the following services for managing data, sending notifications, and searching for flight details:

- [Sheety](https://sheety.co/): Used for communication with the Google Sheet to retrieve and update flight data.

- [Twilio](https://www.twilio.com/): Utilized for sending SMS notifications about flight deals.

- [Tequila Kiwi](https://tequila.kiwi.com/): Integrated for searching flight details, including airport IATA codes and flight prices.


## Overview

Flight Deal Finder is designed to automate the process of finding and notifying users about the best flight deals. The project uses three main components: `DataManager` for managing data in a Google Sheet, `FlightSearch` for searching flight details using the Kiwi API, and `NotificationManager` for sending notifications via Twilio.

## Project Structure

The project is structured into several files, each serving a specific purpose:

- `data_manager.py`: Manages communication with the Google Sheet to retrieve and update flight data.
- `flight_search.py`: Searches for flight details using the Kiwi API, including airport IATA codes and flight prices.
- `notification_manager.py`: Sends notifications about flight deals using Twilio.
- `flight_data.py`: Defines the `FlightData` class to structure flight details.
- `main_script.py`: The main entry point that uses the above components to find and notify about flight deals.

## Prerequisites

Before using Flight Deal Finder, ensure you have the necessary environment variables set up:

- For Google Sheet:
  - `GOOGLE_SHEET_PRICE_COMPARE_URL`: URL of the Google Sheet for price comparison.
  - `SHEETY_AUTHORIZATION`: Authorization token for Sheety API.
    
**Note**: The Google Sheet should follow the following format:

| City          | IATA Code | Lowest Price |
| ------------- | --------- | ------------ |
| Paris         | PAR       | 160          |
| Berlin        | BER       | 42           |
| Tokyo         | TYO       | 485          |
| Sydney        | SYD       | 551          |
| Istanbul      | IST       | 95           |
| Kuala Lumpur  | KUL       | 414          |
| New York      | NYC       | 240          |
| San Francisco | SFO       | 260          |
| Cape Town     | low       | 378          |

Ensure that the columns are labeled "City," "IATA Code," and "Lowest Price" respectively.
- For Twilio:
  - `ACCOUNT_SID`: Twilio account SID.
  - `AUTH_TOKEN`: Twilio authentication token.
  - `TWILIO_SENT_NUMBER`: Twilio phone number used to send messages.
  - `YOUR_NUMBER`: Your phone number to receive messages.
- For Kiwi API:
  - `KIWI_API_KEY`: API key for the Kiwi API.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flight-deal-finder.git
   cd flight-deal-finder
2.Configure the Google Sheet:
- Open the Google Sheet used for price comparison.
- Ensure that it follows the required format

3.Set up the necessary environment variables:
- For Google Sheet:
  - `GOOGLE_SHEET_PRICE_COMPARE_URL`: URL of the Google Sheet for price comparison.
  - `SHEETY_AUTHORIZATION`: Authorization token for Sheety API.
- For Twilio:
  - `ACCOUNT_SID`: Twilio account SID.
  - `AUTH_TOKEN`: Twilio authentication token.
  - `TWILIO_SENT_NUMBER`: Twilio phone number used to send messages.
  - `YOUR_NUMBER`: Your phone number to receive messages.
- For Kiwi API:
  - `KIWI_API_KEY`: API key for the Kiwi API.

 **Note**: Before running the script, ensure to replace the `ORIGIN_COUNTRY_IATA` constant in the main_script.py file with your actual origin IATA city code. This code represents the country of origin for the flight searches.


## Configuration
- `data_manager.py`: Configure Google Sheet URLs and headers.
- `notification_manager.py`: Configure Twilio authentication and
- `flight_search.py`: Configure the Kiwi API endpoint and headers.

  
