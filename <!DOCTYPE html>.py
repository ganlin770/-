<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake Game</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        canvas {
            background-color: #000;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const boxSize = 20;
        let snake = [{ x: boxSize * 5, y: boxSize * 5 }]; // Initial snake position
        let food = getRandomFoodPosition(); // Generate initial food position
        let direction = "RIGHT"; // Initial direction of snake movement
        let gameInterval;
        let changingDirection = false; // Prevent multiple direction changes between frames

        document.addEventListener("keydown", changeDirection); // Listen for key press events to change direction

        function changeDirection(event) {
            if (changingDirection) return; // Ignore if already changed direction in current frame
            changingDirection = true;

            const keyPressed = event.key;
            const goingUp = direction === "UP";
            const goingDown = direction === "DOWN";
            const goingLeft = direction === "LEFT";
            const goingRight = direction === "RIGHT";

            // Prevent snake from reversing
            if (keyPressed === "ArrowUp" && !goingDown) {
                direction = "UP";
            } else if (keyPressed === "ArrowDown" && !goingUp) {
                direction = "DOWN";
            } else if (keyPressed === "ArrowLeft" && !goingRight) {
                direction = "LEFT";
            } else if (keyPressed === "ArrowRight" && !goingLeft) {
                direction = "RIGHT";
            }
        }

        function drawGame() {
            changingDirection = false; // Reset changingDirection flag for next frame
            // Clear canvas
            ctx.fillStyle = "black";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw snake
            ctx.fillStyle = "lime";
            for (let i = 0; i < snake.length; i++) {
                ctx.fillRect(snake[i].x, snake[i].y, boxSize, boxSize);
            }

            // Draw food
            ctx.fillStyle = "red";
            ctx.fillRect(food.x, food.y, boxSize, boxSize);

            // Move snake
            let head = { x: snake[0].x, y: snake[0].y }; // Copy current head position

            // Update head position based on direction
            if (direction === "UP") head.y -= boxSize;
            if (direction === "DOWN") head.y += boxSize;
            if (direction === "LEFT") head.x -= boxSize;
            if (direction === "RIGHT") head.x += boxSize;

            // Check collision with wall or self
            if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height || snakeCollision(head)) {
                clearInterval(gameInterval); // Stop the game if collision occurs
                alert("Game Over!");
                return;
            }

            // Check if snake eats the food
            if (head.x === food.x && head.y === food.y) {
                food = getRandomFoodPosition(); // Generate new food position
            } else {
                snake.pop(); // Remove last part of the snake if no food eaten
            }

            snake.unshift(head); // Add new head to the front of the snake
        }

        function snakeCollision(head) {
            // Check if the new head position collides with any part of the snake
            for (let i = 1; i < snake.length; i++) {
                if (head.x === snake[i].x && head.y === snake[i].y) {
                    return true;
                }
            }
            return false;
        }

        function getRandomFoodPosition() {
            let position;
            while (true) {
                // Generate random position for food within canvas bounds
                position = {
                    x: Math.floor(Math.random() * (canvas.width / boxSize)) * boxSize,
                    y: Math.floor(Math.random() * (canvas.height / boxSize)) * boxSize
                };
                // Ensure food does not spawn on the snake
                if (!snake.some(segment => segment.x === position.x && segment.y === position.y)) {
                    break;
                }
            }
            return position;
        }

        function startGame() {
            gameInterval = setInterval(drawGame, 100); // Start the game loop
        }

        startGame();
    </script>
</body>
</html>