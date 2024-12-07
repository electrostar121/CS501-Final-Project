import client
import matplotlib.pyplot as plt

sampleImages = [
    '14719 flat tile corner 2x2 031L.png',
    '14719 flat tile corner 2x2 132R.png',
    '14719 flat tile corner 2x2 208L.png',
    '14719 flat tile corner 2x2 275L.png',
    '15672 roof tile 1x2 203R.png',
    '2357 brick corner 1x2x2 131R.png',
    '2357 brick corner 1x2x2 348L.png',
    '2420 plate corner 2x2 039L.png',
    '2780 Peg with friction 126R.png',
    '27925 flat tile round 2x2 006L.png',
    '27925 flat tile round 2x2 312L.png',
    '3001 brick 2x4 252L.png',
    '3003 brick 2x2 046L.png',
    '3003 brick 2x2 133R.png',
    '3003 brick 2x2 164R.png',
    '3003 brick 2x2 271L.png',
    '3004 brick 1x2 032L.png',
    '3004 brick 1x2 146R.png',
    '3005 brick 1x1 189L.png',
    '3005 brick 1x1 254R.png',
    '3005 brick 1x1 336L.png',
    '3010 brick 1x4 027R.png',
    '3010 brick 1x4 074L.png',
    '3010 brick 1x4 376R.png',
    '3020 plate 2x4 066L.png'
]

cloud = client.h5Cloud('http://34.217.215.64')

for image in sampleImages:
    img = plt.imshow(cloud.selectFile('test.h5').image(image).pad(100, 100, 100, 100).getImage())
    plt.axis('off')
    img.axes.get_xaxis().set_visible(False)
    img.axes.get_yaxis().set_visible(False)
    plt.savefig('images/' + image, bbox_inches='tight', pad_inches = 0)