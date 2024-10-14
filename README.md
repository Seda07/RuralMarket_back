# 🌳 RuralMarket Back-end

Welcome to the **RuralMarket** backend repository 🌟

## 🌐 Table of Contents

1. [Project Description](#-project-description)
2. [Features](#-features)
3. [Technologies Used](#-technologies-used)
4. [Installation](#-installation)
5. [Usage](#-usage)
6. [Front-end Repository](#-front-end-repository)
7. [Development Team](#-development-team)
8. [License](#-license)

## 📖 Project Description

**RuralMarket** is an online platform that connects rural women entrepreneurs with consumers interested in quality products, promoting transparency in production and facilitating direct contact. It also fosters collaboration networks, improving service for both producers and buyers.

In **RuralMarket**, you can:

- Connect directly with the producers.
- Learn about production processes with full transparency.
- Be part of a community that fosters collaboration among entrepreneurs.

## Features

- 🔒 **User authentication and authorization**.
- 🗄️ **Database management** for products, services, and users.
- ☁️ **Integration with Cloudinary** for image management.
- 🧪 **Tests** with Pytest.

## 🛠 Technologies Used

- 🐍 **Python**: Version 3.12.0.
- 🎸 **Django**: Version 5.1.1.
- 🌐 **Django REST Framework**: Version 3.15.2.
- 🐘 **PostgreSQL**: Version 16.
- ☁️ **Cloudinary**: Version 1.41.0.
- 🧪 **Pytest**: Version 8.3.3.
- 🛢️ **Psycopg2**: Version 2.9.9.
- ✉️ **Mailtrap**: Version Email Testing.
- 🚀 **Postman**: Version 11.

## ⚙️ Installation

Follow these steps to install and run the project in your local environment:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Seda07/RuralMarket_back.git
   
 2. **Navigate to the project directory**

 ```bash
cd RuralMarket_back
 ```
3. **Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
4. **Install dependencies**

```bash
pip install -r requirements.txt
```
5. **Set up environment variables**

-Rename the .env.example file to .env and configure the necessary variables:

```bash
SECRET_KEY='your_secret_key'
DEBUG=True
DATABASE_URL='postgresql://user:password@localhost:5432/db_name'
CLOUDINARY_CLOUD_NAME='your_cloud_name'
CLOUDINARY_API_KEY='your_api_key'
CLOUDINARY_API_SECRET='your_api_secret'
```
6. **Run database migrations**

```bash
python manage.py migrate
```
## 🚀 Usage

5. **To start the application in development mode**
  ```bash
   python manage.py runserver
 ```

## 🧪 Test with Pytest
You can run unit tests with the following command:

 ```bash
pytest
 ```

## Front-end Repository

This project works alongside the RuralMarket front-end. For access to the code and more details about the front-end, visit the following link:


🔗 **RuralMarket Front-end Repository**

[https://github.com/Erieltxu/RuralMarket_front](https://github.com/Erieltxu/RuralMarket_front)

## 👥 Development Team

| Name               | Rol                   | Contact                     |
|----------------------|-----------------------|-------------------------------|
| Seda Gevorgian         | Scrum Manager | [GitHub](https://github.com/Seda07) |
| Belén Sanchez         | Product Owner | [GitHub](https://github.com/Belensanchez1989) |
| Carla Sanchez   | Back-end Developer | [GitHub](https://github.com/Carlassanchez24) |
| Gabriela Rosas        | Back-end Developer       | [GitHub](https://github.com/GabyRosas) |
| Leire Del Hoyo Aldecoa       | Front-end Developer     | [GitHub](https://github.com/Erieltxu)
| Evelyn Quevedo Garrido       | Front-end Developer | [GitHub](https://github.com/evymari)  


## Licence

**This project is licensed under Factoría F5.** 📄
