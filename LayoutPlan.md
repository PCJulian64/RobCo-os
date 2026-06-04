# RobCo OS

## Project Structure

```text
robco-os/
├── install.sh
├── uninstall.sh
│
├── robco-shell/
│   ├── main.py
│   ├── menus/
│   ├── themes/
│   └── assets/
│
├── gaming/
│   ├── steam.sh
│   ├── heroic.sh
│   └── lutris.sh
│
├── themes/
│   ├── fonts/
│   ├── sounds/
│   └── wallpapers/
│
├── configs/
│   ├── hyprland/
│   ├── kitty/
│   └── waybar/
│
└── systemd/
```

## Directory Overview

| Path | Purpose |
|--------|---------|
| `install.sh` | Main installation script |
| `uninstall.sh` | Removes RobCo OS components |
| `robco-shell/` | Core Pip-Boy/RobCo user interface |
| `gaming/` | Game launcher installation and configuration scripts |
| `themes/` | Fonts, sounds, and wallpapers |
| `configs/` | Application and desktop environment configurations |
| `systemd/` | Services and startup units |
