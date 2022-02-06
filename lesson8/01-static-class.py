class Operations:
    """
    Description for the class
    """
    class_name: str
    class_attr: int

    @staticmethod
    def lower_string(content: str):
        return content.lower()

    @staticmethod
    def upper_string(content: str):
        return content.upper()

    @classmethod
    def normalize(cls, content: str):
        a = cls.lower_string(content)
        return cls.upper_string(a)


temp_string = "Hello"

print(Operations.lower_string(temp_string))
print(Operations.normalize(temp_string))

print(Operations.__dict__)
print(Operations.__annotations__)