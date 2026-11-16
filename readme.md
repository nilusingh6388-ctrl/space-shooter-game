# Space Shooter Game

A classic 2D arcade Space Shooter game built in **Python 3** using **Pygame**. Pilot your spaceship to shoot down descending enemies, manage your projectile limits, and survive as long as possible!

---

## Features

* **Object-Oriented Design:** Implements clean, dedicated classes for `Ship`, `Bullet`, and `Enemy`.
* **Smooth Controls:** Move left and right with the arrow keys while respecting window boundaries.
* **Projectile Management:** Fire up to **5 bullets** on screen simultaneously using the spacebar.
* **Collision Detection:** Uses Pygame's `Rect.colliderect()` to handle precise bullet-enemy hits (`+10` points per destroy).
* **Lives & Game Over System:** Start with **3 lives**. Losing a life occurs when an enemy reaches the bottom of the screen ($y = 600$), triggering a **Game Over** screen when lives hit zero.

---

## Requirements

* Python 3.x
* Pygame library

---

## Installation & Running

1. Install Pygame via pip if you haven't already:
   ```bash
   pip install pygame
