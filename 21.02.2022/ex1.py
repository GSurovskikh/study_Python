class Box:
    def __init__(self,width,length,depth):
        self.width = float(width)
        self.length = float(length)
        self.depth = float(depth)


class MaterialBox(Box):
    def __init__(self,width,length,depth,material="paper",color="red"):
        super(MaterialBox, self).__init__(width,length,depth)
        self.material = str(material)
        self.color = str(color)


if __name__ == '__main__':

    box = Box(10,50,5)
    material_box=MaterialBox(3,3,3,"metal","blue")


    print(isinstance(box,Box))
    print(isinstance(box, MaterialBox))
    print(isinstance(material_box, Box))
    print(isinstance(material_box, MaterialBox))

    print(issubclass(Box, MaterialBox))
    print(issubclass(MaterialBox,Box))