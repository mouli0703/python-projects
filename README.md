---

# Electricity Bill Calculator

## Overview

This Python script provides a way to calculate electricity bills based on units consumed. It includes functionality to view historical bills, update personal information, and manage user sessions.

## Features

- **Electricity Bill Calculation**: Calculate the bill based on units consumed with a tiered rate system.
- **History Viewing**: View the history of electricity bills.
- **User Management**: Change user information, update passwords, and manage sessions.

## How to Use

### 1. **Electricity Bill Calculation**

The bill calculation is based on a tiered system where different unit ranges have different rates:

- **0 - 100 units**: No charge.
- **101 - 200 units**: 2 per unit.
- **201 - 300 units**: 3 per unit.
- **301 - 400 units**: 4 per unit.
- **Above 400 units**: 5 per unit.

Additionally, a surcharge is applied based on the total units consumed.

#### Example Usage

1. **Run the EB Function:**

    ```python
    EB('vicky')
    ```

2. **Input the year and month when prompted.**
3. **Input the total units consumed.**
4. **The program will display the total bill amount and update the history.**

### 2. **View History**

You can view the complete history of bills, bills for a specific year, or bills for a particular month within a year.

#### Example Usage

1. **Run the `History` Function:**

    ```python
    History('vicky')
    ```

2. **Select the desired option to view history:**
   - Complete history
   - Particular year
   - Particular month in a particular year

### 3. **Change Information**

Users can update their personal information including name, mobile number, email, and password.

#### Example Usage

1. **Run the `change_info` Function:**

    ```python
    change_info('vicky')
    ```

2. **Select the information to change:**
   - Name
   - Mobile number
   - Email
   - Password

### 4. **Main Menu Options**

The `options` function provides a menu for users to access different features.

#### Example Usage

1. **Run the `options` Function:**

    ```python
    options('vicky')
    ```

2. **Select the desired option:**
   - Calculate EB Bill
   - View History
   - View Personal Info
   - Change Info
   - Logout

## Code Breakdown

### `EB` Function

The `EB` function calculates the electricity bill based on user input for the year, month, and units consumed. It uses the following tiered rates:

- **0 - 100 units**: Free
- **101 - 200 units**: 2 per unit
- **201 - 300 units**: 3 per unit
- **301 - 400 units**: 4 per unit
- **Above 400 units**: 5 per unit

A surcharge is added based on the total units.

**Sample Bill Calculation:**

```python
def EB(name):
    year = int(input('Enter year: '))
    months = {i: j for i, j in zip(range(1, 13), ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])}
    for i, j in months.items():
        print(i, '=', j)
    month = months[int(input('Enter the month: '))]
    units = float(input('Enter total units consumed: '))

    if units <= 100:
        amt = 0
        sur = 0
    elif 100 < units <= 200:
        amt = 0 + 200 + (units - 100) * 3
        sur = 10
    elif 200 < units <= 300:
        amt = 0 + 200 + (units - 200) * 3
        sur = 20
    elif 300 < units <= 400:
        amt = 0 + 200 + 300 + (units - 300) * 4
        sur = 30
    else:
        amt = 0 + 200 + 300 + 400 + (units - 400) * 5
        sur = 50

    print(f'Hello user, the total bill amount for using {units} units is Rs. {amt + sur}')

    if year in data[name]['EB_bills']:
        data[name]['EB_bills'][year][month] = {}
    else:
        data[name]['EB_bills'][year] = {}
        data[name]['EB_bills'][year][month] = {}

    data[name]['EB_bills'][year][month]['units'] = units
    data[name]['EB_bills'][year][month]['bill'] = amt + sur
```

### `History` Function

The `History` function allows users to view their billing history. It can display the complete history, bills for a particular year, or bills for a specific month within a year.

### `view` Function

The `view` function displays the personal information of the user and provides options to change the information, go back to options, or logout.

### `change_info` Function

The `change_info` function provides options to change the user's name, mobile number, email, and password. It ensures that passwords match before updating.

### `options` Function

The `options` function presents a menu for the user to access the electricity bill calculator, view history, view personal information, change information, or logout.

## Data Structure

The data is stored in a nested dictionary format:

```python
data = {
    'username': {
        'password': 'password123',
        'PI': {
            'name': 'User Name',
            'mobile': '1234567890',
            'email': 'user@example.com'
        },
        'EB_bills': {
            year: {
                month: {
                    'units': units_consumed,
                    'bill': bill_amount
                }
            }
        }
    }
}
```

## Error Handling

- **Invalid Selections**: Users are given up to 3 chances to select valid options before the main menu is restarted.
- **Incorrect Passwords**: Users have 3 attempts to enter the correct password before being redirected to the main menu.

## Conclusion

This script provides a simple yet effective way to manage electricity bill calculations and user information. Ensure the data dictionary is correctly defined before using the functions, and follow the prompts for seamless interaction.

---

