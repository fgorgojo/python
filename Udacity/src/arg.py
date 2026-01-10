import sys
import argparse

parser = argparse.ArgumentParser(
        description="Explore past and future close approaches of near-Earth objects."
)

parser.add_argument('name', type=str, help='Nombre persona')
parser.add_argument('--city', type=str, default='Mostoles', help='De aonde eres...')

args = parser.parse_args()
name=args.name
city=args.city

#print(f'hello, {name} from {city}')


