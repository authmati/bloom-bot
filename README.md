<p align="center">
  <img src="https://img.shields.io/badge/Desarrollado%20con-Python%203.10+-blue?logo=python&style=for-the-badge" alt="Python"> 
   <img src="https://img.shields.io/badge/ESTADO-EN%20DESARROLLO-ff69b4?style=for-the-badge" alt="Estado">
  <img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="Licencia">
</p>

# 🌸 Bloom - Discord Bot

**Bloom** es un bot de Discord en desarrollo, creado con el propósito de aprender y experimentar con nuevas funcionalidades. Aunque aún es un proyecto sencillo, está en constante evolución, agregando y modificando características a medida que avanzo en mi aprendizaje.

## 🛠️ Instalación

Para utilizar **Bloom**, necesitas tener Python instalado y las siguientes dependencias:

- `discord.py`
- `logging`
- `mcstatus`
- `googletrans`
- `python-dotenv`

### Pasos para la instalación:

1. Clona este repositorio o descarga el código.
2. Crea un entorno virtual (opcional, pero recomendado):

    ```bash
    python3 -m venv venv
    ```

3. Activa el entorno virtual:
    - **Windows**:

        ```bash
        .\venv\Scripts\activate
        ```

    - **macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

4. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

5. Crea un archivo `.env` en la raíz del proyecto y agrega tu token de Discord:

    ```plaintext
    DISCORD_TOKEN=tu_token_aqui
    ```

---

## 🎯 Comandos

Aquí tienes los comandos que **Bloom** soporta actualmente:

| Comando                        | Descripción                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `!prefix set <nuevo_prefijo>`  | Cambia el prefijo del bot. Si se deja vacío, se quita el prefijo personalizado. |
| `!ping`                        | Responde con el ping actual del bot para verificar la conexión.             |
| `!saludar`                     | El bot saluda a la persona que ejecuta el comando.                          |
| `!mcstatus`                    | Muestra los jugadores conectados a tu servidor de Minecraft (si está configurado). |
| `!user <usuario>`              | Muestra la información del usuario en formato embed.                        |
| `!serverinfo`                  | Muestra la información básica del servidor donde está el bot.               |
| `!reset`                       | Recarga los cogs del bot si se hace alguna modificación.                    |

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si tienes ideas, sugerencias o mejoras, no dudes en crear un **pull request**. Estaré encantado de revisarlo y colaborar contigo.

## 👤 Autor

Este proyecto es desarrollado y mantenido por **Mati**.  
¡Gracias por tu interés en **Bloom**! 🌸
