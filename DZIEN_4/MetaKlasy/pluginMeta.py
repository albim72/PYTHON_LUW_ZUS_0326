from types import new_class

registry = {}

class PluginMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        if name != "Plugin":
            registry[name] = new_class
        return new_class

class Plugin(metaclass=PluginMeta):
    pass

class ImagePlugin(Plugin):
    def process(self, image):
        print(f"processing {image}")

class TextPlugin(Plugin):
    def process(self, text):
        print(f"processing {text}")

print(registry)
