class PPM:
    def __init__(self, fd: str, size: tuple) -> None:
        """
        Init PPM file. Type P3

        Params
        ------
            fd : str
                Path to file

            size : Tuple
                Tuple with the Height,Width of the generated file
        """
        assert isinstance(fd, str), f"Expected str got {type(fd)}"
        assert isinstance(size, tuple), f"Expected tuple got {type(size)}"

        # stack[col][row]
        self.fd = fd
        self.size = size
        self.height = size[0]
        self.width = size[1]
        # 1D of pixels 
        # here pixels is an array of rgb values per pixel
        self.pixels = [[0,0,0] for x in range(0, (self.height+1)*self.width)]
        self.write_chunk(["P3\n", str(self.width), " ", str(self.height), "\n255\n"], False)

    def write_chunk(self, data: list, padding: bool) -> bool:
        """
        Write a chunk of data at the path in the PPM object by row

        Returns
        -------
            tuple(bool, str)
                containing if the write failed or not, with the second element being a message

        Params
        ------
            self : self
                self

            data : list 
                data could be anything really, as long as it is a string
                you could potentially write abitrary data to the ppm file. yikes

            padding : bool
                if you want padding or not, this is used for the file header primarily
        """
        assert isinstance(data, list), f"Expected str got {type(data)}"
        PADDING = "  "

        try:
            with open(self.fd, 'a') as fd:
                # per row add padded chunk to file
                for chunk in data:
                    # apply padding for chunk if specified
                    if padding:
                        chunk = PADDING+chunk

                    # write chunk to file 
                    fd.write(chunk)

            return (True, f"Write to {self.fd}: Successful")

        except IOError as err:
            return (False, err)
        except OSError as err:
            return (False, err)

    def fill_rect(self, w: int, h:int, thck:int, roi: tuple) -> bool:
        """
        Write a chunk of data at the path in the PPM object by row

        Returns
        -------
            tuple(bool, str)
                containing if the write failed or not, with the second element being a message

        Params
        ------
            self : self
                self

            w : int
                width of the rect

            h : int
                height of the rect

            thck : int
                thickness of the rect

            roi : tuple
                region of interest, origin of the rect x,y

        """
        return True

    def draw_rect(self, w: int, h: int, thck: int, roi: tuple) -> bool:
        """
        Write a chunk of data at the path in the PPM object by row

        Returns
        -------
            tuple(bool, str)
                containing if the write failed or not, with the second element being a message

        Params
        ------
            self : self
                self

            w : int
                width of the rect

            h : int
                height of the rect

            thck : int
                thickness of the rect

            roi : tuple
                region of interest, origin of the rect x,y

        """

        assert isinstance(w, int), f"w: Expected int, got {type(w)}"
        assert isinstance(h, int), f"h: Expected int, got {type(h)}"
        assert isinstance(thck, int), f"Thck: Expected int, got {type(h)}"
        assert isinstance(roi, tuple), f"roi: Expected tuple got {type(roi)}"

        

        # here we modify the matrix, not just the file- the file will get filled in later. 
        # stack = []
        # grid = []
        # ptr = 0
        # height = 0
        # for i in range(0, len(self._stack)):
        #     if ptr == self.width:
        #         grid.append(stack)
        #         stack = []
        #         ptr = 0
        #         height += 1
        #     stack.append(self._stack[i])
        #     ptr += 1
        
        for x in self.pixels:
            print(x)
            # self.write_chunk(x, False)


    def draw_cirle(self, diam: int, thck: int, roi: tuple) -> bool:
        """
        Draw a circle at the point in the file

        Returns
        -------
            tuple(bool, str)
                containing if the write failed or not, with the second element being a message

        Params
        ------
            self : self
                self

            diam : int
                diameter of the circle

            thck : int
                thickness of the circle 

            roi : tuple
                region of interest, origin of the rect x,y

        """

        assert isinstance(diam, int), f"diam: Expected int, got {type(w)}"
        assert isinstance(thck, int), f"thck: Expected int, got {type(h)}"
        assert isinstance(roi, tuple), f"roi: Expected tuple got {type(roi)}"
        ...


def test() -> int:
    img = PPM('test.ppm', (32,32))
    img.draw_rect(0,0,0,(1,1))
    return 0

test()