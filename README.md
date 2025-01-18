# snake_game
The Snake game is a classic arcade game where the player controls a snake that moves around the screen, eating food to grow longer. The objective is to avoid hitting walls or the snake's own body while trying to consume as much food as possible to achieve the highest score.

## Features

- Classic snake gameplay
- Simple and intuitive controls
- Score tracking
- Snake head image with rotation based on direction

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/pseudo-00/snake_game.git
cd snake_game
```

2. Install the required dependencies:

```bash
pip install pygame
```

## Usage

Run the game using the following command:

```bash
python snake_game.py
```

## Controls

- Arrow keys to change the direction of the snake:
  - 

UP

 arrow key to move up
  - 

DOWN

 arrow key to move down
  - 

LEFT

 arrow key to move left
  - 

RIGHT

 arrow key to move right

## How to Play

- Control the snake using the arrow keys.
- Eat the red food blocks to grow in length and increase your score.
- Avoid colliding with the walls or the snake's own body.
- The game ends when the snake collides with the wall or itself.

## Future Improvements

- Add levels with increasing difficulty.
- Improve the graphics for the snake and the game overall.
- Implement a high score system.
- Add sound effects and background music.

## Running with Docker

1. **Build the Docker Image:**
   ```bash
   docker build -t snake_game .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -it --rm snake_game
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Pygame](https://www.pygame.org/) - The library used to create the game.
- [Python](https://www.python.org/) - The programming language used.
- This project was created following a tutorial on [freeCodeCamp](https://www.freecodecamp.org/).

## Contact

If you have any questions or suggestions, feel free to contact me at [rankiratsingh00@gmail.com].
```