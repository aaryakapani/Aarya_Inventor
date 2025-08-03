# 8-bit Zelda-like Game Framework

A Python-based game framework inspired by The Legend of Zelda, built with Pygame. This framework provides the foundation for creating 8-bit style adventure games with top-down perspective, tile-based worlds, and classic game mechanics.

## Features

- **Top-down perspective** with smooth player movement
- **Tile-based world system** with different terrain types (grass, water, trees, rocks)
- **Camera system** that follows the player
- **8-bit style graphics** with simple geometric shapes and colors
- **Health and combat system** with attack mechanics
- **Pause menu** and game state management
- **HUD display** showing health, score, and level
- **Modular architecture** for easy expansion

## Game Controls

- **WASD** or **Arrow Keys**: Move the player
- **SPACE**: Attack
- **ESC**: Pause/Resume game
- **Mouse**: Future menu interactions

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Game

Navigate to the sandbox directory and run:

```bash
python3 main.py
```

### Demo Version

For a more complete example with enemies and items, run:

```bash
python3 demo.py
```

## Project Structure

```
sandbox/
├── main.py              # Main game entry point
├── demo.py              # Demo with enemies and items
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── game/               # Game engine package
    ├── __init__.py
    ├── constants.py    # Game constants and configuration
    ├── game_state.py   # Overall game state management
    ├── game_engine.py  # Main game engine and rendering
    ├── player.py       # Player character class
    ├── sprite.py       # Base sprite class
    ├── world.py        # World and tile management
    ├── tile.py         # Individual tile system
    ├── camera.py       # Camera and viewport system
    ├── ui.py           # User interface system
    ├── enemy.py        # Example enemy system
    └── item.py         # Item and collectible system
```

## Game Architecture

### Core Systems

1. **Game Engine** (`game_engine.py`): Coordinates all game systems, handles input, and manages the main loop
2. **Game State** (`game_state.py`): Manages the overall game state including player, world, and progression
3. **Player** (`player.py`): Handles player movement, combat, and animation
4. **World** (`world.py`): Manages the tile-based world and entities
5. **Camera** (`camera.py`): Handles viewport management and follows the player
6. **UI** (`ui.py`): Renders HUD, menus, and user interface elements

### Tile System

The world is built using a tile-based system with different terrain types:
- **Grass**: Walkable, green tiles
- **Water**: Non-walkable, animated blue tiles
- **Trees**: Non-walkable, dark green with brown trunks
- **Rocks**: Non-walkable, gray with texture

### Rendering System

The game uses a simple but effective rendering system:
- Geometric shapes for sprites (rectangles, circles, polygons)
- 8-bit color palette with limited colors
- Camera offset for smooth scrolling
- Only renders visible tiles for performance

## Extending the Framework

### Adding New Features

1. **Enemies**: Create enemy classes inheriting from `Sprite`
2. **Items**: Add collectible items and inventory system
3. **Levels**: Implement multiple levels with different maps
4. **Sound**: Add pygame sound effects and music
5. **Sprites**: Replace geometric shapes with actual sprite images

### Example: Adding an Enemy

```python
class Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32)
        self.health = 50
        self.speed = 1
        
    def update(self):
        # Enemy AI logic here
        pass
        
    def render(self, screen, camera):
        # Render enemy as red rectangle
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        pygame.draw.rect(screen, RED, (screen_x, screen_y, self.width, self.height))
```

## Development Roadmap

- [ ] Add enemy AI and combat
- [ ] Implement item system and inventory
- [ ] Add sound effects and music
- [ ] Create multiple levels
- [ ] Add save/load functionality
- [ ] Implement sprite-based graphics
- [ ] Add particle effects
- [ ] Create level editor

## Contributing

This is a learning project for game development. Feel free to experiment and add new features!

## License

This project is open source and available under the MIT License. 