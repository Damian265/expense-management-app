# Usa una imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY package.json .

# Instala las dependencias
RUN npm install

# Copia el código de la aplicación
COPY server.js .

# Expone el puerto en el que correrá el servicio
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["node", "server.js"]
