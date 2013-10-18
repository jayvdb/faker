from . import BaseProvider
from . import date_time
from datetime import datetime
import random


class Provider(BaseProvider):
    user_agents = ('firefox', 'chrome', 'internet_explorer', 'opera', 'safari')

    windows_platform_tokens = (
        'Windows NT 6.2', 'Windows NT 6.1', 'Windows NT 6.0', 'Windows NT 5.2', 'Windows NT 5.1',
        'Windows NT 5.01', 'Windows NT 5.0', 'Windows NT 4.0', 'Windows 98; Win 9x 4.90',
        'Windows 98', 'Windows 95', 'Windows CE'
    )

    linux_processors = ('i686', 'x86_64',)

    mac_processors = ('Intel', 'PPC', 'U; Intel', 'U; PPC')

    langs = ('en-US', 'sl-SI', 'it-IT')

    @classmethod
    def mac_processor(cls):
        return cls.random_element(cls.mac_processors)

    @classmethod
    def linux_processor(cls):
        return cls.random_element(cls.linux_processors)

    @classmethod
    def user_agent(cls):
        name = cls.random_element(cls.user_agents)
        return getattr(cls, name)()

    @classmethod
    def chrome(cls):
        saf = str(random.randint(531, 536)) + str(random.randint(0, 2))

        platforms = (
            "({0}) AppleWebKit/{1} (KHTML, like Gecko) Chrome/{2}.0.{3}.0 Safari/{4}".format(
                cls.linux_platform_token(), saf, random.randint(13, 15), random.randint(800, 899), saf),
            "({0}) AppleWebKit/{1} (KHTML, like Gecko) Chrome/{2}.0.{3}.0 Safari/{4}".format(
                cls.windows_platform_token(), saf, random.randint(13, 15), random.randint(800, 899), saf),
            "({0}) AppleWebKit/{1} (KHTML, like Gecko) Chrome/{2}.0.{3}.0 Safari/{4}".format(
                cls.mac_platform_token(), saf, random.randint(13, 15), random.randint(800, 899), saf),
        )

        return 'Mozilla/5.0 ' + cls.random_element(platforms)

    @classmethod
    def firefox(cls):
        ver = (
            'Gecko/{0} Firefox/{1}.0'.format(
            date_time.Provider.date_time_between(datetime(2011, 1, 1)), random.randint(4, 15)),
            'Gecko/{0} Firefox/3.6.{1}'.format(
                date_time.Provider.date_time_between(datetime(2010, 1, 1)), random.randint(1, 20)),
            'Gecko/{0} Firefox/3.8'.format(date_time.Provider.date_time_between(datetime(2010, 1, 1)), ),
        )

        platforms = (
            "({0}; {1}; rv:1.9.{2}.20) {3}".format(
                cls.windows_platform_token(), cls.random_element(cls.langs), random.randint(0, 2), random.choice(ver)),
            "({0}; rv:1.9.{1}.20) {2}".format(cls.linux_platform_token(), random.randint(5, 7), random.choice(ver)),
            "({0}; rv:1.9.{1}.20) {2}".format(cls.mac_platform_token(), random.randint(2, 6), random.choice(ver)),
        )

        return 'Mozilla/5.0 ' + cls.random_element(platforms)

    @classmethod
    def safari(cls):
        saf = "{0}.{1}.{2}".format(random.randint(531, 535), random.randint(1, 50), random.randint(1, 7))
        if random.randint(0, 1) == 0:
            ver = "{0}.{1}".format(random.randint(4, 5), random.randint(0, 1))
        else:
            ver = "{0}.0.{1}".format(random.randint(4, 5), random.randint(1, 5))

        platforms = (
            '(Windows; U; {0}) AppleWebKit/{1} (KHTML, like Gecko) Version/{2} Safari/{3}'.format(
                cls.windows_platform_token(), saf, ver, saf),
            '({0} rv:{1}.0; {2}) AppleWebKit/{3} (KHTML, like Gecko) Version/{4} Safari/{5}'.format(
                cls.mac_platform_token(), random.randint(2, 6), cls.random_element(cls.langs), saf, ver, saf),
            '(iPod; U; CPU iPhone OS {0}_{1} like Mac OS X; {2}) AppleWebKit/{3} (KHTML, like Gecko) Version/{4}.0.5 Mobile/8B{5} Safari/6{6}'.format(
                random.randint(3, 4), random.randint(0, 3), cls.random_element(cls.langs), saf, random.randint(3, 4),
                random.randint(111, 119), saf
            )
        )

        return 'Mozilla/5.0 ' + cls.random_element(platforms)

    @classmethod
    def opera(cls):

        platforms = (
            '({0}; {1}) Presto/2.9.{2} Version/{3}.00'.format(
                cls.linux_platform_token(), cls.random_element(cls.langs), random.randint(160, 190),
                random.randint(10, 12)),
            '({0}; {1}) Presto/2.9.{2} Version/{3}.00'.format(
                cls.windows_platform_token(), cls.random_element(cls.langs), random.randint(160, 190),
                random.randint(10, 12)),
        )

        return 'Opera/{0}.{1}.{2}'.format(random.randint(8, 9), random.randint(10, 99), cls.random_element(platforms))

    @classmethod
    def internet_explorer(cls):
        return 'Mozilla/5.0 (compatible; MSIE {0}.0; {1}; Trident/{2}.{3})'.format(
            random.randint(5, 9),
            cls.windows_platform_token(),
            random.randint(3, 5),
            random.randint(0, 1)
        )

    @classmethod
    def windows_platform_token(cls):
        return cls.random_element(cls.windows_platform_tokens)

    @classmethod
    def linux_platform_token(cls):
        return 'X11; Linux {0}'.format(cls.random_element(cls.linux_processors))

    @classmethod
    def mac_platform_token(cls):
        return 'Macintosh; {0} Mac OS X 10_{1}_{2}'.format(
            cls.random_element(cls.mac_processors), random.randint(5, 8), random.randint(0, 9))

