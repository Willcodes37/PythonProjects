
# CS50 P-Shirt

    #### Description:

    In the file called shirt.py, it expects exactly two command-line arguments:

        in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
        in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

    The program should instead exit via sys.exit:

        if the user does not specify exactly two command-line arguments,
        if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
        if the input’s name does not have the same extension as the output’s name, or
        if the specified input does not exist.

    The program should then overlay shirt.png (which has a transparent background) on the input after resizing 
    and cropping the input to be the same size, saving the result as its output.
    
        