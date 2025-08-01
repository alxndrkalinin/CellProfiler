from cubic.skimage import color

from ._url_image import URLImage


class ColorImage(URLImage):
    """Provide a color image, tripling a monochrome plane if needed"""

    def __init__(
        self, name, url, series, index, rescale_range=None, metadata_rescale=False, volume=False, spacing=None, z=None, t=None
    ):
        URLImage.__init__(
            self,
            name,
            url,
            rescale_range=rescale_range,
            metadata_rescale=metadata_rescale,
            series=series,
            index=index,
            volume=volume,
            spacing=spacing,
            z=z,
            t=t
        )

    def provide_image(self, image_set):
        image = URLImage.provide_image(self, image_set)

        if image.pixel_data.ndim == image.dimensions:
            image.pixel_data = color.gray2rgb(image.pixel_data)

        return image
