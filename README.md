# Carro_en_Micropython

Carro móvil con tracción diferencial controlado desde una **app Android** (hecha con Kodular) mediante **Bluetooth Clásico (SPP)**. El 
ESP32 recibe comandos de una sola letra (`F`, `B`, `L`, `R`, etc.) y también permite ajustar la velocidad mediante un número seguido de salto de línea.

## 🚀 Características

- Control de movimiento: adelante, atrás, giros, diagonales y detención.
- **Velocidad ajustable** desde la app (rango 100-255).
- Comunicación por **Bluetooth SPP** (módulo HC-05 o Bluetooth integrado del ESP32 en modo SPP con librerías externas).
- Código en **MicroPython** para ESP32.
- App Android creada con **Kodular** (interfaz sencilla con botones y slider de velocidad).
- **Archivo `.aia` incluido** para que puedas importar y modificar la app en Kodular.

## 🛠️ Tecnologías utilizadas

- **MicroPython** en ESP32
- **UART** (Bluetooth Serial) – protocolo SPP
- **PWM** para control de velocidad de motores
- **Kodular** (diseño de la app Android)

### 1. Hardware necesario

- ESP32 (cualquier modelo)
- Puente H (L298N o similar) para controlar 2 motores DC
- Módulo Bluetooth HC-05 (La version de Bluetooh clasico no esta disponible en MicroPython)
- Batería y chasis de robot

### 2. Conexiones (ajusta según tu setup)

| Componente | Pin ESP32 |
|------------|-----------|
| IN1        | GPIO 5    |
| IN2        | GPIO 6    |
| IN3        | GPIO 9    |
| IN4        | GPIO 10   |
| ENA (PWM)  | GPIO 3    |
| ENB (PWM)  | GPIO 11   |
| UART TX    | GPIO 17   |
| UART RX    | GPIO 16   |

*(Puedes cambiar los pines en el código según tu conveniencia)*

### 3. Cargar el firmware en el ESP32

- Conecta el ESP32 por USB.
- Copia el contenido de `esp32/main.py` a tu dispositivo (con Thonny, ampy o rshell).
- Asegúrate de que el módulo HC-05 esté correctamente conectado y pareado con tu teléfono.

### 4. App Android

- Abre el archivo `app/robot_control.aia` en Kodular.io
- Los comandos enviados por la app son:
  - `F` → Adelante
  - `B` → Retroceder
  - `L` → Girar izquierda
  - `R` → Girar derecha
  - `G` → Diagonal izquierda adelante
  - `I` → Diagonal derecha adelante
  - `H` → Diagonal izquierda atrás
  - `J` → Diagonal derecha atrás
  - `S` → Detener
  - **Número + salto de línea** → Cambia la velocidad (ej. `200\n`)

### 5. Prueba

- Enciende el ESP32.
- Conéctate desde la app al dispositivo Bluetooth (nombre que aparezca, generalmente `HC-05`).
- Prueba los botones y el slider de velocidad.

## ⚠️ Notas importantes

- **Bluetooth Clásico vs BLE**: MicroPython **no soporta Bluetooth Clásico nativamente** en el ESP32. Por eso, este proyecto utiliza un **módulo externo HC-05** conectado por UART. Si deseas usar el Bluetooth nativo del ESP32, tendrías que cambiar a **Arduino** (con la librería `BluetoothSerial`) o implementar BLE (que sí está soportado en MicroPython).
- El código está pensado para **Bluetooth SPP** (Serial Port Profile), el estándar para comunicación serie inalámbrica.
- La velocidad se escala automáticamente de 0-255 a 0-1023 para el PWM.
- Si usas un módulo HC-05 externo, conecta sus pines TX/RX a los GPIO 16 y 17 (o los que definas en el código).

## 🔮 Mejoras futuras

- Implementar **BLE** para usar el Bluetooth nativo del ESP32 y eliminar el módulo HC-05.
- Añadir sensores de distancia para evitar obstáculos.

## 🤝 Contribuciones

Si encuentras algún error o quieres mejorar el proyecto, abre un issue o pull request.

## 📄 Licencia

MIT
