import pygame


class PygameTools:

    def scale_image(image_path, scale):
        pygame.init()

        # 加载图像
        image = pygame.image.load(image_path)

        # 获取图像的原始宽度和高度
        original_width = image.get_width()
        original_height = image.get_height()

        # 计算缩放后的宽度和高度
        scaled_width = int(original_width * scale)
        scaled_height = int(original_height * scale)

        # 缩放图像
        scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))

        pygame.quit()

        return scaled_image
