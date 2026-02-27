## ⚫ Instalación y Configuración de Git en Ubuntu (WSL)

### 1. Instalar Git

```bash
sudo apt-get install git-all
git version
```
### 2. Configurar SSH
Generar una nueva llave SSH con algoritmo moderno ed25519:

⚠️ **Ingresa el correo registrado en github**

```bash
ssh-keygen -t ed25519 -C "correo@dominio.com"
```

### 3. Iniciar el agente SSH
eval "$(ssh-agent -s)"
```bash
eval "$(ssh-agent -s)"
```

### 4. 🗝️ Agregar la llave privada al agente

```bash
ssh-add ~/.ssh/id_ed25519
```

### 5. Obtener la llave pública para agregarla a GitHub

```bash
cat ~/.ssh/id_ed25519.pub
```
Copiar toda cadena obtenida (la llave) y luego agregarla en github, para ello:

> 1. Ingresa a Github
> 2. Ir a "Settings"
> 3. Ir a SSH and GPG keys
> 4. En la sección de SSH dar al botón New SSH Key
> 5. En la sección de SSH dar al botón New SSH Key, agrega un nombre, pega la llave y da click en Add SSH key.

### 6. Configurar parámetros globales de Git.
En la terminal, ingresa:

⚠️ **Ingresa el usuario y correo registrado en github**

```bash
git config --global user.name "nombre-usuario"
git config --global user.email "correo@dominio.com"
```




