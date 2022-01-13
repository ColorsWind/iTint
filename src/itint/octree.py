import collections
import numpy as np

max_depth = 8
Color = collections.namedtuple("Color", ["R", "G", "B"])


class OctreeNode(object):

    def __init__(self):
        self.is_leaf = False
        self.pixel_count = 0
        self.color = np.zeros(3, dtype=int)
        self.children = np.zeros(8, dtype=OctreeNode)


class Octree(object):

    def __init__(self):
        self.root = OctreeNode()
        self.leaf_num = 0
        self.reducible = [list() for _ in range(0, 7)]

    def insert_color(self, node: OctreeNode, color: np.ndarray, level: int):
        if node.is_leaf:
            node.pixel_count += 1
            node.color += color
        else:
            r, g, b = color >> (7 - level) & 1
            idx = (r << 2) + (g << 1) + b
            child = node.children[idx]
            if not child:
                child = self.create_node(idx, level + 1)
                node.children[idx] = child
            self.insert_color(child, color, level + 1)

    def create_node(self, idx: int, level: int) -> OctreeNode:
        node = OctreeNode()
        if level == 7:
            node.is_leaf = True
            self.leaf_num += 1
        else:
            self.reducible[level].append(node)
        return node

    def reduce_tree(self):
        # 从第六层开始查找, 找到一个非空列表
        level = 6
        reducible: list[OctreeNode] = []
        while level >= 0:
            reducible = self.reducible[level]
            if len(reducible) > 0:
                break
            level -= 1

        node = reducible.pop()
        color = np.zeros(3, dtype=int)
        count = 0
        for child in node.children:
            if not child:
                continue
            color += child.color
            count += child.pixel_count
            child.is_leaf = True
            self.leaf_num -= 1

        node.is_leaf = True
        node.color = color
        node.pixel_count = count
        self.leaf_num += 1



    def build(self, pixels: np.ndarray, max_colors: int):
        for color in pixels:
            self.insert_color(self.root, color, 0)
        while self.leaf_num > max_colors:
            self.reduce_tree()

    def get_color(self, node: OctreeNode) -> list:
        colors = list()
        if node.is_leaf:
            color = node.color / node.pixel_count
            colors.append(color)
        else:
            for child in node.children:
                if not child:
                    continue
                color = self.get_color(child)
                colors.extend(color)
        return colors

from PIL import Image

if __name__ == "__main__":
    image = Image.open(r"D:\Desktop\th.jpg")
    resized = image.resize(size=(200, 100))
    data = np.asarray(resized).reshape((-1, 3))
    tree = Octree()
    tree.build(data, 5)
    colors = tree.get_color(tree.root)
    print(tree.leaf_num)
    print(colors)
    colors = np.array(colors, dtype=np.float32)
    print(colors.shape)
    colors = colors.reshape((-1, 1, 3))
    image = Image.fromarray(colors, mode="RGB")
    image.show()
