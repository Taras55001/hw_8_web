from pprint import pprint

from connect import session_hw
from models import Autor, Post, Tag


def find_tag(tag_name):
    posts = Post.objects(tags__name=tag_name)
    return posts

def find_tags(*tag_names):
    posts = Post.objects(tags__name__all=tag_names)
    return posts

def find_author(author_name):
    author = Autor.objects(fullname=author_name).first()
    if author:
        posts = Post.objects(author=author)
        return posts
    return []


def main():
    while True:
        user_input = input()
        action = user_input.split(':')
        match action[0]:
            case 'tag':
                result = find_tag(action[1])
                [pprint(r.quote) for r in result]
            case 'tags':
                tags = action[1].split(',')
                result = find_tags(*tags)
                # print(result)
                [pprint(r.quote) for r in result]
            case 'name':
                result = find_author(action[1])
                [pprint(r.quote) for r in result]
            case 'exit':
                break
            case _:
                print("Unknown command")

if __name__ == "__main__":
    main()