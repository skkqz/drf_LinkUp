import os
from django.utils.crypto import get_random_string
from PIL import Image

from config.settings import MEDIA_ROOT


def rename_image(name_image: str) -> str:

    """
    Изменение название изображения.
    :param name_image: Имя файла.
    :return: Изменённое имя файла.
    """

    root, ext = os.path.splitext(name_image)
    new_name = f'avatars/{get_random_string(length=20)}{ext}'

    return new_name


def resize_image(image):

    """
    Изменение размера изображение.
    :param image: Изображение
    :return: Изображение с изменённым размером 200px 200px
    """

    img = Image.open(image)
    img.thumbnail((200, 200))
    new_name = rename_image(image.name)
    path_image = f'{MEDIA_ROOT}/{new_name}'
    img.save(path_image)

    return new_name
