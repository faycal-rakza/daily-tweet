# Daily Tweet

## Description

The main purpose of this project is to automate a tweet every day using the serverless technology of Google Cloud Platform (GCP) while minimizing costs. The project utilizes Google Cloud Scheduler to trigger a Google Cloud Function that tweets a random line from a text file. The Cloud Run Function starts a container, sends the tweet, and shuts down if no new text is received via an HTTP query.

This is a simple Python script designed to tweet a random line from a text file daily using Google Cloud Scheduler.

## Features

- Automates daily tweets
- Uses serverless technology to minimize costs
- Integrates with Google Cloud Platform services
  - Google Cloud Scheduler
  - Google Cloud Run Functions

## Requirements

- Python
- pip
- Google Cloud Platform account
- Twitter Developer account

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/faycal-rakza/daily-tweet.git
    cd daily-tweet
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    Create a `.env` file in the root directory and add your Twitter API credentials:
    ```env
    BEARER_TOKEN=your_bearer_token
    CONSUMER_KEY=your_consumer_key
    CONSUMER_SECRET=your_consumer_secret
    ACCESS_TOKEN=your_access_token
    ACCESS_TOKEN_SECRET=your_access_token_secret
    ```

## Usage

1. **Deploy the Cloud Function:**
    Follow the instructions in the `main.py` file to deploy the Cloud Function to GCP.

2. **Schedule the Cloud Function:**
    Use Google Cloud Scheduler to trigger the Cloud Function daily.

3. **Run the script locally:**
    ```sh
    python main.py
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.