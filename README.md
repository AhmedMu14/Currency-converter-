# Real-Time Currency Converter
This is a simple Tkinter-based real-time currency converter application. It fetches the latest exchange rates from the ExchangeRate-API and converts an input amount from one currency to another.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

Install the required libraries using:
```sh
pip install requests python-dotenv
```

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
   ```

2. **Create a `.env` File**:
   - Create a `.env` file in the root directory of your project and add your ExchangeRate-API key:
     ```env
     API_KEY=your_actual_api_key_here
     ```

3. **Run the Application**:
   ```sh
   python currency_converter.py
   ```

## Usage

- Enter the amount you want to convert.
- Select the currency you are converting from.
- Select the currency you are converting to.
- Click the "Convert" button to see the converted amount.

## License

This project is licensed under the MIT License.
```

### Notes:
- Replace `https://github.com/yourusername/currency-converter.git` with your actual GitHub repository URL.
- Replace `your_actual_api_key_here` with your actual API key.
