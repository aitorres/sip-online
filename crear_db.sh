#!/bin/bash
echo "Se creará la base de datos para SIP Online"

printf "A continuación, ingrese su contraseña de superusuario (sudo):\n"
sudo echo "hola" >> /dev/null

echo "Se instalarán a continuación las dependencias de bases de datos requeridas"
sudo apt-get install -y postgresql python-psycopg2

echo "A continuación, se le solicitará dos veces la contraseña de la base de datos."
printf "Cuando se solicite, ingrese como la contraseña:\t\ts1p0nl1ne!\n"
sudo -u postgres dropuser siponline >> /dev/null
sudo -u postgres createuser -PE -s siponline
sudo -u postgres createdb -O siponline -E UTF8 siponline_db

echo "Base de datos creada. Ahora, procede a realizar las migraciones correspondientes."