"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""




from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        
        starting_colour: int = image[sr][sc]
        row_height: int = len(image)
        column_length: int = len(image[0])
        
        seen: dict = {}
        stack: List[tuple] = [(sr, sc)]
        
        while stack:
            pixel: tuple = stack.pop()
            if not seen.get(pixel):
                if 0 <= pixel[0] < row_height and 0 <= pixel[1] < column_length:
                    if image[pixel[0]][pixel[1]] == starting_colour:
                        image[pixel[0]][pixel[1]]: int = newColor
                        seen[pixel]: bool = True
                        stack.append((pixel[0] + 1, pixel[1]))
                        stack.append((pixel[0] - 1, pixel[1]))
                        stack.append((pixel[0], pixel[1] + 1))
                        stack.append((pixel[0], pixel[1] - 1))
        
        return image
