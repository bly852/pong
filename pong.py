import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
player_movespeed = 300


class MyGame(arcade.Window):
    """
    main application class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """
        sets up all variables for the game
        """

        # player 1 variables
        self.player1_y = SCREEN_HEIGHT / 2
        self.player1_up = False
        self.player1_down = False

        # player 2 variables
        self.player2_y = SCREEN_HEIGHT / 2
        self.player2_up = False
        self.player_down= = False

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # player 1
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2 - SCREEN_WIDTH / 3), self.player1_y, 10, 50, arcade.color.WHITE)

        # player 2
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2 + SCREEN_WIDTH / 3), self.player2_y, 10, 50, arcade.color.WHITE)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()