import requests
from flask import Flask
app = Flask(__name__)

host = '0.0.0.0:80' #this host needs to be updated to correct IP address
errors = 0
import click


@click.group()
def cli():
    pass
	
	
@cli.command()
@click.option('--phrase', default= 'hello',
              help= 'The phrase to translate to md5')
@click.argument('phrase')
def md5(phrase):
    """This will translate a given phrase to md5"""
    t = requests.get(f'http://{host}/md5/{phrase}')
    click.echo('This is the md5 encryption for %s:' % phrase)
    click.echo(t.json()['output'])
    pass

@cli.command()
@click.option('--number', default= 1,
              help= 'The number to find factorials of')
@click.argument('number')
def factorial(number):
    """Calculates the factorial of a number"""
    t = requests.get(f'http://{host}/factorial/{number}')
    click.echo('Factorial for %d is:' % number)
    click.echo(t.json()['output'])
    pass

@cli.command()
@click.option('--number', default= 1,
              help= 'The number to find fibonacci sequence of')
@click.argument('number')
def fibonacci(number):
    """Returns the fibonacci sequence up to that numbeer"""
    t = requests.get(f'http://{host}/fibonacci/{number}')
    click.echo('Fibonacci sequence for %d:' % number)
    click.echo(t.json()['output'])
    pass

@cli.command()
@click.option('--number', default= 1,
              help= 'The number to be checked if prime')
@click.argument('number')
def is_prime(number):
    """Returns if value is prime or not"""
    t = requests.get(f'http://{host}/is-prime/{number}')
    click.echo('%d prime number status:' % number)
    print(t.json()['output'])
    pass

@cli.command()
@click.option('--message', default= '1',
              help= 'The message to send in slack')
@click.argument('message')
def slack_alert(message):
    """Sends a slack alert and return if the send was successful"""
    t = requests.get(f'http://{host}/slack-alert/{message}')
    print(t.json()['output'])
    pass

@cli.command()
@click.option('--post', default= '',
              help= 'post test')

def post():
    """Insert a single entry into the database"""
    usr_key, usr_value = input("Enter a key followed by its value in the format of: key, value: ").split(", ")
    result = {'key' == usr_key, 'value' == usr_value}
    t = requests.post(f'http://{host}/keyval', json=result)
    print(t.json()['command'])
    print(t.json()['result'])
    print(t.json()['error'])
    pass

@cli.command()
@click.option('--string', default='',
              help='get test')
@click.argument('string')
def get(string):
    """Returns the entry associated with the key"""
    t = requests.get(f'http://{host}/keyval/{string}')
    click.echo('GET %s:' % string)
    if t.json()['result'] is True:
        print(t.json()['value'])
    else:
        print(t.json()['error'])
    pass



@cli.command()
@click.option('--put', default= '',
              help= 'put test')
def put(put):
    """Updates the entry associated with the key with the value provided"""
    pass



@cli.command()
@click.option('--user_key', default= '',
              help= 'delete test')
def delete(user_key):
    """Removes the entries associated with the keys provided"""
    pass

 
if __name__ == '__main__':
   cli()