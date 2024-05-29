# Soil Analysis Flask App

This Flask application determines the soil texture and electrical conductivity based on geographical coordinates provided by the user. By inputting the latitude and longitude of a location, the app retrieves soil data from a predefined database or external API and returns detailed information about the soil's texture and conductivity.

## Features

- Input geographical coordinates (latitude and longitude).
- Retrieve soil texture information.
- Retrieve soil electrical conductivity information.
- User-friendly interface for input and display of results.
- Information of Soil of Different regions of Pakistan is there.
- Details about soil texture and salinity are there

## Requirements

Make sure you have Python installed on your system. The required Python packages are listed in `requirements.txt`. To install the necessary packages, run:

```bash
pip install -r requirements.txt
```

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ikramali585/web-portal.git
    cd web-portal
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a `.env` file in the root directory of the project.
    - Add necessary environment variables (if any) in the `.env` file.

4. **Run the Flask application**:
    ```bash
    python main.py
    ```

## Usage

1. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

2. **Input Coordinates**:
   Enter the latitude and longitude of the location for which you want to determine the soil texture and electrical conductivity.

3. **View Results**:
   Submit the coordinates to view the soil texture and electrical conductivity information.


### GET /soil-data

Retrieve soil texture and electrical conductivity based on geographical coordinates.


## Contributing

We welcome contributions to enhance the functionality and usability of this application. If you would like to contribute, please fork the repository, create a feature branch, and submit a pull request.


## Contact

For any questions or inquiries, please contact (mailto:ikramaliorakzai@gmail.com).

---

Happy soil analyzing!
