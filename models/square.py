from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square shape, inheriting from Rectangle with shared attributes and validations.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance with side length 'size' and inherited attributes.

        Args:
            size (int): The side length of the square.
            x (int, optional): X-coordinate of the bottom left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the bottom left corner. Defaults to 0.
            id (int, optional): Unique identifier for the object. Defaults to None.
        """

        super().__init__(id, size, size, x, y)  # Call Rectangle's __init__ with size for both width and height

    @property
    def size(self):
        """
        Getter for the square's size (equivalent to width or height).

        Returns:
            int: The side length of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the square's size, updating both width and height simultaneously.

        Args:
            value (int): The new value for the size.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A formatted string including square details.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

square = Square(5, 2, 3, 1)
print(str(square))