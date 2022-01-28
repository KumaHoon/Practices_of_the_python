user = 'KUMAHOON'


def hello():
    print(f'hello {user}!')


try:
    hello()
except Exception as e:
    print(e)
