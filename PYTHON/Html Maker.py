class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self,file=None):
        print(self,file=file)


class Doctype(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''


class Head(Tag):

    def __init__(self,title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title',title)
            self.contents = str(self._title_tag)
    #     self._head_contents = []
    #
    # def add_tag(self,name,contents):
    #     new_tag = Tag(name,contents)
    #     self._head_contents.append(new_tag)
    #
    # def display(self,file=None):
    #     for tag in self._head_contents:
    #         self.contents += str(tag)
    #
    #         super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self,file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)

class HtmlDoc(object):

    def __init__(self,title=None):
        self._doc_type = Doctype()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self,name,contents):
        self._body.add_tag(name,contents)

    # def add_head_tag(self,name,contents):
    #     self._head.add_tag(name, contents)


    def display(self,file=None):
        self._doc_type.display(file=file)
        print("<html>")
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>')


if __name__ == "__main__":
    my_page = HtmlDoc('demo html doc')
    my_page.add_tag('h1','Main Heading')
    my_page.add_tag('h2','subheading')
    my_page.add_tag('p','paragraph that will appera on age')
    with open('test.html','w') as test_doc:
        my_page.display(file=test_doc)

new_body = Body()
new_body.add_tag('h1','aggeration')
new_body.add_tag('p',"Unlike <strong> composition </strong> , aggeration uses existing instances"
                 "of objects to build another object")
new_body.add_tag('p',"The composed object does'nt actually own the objects ")


