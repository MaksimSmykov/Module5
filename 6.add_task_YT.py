import time

users = []

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        users.append(self)

    def __str__(self):
        return self.nickname

videos = []

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


    def __str__(self):
        return (f'Название: {self.title}, продолжительность: {self.duration}, '
                f'секунда остановки: {self.time_now}, ограничение по возрасту: {self.adult_mode}')


class UrTube:

    __instance = None
    def __new__(cls, *args, **kwargs):
        cls.users = users
        cls.videos = videos
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self):
        self.current_user = None

    def __str__(self):
        return f'{self.current_user['nickname']}'

    def log_in(self, nickname, password):
        for user in users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        exist = False
        if isinstance(nickname, str) and isinstance(password, str) and isinstance(age, int):
            for user in users:
                if nickname == user.nickname:
                    print(f'Пользователь {nickname} уже существует')
                    exist = True
                    break
            if not exist:
                new_user = User(nickname, password, age)
                self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        exist = False
        for arg in args:
            if isinstance(arg, Video):
                for video in videos:
                    if arg.title == video['title']:
                        exist = True
                        break
                if not exist:
                    new_video = {'title': arg.title, 'duration': arg.duration,
                                 'time_now': arg.time_now, 'adult_mode': arg.adult_mode}
                    videos.append(new_video)

    def get_videos(self, search_word):
        if isinstance(search_word, str):
            found = []
            if len(videos) > 0:
                for video in videos:
                    if search_word.lower() in video['title'].lower():
                        found.append(video['title'])
            return found


    def watch_video(self, title):
        if isinstance(title, str):
            if self.current_user != None:
                for video in videos:
                    if title.lower() == video['title'].lower():
                        if self.current_user.age >= 18:
                            for i in range(1, video['duration'] + 1):
                                video['time_now'] += 1
                                print(video['time_now'])
                                time.sleep(1)
                            print('Конец видео')
                        else:
                            print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    video['time_now'] = 0
                    time.sleep(1)
            else:
                print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
