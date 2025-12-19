# orion-core
orion-system/
├── docker/                 # Configuraciones de contenedores
│   ├── brain.Dockerfile
│   ├── messenger.Dockerfile
│   └── analyst.Dockerfile
├── config/                 # Archivos de configuración y léxico
│   ├── dialogo.yaml        # Diccionario para el MGG (Personalidad) [cite: 99]
│   ├── settings.yaml       # Umbrales SVEP y configuraciones de red
│   └── .env.example        # Plantilla para tokens (Spotify, Discord, Telegram)
├── src/                    # Código fuente dividido por responsabilidades
│   ├── brain/              # El Núcleo de Conciencia
│   │   ├── svep_engine.py  # Lógica del Vector 3D (H, A, R) [cite: 60, 291]
│   │   └── mgg_core.py     # Motor de Generación Gramatical [cite: 94, 301]
│   ├── messengers/         # Interfaces de comunicación
│   │   ├── discord_bot.py
│   │   └── telegram_bot.py
│   ├── sensors/            # Captación de datos (Sentidos)
│   │   ├── environment.py  # DHT11 (Temp/Hum) [cite: 186]
│   │   ├── presence.py     # Escaneo BT/WiFi (Móvil, PC, Watch)
│   │   └── health.py       # Monitoreo de CPU/Temp del NSR [cite: 62, 198]
│   ├── actuators/          # Control físico (Músculo)
│   │   └── relays.py       # Control binario de luces [cite: 186, 192]
│   ├── analyst/            # Procesamiento de datos externos
│   │   ├── spotify_api.py  # Integración y control de música
│   │   └── wrapped.py      # Generador de informes de hábitos
│   └── utils/              # Herramientas compartidas (Logger, MQTT Wrapper)
│       └── watchdog.py     # Auto-diagnóstico y recuperación de servicios
├── scripts/                # Utilidades de despliegue y mantenimiento
│   ├── setup_pi.sh         # Script de instalación inicial en la 4B
│   └── daily_check.sh      # Ejecutable para el análisis diario
├── docker-compose.yml      # Orquestador de la constelación [cite: 57]
└── README.md               # Documentación y bitácora del Arquitecto
