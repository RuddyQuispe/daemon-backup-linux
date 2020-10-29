# Linux Daemons with Systemd

_Dos ejemplos basicos de daemons para la materia Sistemas Operativos 2 UAGRM-FICCT_
_1.- Daemon de Backup en un determinado tiempo._
_2.- Daemon de subir archivos automático a un servidor FTP._

## Comenzando 🚀

_A continuación, estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **la Descripción** para conocer como desplegar estos dos programitas.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el daemon y como ejecutarlas_

```
Systemd
Python3
Servidor FTP 
```

### Instalación 🔧

_1. Backup-service_
 * los script backup.sh y backup_const.sh en /usr/bin
 * El archivo backup_so2.service se debe alojar en /etc/systemd/system
 * crear la carpeta /mnt/backup donde se guardará los backup realizados
 * en el archivo backup_const.sh define la hora que el usuario guste
 * ejecutar el comando systemctl enable backup_so2.service
 * ejecutar el comando systemctl start backup_so2.service

_2. FTP-upload-service_

* Los scripts daemon_ftp.py y ip_addr_ftpsrvr.conf copiar en /usr/bin
* El archivo ftp_daemon_so2.service se debe alojar en /etc/systemd/system
* crear la carpeta /home/$WHOAMI/Documents/ftp_files
* en el archivo ip_addr_ftpsrvr.conf define la conexion al servidor FTP (IPADDR, USER, PASSWD)
* ejecutar el comando systemctl enable ftp_daemon_so2.service
* ejecutar el comando systemctl start ftp_daemon_so2.service

## Ejecutando las pruebas ⚙️

_Ya esta explicado alli arriba_

### Analice las pruebas end-to-end 🔩

_Comando: systemctl start backup-so2.service_
_Comando: systemctl start ftp-daemon-so2.service_

## Despliegue 📦

_Address: /etc/systemd/system_

## Construido con 🛠️

_herramientas que utiliza para crear tu proyecto_

* [Python3](https://www.python.org/download/releases/3.0/) - Lenguaje de programacion Python v3
* [Bash](https://www.gnu.org/software/bash/) - Lenguaje Linux Bash 
* [vsftpd](http://www.v-espino.com/~chema/smr2/practicas/p41.html) - Servicio de protocolo FTP

## Versionado 📌

Usamos [Git](http://git.org/) para el versionado de código fuente.

## Autores ✒️

_Agradecido con el de Arriba_

* **Quispe Mamani Ruddy Bryan** - *Equipo Scrum* - [Github](https://github.com/RuddyQuispe) [Bitbucket](https://bitbucket.org/ruddyq/workspace/projects/)

## Licencia 📄

Este proyecto está bajo la Licencia (Sin Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Agradecido con el de Arriba 📢
* Este proyecto tiene fines de aportar con la comunidad de software libre
* Este proyecto fue diseñado con muhco esfuerzo y dedicacion

---
⌨️ con ❤️ por el autor 😊