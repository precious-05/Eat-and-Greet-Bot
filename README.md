
# Eat and Greet - Instagram DM Automation Bot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![Meta Graph API](https://img.shields.io/badge/Meta%20Graph%20API-v18.0-orange)](https://developers.facebook.com/docs/graph-api)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-red)](https://www.python.org/dev/peps/pep-0008/)
[![Status](https://img.shields.io/badge/status-production-brightgreen)]()

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Response Logic](#response-logic)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Submission Requirements](#submission-requirements)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

## Project Overview

Eat and Greet is an intelligent Instagram DM automation bot built for a premium restaurant. The bot automatically responds to customer inquiries about menu, pricing, delivery, reservations, opening hours, payments, and special deals. It runs on a Flask server, receives messages via Meta webhooks, and sends replies through the Instagram Graph API.

This project was developed as an AI automation internship task at CodeCelix.

## Features

- Automated reply to customer DMs on Instagram
- Keyword-based intent recognition
- Support for multiple inquiry types:
  - Menu and food items
  - Pricing information
  - Delivery zones, timeframes, and charges
  - Table reservations
  - Opening hours
  - Payment methods (JazzCash, EasyPaisa, COD, Cards)
  - Special deals and offers
  - Order tracking
- Webhook integration with Meta Graph API v18.0
- Secure token management using environment variables
- Local testing support via ngrok

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Backend programming language |
| Flask | 2.3.3 | Web server framework |
| Requests | 2.31.0 | HTTP API calls to Meta Graph API |
| python-dotenv | 1.0.0 | Environment variable management |
| Meta Graph API | v18.0 | Instagram messaging integration |
| ngrok | Latest | Local tunnel for webhook testing |

## Architecture

The bot follows a simple webhook-based architecture:

1. Customer sends a Direct Message to the Instagram Business account
2. Meta forwards the message to the Flask server via webhook (POST request)
3. Flask server processes the message and extracts text and sender ID
4. Response logic generates appropriate reply based on keywords
5. Server sends reply back through Meta Graph API
6. Customer receives automated response

## Prerequisites

Before running this bot, ensure you have the following:

- Python 3.8 or later installed
- Facebook Developer Account (free at developers.facebook.com)
- Instagram Business or Creator Account (personal accounts do not work)
- Facebook Page connected to Instagram account
- ngrok account (free tier) for local testing

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Eat-and-Greet-Bot.git
cd Eat-and-Greet-Bot
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
ACCESS_TOKEN=your_page_access_token_here
VERIFY_TOKEN=your_verify_token
PORT=5000
```

## Configuration

### Meta App Setup

1. Go to developers.facebook.com and create a new Business app named "Eat and Greet 2"
2. Add Instagram Graph API product
3. Add Messenger product
4. Connect your Instagram Business account
5. Generate Page Access Token with following permissions:
   - pages_manage_metadata
   - pages_messaging
   - instagram_basic
   - instagram_manage_messages
   - pages_read_engagement
6. Copy the token to `.env` file

### Webhook Configuration

1. Install and authenticate ngrok
2. Run ngrok on port 5000:
```bash
ngrok http 5000
```
3. Copy the ngrok URL (e.g., https://abc123.ngrok-free.app)
4. In Meta Dashboard, go to Messenger -> Webhooks
5. Add Callback URL: `https://your-ngrok-url.ngrok-free.app/webhook`
6. Set Verify Token: `greet123`
7. Subscribe to `messages` event

### Page Subscription

1. Go to Instagram Graph API -> Instagram Messaging
2. Click "Add or Remove Pages"
3. Select your Facebook Page
4. Generate token with required permissions
5. Click "Edit Subscriptions" and subscribe to `messages`

## Running the Bot

### Start Flask Server

```bash
python app.py
```

Expected output:
```
Eat and Greet Instagram Bot is Running!
Running on http://127.0.0.1:5000
```

### Start ngrok (in separate terminal)

```bash
ngrok http 5000
```

### Keep Both Terminals Running

The bot requires both Flask and ngrok to run simultaneously.

## Testing

### Test Scenarios

| Message to Send | Expected Response Contains |
|----------------|---------------------------|
| Hi | Welcome message with help options |
| menu | Menu categories and prices |
| price | Price ranges for all categories |
| delivery to Lahore | Delivery time and charges |
| book a table | Reservation instructions |
| timings | Daily opening hours |
| JazzCash | Payment confirmation |
| deal | Special offers information |
| track order | Order ID request |

### Test from Personal Account

1. Open Instagram on your phone
2. Switch to your personal Instagram account (not the business account)
3. Send a DM to your Eat and Greet business account
4. Wait for automated reply (should receive within 2-3 seconds)

## Project Structure

```
Eat-and-Greet-Bot/
│
├── app.py                 # Main Flask server, webhook handler
├── responses.py           # Response logic and keyword matching
├── requirements.txt       # Python dependencies
├── .env                   # Secret tokens (not committed)
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## API Endpoints

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/` | GET | Health check - returns "Eat and Greet Instagram Bot is Running" |
| `/webhook` | GET | Meta webhook verification |
| `/webhook` | POST | Receives incoming messages from Instagram |

## Response Logic

The `responses.py` file contains keyword-based intent recognition:

- `hi, hello, hey, salam` -> Welcome message
- `menu, food, dish` -> Full menu with categories and prices
- `price, cost, rate` -> Price ranges for all categories
- `delivery, deliver` -> Delivery info, timeframes, charges
- `book, reserve, table` -> Reservation process
- `open, close, time` -> Operating hours
- `pay, jazzcash, cod` -> Accepted payment methods
- `deal, offer, discount` -> Current special deals
- `order, track` -> Order tracking instructions

## Deployment

For production deployment (24/7 operation), deploy to free hosting platforms:

### Option 1: Render
1. Push code to GitHub
2. Create new Web Service on render.com
3. Connect GitHub repository
4. Set environment variables
5. Deploy

### Option 2: Railway
1. Push code to GitHub
2. Create new project on railway.app
3. Connect GitHub repository
4. Add environment variables
5. Deploy

## Troubleshooting

### Issue 1: Webhook verification fails
- Ensure ngrok URL includes `/webhook` at the end
- Verify Verify Token matches `.env` file
- Check Flask server is running before ngrok

### Issue 2: No reply to DMs
- Confirm `messages` event is subscribed in webhook settings
- Verify Page Access Token has correct permissions
- Check ngrok URL is still active (free tier URL changes on restart)
- Ensure Instagram account is Business type, not Personal

### Issue 3: "Invalid Scopes" error
- Generate new Page Access Token with proper permissions
- Required scopes: `pages_messaging`, `instagram_manage_messages`, `pages_manage_metadata`

### Issue 4: Token expired
- Tokens expire after approximately 60 days
- Regenerate token in Meta Dashboard and update `.env`

## Submission Requirements

For task submission, ensure the following:

1. Code pushed to public GitHub repository
2. `.env` file included in `.gitignore` (not visible in repo)
3. Screen recording showing complete DM flow:
   - Send message from personal account
   - Receive automated reply from bot
4. Repository contains:
   - `app.py`
   - `responses.py`
   - `requirements.txt`
   - `.gitignore`
   - `README.md`

## Future Improvements

- Integrate Groq API for AI-powered responses using LLaMA 3 model
- Add database support for storing conversation history
- Implement multi-language support (Urdu/English)
- Add analytics dashboard for message tracking
- Support for media attachments (images, videos)
- Implement conversation context memory

## Acknowledgments

- Meta Graph API Documentation
- Flask Framework Documentation
- ngrok Tunneling Service
- CodeCelix Internship Program

## Author

**Alina Liaquat**

- Internship: CodeCelix - AI Intern
- Date: 12 June 2026

---

## License

This project is for educational purposes as part of internship requirements.



---

