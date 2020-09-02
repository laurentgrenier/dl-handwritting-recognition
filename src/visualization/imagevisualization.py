from PIL import Image
from src.visualization.transforms import RGBTransform # from source code mentioned above
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np


def visualize_labels(image, masks, labels=None):
    """ Display an image with the (h,w,3) format and its masks with a (h,w,c) format
    Example with a mrcnn Dataset
        idx, image = dataset_train.get_random_image()
        masks, class_ids = dataset_train.load_mask(idx)
        class_names = np.take(dataset_train.class_names, class_ids)
        visualize_labels(image, masks, class_names)
    """

    pil_image = Image.fromarray(image)

    # colors from constants
    color = (209, 48, 192)

    # for each mask
    for i in range(masks.shape[2]):
        # get the mask
        mask = masks[:, :, i]

        # colorize the image
        new_image = RGBTransform().mix_with(color, factor=.30).applied_to(pil_image)

        # apply the mask
        image[mask] = np.array(new_image)[mask]

        # update the current image
        pil_image = Image.fromarray(image)

        # display
    fig, ax = plt.subplots(figsize=(18, 18))
    ax.imshow(np.array(image))

    plt.show()
