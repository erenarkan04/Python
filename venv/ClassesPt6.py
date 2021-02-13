
# Can make any new class a child of a built in Python class

class Text(str):

    def duplicate(self):
        return self + self

text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("append called: " + object)
        super().append(object)

list = TrackableList()

list.append("1")
print(list)