#!/usr/bin/env python
import click

@click.command()
def hello():
    print('Hello World!')

if __name__ == '__main__':
    hello()