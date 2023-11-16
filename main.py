import pygame
import PIL.Image
import time

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
CUSTOM_COLORS = {
    "@": (0, 0, 0),
    "#": (30, 30, 30),
    "S": (60, 60, 60),
    "%": (90, 90, 90),
    "?": (120, 120, 120),
    "*": (150, 150, 150),
    "+": (180, 180, 180),
    ";": (210, 210, 210),
    ":": (240, 240, 240),
    ",": (255, 255, 255),
    ".": (255, 255, 255),
}


# resize image according to new width and height
def get_color(char, intensity):
    if char in CUSTOM_COLORS:
        return CUSTOM_COLORS[char]
    else:
        # You can customize the color gradient here
        r = g = b = intensity
        return r, g, b


def resize_image(image, new_width=1000, new_height=1000):
    resized_image = image.resize((new_width, new_height))
    return resized_image


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=700, new_height=500):
    running = True
    picOrd = 0
    pygame.init()
    # create window
    screen = pygame.display.set_mode((new_width, new_height))
    pygame.display.set_caption("Ascii Image")
    clock = pygame.time.Clock()

    while running:
        # attempt to open image from user-input
        paths = [
            "0001.jpg", "0002.jpg", "0003.jpg", "0004.jpg", "0005.jpg", "0006.jpg", "0007.jpg",
            "0008.jpg", "0009.jpg", "0010.jpg", "0011.jpg", "0012.jpg", "0013.jpg", "0014.jpg", "0015.jpg",
            "0016.jpg", "0017.jpg", "0018.jpg", "0019.jpg", "0020.jpg", "0021.jpg", "0022.jpg", "0023.jpg",
            "0024.jpg", "0025.jpg", "0026.jpg", "0027.jpg", "0028.jpg", "0029.jpg", "0030.jpg", "0031.jpg",
            "0032.jpg", "0033.jpg", "0034.jpg", "0035.jpg", "0036.jpg", "0037.jpg", "0038.jpg", "0039.jpg",
            "0040.jpg", "0041.jpg", "0042.jpg", "0043.jpg", "0044.jpg", "0045.jpg", "0046.jpg", "0047.jpg",
            "0048.jpg", "0049.jpg", "0050.jpg", "0051.jpg", "0052.jpg", "0053.jpg", "0054.jpg", "0055.jpg",
            "0056.jpg", "0057.jpg", "0058.jpg", "0059.jpg", "0060.jpg", "0061.jpg", "0062.jpg", "0063.jpg",
            "0064.jpg", "0065.jpg", "0066.jpg", "0067.jpg", "0068.jpg", "0069.jpg", "0070.jpg", "0071.jpg",
            "0072.jpg", "0073.jpg", "0074.jpg", "0075.jpg", "0076.jpg", "0077.jpg", "0078.jpg", "0079.jpg",
            "0080.jpg", "0081.jpg", "0082.jpg", "0083.jpg", "0084.jpg", "0085.jpg", "0086.jpg", "0087.jpg",
            "0088.jpg", "0089.jpg", "0090.jpg", "0091.jpg", "0092.jpg", "0093.jpg", "0094.jpg", "0095.jpg",
            "0096.jpg", "0097.jpg", "0098.jpg", "0099.jpg", "0100.jpg", "0101.jpg", "0102.jpg", "0103.jpg",
            "0104.jpg", "0105.jpg", "0106.jpg", "0107.jpg", "0108.jpg", "0109.jpg", "0110.jpg", "0111.jpg",
            "0112.jpg", "0113.jpg", "0114.jpg", "0115.jpg", "0116.jpg", "0117.jpg", "0118.jpg", "0119.jpg",
            "0120.jpg", "0121.jpg", "0122.jpg", "0123.jpg", "0124.jpg", "0125.jpg", "0126.jpg", "0127.jpg",
            "0128.jpg", "0129.jpg", "0130.jpg", "0131.jpg", "0132.jpg", "0133.jpg", "0134.jpg", "0135.jpg",
            "0136.jpg", "0137.jpg", "0138.jpg", "0139.jpg", "0140.jpg", "0141.jpg", "0142.jpg", "0143.jpg",
            "0144.jpg", "0145.jpg", "0146.jpg", "0147.jpg", "0148.jpg", "0149.jpg", "0150.jpg", "0151.jpg",
            "0152.jpg", "0153.jpg", "0154.jpg", "0155.jpg", "0156.jpg", "0157.jpg", "0158.jpg", "0159.jpg",
            "0160.jpg", "0161.jpg", "0162.jpg", "0163.jpg", "0164.jpg", "0165.jpg", "0166.jpg", "0167.jpg",
            "0168.jpg", "0169.jpg", "0170.jpg", "0171.jpg", "0172.jpg", "0173.jpg", "0174.jpg", "0175.jpg",
            "0176.jpg", "0177.jpg", "0178.jpg", "0179.jpg", "0180.jpg", "0181.jpg", "0182.jpg", "0183.jpg",
            "0184.jpg", "0185.jpg", "0186.jpg", "0187.jpg", "0188.jpg", "0189.jpg", "0190.jpg", "0191.jpg",
            "0192.jpg", "0193.jpg", "0194.jpg", "0195.jpg", "0196.jpg", "0197.jpg", "0198.jpg", "0199.jpg",
            "0200.jpg", "0201.jpg", "0202.jpg", "0203.jpg", "0204.jpg", "0205.jpg", "0206.jpg", "0207.jpg",
            "0208.jpg", "0209.jpg", "0210.jpg", "0211.jpg", "0212.jpg", "0213.jpg", "0214.jpg", "0215.jpg",
            "0216.jpg", "0217.jpg", "0218.jpg", "0219.jpg", "0220.jpg", "0221.jpg", "0222.jpg", "0223.jpg",
            "0224.jpg", "0225.jpg", "0226.jpg", "0227.jpg", "0228.jpg", "0229.jpg", "0230.jpg", "0231.jpg",
            "0232.jpg", "0233.jpg", "0234.jpg", "0235.jpg", "0236.jpg", "0237.jpg", "0238.jpg", "0239.jpg", "0240.jpg", "0241.jpg", "0242.jpg", "0243.jpg", "0244.jpg", "0245.jpg",
"0246.jpg", "0247.jpg", "0248.jpg", "0249.jpg", "0250.jpg", "0251.jpg", "0252.jpg", "0253.jpg", "0254.jpg", "0255.jpg",
"0256.jpg", "0257.jpg", "0258.jpg", "0259.jpg", "0260.jpg", "0261.jpg", "0262.jpg", "0263.jpg", "0264.jpg", "0265.jpg",
"0266.jpg", "0267.jpg", "0268.jpg", "0269.jpg", "0270.jpg", "0271.jpg", "0272.jpg", "0273.jpg", "0274.jpg", "0275.jpg",
"0276.jpg", "0277.jpg", "0278.jpg", "0279.jpg", "0280.jpg", "0281.jpg", "0282.jpg", "0283.jpg", "0284.jpg", "0285.jpg",
"0286.jpg", "0287.jpg", "0288.jpg", "0289.jpg", "0290.jpg", "0291.jpg", "0292.jpg", "0293.jpg", "0294.jpg", "0295.jpg",
"0296.jpg", "0297.jpg", "0298.jpg", "0299.jpg", "0300.jpg", "0301.jpg", "0302.jpg", "0303.jpg", "0304.jpg", "0305.jpg",
"0306.jpg", "0307.jpg", "0308.jpg", "0309.jpg", "0310.jpg", "0311.jpg", "0312.jpg", "0313.jpg", "0314.jpg", "0315.jpg",
"0316.jpg", "0317.jpg", "0318.jpg", "0319.jpg", "0320.jpg", "0321.jpg", "0322.jpg", "0323.jpg", "0324.jpg", "0325.jpg",
"0326.jpg", "0327.jpg", "0328.jpg", "0329.jpg", "0330.jpg", "0331.jpg", "0332.jpg", "0333.jpg", "0334.jpg", "0335.jpg",
"0336.jpg", "0337.jpg", "0338.jpg", "0339.jpg", "0340.jpg", "0341.jpg", "0342.jpg", "0343.jpg", "0344.jpg", "0345.jpg",
"0346.jpg", "0347.jpg", "0348.jpg", "0349.jpg", "0350.jpg", "0351.jpg", "0352.jpg", "0353.jpg", "0354.jpg", "0355.jpg",
"0356.jpg", "0357.jpg", "0358.jpg", "0359.jpg", "0360.jpg", "0361.jpg", "0362.jpg", "0363.jpg", "0364.jpg", "0365.jpg",
"0366.jpg", "0367.jpg", "0368.jpg", "0369.jpg", "0370.jpg", "0371.jpg", "0372.jpg", "0373.jpg", "0374.jpg", "0375.jpg",
"0376.jpg", "0377.jpg", "0378.jpg", "0379.jpg", "0380.jpg", "0381.jpg", "0382.jpg", "0383.jpg", "0384.jpg", "0385.jpg",
"0386.jpg", "0387.jpg", "0388.jpg", "0389.jpg", "0390.jpg", "0391.jpg", "0392.jpg", "0393.jpg", "0394.jpg", "0395.jpg",
"0396.jpg", "0397.jpg", "0398.jpg", "0399.jpg", "0400.jpg", "0401.jpg", "0402.jpg", "0403.jpg", "0404.jpg", "0405.jpg",
"0406.jpg", "0407.jpg", "0408.jpg", "0409.jpg", "0410.jpg", "0411.jpg", "0412.jpg", "0413.jpg", "0414.jpg", "0415.jpg",
"0416.jpg", "0417.jpg", "0418.jpg", "0419.jpg", "0420.jpg", "0421.jpg", "0422.jpg", "0423.jpg", "0424.jpg", "0425.jpg",
"0426.jpg", "0427.jpg", "0428.jpg", "0429.jpg", "0430.jpg", "0431.jpg", "0432.jpg", "0433.jpg", "0434.jpg", "0435.jpg",
"0436.jpg", "0437.jpg", "0438.jpg", "0439.jpg", "0440.jpg", "0441.jpg", "0442.jpg", "0443.jpg", "0444.jpg", "0445.jpg",
"0446.jpg", "0447.jpg", "0448.jpg", "0449.jpg", "0450.jpg", "0451.jpg", "0452.jpg", "0453.jpg", "0454.jpg", "0455.jpg",
"0456.jpg", "0457.jpg", "0458.jpg", "0459.jpg", "0460.jpg", "0461.jpg", "0462.jpg", "0463.jpg", "0464.jpg", "0465.jpg",
"0466.jpg", "0467.jpg", "0468.jpg", "0469.jpg", "0470.jpg", "0471.jpg", "0472.jpg", "0473.jpg", "0474.jpg", "0475.jpg",
"0476.jpg", "0477.jpg", "0478.jpg", "0479.jpg", "0480.jpg", "0481.jpg", "0482.jpg", "0483.jpg", "0484.jpg", "0485.jpg",
"0486.jpg", "0487.jpg", "0488.jpg", "0489.jpg", "0490.jpg", "0491.jpg", "0492.jpg", "0493.jpg", "0494.jpg", "0495.jpg",
"0496.jpg", "0497.jpg", "0498.jpg", "0499.jpg", "0500.jpg"

        ]
        path = paths[picOrd]
        if path.lower() == 'exit':
            break

        try:
            image = PIL.Image.open(path)
        except:
            print(path, " is not a valid pathname to an image.")
            continue

        # resize image to fit the window
        resized_image = resize_image(image, new_width, new_height)

        # convert image to ascii
        new_image_data = pixels_to_ascii(grayify(resized_image))

        # format
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(
            [new_image_data[index: (index + new_width)] for index in range(0, pixel_count, new_width)])

        # save result to "ascii_image.txt"
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)

        start_time = time.time()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # update screen
            screen.fill((0, 0, 0))
            x, y = 0, 0
            for char in ascii_image:
                if char != "\n":
                    # get pixel intensity (0 to 255) and map it to the color gradient or use custom color
                    pixel_intensity = ASCII_CHARS.index(char) * (255 // len(ASCII_CHARS))
                    color = get_color(char, pixel_intensity)
                    screen.set_at((x, y), color)
                    x += 1
                else:
                    print("Enums Page Frame: "+ str(picOrd))
                    x = 0
                    y += 1

            pygame.display.flip()
            clock.tick(6000)

            # Check if 2 seconds have passed
            if time.time() - start_time > .1:
                picOrd +=1
                print(picOrd)
                if picOrd > 499:
                    picOrd = 0
                    running = False
            break




    pygame.quit()


# run program
main()
