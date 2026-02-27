## 🟢 Instalar Node.js y NPM en Ubuntu (WSL)

### 1. Abrir la terminal de Ubuntu
Una vez tengas WSL instalado, abre la terminal y selecciona **Ubuntu**.

Allí ejecutarás todos los siguientes comandos.

---

### 2. Instalar Node.js
Instala y revisa la versión.
```bash
sudo apt update
sudo apt install nodejs
node -v
```

### 3. Instalar npm (Manejador de paquetes)

Una vez instalado nodejs ejecuta:

```bash
sudo apt install npm
```

### 4. Actualizar la versión de nodejs
Esta actualización usa el gestor n, que requiere permisos globales.
Úsalo solo si deseas tener siempre la versión más reciente de Node.js

Una vez instalado nodejs ejecuta:

```bash
sudo npm install -g n
sudo n latest
```