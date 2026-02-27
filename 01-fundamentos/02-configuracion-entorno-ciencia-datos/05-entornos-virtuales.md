## 🔷 Ambientes virtuales

`Conda` es una herramienta esencial para la gestión de paquetes y entornos, que facilita el trabajo con diversos lenguajes de programación como Python y R.

## ¿Cómo instalar Conda?

Instalar Conda se puede hacer de dos maneras principales: a través de MiniConda o Anaconda.

- MiniConda: Ofrece una instalación mínima, proveyendo solo lo necesario para que Conda funcione, incluyendo Python.

- Anaconda: Es una instalación más completa que incluye MiniConda y una multitud de paquetes y herramientas útiles para la ciencia de datos.

---

En la terminal de ubuntu ejecuta el siguiente comando que instalará y abrirá VSC:

### 1. Instalar Anaconda

- Ingresa a la página oficial de [Ananconda](https://www.anaconda.com/download/success)
- Dirigete a descargas, sección linux y copia la url para descargar. Una vez copiada la url te aconsejamos que pegues esta liga en el buscador verifica que contenga la siguiente estructura, a la actualización de esta documentación es: https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh

\*Puede que esta liga este desactualizada por lo que te recomendas ingresar y validar

- Una vez copiada la liga ingresa a tu terminal y ejecuta:

Actualiza paquetes en tu versión de linux

```bash
sudo apt update
```

Descarga el instalador, asegurate de estar en la carpeta donde quieres que se descargue este instaldor.

```bash
wget -O anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh
```

Verifica que se haya descagardo el instalador

```bash
ls -al
```

Ejecuta el instalador

```bash
bash anaconda.sh
```

Una vez ejecutes el instalador sigue las instrucciones en la terminal.

**Recomendación**: Ejecuta la inicialización de anaconda con una vez te pregunte la termina digita "yes"

Luego de instalar anaconda abre una nueva. Podrás observar en esa nueva terminal indicación (base) esto confirmará que haz instalado anaconda con exito

Si deseas conocer mayor detalle ejecuta, podrás ver el ambiente en el que estás (base, etc), la ubicación de anaconda entre otros detalles.

```bash
conda info
```

### 2. Ejecutar Jupyer NoteBook

Ejecuta el comando

```bash
jupyter-notebook
```

En wsl se mostrará diferentes enlaces, copia y pega el localhost en tu navegador para abrir un jupyer notebook, escoge nuevo notebook usando python http://localhost:8888/.....

Para salir ejecuta `CTRL + C`

### 3. Notebook en VSC

Abre visual estudio code, asegurate de estar en la carpeta de tu proyecto y ejecuta

```bash
code .
```

Luego crea un archivo con la extensión **.ipynb** ejemplo: `notebook.ipynb`. Ingresa al archivo, en la parte superior derecha verás la acción **Select Kernel** da click allí y luego selecciona el entorno base(Python #versión)

**Recomendación**: Si no ves el kernel solo es cuestión de cerrar tu visual y volver abrirlo, esto hará que refresque detecte el nuevo entorno
