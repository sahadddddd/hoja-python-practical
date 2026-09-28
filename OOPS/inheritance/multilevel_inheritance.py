class grandparent():
    def feature_grandparent(self):
        print("grand parent feature")

class parent(grandparent):
    def feature_parent(self):
        print("parent feature")

class child(parent):
    def feature_child(self):
        print("child feautures")

a=child()
a.feature_grandparent()
a.feature_parent()
a.feature_child()