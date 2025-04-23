# House Estimator

A Django-based web application for estimating construction material requirements and costs for house projects.

## Features

- **Room Management**
  - Create and manage rooms with dimensions
  - Support for different room types (bedroom, bathroom, kitchen, etc.)
  - Room quantity tracking

- **Tile Calculations**
  - Define tile specifications (dimensions, pieces per box, price)
  - Calculate required boxes and pieces for rooms
  - Include waste percentage in calculations
  - Automatic cost estimation

- **Plywood Calculations**
  - Define plywood sheet specifications
  - Calculate required sheets for rooms
  - Include waste percentage in calculations
  - Automatic cost estimation

- **Electrical Component Management**
  - Define electrical components with specifications
  - Track components by type (wires, switches, outlets, etc.)
  - Set default quantities per room type
  - Automatic cost calculations

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd house_estimator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the admin interface at `http://localhost:8000/admin/` to manage:
   - Rooms
   - Tiles
   - Plywood sheets
   - Electrical components

2. Use the web interface at `http://localhost:8000/` to:
   - View and manage rooms
   - Calculate material requirements
   - Estimate costs
   - Track electrical components

## Project Structure

```
house_estimator/
├── house_estimator/          # Project settings and configuration
├── materiais/                # Main application
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Form definitions
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
└── templates/               # Base templates
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers. 