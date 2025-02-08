#!/bin/bash

# Definir la nueva carpeta del proyecto
PROJECT_PATH="/var/www/IST105-Assignment5"

# Cambiar permisos y propietario
sudo chown -R apache:apache "$PROJECT_PATH"  # Para Amazon Linux / CentOS
sudo chown -R www-data:www-data "$PROJECT_PATH"  # Para Ubuntu / Debian
sudo chmod -R 755 "$PROJECT_PATH"

# Modificar configuración de Apache
APACHE_CONF="/etc/httpd/conf/httpd.conf"  # Para Amazon Linux / CentOS
fi

# Reemplazar la configuración de DocumentRoot
sudo sed -i "s|DocumentRoot .*|DocumentRoot $PROJECT_PATH|g" "$APACHE_CONF"

# Agregar directiva para permitir acceso
sudo sed -i "/<Directory \\/var\\/www\\//,/<\\/Directory>/d" "$APACHE_CONF"
echo -e "<Directory $PROJECT_PATH>\n    AllowOverride All\n    Require all granted\n</Directory>" | sudo tee -a "$APACHE_CONF"

sudo systemctl restart httpd 2>/dev/null || sudo systemctl restart apache2