# Code to read a Base64 decoded image string

# pip install pillow

import base64
from io import BytesIO
import re

from PIL import Image

# Replace this string with the created Base64 image string
image_str = r"data:image/jpeg;base64,/9j/4AAQSkZJ........oxwRkZ+lf/Z"

# Remove data url prefix
# It is also possible to do some checks with the data url
image_data = re.sub('^data:image/.+;base64,','', image_str)

im = Image.open(BytesIO(base64.b64decode(image_data)))
im.show()