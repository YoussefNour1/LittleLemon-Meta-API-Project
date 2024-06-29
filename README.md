# Little Lemon Meta API Project

This repository contains the final project for the Meta Backend Django REST Framework course on Coursera. 
It demonstrates the implementation of a RESTful API using Django and Django REST Framework. This project is part of the Meta Backend Developer course on Coursera. 
It showcases a comprehensive implementation of a RESTful API for a hypothetical restaurant using Django and Django REST Framework. The API allows for managing users, menu items, categories, orders, and more, with a robust permission system to handle different user roles such as managers, customers, and delivery crew. 

Dive in to explore the full functionality and contribute to enhance it further!


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Permissions](#permissions)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YoussefNour1/LittleLemon-Meta-API-Project.git
    cd LittleLemon-Meta-API-Project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

Once the development server is running, you can interact with the API through the following base URL:

```
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

- **Register**: `POST /auth/register/`
- **Login**: `POST /auth/login/`
- **Logout**: `POST /auth/logout/`

### Users and Roles

- **Manager Users**: 
  - `GET /api/manager-users/`: List all manager users.
  - `POST /api/manager-users/`: Add a user to the manager group.
  - `DELETE /api/manager-users/{id}/`: Remove a user from the manager group.
- **Delivery Crew Users**: 
  - `GET /api/delivery-crew-users/`: List all delivery crew users.
  - `POST /api/delivery-crew-users/`: Add a user to the delivery crew group.
  - `DELETE /api/delivery-crew-users/{id}/`: Remove a user from the delivery crew group.

### Cart

- **Cart**: 
  - `GET /api/cart/`: List all cart items for the authenticated user.
  - `POST /api/cart/`: Add an item to the cart.
  - `DELETE /api/cart/{id}/`: Remove an item from the cart.

### Category

- **Categories**: 
  - `GET /api/categories/`: List all categories.
  - `POST /api/categories/`: Create a new category (Manager/Admin only).
  - `GET /api/categories/{id}/`: Retrieve a category by ID.
  - `PUT /api/categories/{id}/`: Update a category by ID (Manager/Admin only).
  - `DELETE /api/categories/{id}/`: Delete a category by ID (Manager/Admin only).

### Menu Items

- **Menu Items**: 
  - `GET /api/menu-items/`: List all menu items with filtering and ordering options.
  - `POST /api/menu-items/`: Create a new menu item (Manager only).
- **Single Menu Item**: 
  - `GET /api/menu-items/{id}/`: Retrieve a menu item by ID.
  - `PUT /api/menu-items/{id}/`: Update a menu item by ID (Manager/Admin only).
  - `DELETE /api/menu-items/{id}/`: Delete a menu item by ID (Manager/Admin only).

### Orders

- **Orders**: 
  - `GET /api/orders/`: List all orders for the authenticated user (Customer) or all orders (Manager/Delivery).
  - `POST /api/orders/`: Create a new order from the cart items of the authenticated user (Customer only).
- **Single Order**: 
  - `GET /api/orders/{id}/`: Retrieve an order by ID.
  - `PATCH /api/orders/{id}/`: Update order status (Delivery/Manager).
  - `PUT /api/orders/{id}/`: Update an order by ID (Manager only).
  - `DELETE /api/orders/{id}/`: Delete an order by ID (Manager only).

## Permissions

- **IsManagerUser**: Only manager users can access.
- **IsCustomerUser**: Only customer users can access.
- **IsDeliveryUser**: Only delivery crew users can access.
- **IsManagerOrDeliveryUser**: Only manager or delivery crew users can access.
- **IsManagerOrDeliveryOrCustomerUser**: Manager, delivery crew, or customer users can access.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

This `README.md` covers installation, usage, API endpoints, permissions, contributing, and licensing. Adjust any specific details according to your project's actual structure and requirements.
