import requests


def main():
    header()
    code = input('What zipcode do you want the weather for?' )
    get_html(code)
    #ToDo parse html
    #ToDo display the forcast


def header():
    print('-----------------------------')
    print('         WEATHER APP')
    print('-----------------------------')
    print()


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather/{}'.format(zipcode)
    response = requests.get(url)
    print(response.text[0:250])


if __name__ == '__main__':
    main()