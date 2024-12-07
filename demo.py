import client
import localH5
import matplotlib.pyplot as plt

cloud = client.h5Cloud('http://34.215.68.78')

imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').getImage())
# imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').flip().getImage())
# imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').scale(10, 10).getImage())
# imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').crop(0, 0, 100, 100).getImage())
# imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').invert().getImage())
# imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').reduction(128).getImage())
# imgplot = plt.imshow(cloud.selectFile('test.h5').image('monke.jpeg').pad(100, 100, 100, 100).getImage())


local = localH5.h5Ext(location=".")

# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').data)
# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').flip().data)
# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').scale(10, 10).data)
# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').crop(0, 0, 100, 100).data)
# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').invert().data)
# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').reduction(128).data)
# imgplot = plt.imshow(local.selectFile('test.h5').image('monke.jpeg').pad(100, 100, 100, 100).data)

plt.show()