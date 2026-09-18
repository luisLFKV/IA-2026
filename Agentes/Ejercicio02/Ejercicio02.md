# Ejercicio 2 — Descripción PEAS de agentes inteligentes

### 1. Asistente virtual de voz

- **Performance:** entender bien al usuario, responder rápido y cumplir correctamente las tareas.
- **Environment:** usuarios, dispositivos conectados, aplicaciones, Internet y ruido del ambiente. Es parcialmente observable, estocástico, secuencial y dinámico.
- **Actuators:** responder por voz, mostrar información, reproducir música, enviar mensajes y controlar dispositivos.
- **Sensors:** micrófono, comandos de voz, historial del usuario y datos de servicios en Internet.

El entorno es parcialmente observable porque el asistente no conoce todo lo que pasa a su alrededor. También es estocástico porque puede interpretar de distintas formas una misma frase.

### 2. Robot aspirador doméstico

- **Performance:** limpiar la mayor superficie posible, gastar poca batería y evitar choques.
- **Environment:** habitaciones, muebles, paredes, personas, mascotas y objetos. Es parcialmente observable, estocástico, secuencial y dinámico.
- **Actuators:** ruedas, aspiradora, cepillos y sistema de dirección.
- **Sensors:** sensores de proximidad, choque, desnivel, suciedad y batería.

El robot no puede ver toda la casa al mismo tiempo. Además, objetos o personas pueden cambiar de lugar mientras limpia.

### 3. Sistema de recomendación de streaming

- **Performance:** ofrecer contenido que le interese al usuario y aumentar la satisfacción y tiempo de uso.
- **Environment:** usuarios, perfiles, catálogo, contenido nuevo y tendencias. Es parcialmente observable, estocástico, secuencial y dinámico.
- **Actuators:** mostrar recomendaciones, ordenar contenido y enviar sugerencias.
- **Sensors:** historial de reproducción, búsquedas, clics, favoritos y calificaciones.

Es parcialmente observable porque el sistema no conoce exactamente los gustos del usuario. Estos gustos también pueden cambiar con el tiempo.

### 4. Vehículo autónomo en ciudad

- **Performance:** llegar al destino de forma segura, respetar las reglas y reducir el tiempo de viaje.
- **Environment:** calles, vehículos, peatones, semáforos, señales y clima. Es parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** volante, acelerador, frenos, luces y claxon.
- **Sensors:** cámaras, radar, LiDAR, GPS y sensores de velocidad y distancia.

Es un entorno dinámico porque todo cambia mientras el vehículo avanza. También es estocástico porque no puede saber con certeza qué harán los demás conductores o peatones.

### 5. Agente de trading algorítmico en bolsa

- **Performance:** obtener ganancias, reducir pérdidas y controlar el riesgo.
- **Environment:** mercados financieros, acciones, inversionistas, noticias y precios. Es parcialmente observable, estocástico, secuencial y dinámico.
- **Actuators:** comprar, vender, modificar o cancelar órdenes.
- **Sensors:** precios, volumen de operaciones, historial, noticias y estado de la cartera.

El agente no conoce todo lo que influye en el mercado. Además, los precios cambian constantemente y no siempre se pueden predecir.

### 6. Sistema de diagnóstico médico asistido por IA

- **Performance:** apoyar al médico con diagnósticos precisos y reducir errores.
- **Environment:** pacientes, médicos, hospitales, expedientes y laboratorios. Es parcialmente observable, estocástico, secuencial y dinámico.
- **Actuators:** mostrar posibles diagnósticos, generar reportes y señalar resultados importantes.
- **Sensors:** síntomas, historial clínico, análisis, signos vitales e imágenes médicas.

Es parcialmente observable porque la información del paciente puede estar incompleta. También es estocástico porque síntomas parecidos pueden corresponder a distintas enfermedades.

### 7. Dron de inspección de infraestructura

- **Performance:** detectar daños correctamente, cubrir la zona de inspección y evitar accidentes.
- **Environment:** puentes, tuberías, torres, obstáculos, viento y clima. Es parcialmente observable, estocástico, secuencial y dinámico.
- **Actuators:** motores, hélices, control de dirección, altura y cámara.
- **Sensors:** cámaras, GPS, sensores de distancia, giroscopio y nivel de batería.

El dron no siempre puede observar toda la estructura desde una sola posición. Además, factores como el viento pueden afectar su movimiento.

### 8. Agente jugador de ajedrez

- **Performance:** ganar partidas, evitar derrotas y elegir buenas jugadas.
- **Environment:** tablero, piezas, reloj y adversario. Es totalmente observable, determinista, secuencial y discreto.
- **Actuators:** mover piezas, capturar, hacer enroque y promoción de peones.
- **Sensors:** posición de las piezas, movimientos del rival, turno y tiempo restante.

Es totalmente observable porque todas las piezas están visibles. También es determinista porque cada movimiento tiene un resultado conocido.