# Pattern Problems - Various pattern printing solutions for DSA practice

class PatternProblems:
    """
    A collection of pattern printing problems commonly used in programming practice.
    Each method demonstrates different algorithmic thinking and loop control.
    """
    
    def right_triangle_pattern(self, n):
        """
        Print a right triangle pattern with stars
        Example for n=5:
        *
        **
        ***
        ****
        *****
        """
        for i in range(1, n + 1):
            print('*' * i)
    
    def left_triangle_pattern(self, n):
        """
        Print a left triangle pattern with stars
        Example for n=5:
            *
           **
          ***
         ****
        *****
        """
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * i
            print(spaces + stars)
    
    def pyramid_pattern(self, n):
        """
        Print a pyramid pattern with stars
        Example for n=5:
            *
           ***
          *****
         *******
        *********
        """
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    def inverted_pyramid_pattern(self, n):
        """
        Print an inverted pyramid pattern with stars
        Example for n=5:
        *********
         *******
          *****
           ***
            *
        """
        for i in range(n, 0, -1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    def diamond_pattern(self, n):
        """
        Print a diamond pattern with stars
        Example for n=5:
            *
           ***
          *****
         *******
        *********
         *******
          *****
           ***
            *
        """
        # Upper half (including middle)
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
        
        # Lower half
        for i in range(n - 1, 0, -1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    def hollow_square_pattern(self, n):
        """
        Print a hollow square pattern with stars
        Example for n=5:
        *****
        *   *
        *   *
        *   *
        *****
        """
        for i in range(n):
            if i == 0 or i == n - 1:
                # First and last rows - all stars
                print('*' * n)
            else:
                # Middle rows - stars only at edges
                print('*' + ' ' * (n - 2) + '*')
    
    def hollow_triangle_pattern(self, n):
        """
        Print a hollow triangle pattern
        Example for n=5:
            *
           * *
          *   *
         *     *
        *********
        """
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            if i == 1:
                print(spaces + '*')
            elif i == n:
                print(spaces + '*' * (2 * i - 1))
            else:
                stars_gap = ' ' * (2 * i - 3)
                print(spaces + '*' + stars_gap + '*')
    
    def number_triangle_pattern(self, n):
        """
        Print a triangle pattern with numbers
        Example for n=5:
        1
        12
        123
        1234
        12345
        """
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end='')
            print()
    
    def number_pyramid_pattern(self, n):
        """
        Print a pyramid pattern with numbers
        Example for n=5:
            1
           121
          12321
         1234321
        123454321
        """
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            
            # Ascending numbers
            ascending = ''
            for j in range(1, i + 1):
                ascending += str(j)
            
            # Descending numbers
            descending = ''
            for j in range(i - 1, 0, -1):
                descending += str(j)
            
            print(spaces + ascending + descending)
    
    def floyd_triangle_pattern(self, n):
        """
        Print Floyd's triangle pattern
        Example for n=5:
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
        """
        num = 1
        for i in range(1, n + 1):
            for j in range(i):
                print(num, end=' ')
                num += 1
            print()
    
    def pascal_triangle_pattern(self, n):
        """
        Print Pascal's triangle pattern
        Example for n=5:
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
        """
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            print(spaces, end='')
            
            coeff = 1
            for j in range(i + 1):
                print(coeff, end=' ')
                coeff = coeff * (i - j) // (j + 1)
            print()
    
    def alphabet_triangle_pattern(self, n):
        """
        Print a triangle pattern with alphabets
        Example for n=5:
        A
        AB
        ABC
        ABCD
        ABCDE
        """
        for i in range(1, n + 1):
            for j in range(i):
                print(chr(65 + j), end='')
            print()
    
    def zigzag_pattern(self, rows, cols):
        """
        Print a zigzag pattern
        Example for rows=4, cols=20:
        *   *   *   *   *
         * * * * * * * *
          *   *   *   *
         * * * * * * * *
        """
        for i in range(rows):
            for j in range(cols):
                if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 2):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    
    def butterfly_pattern(self, n):
        """
        Print a butterfly pattern
        Example for n=4:
        *      *
        **    **
        ***  ***
        ********
        ********
        ***  ***
        **    **
        *      *
        """
        # Upper half
        for i in range(1, n + 1):
            # Left stars
            print('*' * i, end='')
            # Middle spaces
            print(' ' * (2 * (n - i)), end='')
            # Right stars
            print('*' * i)
        
        # Lower half
        for i in range(n, 0, -1):
            # Left stars
            print('*' * i, end='')
            # Middle spaces
            print(' ' * (2 * (n - i)), end='')
            # Right stars
            print('*' * i)


# Example usage and testing
if __name__ == "__main__":
    patterns = PatternProblems()
    
    print("=== Pattern Problems Demo ===\n")
    
    n = 5
    
    print("1. Right Triangle Pattern:")
    patterns.right_triangle_pattern(n)
    print()
    
    print("2. Left Triangle Pattern:")
    patterns.left_triangle_pattern(n)
    print()
    
    print("3. Pyramid Pattern:")
    patterns.pyramid_pattern(n)
    print()
    
    print("4. Diamond Pattern:")
    patterns.diamond_pattern(n)
    print()
    
    print("5. Hollow Square Pattern:")
    patterns.hollow_square_pattern(n)
    print()
    
    print("6. Number Triangle Pattern:")
    patterns.number_triangle_pattern(n)
    print()
    
    print("7. Floyd's Triangle Pattern:")
    patterns.floyd_triangle_pattern(n)
    print()
    
    print("8. Pascal's Triangle Pattern:")
    patterns.pascal_triangle_pattern(n)
    print()
    
    print("9. Alphabet Triangle Pattern:")
    patterns.alphabet_triangle_pattern(n)
    print()
    
    print("10. Butterfly Pattern:")
    patterns.butterfly_pattern(4)
    print()