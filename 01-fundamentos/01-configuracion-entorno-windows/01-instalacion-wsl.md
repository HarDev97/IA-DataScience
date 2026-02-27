## 🐧 Instalar WSL y Ubuntu en Windows

### 1. Abrir la terminal de Windows
Abre **PowerShell** o **CMD** y ejecuta:

```bash
wsl --install
```

### 2. Habilitar la plataforma de máquinas virtuales
Una vez instalado wsl ejecuta:

```bash
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
⚠️ **Advertencia: Activación manual del Subsistema de Windows para Linux**
>
> Si no se instala el Subsistema de Windows para Linux automáticamente:
>
> 1. Ve al menú **Inicio** de Windows.  
> 2. Busca **“Activar o desactivar las características de Windows”**.  
> 3. En la lista, asegúrate de marcar la opción:
>
>    - **Activar Subsistema de Windows para Linux**
>
> Pon la palomita (✔️) y confirma los cambios.


