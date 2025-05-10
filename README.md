# Cosmic Inventory Portal

A futuristic inventory management system with a space-themed UI that provides a seamless and immersive experience for managing inventory items.

## Tech Stack

### Backend
- **Flask**: Python web framework for building the RESTful API
- **MySQL**: Relational database (using the 'stocks' database)
- **PyMySQL**: MySQL connector for Python without compilation dependencies
- **Python dotenv**: For managing environment variables

### Frontend
- **HTML5/CSS3**: Modern markup and styling with advanced CSS features
- **JavaScript (ES6+)**: Client-side scripting with modern JavaScript features
- **Bootstrap 5**: Responsive UI framework for layout and components
- **Animate.css**: Library for smooth animations and transitions
- **Google Fonts**: Custom typography with Orbitron and Exo 2 fonts
- **Bootstrap Icons**: Comprehensive icon library

## Features

### Futuristic User Interface
- **Space-Themed Design**: Dark cosmic background with star-like patterns and orbital decorations
- **Glassmorphism**: Translucent card elements with backdrop blur for a modern, futuristic feel
- **Dynamic Animations**: Smooth transitions, floating elements, and micro-interactions
- **Color Scheme**: Vibrant neon accents (purple, cyan, pink) against deep space background
- **Custom Typography**: Sci-fi inspired fonts with Orbitron for headings and Exo 2 for body text

### Enhanced User Experience
- **Real-time Feedback**: Visual and (simulated) audio feedback for all user actions
- **Animated Notifications**: Sleek toast notifications for operation status
- **Smart Inventory Indicators**: Color-coded badges for stock levels
- **Staggered Loading**: Progressive item loading with delay for visual appeal
- **Custom Modal Dialogs**: Animated confirmation dialogs for critical actions
- **Responsive Layout**: Fully adaptive design for all device sizes

### Core Functionality
- **Complete CRUD Operations**: Create, read, update, and delete inventory items
- **Form Validation**: Client-side validation with visual feedback
- **API Status Monitoring**: Real-time connection status indicator
- **Empty State Handling**: Intuitive guidance when inventory is empty

## Setup Instructions

1. **Install dependencies**:
   ```
   python3 -m pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   Edit the `.env` file with your MySQL database credentials.

3. **Run the application**:
   ```
   python3 main.py
   ```

## API Endpoints

### Health Check
- `GET /api/health` - Check if the API is running

### Items
- `GET /api/items` - Get all items
- `GET /api/items/<id>` - Get a specific item
- `POST /api/items` - Create a new item
- `PUT /api/items/<id>` - Update an existing item
- `DELETE /api/items/<id>` - Delete an item

## Request/Response Examples

### Create Item (POST /api/items)
Request:
```json
{
  "name": "Sample Item",
  "description": "This is a sample item",
  "price": 19.99,
  "quantity": 10
}
```

Response:
```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item",
  "price": 19.99,
  "quantity": 10
}
```

![alt text](image.png)