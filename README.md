# Chopsticks
This project is using TensorFlow to teach a computer how to learn how to play the game Chopsticks. This game can be hardcoded to win every time without machine learning, but I thought it would be a good first concept to introduce myself to the concepts.

Rules I will be using (there are different variations used)

- Two players start with hands with one finger
- Each player has an option to
    1. split an amount of fingers from one hand to another
    2. attack the enemy's hand with the amount of fingers they have on a particular hand, the attacked hand has a new amount of fingers which is equal to the sum of the attackers hand and the attacked hand
- If a hand reaches a quantity greater than four, they will lose all fingers and end up with 0
- If both hands of a player reach 0, they lose

I will be using TensorFlow to find the best possible moves with machine learning
