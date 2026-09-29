class grandfather():
    def feature_grandfather(self):
        print("grandfather:wise and expirence")

class father(grandfather):
    def feature_father(self):
        print("father:hardwork and caring")

class aunt(grandfather):
    def feature_aunt(self):
        print("aunt:kind and supportive")

class child(father,aunt):
    def feature_child(self):
        print("child:energetic and curious")

a=child()
a.feature_grandfather()
a.feature_father()
a.feature_aunt()
a.feature_child()