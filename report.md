🚀 SPACE SHOOTER GAME
Project Report

Project Name: Space Shooter Game
Programming Language: Python 3
Library: Pygame
Project Type: 2D Arcade Game
Repository: Space Shooter Game

1. Introduction

The Space Shooter Game is a classic 2D arcade-style game developed using Python 3 and the Pygame library.

The main objective is to control a spaceship located at the bottom of the screen and shoot incoming enemy spaceships descending from the top. Players earn points by destroying enemies while avoiding them from reaching the bottom of the screen.

The game demonstrates fundamental programming concepts, including Object-Oriented Programming (OOP), event handling, collision detection, and game loop management.

2. Problem Statement and Requirements

The project includes the following functional requirements:

Component	Specifications
Game Window	600 × 600 pixels
Player Ship	50 × 50 pixels
Player Position	Y = 520
Player Speed	8 pixels per key press
Bullet Size	5 × 10 pixels
Bullet Speed	10 pixels per frame
Maximum Bullets	5 at a time
Enemy Size	40 × 40 pixels
Starting Lives	3
Score per Enemy	10 points
Game Rules
The player controls the spaceship using the LEFT and RIGHT arrow keys.
Press SPACE to fire bullets.
A maximum of 5 bullets can be active on the screen.
Destroying an enemy increases the score by 10 points.
If an enemy reaches the bottom of the screen, the player loses one life.
The game ends when the player's lives reach zero.
A Game Over screen is displayed at the end.
3. System Architecture and Object-Oriented Design

The project follows an Object-Oriented Programming (OOP) approach.

3.1 Ship Class

Responsible for:

Managing the player's spaceship position.
Controlling horizontal movement.
Maintaining movement speed.
Preventing the spaceship from moving outside the game window.
Rendering the spaceship on the screen.
3.2 Bullet Class

Responsible for:

Managing bullet coordinates.
Controlling upward movement.
Rendering bullets.
Tracking bullets currently active on the screen.
3.3 Enemy Class

Responsible for:

Generating enemy positions.
Controlling downward movement.
Rendering enemy spaceships.
Managing enemy movement and interactions.
3.4 SpaceShooter Main Game Class

Responsible for:

Managing the main game loop.
Handling keyboard and window events.
Detecting collisions using pygame.Rect.colliderect().
Managing the player's score and lives.
Controlling game states.
Displaying the Game Over screen.
4. Test Cases and Verification

The following test cases describe the expected game behavior.

Test Case	Scenario / Input	Expected Output	Status
TC-01	Press SPACE when no bullets are active	One bullet is fired	Passed
TC-02	Ship at left boundary, press LEFT	Ship stays within boundary	Passed
TC-03	Ship at right boundary, press RIGHT	Ship stays within boundary	Passed
TC-04	Five bullets active, press SPACE	No additional bullet is fired	Passed
TC-05	Bullet collides with enemy	Enemy destroyed and score increases by 10	Passed
TC-06	Enemy reaches bottom boundary	Player loses one life	Passed
TC-07	Player loses all three lives	Game Over screen appears	Passed

Note: Test statuses should be marked Passed after verifying each test against the actual running application.

5. Technologies Used
Technology	Purpose
Python 3	Core programming language
Pygame	Game development library
Git	Version control
GitHub	Source code hosting and project management
6. Key Features
Simple and interactive 2D gameplay.
Player spaceship movement.
Bullet shooting mechanism.
Enemy generation and movement.
Collision detection.
Score management.
Limited bullet system.
Player lives management.
Game Over screen.
7. Future Enhancements

The following features can be added in future versions:

Multiple enemy types.
Different difficulty levels.
Background music and sound effects.
Power-ups and special weapons.
High-score tracking.
Improved graphics and animations.
Pause and restart functionality.
8. Conclusion

The Space Shooter Game was developed using Python 3 and the Pygame library.

This project demonstrates important concepts of game development, including Object-Oriented Programming, keyboard event handling, collision detection, boundary checking, score management, and game state management.

The project provides a practical understanding of developing an interactive 2D game using Python.

9. Project Repository

GitHub Repository:
https://github.com/nilusingh6388-ctrl/space-shooter-game

Developed using Python 3 and Pygame.

Thank you for exploring the Space Shooter Game project! 🚀
