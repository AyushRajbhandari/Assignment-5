# Author: Ayush Rajbhandari
# GitHub username: AyushRajbhandari
# Date: 6-13-26
# Description: Defines a Box class with private dimensions and volume,
# #            and a box_sort function to sort boxes from greatest to least volume.

class Box:
    """
    A class to represent a Box with private length, width, and height.
    """
    def __init__(self, length, width, height):
        """Initializes the private data members of the Box."""
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """Returns the length of the Box."""
        return self._length

    def get_width(self):
        """Returns the width of the Box."""
        return self._width

    def get_height(self):
        """Returns the height of the Box."""
        return self._height

    def volume(self):
        """Calculates and returns the volume of the Box."""
        return self._length * self._width * self._height


def box_sort(box_list):
    """
    Sorts a list of Box objects from greatest volume to least volume
    using the insertion sort algorithm. Mutates the list in place.
    """
    for index in range(1, len(box_list)):
        current_box = box_list[index]
        pos = index - 1

        # Shift boxes with a smaller volume to the right
        while pos >= 0 and box_list[pos].volume() < current_box.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1

        # Insert the current box in its correct sorted position
        box_list[pos + 1] = current_box

b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]
box_sort(box_list)
for box in box_list:
    print(box.volume())
