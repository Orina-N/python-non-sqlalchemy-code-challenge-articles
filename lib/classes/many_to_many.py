class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        author.add_article(self)
        author.add_magazine(magazine)
        self.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot set attribute 'title'")

    def _validate_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters inclusive")
        return title
        

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must have more than 0 characters")
        self._name = name
        self._articles = []
        self._magazines = []
        
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        raise ValueError("Cannot change authors name")

    def articles(self):
        return self._articles
 

    def magazines(self):
        return self._magazines

    
    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Article must be an instance of Article")
        self._articles.append(article) 
        return article

    def add_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if magazine not in self._magazines:
            self._magazines.append(magazine)
        return magazine 

    def topic_areas(self):
        return {magazine.category for magazine in self._magazines}

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass



author_1 = Author("Carry Bradshaw")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")
magazine_3 = Magazine("GQ", "Fashion")

author_1.add_magazine(magazine_1)
author_1.add_magazine(magazine_2)
author_1.add_magazine(magazine_3)
